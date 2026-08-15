"""FIXPLAN M3: /ask rate-limited per session_id (30/minute)."""
import os
import sys
from pathlib import Path
from unittest.mock import patch

os.environ.setdefault("CHATBOT_CLIENT", "morec")

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from fastapi.testclient import TestClient

from api.server import app

client = TestClient(app)


def _burst(session_id: str, n: int):
    with patch("api.server.agent.ask_stream", return_value=[{"type": "done", "answer": "ok", "needs_ask": None}]):
        return [
            client.post(
                "/ask",
                json={"question": "hi", "session_id": session_id},
                headers={"X-Session-Id": session_id},
            ).status_code
            for _ in range(n)
        ]


def test_burst_past_limit_gets_429():
    codes = _burst("RATE_LIMIT_SESSION_A", 35)
    assert codes[:30] == [200] * 30
    assert all(c == 429 for c in codes[30:])


def test_different_session_is_a_separate_bucket():
    codes = _burst("RATE_LIMIT_SESSION_B", 3)
    assert codes == [200, 200, 200]
