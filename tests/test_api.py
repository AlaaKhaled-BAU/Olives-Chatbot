"""Phase 7 acceptance: /health, /metrics, /ask SSE, /context."""
import json
import sys
import types
from pathlib import Path
from unittest.mock import patch

import os

os.environ.setdefault("CHATBOT_CLIENT", "morec")

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from fastapi.testclient import TestClient

from api.server import app
from core import llm
from api.server import SESSIONS

client = TestClient(app)


def test_health_reports_pinned_client():
    resp = client.get("/health")
    assert resp.status_code == 200
    body = resp.json()
    assert "pinned_client" in body
    assert body["pinned_client"] == os.environ["CHATBOT_CLIENT"]
    for name, status in body["clients"].items():
        assert "pinned" in status
        assert "nullable_companyid_rows" in status


def test_health_provider_probe_via_llm_module():
    """/health asks core.llm.provider_health (DeepSeek /models) — no gateway."""
    with patch("api.server.llm.provider_health", return_value=True):
        resp = client.get("/health")
    assert resp.status_code == 200
    body = resp.json()
    assert body["provider"] is True
    assert "gateway" not in body


def test_context_endpoint_returns_shape():
    with patch("api.server._context_payload", return_value={
        "client": "morec", "company_id": 1, "company": {"ID": 1, "Name": "Test"},
        "companies": [{"id": 1, "name": "Test"}], "clients_active": [{"CompanyID": 1, "ClientID": 1}],
        "multi_company": False,
    }):
        resp = client.get("/context?session_id=s1")
    assert resp.status_code == 200
    data = resp.json()
    assert data["company_id"] == 1
    assert data["clients_active"][0]["ClientID"] == 1
    assert data["transcript"] == []


def test_context_without_session_id_has_empty_transcript():
    resp = client.get("/context")
    assert resp.status_code == 200
    assert resp.json()["transcript"] == []


def test_context_loads_companies_from_db():
  class FakeCursor:
      def __init__(self, rows):
          self._rows = rows

      def execute(self, sql):
          self._sql = sql

      def fetchall(self):
          return self._rows

  class FakeConn:
      def cursor(self, as_dict=True):
          return FakeCursor([{"ID": 2, "Name": "Live Co"}])

      def close(self):
          pass

  with patch("api.server.params.discover_profile", return_value={"_companies": [{"id": 2, "name": "Stale"}]}):
      with patch("api.server.sql.get_conn", return_value=FakeConn()):
          with patch("api.server.sql.set_tenant"):
              companies = __import__("api.server", fromlist=["_load_companies_live"])._load_companies_live(
                  "morec", {}
              )
  assert companies == [{"id": 2, "name": "Live Co"}]


def test_ask_done_sse_includes_tools_ms():
    events = [
        {"type": "done", "answer": "ok", "needs_ask": None,
         "answer_sql": "SELECT 1", "cache_key": "k1",
         "tools_ms": {"search_docs": 42}},
    ]
    with patch("api.server.agent.ask_stream", return_value=events):
        resp = client.post("/ask", json={"question": "test", "session_id": "tools-ms-test"})
    assert resp.status_code == 200
    lines = [line for line in resp.text.split("\n\n") if line.startswith("data: ") and line != "data: [DONE]"]
    frames = [json.loads(line[len("data: "):]) for line in lines]
    assert "tools_ms" in frames[-1]
    assert frames[-1]["tools_ms"] == {"search_docs": 42}


def test_ask_done_sse_tools_ms_defaults_to_empty_dict():
    events = [
        {"type": "done", "answer": "ok", "needs_ask": None,
         "answer_sql": "SELECT 1", "cache_key": "k1"},
    ]
    with patch("api.server.agent.ask_stream", return_value=events):
        resp = client.post("/ask", json={"question": "test", "session_id": "tools-ms-empty"})
    lines = [line for line in resp.text.split("\n\n") if line.startswith("data: ") and line != "data: [DONE]"]
    frames = [json.loads(line[len("data: "):]) for line in lines]
    assert frames[-1].get("tools_ms") == {}


