"""FIXPLAN M1: /ask must be reachable only with a valid per-client bearer
token, and the token -- never the request body -- decides the tenant.
Mocks core.agent.ask so this runs without a live gateway/DB (test_api.py's
own reason for not exercising /ask directly no longer applies once the real
call is mocked out)."""
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from fastapi.testclient import TestClient

from api.server import app, TOKEN_MAP

client = TestClient(app)
MOREC_TOKEN = next(t for t, c in TOKEN_MAP.items() if c == "morec")
RUKN_TOKEN = next(t for t, c in TOKEN_MAP.items() if c == "rukn")


def _stream_of(result):
    """C7: api/server.py now calls agent.ask_stream() (a generator), not
    agent.ask(). A list (not a real generator) so a mocked return_value
    can be read more than once without exhausting."""
    return [{"type": "done", **result}]


def test_no_token_is_401():
    resp = client.post("/ask", json={"question": "hi"})
    assert resp.status_code == 401


def test_wrong_token_is_403():
    resp = client.post("/ask", json={"question": "hi"}, headers={"authorization": "Bearer WRONG"})
    assert resp.status_code == 403


def test_malformed_scheme_is_401():
    resp = client.post("/ask", json={"question": "hi"}, headers={"authorization": "Basic WRONG"})
    assert resp.status_code == 401


def test_bearer_with_no_token_is_401():
    resp = client.post("/ask", json={"question": "hi"}, headers={"authorization": "Bearer"})
    assert resp.status_code == 401


def test_token_decides_tenant_body_is_ignored():
    """The core adversarial case: a valid morec token with a body that lies
    and claims client=rukn must still resolve to morec, server-side."""
    with patch("api.server.agent.ask_stream") as mock_ask:
        mock_ask.return_value = _stream_of({"answer": "ok", "needs_ask": None})
        resp = client.post(
            "/ask",
            json={"client": "rukn", "question": "hi"},
            headers={"authorization": f"Bearer {MOREC_TOKEN}"},
        )
        assert resp.status_code == 200
        assert mock_ask.call_args[0][0] == "morec"  # first positional arg = client


def test_each_token_maps_to_its_own_client():
    with patch("api.server.agent.ask_stream") as mock_ask:
        mock_ask.return_value = _stream_of({"answer": "ok", "needs_ask": None})
        client.post("/ask", json={"question": "hi"}, headers={"authorization": f"Bearer {RUKN_TOKEN}"})
        assert mock_ask.call_args[0][0] == "rukn"
