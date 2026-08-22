"""Pytest setup — pin CHATBOT_CLIENT before api.server import."""
import os
from unittest.mock import patch

import pytest

os.environ.setdefault("CHATBOT_CLIENT", "morec")
# Hermetic tests mock llm._client; the key guard only checks presence.
os.environ.setdefault("DEEPSEEK_API_KEY", "test-key-dummy")


@pytest.fixture(autouse=True)
def _isolated_session_store(tmp_path, monkeypatch):
    """Every test gets its own sessions.sqlite — the server's write-through
    must never leak conversation state between tests or across runs."""
    from core import sessions
    monkeypatch.setattr(sessions, "DB_PATH", tmp_path / "sessions.sqlite")

# Tenant pack live probes call sql.run_select; keep agent tests deterministic.
patch("core.tenant_pack._live_facts", return_value={}).start()
