"""C3: POST /feedback — thumbs-up promotes; thumbs-down stores negative."""
import os
import sys
from pathlib import Path
from unittest.mock import patch

os.environ.setdefault("CHATBOT_CLIENT", "morec")

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from fastapi.testclient import TestClient

import api.server as server
from api.server import app
from core import memory

client = TestClient(app)


def _ask(session_id="s1", question="how many companies?", sql="SELECT COUNT(*) FROM t.Companies"):
    with patch.object(server.agent, "ask_stream", return_value=[{
        "type": "done", "answer": "There is 1 company.", "needs_ask": None,
        "answer_sql": sql, "cache_key": f"key-for-{session_id}",
    }]):
        resp = client.post("/ask", json={"question": question, "session_id": session_id},
                            headers={"X-Session-Id": session_id})
        assert resp.status_code == 200
        list(resp.iter_lines())


def test_feedback_without_a_prior_ask_is_404(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    resp = client.post("/feedback", json={"session_id": "never-asked", "helpful": True},
                        headers={"X-Session-Id": "never-asked"})
    assert resp.status_code == 404


def test_thumbs_up_promotes_the_query(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    _ask(session_id="up1")
    resp = client.post("/feedback", json={"session_id": "up1", "helpful": True},
                        headers={"X-Session-Id": "up1"})
    assert resp.status_code == 200
    stored = memory.get_verified_query("morec", 1, "how many companies?")
    assert stored["proc_or_sql"] == "SELECT COUNT(*) FROM t.Companies"
    assert len(memory.few_shots("morec", 1)) == 1


def test_thumbs_down_clears_plan_and_stores_negative(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    memory.set_plan("key-for-down1", "morec", {"sql": "SELECT COUNT(*) FROM t.Companies"})
    _ask(session_id="down1")
    resp = client.post("/feedback", json={"session_id": "down1", "helpful": False, "reason": "wrong"},
                        headers={"X-Session-Id": "down1"})
    assert resp.status_code == 200
    assert memory.get_plan("key-for-down1") is None
    assert memory.get_verified_query("morec", 1, "how many companies?") is None
    negs = memory.negative_shots("morec", 1)
    assert len(negs) == 1
    assert negs[0]["reason"] == "wrong"


def test_feedback_requires_prior_ask_on_session():
    resp = client.post("/feedback", json={"session_id": "ghost", "helpful": True})
    assert resp.status_code == 404
