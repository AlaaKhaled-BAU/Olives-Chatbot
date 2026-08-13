"""FIXPLAN M3: /ask is rate-limited per bearer token (30/minute), so one
client (or a runaway loop) can't drain the model budget for everyone.
Uses distinct fake tokens from tests/test_auth.py's real ones so the two
files' request counts never share a slowapi bucket."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from fastapi.testclient import TestClient

from api.server import app

client = TestClient(app)


def _burst(token: str, n: int):
    return [
        client.post("/ask", json={"question": "hi"}, headers={"authorization": f"Bearer {token}"}).status_code
        for _ in range(n)
    ]


def test_burst_past_limit_gets_429():
    codes = _burst("RATE_LIMIT_TEST_TOKEN_A", 35)
    assert codes[:30] == [403] * 30  # under budget: token is bogus but that's checked AFTER the limiter
    assert all(c == 429 for c in codes[30:])


def test_different_token_is_a_separate_bucket():
    # token A above is already over budget; a different token must be unaffected.
    codes = _burst("RATE_LIMIT_TEST_TOKEN_B", 3)
    assert codes == [403, 403, 403]  # rejected for being a bad token, NOT 429
