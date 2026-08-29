"""FastAPI service: POST /ask (SSE), GET /context, GET /health, GET /metrics, static/."""
import asyncio
import hashlib
import json
import os
import queue
import re
import sys
import threading
import time
from collections import OrderedDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

import yaml  # noqa: E402
from fastapi import FastAPI, HTTPException, Request, Response  # noqa: E402
from fastapi.responses import StreamingResponse  # noqa: E402
from fastapi.staticfiles import StaticFiles  # noqa: E402
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest  # noqa: E402
from pydantic import BaseModel  # noqa: E402
from slowapi import Limiter, _rate_limit_exceeded_handler  # noqa: E402
from slowapi.errors import RateLimitExceeded  # noqa: E402
from slowapi.util import get_remote_address  # noqa: E402

from core import agent, config, dblink, gate, llm, memory, params, sessions, sql, trace  # noqa: E402
from core.sessions import record_session_turn  # noqa: E402

app = FastAPI()


def _rl_key(request: Request) -> str:
    """Rate-limit bucket = session_id (per chat session), not bearer token."""
    sid = request.headers.get("x-session-id")
    if sid:
        return f"session:{sid}"
    return f"ip:{get_remote_address(request)}"


limiter = Limiter(key_func=_rl_key)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


def _validate_client_name(name: str) -> str:
    path = BASE_DIR / "clients" / f"{name}.yaml"
    if not path.exists() or name.startswith("_"):
        raise RuntimeError(f"CHATBOT_CLIENT={name!r} has no clients/{name}.yaml")
    return name


def pinned_client() -> str:
    """Server-pinned tenant from env — browser cannot switch yaml client."""
    name = os.environ.get("CHATBOT_CLIENT")
    if not name:
        raise RuntimeError("CHATBOT_CLIENT is not set — pin the tenant in .env")
    return _validate_client_name(name.strip())


# Validate at import so misconfiguration fails startup
PINNED_CLIENT = pinned_client()


class AskRequest(BaseModel):
    question: str
    client: str | None = None      # IGNORED — kept so old bodies don't 422
    session_id: str | None = None
    company_id: int | None = None  # header dropdown; never ask in chat


class FeedbackRequest(BaseModel):
    session_id: str
    helpful: bool
    reason: str | None = None
    turn_id: str | None = None


class ContextSetRequest(BaseModel):
    session_id: str
    company_id: int


class DbConnectRequest(BaseModel):
    server: str          # '(.)' = local default instance
    port: int | None = None
    user: str = ""
    password: str = ""
    database: str | None = None
    trusted: bool = False  # Windows auth, best-effort on Linux


SESSIONS: OrderedDict = OrderedDict()
SESSION_MAX = 500
SESSION_IDLE_SECONDS = 3600
_NUMBER_RE = re.compile(r"\d+")


def _with_heartbeat(gen, interval: float = 15.0):
    """SSE keep-alive during silent phases: long LLM thinking turns emit no
    frames, and proxies (ARR/nginx) buffer or idle-timeout quiet streams.
    Pumps gen on a daemon thread; on queue timeout yields an SSE comment
    line, which is spec-legal and ignored by SSE parsers."""
    q: queue.Queue = queue.Queue()
    sentinel = object()

    def _pump():
        try:
            for item in gen:
                q.put(item)
        except BaseException as e:  # noqa: BLE001 — re-raised in consumer thread
            q.put(e)
        finally:
            q.put(sentinel)

    threading.Thread(target=_pump, daemon=True).start()
    while True:
        try:
            item = q.get(timeout=interval)
        except queue.Empty:
            yield ": keep-alive\n\n"
            continue
        if item is sentinel:
            return
        if isinstance(item, BaseException):
            raise item
        yield item


def _persist_session(session_id: str | None, state: dict) -> None:
    """TRACK E: write-through to work/sessions.sqlite (minus the hot-cache
    bookkeeping key) so conversations survive restarts."""
    if not session_id:
        return
    payload = {k: v for k, v in state.items() if k != "_touched"}
    try:
        sessions.save(session_id, payload)
    except Exception:  # noqa: BLE001 — persistence is best-effort, never break a turn
        pass


