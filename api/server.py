"""FastAPI service (PLAN.md Phase 7): POST /ask (SSE), GET /health,
GET /metrics, serves static/ (the chat UI)."""
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
from fastapi import FastAPI, Header, HTTPException, Request, Response  # noqa: E402
from fastapi.responses import StreamingResponse  # noqa: E402
from fastapi.staticfiles import StaticFiles  # noqa: E402
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest  # noqa: E402
from pydantic import BaseModel  # noqa: E402
from slowapi import Limiter, _rate_limit_exceeded_handler  # noqa: E402
from slowapi.errors import RateLimitExceeded  # noqa: E402
from slowapi.util import get_remote_address  # noqa: E402

from core import agent, config, memory, params, sql, trace  # noqa: E402

app = FastAPI()


def _rl_key(request: Request) -> str:
    """Rate-limit bucket = the bearer token (so it's per-CLIENT, not per-IP --
    several users behind one office NAT shouldn't share a budget). Falls back
    to remote address only for unauthenticated requests, which 401 anyway."""
    return request.headers.get("authorization", get_remote_address(request))


limiter = Limiter(key_func=_rl_key)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


def _token_map() -> dict:
    """bearer token -> client name. Built once at startup from clients/*.yaml
    (FIXPLAN M1) -- a client is reachable only by knowing its own token; the
    request body's `client` field is never trusted for tenant selection.

    C2 (2026-07-26): the token VALUE never lives in clients/*.yaml (that file
    is git-tracked; two real tokens were previously committed there in
    plaintext). Each client config instead names an env var
    (`api_token_env`), and the value is read from the environment here --
    populate it from client-chatbot/.env (gitignored) via
    `set -a && source .env && set +a` before starting the server, same
    convention as gateway/.env. A client naming an env var that is unset is
    fail-closed: it's excluded from TOKEN_MAP entirely (unreachable, never
    reachable with an empty/default token) and a warning is printed so a
    misconfigured client doesn't silently disappear."""
    m = {}
    for p in (BASE_DIR / "clients").glob("*.yaml"):
        if p.stem.startswith("_"):
            continue
        cfg = yaml.safe_load(p.read_text()) or {}
        env_name = cfg.get("api_token_env")
        if not env_name:
            print(f"[server] WARNING: {p.name} has no api_token_env -- this client is unreachable", file=sys.stderr)
            continue
        tok = os.environ.get(env_name)
        if not tok:
            print(f"[server] WARNING: {p.name} names api_token_env={env_name!r} but it is unset -- "
                  f"this client is unreachable until it's set (not defaulted to empty/reachable)", file=sys.stderr)
            continue
        m[tok] = p.stem
    return m


TOKEN_MAP = _token_map()  # ponytail: built once at startup; restart to add a client


def _client_from_auth(authorization: str | None) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="missing bearer token")
    client = TOKEN_MAP.get(authorization.removeprefix("Bearer "))
    if not client:
        raise HTTPException(status_code=403, detail="invalid token")
    return client


class AskRequest(BaseModel):
    question: str
    client: str | None = None      # IGNORED -- kept only so old bodies don't 422
    session_id: str | None = None


# FIXPLAN M8 part 1: session_id -> {"conversation": {...}, "pending_ask": str|None}.
# ponytail: in-memory dict, single process, lost on restart -- fine for pilot; a
# real deployment behind multiple workers would need this in memory.py's sqlite
# (or redis) instead. Only clients that pass a session_id opt into this at all;
# omitting it keeps today's fully-stateless behavior.
#
# C9: bounded LRU (SESSION_MAX entries) with idle expiry -- an unbounded dict
# keyed by client-chosen session_id is an unbounded-memory-growth risk (every
# distinct id, real or garbage, gets an entry forever). OrderedDict gives
# recency order for free via move_to_end()/popitem(last=False); a per-entry
# "_touched" wall-clock stamp (not exposed to clients) handles idle expiry,
# which recency order alone can't ("least recently used" isn't "how long ago").
SESSIONS: OrderedDict = OrderedDict()
SESSION_MAX = 500
SESSION_IDLE_SECONDS = 3600  # 1 hour
_NUMBER_RE = re.compile(r"\d+")


