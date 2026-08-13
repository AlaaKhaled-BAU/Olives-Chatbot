"""Phase 7 acceptance: /health and /metrics wiring, plus (C7) the /ask SSE
frame sequence itself, mocked at agent.ask_stream so it runs without a live
gateway/DB (same boundary test_auth.py/test_feedback.py/test_session_memory.py
already mock for /ask's auth/session mechanics)."""
import json
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from fastapi.testclient import TestClient

from api.server import app, TOKEN_MAP

client = TestClient(app)
MOREC_TOKEN = next(t for t, c in TOKEN_MAP.items() if c == "morec")


def test_health_reports_per_client_db_and_gateway():
    """C9: /health used to hardcode a single representative client ("morec")
    -- now it must report EVERY configured client separately, not one
    combined guess, so a broken client-2 can't hide behind a healthy
    client-1."""
    resp = client.get("/health")
    assert resp.status_code == 200
    body = resp.json()
    assert set(body.keys()) == {"gateway", "ok", "clients"}
    assert isinstance(body["clients"], dict)
    assert "morec" in body["clients"], "the real configured test client must appear in the per-client map"
    for name, status in body["clients"].items():
        assert set(status.keys()) == {"db", "token_configured", "nullable_companyid_rows"}
        assert isinstance(status["nullable_companyid_rows"], dict)
    assert body["ok"] == (body["gateway"] and all(c["db"] for c in body["clients"].values()))


def test_ask_streams_step_and_answer_chunk_frames_before_the_final_answer():
    """C7's actual accept criteria: /ask must emit progress over time --
    step frames while tools run, then live answer_chunk frames -- not one
    frame at the end. Mocks agent.ask_stream with a realistic event
    sequence and asserts the raw SSE body carries every frame, in order,
    ending with the authoritative "answer" frame."""
    events = [
        {"type": "step", "step": "searching schema"},
        {"type": "step", "step": "running query 1 of 4"},
        {"type": "answer_chunk", "text": "There"},
        {"type": "answer_chunk", "text": " are 3"},
        {"type": "answer_chunk", "text": " companies."},
        {"type": "done", "answer": "There are 3 companies.", "needs_ask": None,
         "answer_sql": "SELECT COUNT(*) FROM t.Companies", "cache_key": "k1",
         "table": {"columns": ["n"], "rows": [[3]]}, "chart": None,
         "followups": ["How many last year?"], "sources": ["Companies"]},
    ]
    with patch("api.server.agent.ask_stream", return_value=events):
        resp = client.post("/ask", json={"question": "how many companies?", "session_id": "sse-test-1"},
                            headers={"authorization": f"Bearer {MOREC_TOKEN}"})
    assert resp.status_code == 200
    lines = [line for line in resp.text.split("\n\n") if line.startswith("data: ") and line != "data: [DONE]"]
    frames = [json.loads(line[len("data: "):]) for line in lines]
    assert frames == [
        {"step": "searching schema"},
        {"step": "running query 1 of 4"},
        {"answer_chunk": "There"},
        {"answer_chunk": " are 3"},
        {"answer_chunk": " companies."},
        # C8: the final frame also carries the structured envelope.
        {"answer": "There are 3 companies.", "table": {"columns": ["n"], "rows": [[3]]}, "chart": None,
         "followups": ["How many last year?"], "sources": ["Companies"]},
    ], "progress must arrive as separate frames over time, never collapsed into one"


def test_ask_table_with_a_datetime_value_does_not_crash_the_stream():
    """Real bug, caught live: a table's row values come straight from real
    SQL results and can be a datetime (e.g. any date-grouped query) --
    json.dumps() doesn't know how to serialize one on its own, and without
    default=str this crashed mid-stream, after the prose answer had
    already sent but before [DONE] or the envelope ever arrived (silently
    losing table/chart/sources/followups AND the feedback buttons, which
    only render on a successful "answer" frame)."""
    import datetime
    events = [
        {"type": "done", "answer": "3 orders in June.", "needs_ask": None,
         "answer_sql": "SELECT OrderDate, COUNT(*) FROM t.Orders GROUP BY OrderDate", "cache_key": "k1",
         "table": {"columns": ["OrderDate", "n"], "rows": [[datetime.date(2026, 6, 1), 3]]},
         "chart": None, "followups": [], "sources": ["Orders"]},
    ]
    with patch("api.server.agent.ask_stream", return_value=events):
        resp = client.post("/ask", json={"question": "orders by date", "session_id": "sse-test-2"},
                            headers={"authorization": f"Bearer {MOREC_TOKEN}"})
    assert resp.status_code == 200
    assert "data: [DONE]" in resp.text, "the stream must reach the end, not die mid-way on a non-JSON-native value"
    last_frame = json.loads([line for line in resp.text.split("\n\n")
                              if line.startswith("data: {\"answer\"")][0][len("data: "):])
    assert last_frame["table"]["rows"] == [["2026-06-01", 3]]


def test_metrics_is_prometheus_text_format():
    resp = client.get("/metrics")
    assert resp.status_code == 200
    assert "chatbot_requests_total" in resp.text


def test_static_index_served_at_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert "مساعد بيانات" in resp.text
