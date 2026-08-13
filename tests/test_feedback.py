"""C3: POST /feedback -- thumbs-up promotes a query to verified_queries,
thumbs-down clears its plan_cache entry. Mocks core.agent.ask (same
pattern as test_auth.py) so this runs without a live gateway/DB, and uses
an isolated sqlite file so it never touches the real work/cache.sqlite."""
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from fastapi.testclient import TestClient

import api.server as server
from api.server import TOKEN_MAP, app
from core import memory

client = TestClient(app)
MOREC_TOKEN = next(t for t, c in TOKEN_MAP.items() if c == "morec")
RUKN_TOKEN = next(t for t, c in TOKEN_MAP.items() if c == "rukn")


def _ask(session_id="s1", question="how many companies?", sql="SELECT COUNT(*) FROM t.Companies", token=MOREC_TOKEN):
    # C7: api/server.py now calls agent.ask_stream() (a generator yielding
    # step/answer_chunk/done events), not agent.ask() -- a one-item list
    # carrying just the "done" event mocks it at the new boundary.
    with patch.object(server.agent, "ask_stream", return_value=[{
        "type": "done", "answer": "There is 1 company.", "needs_ask": None,
        "answer_sql": sql, "cache_key": f"key-for-{session_id}",
    }]):
        resp = client.post("/ask", json={"question": question, "session_id": session_id},
                            headers={"authorization": f"Bearer {token}"})
        assert resp.status_code == 200
        list(resp.iter_lines())  # drain the SSE stream so session["last_turn"] is set before returning


def test_feedback_without_a_prior_ask_is_404(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    resp = client.post("/feedback", json={"session_id": "never-asked", "helpful": True},
                        headers={"authorization": f"Bearer {MOREC_TOKEN}"})
    assert resp.status_code == 404


def test_thumbs_up_promotes_the_query(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    _ask(session_id="up1")
    resp = client.post("/feedback", json={"session_id": "up1", "helpful": True},
                        headers={"authorization": f"Bearer {MOREC_TOKEN}"})
    assert resp.status_code == 200
    stored = memory.get_verified_query("morec", "how many companies?")
    assert stored["proc_or_sql"] == "SELECT COUNT(*) FROM t.Companies"
    assert len(memory.few_shots("morec")) == 1


def test_thumbs_down_clears_the_plan_cache_entry(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    memory.set_plan("key-for-down1", "morec", {"sql": "SELECT COUNT(*) FROM t.Companies"})
    _ask(session_id="down1")
    resp = client.post("/feedback", json={"session_id": "down1", "helpful": False},
                        headers={"authorization": f"Bearer {MOREC_TOKEN}"})
    assert resp.status_code == 200
    assert memory.get_plan("key-for-down1") is None
    assert memory.get_verified_query("morec", "how many companies?") is None, \
        "a thumbs-down must never promote anything"


def test_a_client_cannot_feed_back_on_another_clients_session(monkeypatch, tmp_path):
    """The session's own recorded client (set server-side during /ask) must
    match the feedback caller's token -- session_id alone is never enough,
    same 'token decides tenant' rule /ask already enforces."""
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    _ask(session_id="cross1", token=MOREC_TOKEN)
    resp = client.post("/feedback", json={"session_id": "cross1", "helpful": True},
                        headers={"authorization": f"Bearer {RUKN_TOKEN}"})
    assert resp.status_code == 404
    assert memory.get_verified_query("morec", "how many companies?") is None


def test_feedback_requires_a_token():
    resp = client.post("/feedback", json={"session_id": "s1", "helpful": True})
    assert resp.status_code == 401
