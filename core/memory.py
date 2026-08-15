"""SQLite memory: verified/negative queries, plan cache, result cache.
Cache keys include client+CompanyID+role+model (golden rule 7).
verified_queries written ONLY via promote_verified_query (thumbs-up / eval).
result_cache stores identical SQL row payloads for ~45s only — never treat
cached numbers or answer text as long-term truth."""
import hashlib
import json
import sqlite3
import time
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "work" / "cache.sqlite"

_SCHEMA = """
CREATE TABLE IF NOT EXISTS verified_queries (
    client TEXT NOT NULL,
    company_id INTEGER NOT NULL DEFAULT 0,
    question_norm TEXT NOT NULL,
    proc_or_sql TEXT NOT NULL,
    ok_count INTEGER NOT NULL DEFAULT 1,
    source TEXT NOT NULL DEFAULT 'unknown',
    PRIMARY KEY (client, company_id, question_norm)
);
CREATE TABLE IF NOT EXISTS negative_queries (
    client TEXT NOT NULL,
    company_id INTEGER NOT NULL,
    question_norm TEXT NOT NULL,
    proc_or_sql TEXT,
    reason TEXT,
    ts REAL NOT NULL,
    PRIMARY KEY (client, company_id, question_norm)
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
    for stmt in (
        "ALTER TABLE plan_cache ADD COLUMN client TEXT NOT NULL DEFAULT ''",
        "ALTER TABLE verified_queries ADD COLUMN source TEXT NOT NULL DEFAULT 'unknown'",
        "ALTER TABLE verified_queries ADD COLUMN company_id INTEGER NOT NULL DEFAULT 0",
    ):
        try:
            conn.execute(stmt)
        except sqlite3.OperationalError:
            pass
    conn.execute(
        "CREATE VIRTUAL TABLE IF NOT EXISTS verified_queries_fts USING fts5("
        "question_norm, proc_or_sql, client UNINDEXED, company_id UNINDEXED)"
    )
    # backfill fts if empty
    try:
        count = conn.execute("SELECT COUNT(*) FROM verified_queries_fts").fetchone()[0]
        if count == 0:
            rows = conn.execute(
                "SELECT client, company_id, question_norm, proc_or_sql FROM verified_queries "
                "WHERE source IN ('user_feedback', 'eval')"
            ).fetchall()
            for r in rows:
                conn.execute(
                    "INSERT INTO verified_queries_fts (question_norm, proc_or_sql, client, company_id) "
                    "VALUES (?, ?, ?, ?)",
                    (r[2], r[3], r[0], str(r[1])),
                )
    except sqlite3.OperationalError:
        pass
    return conn


def normalize_question(question: str) -> str:
    return " ".join(question.strip().lower().split())


def cache_key(client: str, company_id, role: str, model: str, question: str, schema_version: str = "") -> str:
    raw = "|".join([str(client), str(company_id), str(role), str(model),
                     normalize_question(question), str(schema_version)])
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def result_cache_key(client: str, company_id: int, sql: str) -> str:
    raw = f"result|{client}|{company_id}|{sql.strip().lower()}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def promote_verified_query(client: str, company_id: int, question: str, proc_or_sql: str, source: str):
    q = normalize_question(question)
    conn = _conn()
    try:
        conn.execute(
            "INSERT INTO verified_queries (client, company_id, question_norm, proc_or_sql, ok_count, source) "
            "VALUES (?, ?, ?, ?, 1, ?) "
            "ON CONFLICT(client, company_id, question_norm) DO UPDATE SET "
            "proc_or_sql = excluded.proc_or_sql, ok_count = ok_count + 1, source = excluded.source",
            (client, int(company_id), q, proc_or_sql, source),
        )
        conn.execute("DELETE FROM verified_queries_fts WHERE client = ? AND company_id = ? AND question_norm = ?",
                     (client, str(company_id), q))
        conn.execute(
            "INSERT INTO verified_queries_fts (question_norm, proc_or_sql, client, company_id) VALUES (?, ?, ?, ?)",
            (q, proc_or_sql, client, str(company_id)),
        )
        conn.commit()
    finally:
        conn.close()


def promote_negative_query(client: str, company_id: int, question: str, proc_or_sql: str | None, reason: str | None = None):
    q = normalize_question(question)
    conn = _conn()
    try:
        conn.execute(
            "INSERT INTO negative_queries (client, company_id, question_norm, proc_or_sql, reason, ts) "
            "VALUES (?, ?, ?, ?, ?, ?) "
            "ON CONFLICT(client, company_id, question_norm) DO UPDATE SET "
            "proc_or_sql = excluded.proc_or_sql, reason = excluded.reason, ts = excluded.ts",
            (client, int(company_id), q, proc_or_sql, reason, time.time()),
        )
        conn.commit()
    finally:
        conn.close()


def get_verified_query(client: str, company_id: int, question: str):
    q = normalize_question(question)
    conn = _conn()
    try:
        row = conn.execute(
            "SELECT proc_or_sql, ok_count FROM verified_queries "
            "WHERE client = ? AND company_id = ? AND question_norm = ?",
            (client, int(company_id), q),
        ).fetchone()
        return {"proc_or_sql": row[0], "ok_count": row[1]} if row else None
    finally:
        conn.close()


def few_shots(client: str, company_id: int, question: str = "", limit: int = 3) -> list:
    """FTS few-shots for this client + CompanyID only."""
    conn = _conn()
    try:
        if question:
            q_norm = normalize_question(question)
            terms = [t for t in q_norm.split() if len(t) >= 3]
            match_expr = " OR ".join(f'"{t}"' for t in terms[:8]) if terms else q_norm
            try:
                rows = conn.execute(
                    "SELECT f.question_norm, f.proc_or_sql FROM verified_queries_fts f "
                    "JOIN verified_queries v ON v.client = f.client "
                    "AND v.company_id = CAST(f.company_id AS INTEGER) "
                    "AND v.question_norm = f.question_norm "
                    "WHERE f.client = ? AND f.company_id = ? AND v.source IN ('user_feedback', 'eval') "
                    "AND verified_queries_fts MATCH ? "
                    "ORDER BY rank LIMIT ?",
                    (client, str(int(company_id)), match_expr, limit),
                ).fetchall()
                if rows:
                    return [{"question": r[0], "proc_or_sql": r[1]} for r in rows]
            except sqlite3.OperationalError:
                pass
        rows = conn.execute(
            "SELECT question_norm, proc_or_sql FROM verified_queries "
            "WHERE client = ? AND company_id = ? AND source IN ('user_feedback', 'eval') "
            "ORDER BY ok_count DESC LIMIT ?",
            (client, int(company_id), limit),
        ).fetchall()
        return [{"question": r[0], "proc_or_sql": r[1]} for r in rows]
    finally:
        conn.close()


def negative_shots(client: str, company_id: int, question: str = "", limit: int = 2) -> list:
    conn = _conn()
    try:
        rows = conn.execute(
            "SELECT question_norm, proc_or_sql, reason FROM negative_queries "
            "WHERE client = ? AND company_id = ? ORDER BY ts DESC LIMIT ?",
            (client, int(company_id), limit * 3),
        ).fetchall()
        if not question:
            return [{"question": r[0], "proc_or_sql": r[1], "reason": r[2]} for r in rows[:limit]]
        q_tokens = set(normalize_question(question).split())
        scored = []
        for r in rows:
            overlap = len(q_tokens & set(r[0].split()))
            if overlap:
                scored.append((overlap, r))
        scored.sort(key=lambda x: -x[0])
        return [{"question": r[0], "proc_or_sql": r[1], "reason": r[2]} for _, r in scored[:limit]]
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
    conn = _conn()
    try:
        conn.execute("DELETE FROM plan_cache WHERE key = ?", (key,))
        conn.commit()
    finally:
        conn.close()


def clear_plan_cache(client: str):
    conn = _conn()
    try:
        cur = conn.execute("DELETE FROM plan_cache WHERE client = ?", (client,))
        conn.commit()
        return cur.rowcount
    finally:
        conn.close()


def get_result(key: str, ttl_seconds: int = 300):
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
