"""Session persistence: conversations survive restarts (plan TRACK E).

Backing store is work/sessions.sqlite in WAL mode — safe for multiple
uvicorn workers on ONE machine (busy_timeout arbitrates writers); the
in-memory dict in api/server.py stays as the hot read-cache with
write-through on every mutation. NOT shared across machines.
"""
import json
import sqlite3
import threading
import time
import uuid
from pathlib import Path

TRANSCRIPT_CAP = 100

import os

DB_PATH = Path(__file__).resolve().parent.parent / "work" / "sessions.sqlite"

def _db_path() -> Path:
    env_work = os.environ.get("CHATBOT_WORK_DIR")
    if env_work:
        return Path(env_work) / "sessions.sqlite"
    return DB_PATH

IDLE_SECONDS = 30 * 86400  # 30 days retention for chat histories
MAX_SESSIONS = 5000

_SCHEMA = (
    "CREATE TABLE IF NOT EXISTS sessions ("
    " sid TEXT PRIMARY KEY,"
    " data TEXT NOT NULL,"
    " touched REAL NOT NULL)"
)

_lock = threading.Lock()


def _conn() -> sqlite3.Connection:
    p = _db_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(p, timeout=10)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA busy_timeout=5000")
    conn.execute(_SCHEMA)
    return conn


def record_session_turn(
    session: dict,
    *,
    question: str,
    result: dict,
    client: str,
    company_id,
    max_history: int,
) -> str | None:
    """Append UI transcript (full text) and model history (compressed).
    Returns turn_id or None if there is no answer to record.
    result is the ask_stream `done` event dict.
    max_history must equal agent.MAX_HISTORY_TURNS.
    """
    if not str(question or "").strip():
        return None
    answer = result.get("answer")
    if answer is None or not str(answer).strip():
        return None
    turn_id = uuid.uuid4().hex
    sql_full = result.get("answer_sql") or ""
    session.setdefault("transcript", [])
    session["transcript"].append({
        "id": turn_id,
        "q": question,
        "a": str(answer),
        "sql": sql_full,
        "ts": time.time(),
        "cache_key": result.get("cache_key"),
        "client": client,
        "company_id": company_id,
    })
    del session["transcript"][:-TRANSCRIPT_CAP]
    hist = session.setdefault("history", [])
    hist.append({
        "q": question,
        "a": str(answer)[:400],
        "sql": sql_full[:200],
    })
    del hist[:-max_history]
    if result.get("thread_head"):
        session["thread_head"] = result["thread_head"]
    return turn_id


def load(sid: str) -> dict | None:
    with _lock:
        conn = _conn()
        try:
            row = conn.execute("SELECT data FROM sessions WHERE sid=?", (sid,)).fetchone()
            return json.loads(row[0]) if row else None
        finally:
            conn.close()


def save(sid: str, data: dict) -> None:
    payload = json.dumps(data, default=str)
    now = time.time()
    with _lock:
        conn = _conn()
        try:
            conn.execute(
                "INSERT INTO sessions(sid, data, touched) VALUES (?, ?, ?) "
                "ON CONFLICT(sid) DO UPDATE SET data=excluded.data, touched=excluded.touched",
                (sid, payload, now),
            )
            conn.commit()
        finally:
            conn.close()


def delete(sid: str) -> None:
    with _lock:
        conn = _conn()
        try:
            conn.execute("DELETE FROM sessions WHERE sid=?", (sid,))
            conn.commit()
        finally:
            conn.close()


def list_sessions(limit: int = 50) -> list[dict]:
    """Return past chat session summaries ordered by most recently touched."""
    with _lock:
        conn = _conn()
        try:
            cur = conn.execute(
                "SELECT sid, data, touched FROM sessions ORDER BY touched DESC LIMIT ?",
                (limit,),
            )
            out = []
            for sid, raw, touched in cur.fetchall():
                try:
                    data = json.loads(raw)
                except Exception:
                    continue
                transcript = data.get("transcript") or []
                if not transcript:
                    continue
                first_q = str(transcript[0].get("q") or "").strip()
                title = data.get("title") or first_q
                if len(title) > 40:
                    title = title[:40].rstrip() + "..."
                if not title:
                    title = "محادثة سابقة"
                out.append({
                    "id": sid,
                    "title": title,
                    "touched": touched,
                    "turns": len(transcript),
                })
            return out
        finally:
            conn.close()


def sweep(idle_seconds: int | None = None) -> int:
    """Delete sessions idle longer than the window; returns rows removed."""
    if idle_seconds is None:
        idle_seconds = IDLE_SECONDS
    cutoff = time.time() - idle_seconds
    with _lock:
        conn = _conn()
        try:
            cur = conn.execute("DELETE FROM sessions WHERE touched < ?", (cutoff,))
            conn.commit()
            n = conn.execute("SELECT COUNT(*) FROM sessions").fetchone()[0]
            if n > MAX_SESSIONS:
                conn.execute(
                    "DELETE FROM sessions WHERE sid IN ("
                    " SELECT sid FROM sessions ORDER BY touched ASC LIMIT ?)",
                    (n - MAX_SESSIONS,),
                )
                conn.commit()
            return cur.rowcount
        finally:
            conn.close()
