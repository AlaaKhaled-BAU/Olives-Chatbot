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
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "work" / "sessions.sqlite"
IDLE_SECONDS = 3600
MAX_SESSIONS = 5000

_SCHEMA = (
    "CREATE TABLE IF NOT EXISTS sessions ("
    " sid TEXT PRIMARY KEY,"
    " data TEXT NOT NULL,"
    " touched REAL NOT NULL)"
)

_lock = threading.Lock()


def _conn() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA busy_timeout=5000")
    conn.execute(_SCHEMA)
    return conn


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