def _touch_session(session_id: str, default_factory) -> dict:
    """Fetch-or-create session_id's entry, marking it most-recently-used and
    sweeping idle/excess entries. The sweep piggybacks on real request
    traffic rather than a background thread -- no thread lifecycle to manage,
    and cost is proportional to expired entries, not wall-clock time."""
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
    """C6c: match against the REAL (id, name) set only -- the fixed bug was
    accepting ANY digit in the message as a CompanyID ("how many invoices
    in 2024" silently resolving CompanyID=2024, then every later answer in
    that session silently scoped to a nonexistent company). An exact
    known ID wins first; otherwise a case-insensitive substring match on
    the company name (Arabic has no case distinction, so this needs no
    special-casing there -- but it is still a plain substring match, not
    fuzzy/diacritic-normalized). No match at all returns None rather than
    guessing, and the caller must leave CompanyID unresolved so the next
    turn re-asks with the same valid-options list instead of silently
    scoping to the wrong company."""
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
    """If the previous turn asked a clarifying CompanyID question, try to
    resolve THIS message against the client's real company list. No real
    multi-company client exists yet to validate this against live -- morec
    and rukn are both company_scope: single (see setup/02_introspect.py's
    probe_profile) -- so this is honestly untested against real multi-
    company data, only against the resolution mechanism itself."""
    if session.get("pending_ask") == "CompanyID":
        profile = params.discover_profile(client)
        companies = profile.get("_companies") or []
        match = _match_company(question, companies)
        if match is not None:
            session["conversation"]["CompanyID"] = match
        # else: leave conversation untouched. params.resolve() hits
        # NEEDS_ASK again on the next turn, re-prompting with the same
        # valid-options list -- never silently accepts a bare number that
        # isn't a real ID, and never leaves the client stuck with no
        # explanation either.


@app.post("/ask")
@limiter.limit("30/minute")
def ask(request: Request, req: AskRequest, authorization: str | None = Header(default=None)):
    client = _client_from_auth(authorization)   # token decides tenant, NOT the body
    # FIXPLAN M4: audit identity = a hash of the token, never the token itself
    # (the trace file must not become a second copy of live credentials).
    subject = hashlib.sha256(authorization.encode()).hexdigest()[:12]

    session = _touch_session(req.session_id, lambda: {"conversation": {}, "pending_ask": None}) \
        if req.session_id else {"conversation": {}, "pending_ask": None}
    _apply_pending_answer(session, req.question, client)

    def stream():
        # C7: real progress, not one frame at the end. agent.ask_stream()
        # yields {"step": ...} between tool calls and {"answer_chunk": ...}
        # live as the final answer streams from the gateway -- never tool-
        # call arguments or SQL text (that leaks schema shape and other
        # clients' branch structure), only a human-readable activity label.
        result = None
        try:
            for event in agent.ask_stream(client, req.question, conversation=session["conversation"], subject=subject):
                if event["type"] == "step":
                    yield f"data: {json.dumps({'step': event['step']})}\n\n"
                elif event["type"] == "answer_chunk":
                    yield f"data: {json.dumps({'answer_chunk': event['text']})}\n\n"
                elif event["type"] == "done":
                    result = event
        except Exception as e:  # noqa: BLE001 - surface as an SSE error event, not a 500 mid-stream
            yield f"data: {json.dumps({'error': str(e)})}\n\n"
            return

        session["pending_ask"] = "CompanyID" if result["needs_ask"] else None
        if result["needs_ask"]:
            yield f"data: {json.dumps({'needs_ask': result['needs_ask']})}\n\n"
        else:
            # C3: remembered server-side (never trust a client-supplied SQL/
            # question for /feedback) so a thumbs-up/down can act on THIS
            # exact turn without the client needing to echo anything back
            # beyond session_id. Only real turns with a session_id at all --
            # a sessionless request already opts out of state by design.
            if req.session_id:
                session["last_turn"] = {
                    "client": client, "question": req.question,
                    "answer_sql": result.get("answer_sql"), "cache_key": result.get("cache_key"),
                }
            # Full text sent once more, authoritative -- the client already
            # has it assembled from answer_chunk events, this is a snap-to-
            # correct safety net (and what a non-streaming consumer reads).
            # C8: table/chart/followups/sources -- .get() with an empty
            # default since the needs_ask/refusal paths never built an
            # envelope (nothing to show a table/chart/followups for).
            # default=str: a table's row values come straight from real SQL
            # results and can be a datetime/Decimal/etc, never JSON-native
            # on their own (confirmed live -- a date-grouped query crashed
            # this exact yield before this fix).
            yield f"data: {json.dumps({
                'answer': result['answer'],
                'table': result.get('table'), 'chart': result.get('chart'),
                'followups': result.get('followups') or [], 'sources': result.get('sources') or [],
            }, default=str)}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(stream(), media_type="text/event-stream")


