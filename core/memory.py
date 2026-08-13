"""SQLite memory (PLAN.md Phase 5): verified queries (procedural few-shots),
plan cache, result cache. Cache keys MUST include client+CompanyID+role+model
(golden rule 7) -- a cache-key bug here is a tenant leak, not a stale
answer. Exact-match only, never semantic/embedding (would confuse customer
4022 with 4023).

C3 (2026-07-26): verified_queries used to be written by core/agent.py on
EVERY answered question, with no correctness signal at all -- a confidently
wrong query got stored under the name "verified", and since few_shots()
orders by ok_count DESC and the old writer incremented it on every repeat,
a wrong query asked twice climbed ABOVE a correct one asked once. Fixed by
splitting what "cheap to regenerate" (plan_cache, may still be written
automatically) from what "trusted enough to teach the model from"
(verified_queries, written ONLY by promote_verified_query -- called from an
explicit user thumbs-up or a passing eval, never from the agent's own
success path). plan_cache also gained schema_version in its key: a stale
cached plan from before a schema change (renamed column, dropped table)
must never silently reuse the old shape -- setup/refresh.py clears it
after rebuilding schema_cache.json."""
import hashlib
import json
import sqlite3
import time
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "work" / "cache.sqlite"

_SCHEMA = """
CREATE TABLE IF NOT EXISTS verified_queries (
    client TEXT NOT NULL,
    question_norm TEXT NOT NULL,
    proc_or_sql TEXT NOT NULL,
    ok_count INTEGER NOT NULL DEFAULT 1,
    source TEXT NOT NULL DEFAULT 'unknown',
    PRIMARY KEY (client, question_norm)
);
CREATE TABLE IF NOT EXISTS plan_cache (
    key TEXT PRIMARY KEY,
    client TEXT NOT NULL DEFAULT '',
    plan TEXT NOT NULL,
    ts REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS result_cache (
    key TEXT PRIMARY KEY,
    rows TEXT NOT NULL,
    ts REAL NOT NULL
);
"""


def _conn():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(_SCHEMA)
    # C3: CREATE TABLE IF NOT EXISTS leaves an already-existing pre-C3
    # cache.sqlite (client-less plan_cache, source-less verified_queries)
    # untouched -- additive migration for a file that predates this
    # column, silently a no-op (existing column) for one that doesn't.
    for stmt in (
        "ALTER TABLE plan_cache ADD COLUMN client TEXT NOT NULL DEFAULT ''",
        "ALTER TABLE verified_queries ADD COLUMN source TEXT NOT NULL DEFAULT 'unknown'",
    ):
        try:
            conn.execute(stmt)
        except sqlite3.OperationalError:
            pass  # column already exists
    return conn


def normalize_question(question: str) -> str:
    return " ".join(question.strip().lower().split())


def cache_key(client: str, company_id, role: str, model: str, question: str, schema_version: str = "") -> str:
    """Exact-match key ONLY -- client+CompanyID+role+model+question_norm+
    schema_version. Never a semantic/embedding key (golden rule 7): that
    would confuse customer 4022 with 4023. schema_version defaults to ""
    for callers that don't have one yet (a bare miss is always safe --
    worse case is a cache miss, never a wrong hit)."""
    raw = "|".join([str(client), str(company_id), str(role), str(model),
                     normalize_question(question), str(schema_version)])
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def promote_verified_query(client: str, question: str, proc_or_sql: str, source: str):
    """The ONLY writer for verified_queries -- callers must state WHY this
    is trusted (source is required, not defaulted, so a future accidental
    call from the agent's own success path can't silently reintroduce C3's
    bug). Known sources: "user_feedback" (an explicit thumbs-up on a real
    answer) and "eval" (a passing evals/accuracy.jsonl case, see C3a)."""
    q = normalize_question(question)
    conn = _conn()
    try:
        conn.execute(
            "INSERT INTO verified_queries (client, question_norm, proc_or_sql, ok_count, source) "
            "VALUES (?, ?, ?, 1, ?) "
            "ON CONFLICT(client, question_norm) DO UPDATE SET "
            "proc_or_sql = excluded.proc_or_sql, ok_count = ok_count + 1, source = excluded.source",
            (client, q, proc_or_sql, source),
        )
        conn.commit()
    finally:
        conn.close()