def _touch_session(session_id: str, default_factory) -> dict:
    now = time.time()
    for sid in [sid for sid, s in SESSIONS.items() if now - s["_touched"] > SESSION_IDLE_SECONDS]:
        del SESSIONS[sid]
        sessions.delete(sid)
    sessions.sweep()
    if session_id in SESSIONS:
        SESSIONS.move_to_end(session_id)
        SESSIONS[session_id]["_touched"] = now
    else:
        persisted = sessions.load(session_id)
        state = persisted if isinstance(persisted, dict) else default_factory()
        state["_touched"] = now
        state.setdefault("conversation", {})
        state.setdefault("pending_ask", None)
        state.setdefault("history", [])
        state.setdefault("transcript", [])
        SESSIONS[session_id] = state
        while len(SESSIONS) > SESSION_MAX:
            old_sid, _ = SESSIONS.popitem(last=False)
            sessions.delete(old_sid)
    return SESSIONS[session_id]


def _match_company(question: str, companies: list) -> int | None:
    ids = {c["id"] for c in companies}
    m = _NUMBER_RE.search(question)
    if m and int(m.group()) in ids:
        return int(m.group())
    q_lower = question.strip().lower()
    for c in companies:
        name_lower = str(c["name"]).lower()
        if name_lower and (name_lower in q_lower or q_lower in name_lower):
            return c["id"]
    return None


def _apply_pending_answer(session: dict, question: str, client: str) -> None:
    # Company is chosen in the header dropdown, not parsed from chat.
    if session.get("pending_ask") == "CompanyID":
        session["pending_ask"] = None


def _set_session_company(session: dict, conv: dict, cid: int) -> None:
    prev = conv.get("CompanyID")
    conv["CompanyID"] = cid
    # Tenant switch mid-conversation: prior turns were answered under another
    # company -- drop them so the model can never parrot an old company's
    # number when the same question is asked again after the dropdown change.
    if prev is not None and int(prev) != int(cid):
        session["history"] = []
        session["transcript"] = []
        session.pop("last_turn", None)


def _ensure_session_company(session: dict, client: str, company_id: int | None = None) -> None:
    conv = session.setdefault("conversation", {})
    live = _load_companies_live(client, conv)
    valid = {int(c["id"]) for c in live}
    if company_id is not None:
        cid = int(company_id)
        if not valid or cid in valid:
            _set_session_company(session, conv, cid)
            return
    pinned = params.pin_company_id(conv, params.discover_profile(client))
    if pinned is not None and (not valid or pinned in valid):
        _set_session_company(session, conv, int(pinned))
        return
    if live:
        _set_session_company(session, conv, int(live[0]["id"]))


def _resolve_context_company_id(client: str, conversation: dict) -> int | None:
    profile = params.discover_profile(client)
    company_id = params.resolve("CompanyID", conversation, profile)
    if company_id not in (params.NEEDS_ASK, params.MULTI):
        return company_id
    companies = profile.get("_companies") or []
    if conversation.get("CompanyID") is not None:
        return conversation["CompanyID"]
    if len(companies) == 1:
        return companies[0]["id"]
    return companies[0]["id"] if companies else None


def _load_companies_live(client: str, conversation: dict) -> list[dict]:
    """Load company ID+Name rows from t.Companies (live DB, not cached probe)."""
    profile = params.discover_profile(client)
    seed_ids: list[int] = []
    for row in profile.get("_companies") or []:
        seed_ids.append(int(row["id"]))
    if conversation.get("CompanyID") is not None:
        seed_ids.append(int(conversation["CompanyID"]))
    if not seed_ids:
        seed_ids = [1]
    seed_ids = sorted(set(seed_ids))

    companies: list[dict] = []
    seen: set[int] = set()
    conn = sql.get_conn(client)
    try:
        for cid in seed_ids:
            sql.set_tenant(conn, cid)
            cur = conn.cursor(as_dict=True)
            cur.execute("SELECT ID, Name FROM t.Companies")
            for row in cur.fetchall():
                rid = int(row["ID"])
                if rid not in seen:
                    seen.add(rid)
                    companies.append({"id": rid, "name": row["Name"]})
    finally:
        conn.close()
    return sorted(companies, key=lambda c: c["id"])


