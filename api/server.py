"""FastAPI service: POST /ask (SSE), GET /context, GET /health, GET /metrics, static/."""
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
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

from core import agent, config, llm, memory, params, sql, trace  # noqa: E402

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


class FeedbackRequest(BaseModel):
    session_id: str
    helpful: bool
    reason: str | None = None


class ContextSetRequest(BaseModel):
    session_id: str
    company_id: int


SESSIONS: OrderedDict = OrderedDict()
SESSION_MAX = 500
SESSION_IDLE_SECONDS = 3600
_NUMBER_RE = re.compile(r"\d+")


def _touch_session(session_id: str, default_factory) -> dict:
    now = time.time()
    for sid in [sid for sid, s in SESSIONS.items() if now - s["_touched"] > SESSION_IDLE_SECONDS]:
        del SESSIONS[sid]
    if session_id in SESSIONS:
        SESSIONS.move_to_end(session_id)
        SESSIONS[session_id]["_touched"] = now
    else:
        SESSIONS[session_id] = default_factory()
        SESSIONS[session_id]["_touched"] = now
        while len(SESSIONS) > SESSION_MAX:
            SESSIONS.popitem(last=False)
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
    if session.get("pending_ask") == "CompanyID":
        profile = params.discover_profile(client)
        companies = profile.get("_companies") or []
        match = _match_company(question, companies)
        if match is not None:
            session["conversation"]["CompanyID"] = match


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
    }


@app.get("/context")
def get_context(session_id: str | None = None):
    client = pinned_client()
    session = SESSIONS.get(session_id) if session_id else None
    conversation = session.get("conversation", {}) if session else {}
    return _context_payload(client, conversation)


@app.post("/context")
def set_context(req: ContextSetRequest):
    client = pinned_client()
    session = _touch_session(req.session_id, lambda: {"conversation": {}, "pending_ask": None})
    companies = _load_companies_live(client, session.get("conversation", {}))
    valid_ids = {c["id"] for c in companies}
    if req.company_id not in valid_ids:
        raise HTTPException(status_code=400, detail="invalid CompanyID for this client")
    session["conversation"]["CompanyID"] = req.company_id
    return _context_payload(client, session["conversation"])


@app.post("/ask")
@limiter.limit("30/minute")
def ask(request: Request, req: AskRequest):
    client = pinned_client()  # env-pinned; body client field ignored
    subject = hashlib.sha256((req.session_id or "anon").encode()).hexdigest()[:12]

    session = _touch_session(req.session_id, lambda: {"conversation": {}, "pending_ask": None}) \
        if req.session_id else {"conversation": {}, "pending_ask": None}
    _apply_pending_answer(session, req.question, client)

    def stream():
        result = None
        try:
            for event in agent.ask_stream(client, req.question, conversation=session["conversation"], subject=subject):
                if event["type"] == "step":
                    yield f"data: {json.dumps({'step': event['step']})}\n\n"
                elif event["type"] == "answer_chunk":
                    yield f"data: {json.dumps({'answer_chunk': event['text']})}\n\n"
                elif event["type"] == "done":
                    result = event
        except llm.GatewayUnavailableError as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"
            return
        except Exception:  # noqa: BLE001 — never leak raw exception text (may contain tool XML)
            yield f"data: {json.dumps({'error': 'عذراً، حدث خطأ أثناء معالجة طلبك. يرجى المحاولة مرة أخرى.'})}\n\n"
            return

        session["pending_ask"] = "CompanyID" if result["needs_ask"] else None
        if result["needs_ask"]:
            yield f"data: {json.dumps({'needs_ask': result['needs_ask']})}\n\n"
        else:
            answer = result.get("answer")
            if answer is not None and not str(answer).strip():
                answer = None
            if req.session_id:
                session["last_turn"] = {
                    "client": client,
                    "company_id": session["conversation"].get("CompanyID"),
                    "question": req.question,
                    "answer_sql": result.get("answer_sql"),
                    "cache_key": result.get("cache_key"),
                }
            yield f"data: {json.dumps({
                'answer': answer,
                'answer_sql': result.get('answer_sql'),
                'table': result.get('table'), 'chart': result.get('chart'),
                'followups': result.get('followups') or [], 'sources': result.get('sources') or [],
            }, default=str)}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(stream(), media_type="text/event-stream")


@app.post("/feedback")
def feedback(req: FeedbackRequest):
    client = pinned_client()
    subject = hashlib.sha256(req.session_id.encode()).hexdigest()[:12]

    session = SESSIONS.get(req.session_id)
    turn = session.get("last_turn") if session else None
    if not turn or turn["client"] != client:
        raise HTTPException(status_code=404, detail="no recent answer on this session to give feedback on")

    company_id = turn.get("company_id")
    if company_id is None:
        company_id = _resolve_context_company_id(client, session.get("conversation", {}))
    if company_id is None:
        raise HTTPException(status_code=400, detail="CompanyID not resolved for this session")

    if req.helpful:
        if turn.get("answer_sql"):
            memory.promote_verified_query(
                client, company_id, turn["question"], turn["answer_sql"], source="user_feedback",
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
    gateway_url = os.environ.get("GATEWAY_URL", "http://localhost:20128/v1").rstrip("/")
    models_url = gateway_url if gateway_url.endswith("/models") else f"{gateway_url}/models"
    gateway_ok = False
    try:
        with urllib.request.urlopen(models_url, timeout=5) as resp:
            gateway_ok = getattr(resp, "status", 200) == 200
    except (urllib.error.URLError, TimeoutError):
        pass

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
        "gateway": gateway_ok,
        "ok": gateway_ok and clients.get(PINNED_CLIENT, {}).get("db", False),
        "pinned_client": PINNED_CLIENT,
        "clients": clients,
    }


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


app.mount("/", StaticFiles(directory=str(BASE_DIR / "static"), html=True), name="static")