def get_verified_query(client: str, question: str):
    q = normalize_question(question)
    conn = _conn()
    try:
        row = conn.execute(
            "SELECT proc_or_sql, ok_count FROM verified_queries WHERE client = ? AND question_norm = ?",
            (client, q),
        ).fetchone()
        return {"proc_or_sql": row[0], "ok_count": row[1]} if row else None
    finally:
        conn.close()


def few_shots(client: str, limit: int = 5):
    """Most-reused verified queries for this client, as few-shot examples.
    Trustworthy now that promote_verified_query is the only writer (C3) --
    ok_count DESC used to be gameable by asking a wrong query repeatedly.
    source filter excludes legacy rows written by the old agent-side
    auto-write (source='unknown' after the migration in _conn()) -- those
    were written under exactly the bug this fix closes, with no real
    correctness signal behind their ok_count. They'll come back on their
    own via promote_verified_query the moment they're genuinely confirmed
    (a thumbs-up, or turning up in evals/accuracy.jsonl)."""
    conn = _conn()
    try:
        rows = conn.execute(
            "SELECT question_norm, proc_or_sql FROM verified_queries "
            "WHERE client = ? AND source IN ('user_feedback', 'eval') "
            "ORDER BY ok_count DESC LIMIT ?",
            (client, limit),
        ).fetchall()
        return [{"question": r[0], "proc_or_sql": r[1]} for r in rows]
    finally:
        conn.close()


def get_plan(key: str):
    conn = _conn()
    try:
        row = conn.execute("SELECT plan FROM plan_cache WHERE key = ?", (key,)).fetchone()
        return json.loads(row[0]) if row else None
    finally:
        conn.close()


def set_plan(key: str, client: str, plan):
    """client is stored (not just baked into the opaque key) so
    clear_plan_cache(client) can sweep a single client's entries after a
    schema refresh without needing to recompute every possible key."""
    conn = _conn()
    try:
        conn.execute(
            "INSERT INTO plan_cache (key, client, plan, ts) VALUES (?, ?, ?, ?) "
            "ON CONFLICT(key) DO UPDATE SET client = excluded.client, plan = excluded.plan, ts = excluded.ts",
            (key, client, json.dumps(plan), time.time()),
        )
        conn.commit()
    finally:
        conn.close()


def delete_plan(key: str):
    """Thumbs-down on a cached-plan answer: remove just that one entry, not
    the whole client's cache -- other cached questions may still be fine."""
    conn = _conn()
    try:
        conn.execute("DELETE FROM plan_cache WHERE key = ?", (key,))
        conn.commit()
    finally:
        conn.close()


def clear_plan_cache(client: str):
    """setup/refresh.py calls this after rebuilding schema_cache.json --
    schema_version in the key already stops an old-shape plan from being
    matched by a new query, but old rows would otherwise accumulate in the
    table forever with no cleanup path."""
    conn = _conn()
    try:
        cur = conn.execute("DELETE FROM plan_cache WHERE client = ?", (client,))
        conn.commit()
        return cur.rowcount
    finally:
        conn.close()


def get_result(key: str, ttl_seconds: int = 300):
    """Closed-period questions only, short TTL -- callers decide what counts
    as closed-period; this just enforces the expiry once cached."""
    conn = _conn()
    try:
        row = conn.execute("SELECT rows, ts FROM result_cache WHERE key = ?", (key,)).fetchone()
        if not row:
            return None
        rows_json, ts = row
        if time.time() - ts > ttl_seconds:
            return None
        return json.loads(rows_json)
    finally:
        conn.close()


def set_result(key: str, rows):
    conn = _conn()
    try:
        conn.execute(
            "INSERT INTO result_cache (key, rows, ts) VALUES (?, ?, ?) "
            "ON CONFLICT(key) DO UPDATE SET rows = excluded.rows, ts = excluded.ts",
            (key, json.dumps(rows, default=str), time.time()),
        )
        conn.commit()
    finally:
        conn.close()