def _context_payload(client: str, conversation: dict) -> dict:
    companies = _load_companies_live(client, conversation)
    company_id = _resolve_context_company_id(client, conversation)
    company_row = None
    clients_active = []
    if company_id is not None:
        conn = sql.get_conn(client)
        try:
            sql.set_tenant(conn, company_id)
            cur = conn.cursor(as_dict=True)
            cur.execute("SELECT ID, Name FROM t.Companies")
            rows = cur.fetchall()
            if rows:
                company_row = rows[0]
            cur.execute("SELECT CompanyID, ClientID FROM t.ClientsActive")
            clients_active = cur.fetchall()
        finally:
            conn.close()
    return {
        "client": client,
        "company_id": company_id,
        "company": company_row,
        "companies": companies,
        "clients_active": clients_active,
        "multi_company": len(companies) > 1,
        "multi_company": len(companies) > 1,
    }


@app.get("/context")
def get_context(session_id: str | None = None):
    client = pinned_client()
    transcript = []
    if session_id:
        session = _touch_session(session_id, lambda: {"conversation": {}, "pending_ask": None})
        _ensure_session_company(session, client)
        conversation = session["conversation"]
        transcript = list(session.get("transcript") or [])
    else:
        conversation = {}
    payload = _context_payload(client, conversation)
    payload["transcript"] = transcript
    return payload


@app.post("/db/test")
def db_test(req: DbConnectRequest):
    """Probe a server without persisting — drift-tool's picker semantics."""
    return dblink.test_connection(
        req.server, req.user, req.password,
        database=req.database, port=req.port, trusted=req.trusted)


@app.post("/db/connect")
def db_connect(req: DbConnectRequest):
    """Test then persist the runtime override; all subsequent get_conn()
    calls hit this server. Password stored 0600 in gitignored work/ and
    never echoed back (GETs return bullets). Empty password reuses the
    stored one when host+user match — reconnects don't demand retyping."""
    if not req.password:
        prev = dblink.raw_override()
        try:
            host, _ = dblink.resolve_target(req.server)
        except dblink.ConnectionTargetError as e:
            return {"ok": False, "error": str(e)}
        if prev and prev.get("user") == req.user and prev.get("host") == host:
            req.password = prev.get("password", "")
    probe = dblink.test_connection(
        req.server, req.user, req.password,
        database=req.database, port=req.port, trusted=req.trusted)
    if not probe.get("ok"):
        return {"ok": False, "error": probe.get("error", "تعذر الاتصال")}
    if req.database and not probe.get("target_db_ok"):
        return {"ok": False, "error": f"قاعدة البيانات {req.database!r} غير موجودة أو غير متاحة"}
    saved = dblink.save_override(
        req.server, req.user, req.password,
        req.database or "", port=req.port, trusted=req.trusted)
    trace.log_event(PINNED_CLIENT, "db_connect", event="db_source_changed",
                    param=f"{saved['host']}:{saved['port']}/{saved['database']} as {saved['user']}")
    return {"ok": True, "active": saved, "probe": {
        k: v for k, v in probe.items() if k != "databases"}}


@app.post("/db/reset")
def db_reset():
    """Back to the .env snapshot source."""
    dblink.clear_override()
    return {"ok": True, "active": None}


@app.get("/db/status")
def db_status():
    override = dblink.active_override()
    if override:
        return {"source": "live", "active": override}
    return {
        "source": "snapshot",
        "active": {
            "host": os.environ.get("DB_HOST", "127.0.0.1"),
            "port": int(os.environ.get("DB_PORT", "1433")),
            "user": "chatbot_ro",
            "password": "••••••",
            "database": config.load_client(PINNED_CLIENT)["db_name"],
        },
    }


@app.post("/context")
def set_context(req: ContextSetRequest):
    client = pinned_client()
    session = _touch_session(req.session_id, lambda: {"conversation": {}, "pending_ask": None})
    companies = _load_companies_live(client, session.get("conversation", {}))
    valid_ids = {c["id"] for c in companies}
    if req.company_id not in valid_ids:
        raise HTTPException(status_code=400, detail="invalid CompanyID for this client")
    _set_session_company(session, session["conversation"], int(req.company_id))
    return _context_payload(client, session["conversation"])