class FeedbackRequest(BaseModel):
    session_id: str
    helpful: bool


@app.post("/feedback")
def feedback(req: FeedbackRequest, authorization: str | None = Header(default=None)):
    """Thumbs-up promotes the just-answered turn's query to verified_queries
    (source="user_feedback") -- the ONLY other legitimate promotion path
    besides evals/run_evals.py's eval-seeding (C3). Thumbs-down deletes that
    turn's plan_cache entry (so the same wrong plan isn't served again) and
    logs the question for review. Token-authenticated like /ask, and the
    session's own recorded client must match the token's -- session_id is
    never enough on its own, same "token decides tenant" rule as /ask."""
    client = _client_from_auth(authorization)
    subject = hashlib.sha256(authorization.encode()).hexdigest()[:12]

    session = SESSIONS.get(req.session_id)
    turn = session.get("last_turn") if session else None
    if not turn or turn["client"] != client:
        raise HTTPException(status_code=404, detail="no recent answer on this session to give feedback on")

    if req.helpful:
        if turn.get("answer_sql"):
            memory.promote_verified_query(client, turn["question"], turn["answer_sql"], source="user_feedback")
    else:
        if turn.get("cache_key"):
            memory.delete_plan(turn["cache_key"])
        trace.log_event(client, turn["question"], event="feedback_negative", subject=subject)

    return {"ok": True}


def _client_names() -> list:
    return sorted(p.stem for p in (BASE_DIR / "clients").glob("*.yaml") if not p.stem.startswith("_"))


@app.get("/health")
def health():
    gateway_ok = False
    try:
        with urllib.request.urlopen("http://localhost:4000/health/liveliness", timeout=5):
            gateway_ok = True
    except (urllib.error.URLError, TimeoutError):
        pass

    # C9: was hardcoded to a single representative client ("morec") -- with
    # more than one real client this silently reported "healthy" while a
    # different client's DB/token was actually broken. Now iterates every
    # clients/*.yaml the same way _token_map() does.
    clients = {}
    for name in _client_names():
        db_ok = False
        try:
            conn = sql.get_conn(name)
            conn.cursor().execute("SELECT 1")
            conn.close()
            db_ok = True
        except Exception:  # noqa: BLE001 - health check reports status, doesn't raise
            pass

        # C0: nullable_companyid_rows is pre-computed at introspection time
        # (SA context, cheap to read here vs re-querying every table's row
        # count on every health hit). Non-zero means those rows are safely
        # invisible through every t. view (fail-closed, not a leak) but
        # silently missing from any answer that touches them -- surfaced so
        # that's a known, visible condition rather than a silent
        # under-reporting risk nobody's watching.
        nullable_companyid_rows = {}
        try:
            cache = json.loads((config.work_dir(name) / "schema_cache.json").read_text())
            nullable_companyid_rows = cache.get("nullable_companyid_rows", {})
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        clients[name] = {
            "db": db_ok,
            "token_configured": name in TOKEN_MAP.values(),
            "nullable_companyid_rows": nullable_companyid_rows,
        }

    return {
        "gateway": gateway_ok,
        "ok": gateway_ok and all(c["db"] for c in clients.values()),
        "clients": clients,
    }


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


app.mount("/", StaticFiles(directory=str(BASE_DIR / "static"), html=True), name="static")
