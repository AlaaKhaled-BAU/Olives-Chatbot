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


def test_health_gateway_probes_models_not_liveliness():
    """OmniRoute exposes /v1/models (200) but not /health/liveliness."""
    from contextlib import contextmanager

    @contextmanager
    def fake_urlopen(url, timeout=5):
        assert url.endswith("/models")
        yield types.SimpleNamespace(status=200)

    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
        resp = client.get("/health")
    assert resp.status_code == 200
    body = resp.json()
    assert body["gateway"] is True


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


def test_ask_gateway_unavailable_returns_arabic_error():
    def boom(*args, **kwargs):
        raise llm.GatewayUnavailableError(llm.GATEWAY_UNAVAILABLE_AR)

    with patch("api.server.agent.ask_stream", side_effect=boom):
        resp = client.post("/ask", json={"question": "test", "session_id": "gw-down"})
    assert resp.status_code == 200
    lines = [line for line in resp.text.split("\n\n") if line.startswith("data: ") and line != "data: [DONE]"]
    frames = [json.loads(line[len("data: "):]) for line in lines]
    assert frames[0]["error"] == llm.GATEWAY_UNAVAILABLE_AR


def test_static_index_served_at_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert "مساعد بيانات" in resp.text
    assert "رمز الدخول" not in resp.text