@app.post("/ask")
@limiter.limit("30/minute")
async def ask(request: Request, req: AskRequest):
    client = pinned_client()  # env-pinned; body client field ignored
    subject = hashlib.sha256((req.session_id or "anon").encode()).hexdigest()[:12]

    session = _touch_session(req.session_id, lambda: {"conversation": {}, "pending_ask": None}) \
        if req.session_id else {"conversation": {}, "pending_ask": None}
    _apply_pending_answer(session, req.question, client)
    _ensure_session_company(session, client, req.company_id)

    if not req.question.strip():
        async def blank_stream():
            yield f"data: {json.dumps({'error': 'يرجى إدخال سؤال.'})}\n\n"
            yield "data: [DONE]\n\n"
        return StreamingResponse(
            blank_stream(),
            media_type="text/event-stream",
            headers={"X-Accel-Buffering": "no", "Cache-Control": "no-transform"},
        )

    cancel = threading.Event()  # TRACK D: set on client disconnect

    def stream():
        result = None
        try:
            for event in agent.ask_stream(client, req.question,
                                          conversation=session["conversation"],
                                          subject=subject,
                                          history=session.get("history") or [],
                                          transcript=session.get("transcript") or [],
                                          cancel=cancel):
                if event["type"] == "step":
                    yield f"data: {json.dumps({'step': event['step']})}\n\n"
                elif event["type"] == "answer_chunk":
                    yield f"data: {json.dumps({'answer_chunk': event['text']})}\n\n"
                elif event["type"] == "done":
                    result = event
        except agent.TurnCancelled:
            return  # client gone mid-turn — no frames to send, tokens already stopped
        except llm.ProviderUnavailableError as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"
            yield "data: [DONE]\n\n"
            return
        except Exception:  # noqa: BLE001 — never leak raw exception text (may contain tool XML)
            yield f"data: {json.dumps({'error': 'عذراً، حدث خطأ أثناء معالجة طلبك. يرجى المحاولة مرة أخرى.'})}\n\n"
            yield "data: [DONE]\n\n"
            return

        session["pending_ask"] = "CompanyID" if result["needs_ask"] else None
        turn_id = None
        if result["needs_ask"]:
            yield f"data: {json.dumps({'needs_ask': result['needs_ask']})}\n\n"
        else:
            answer = result.get("answer")
            if answer is not None and not str(answer).strip():
                answer = None
            if req.session_id:
                cid = session["conversation"].get("CompanyID")
                turn_id = record_session_turn(
                    session,
                    question=req.question,
                    result=result,
                    client=client,
                    company_id=cid,
                    max_history=agent.MAX_HISTORY_TURNS,
                )
                session["last_turn"] = {
                    "client": client,
                    "company_id": cid,
                    "question": req.question,
                    "answer_sql": result.get("answer_sql"),
                    "cache_key": result.get("cache_key"),
                    "turn_id": turn_id,
                }
            yield f"data: {json.dumps({
                'answer': answer,
                'answer_sql': result.get('answer_sql'),
                'report_name': result.get('report_name'),
                'table': result.get('table'), 'chart': result.get('chart'),
                'followups': result.get('followups') or [], 'sources': result.get('sources') or [],
                'confidence': result.get('confidence'),
                'turn_id': turn_id,
                'tools_ms': result.get('tools_ms') or {},
            }, default=str)}\n\n"
        yield "data: [DONE]\n\n"
        _persist_session(req.session_id, session)

    async def asgi_stream():
        """TRACK D: pump the sync generator on a thread. A dedicated
        watcher polls is_disconnected every 0.5s — critical during silent
        thinking phases when the agent emits no events for tens of seconds;
        without it, abort latency equals the longest quiet window."""
        q: queue.Queue = queue.Queue()
        sentinel = object()
        wake = object()

        def _pump():
            try:
                for item in stream():
                    q.put(item)
            except BaseException as e:  # noqa: BLE001 — forwarded to consumer
                q.put(e)
            finally:
                q.put(sentinel)

        threading.Thread(target=_pump, daemon=True).start()
        loop = asyncio.get_running_loop()

        async def _watch_disconnect():
            while not cancel.is_set():
                if await request.is_disconnected():
                    cancel.set()
                    try:
                        q.put_nowait(wake)
                    except queue.Full:
                        pass
                    return
                await asyncio.sleep(0.5)

        watcher = asyncio.create_task(_watch_disconnect())
        try:
            while True:
                try:
                    item = await asyncio.wait_for(
                        loop.run_in_executor(None, q.get), timeout=20.0)
                except asyncio.TimeoutError:
                    # Belt-and-braces: watcher owns detection; this also
                    # re-checks in case the watcher task itself died.
                    if await request.is_disconnected():
                        cancel.set()
                        return
                    yield ": keep-alive\n\n"
                    continue
                if item is wake or item is sentinel:
                    return
                if isinstance(item, agent.TurnCancelled):
                    return
                if isinstance(item, BaseException):
                    raise item
                yield item
        finally:
            watcher.cancel()

    return StreamingResponse(
        asgi_stream(),
        media_type="text/event-stream",
        headers={"X-Accel-Buffering": "no", "Cache-Control": "no-transform"},
    )


