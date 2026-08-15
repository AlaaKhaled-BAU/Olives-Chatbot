"""Wave 1: no bearer auth; CHATBOT_CLIENT env-pinned tenant."""
import os
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

os.environ.setdefault("CHATBOT_CLIENT", "morec")

from fastapi.testclient import TestClient  # noqa: E402

from api.server import app, PINNED_CLIENT  # noqa: E402

client = TestClient(app)


def _stream_of(result):
    return [{"type": "done", **result}]


def test_no_bearer_required():
    with patch("api.server.agent.ask_stream") as mock_ask:
        mock_ask.return_value = _stream_of({"answer": "ok", "needs_ask": None})
        resp = client.post("/ask", json={"question": "hi", "session_id": "auth-none"})
        assert resp.status_code == 200


def test_body_client_field_is_ignored():
    with patch("api.server.agent.ask_stream") as mock_ask:
        mock_ask.return_value = _stream_of({"answer": "ok", "needs_ask": None})
        resp = client.post(
            "/ask",
            json={"client": "rukn", "question": "hi", "session_id": "auth-ignore"},
        )
        assert resp.status_code == 200
        assert mock_ask.call_args[0][0] == PINNED_CLIENT


def test_unknown_chatbot_client_fails_startup():
    with pytest.raises(RuntimeError, match="CHATBOT_CLIENT"):
        import importlib
        import api.server as srv
        with patch.dict(os.environ, {"CHATBOT_CLIENT": "nonexistent_client_xyz"}):
            # re-validate helper directly
            from api.server import _validate_client_name
            _validate_client_name("nonexistent_client_xyz")