def test_ask_streams_step_and_answer_chunk_frames_before_the_final_answer():
    events = [
        {"type": "step", "step": "searching schema"},
        {"type": "answer_chunk", "text": "There are 3 companies."},
        {"type": "done", "answer": "There are 3 companies.", "needs_ask": None,
         "answer_sql": "SELECT COUNT(*) FROM t.Companies", "cache_key": "k1",
         "table": None, "chart": None, "followups": [], "sources": ["Companies"]},
    ]
    with patch("api.server.agent.ask_stream", return_value=events):
        resp = client.post("/ask", json={"question": "how many companies?", "session_id": "sse-test-1"},
                            headers={"X-Session-Id": "sse-test-1"})
    assert resp.status_code == 200
    lines = [line for line in resp.text.split("\n\n") if line.startswith("data: ") and line != "data: [DONE]"]
    frames = [json.loads(line[len("data: "):]) for line in lines]
    assert frames[-1]["answer_sql"] == "SELECT COUNT(*) FROM t.Companies"


def test_ask_table_with_a_datetime_value_does_not_crash_the_stream():
    import datetime
    events = [
        {"type": "done", "answer": "3 orders in June.", "needs_ask": None,
         "answer_sql": "SELECT OrderDate, COUNT(*) FROM t.Orders GROUP BY OrderDate", "cache_key": "k1",
         "table": {"columns": ["OrderDate", "n"], "rows": [[datetime.date(2026, 6, 1), 3]]},
         "chart": None, "followups": [], "sources": ["Orders"]},
    ]
    with patch("api.server.agent.ask_stream", return_value=events):
        resp = client.post("/ask", json={"question": "orders by date", "session_id": "sse-test-2"})
    assert resp.status_code == 200
    assert "data: [DONE]" in resp.text


def test_metrics_is_prometheus_text_format():
    resp = client.get("/metrics")
    assert resp.status_code == 200
    assert "chatbot_requests_total" in resp.text


def test_ask_provider_unavailable_returns_arabic_error_and_done_sentinel():
    def boom(*args, **kwargs):
        raise llm.ProviderUnavailableError(llm.PROVIDER_UNAVAILABLE_AR)

    with patch("api.server.agent.ask_stream", side_effect=boom):
        resp = client.post("/ask", json={"question": "test", "session_id": "gw-down"})
    assert resp.status_code == 200
    assert resp.headers["x-accel-buffering"] == "no"
    lines = [line for line in resp.text.split("\n\n") if line.startswith("data: ") and line != "data: [DONE]"]
    frames = [json.loads(line[len("data: "):]) for line in lines]
    assert frames[0]["error"] == llm.PROVIDER_UNAVAILABLE_AR
    # B1: the [DONE] sentinel must close EVERY stream, including error paths.
    assert "data: [DONE]" in resp.text


def test_ask_generic_error_also_closes_with_done_sentinel():
    def boom(*args, **kwargs):
        raise RuntimeError("internal detail that must never leak")

    with patch("api.server.agent.ask_stream", side_effect=boom):
        resp = client.post("/ask", json={"question": "test", "session_id": "generic-err"})
    assert resp.status_code == 200
    assert "internal detail" not in resp.text
    assert resp.text.rstrip().endswith("data: [DONE]")


def test_static_index_served_at_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert "مساعد بيانات" in resp.text
    assert "رمز الدخول" not in resp.text


def test_six_asks_transcript_keeps_six_history_keeps_four():
    sid = "test-six-asks-transcript"
    SESSIONS.pop(sid, None)
    captured: list = []

    def fake_stream(*args, **kwargs):
        captured.append(kwargs.get("history"))
        i = len(captured) - 1
        answer = "A" * 500 if i == 0 else f"ans{i}"
        return [{"type": "done", "answer": answer, "needs_ask": None,
                 "answer_sql": f"SELECT {i}", "cache_key": f"k{i}"}]

    with patch("api.server.agent.ask_stream", side_effect=fake_stream):
        for i in range(6):
            resp = client.post("/ask", json={"question": f"q{i}", "session_id": sid},
                               headers={"X-Session-Id": sid})
            resp.read()

    ctx = client.get(f"/context?session_id={sid}").json()
    assert len(ctx["transcript"]) == 6
    assert ctx["transcript"][0]["a"] == "A" * 500
    assert ctx["transcript"][0]["sql"] == "SELECT 0"
    assert len(captured[5]) == 4
    SESSIONS.pop(sid, None)