@app.post("/feedback")
def feedback(req: FeedbackRequest):
    client = pinned_client()
    subject = hashlib.sha256(req.session_id.encode()).hexdigest()[:12]

    session = SESSIONS.get(req.session_id)
    if not session:
        raise HTTPException(status_code=404, detail="no recent answer on this session to give feedback on")

    turn = None
    if req.turn_id:
        for row in session.get("transcript") or []:
            if row.get("id") == req.turn_id:
                turn = {
                    "client": row.get("client") or client,
                    "company_id": row.get("company_id"),
                    "question": row["q"],
                    "answer_sql": row.get("sql"),
                    "cache_key": row.get("cache_key"),
                }
                break
        if turn is None:
            raise HTTPException(status_code=404, detail="unknown turn_id")
    else:
        turn = session.get("last_turn")
    if not turn or turn["client"] != client:
        raise HTTPException(status_code=404, detail="no recent answer on this session to give feedback on")

    company_id = turn.get("company_id")
    if company_id is None:
        company_id = _resolve_context_company_id(client, session.get("conversation", {}))
    if company_id is None:
        raise HTTPException(status_code=400, detail="CompanyID not resolved for this session")

    if req.helpful:
        sql_text = turn.get("answer_sql")
        if sql_text:
            # Verify-before-promote: a thumbs-up must never write SQL into
            # the few-shot pool that the gate itself would reject on the
            # next turn (EXEC, multi-statement, cross-company literals).
            try:
                cache = json.loads((config.work_dir(client) / "schema_cache.json").read_text())
                gate.validate(
                    sql_text,
                    allowed_procs=gate.DEFAULT_ALLOWED_PROCS,
                    company_id=company_id,
                    schema_cache=cache,
                )
            except Exception:  # noqa: BLE001 — GateError/missing cache both mean "don't promote"
                trace.log_event(client, turn["question"], event="feedback_invalid_sql", subject=subject)
            else:
                memory.promote_verified_query(
                    client, company_id, turn["question"], sql_text, source="user_feedback",
                )
    else:
        if turn.get("cache_key"):
            memory.delete_plan(turn["cache_key"])
        memory.promote_negative_query(
            client, company_id, turn["question"], turn.get("answer_sql"), reason=req.reason,
        )
        trace.log_event(client, turn["question"], event="feedback_negative", subject=subject)

    return {"ok": True}


def _client_names() -> list:
    return sorted(p.stem for p in (BASE_DIR / "clients").glob("*.yaml") if not p.stem.startswith("_"))


@app.get("/health")
def health():
    provider_ok = llm.provider_health(timeout=5)

    clients = {}
    for name in _client_names():
        db_ok = False
        try:
            conn = sql.get_conn(name)
            conn.cursor().execute("SELECT 1")
            conn.close()
            db_ok = True
        except Exception:  # noqa: BLE001
            pass

        nullable_companyid_rows = {}
        try:
            cache = json.loads((config.work_dir(name) / "schema_cache.json").read_text())
            nullable_companyid_rows = cache.get("nullable_companyid_rows", {})
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        clients[name] = {
            "db": db_ok,
            "pinned": name == PINNED_CLIENT,
            "nullable_companyid_rows": nullable_companyid_rows,
        }

    return {
        "provider": provider_ok,
        "ok": provider_ok and clients.get(PINNED_CLIENT, {}).get("db", False),
        "pinned_client": PINNED_CLIENT,
        "clients": clients,
    }


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


app.mount("/", StaticFiles(directory=str(BASE_DIR / "static"), html=True), name="static")
