"""FIXPLAN M8 part 1: a session shouldn't be re-asked for CompanyID every
turn once it's been resolved once. Mocked at the agent.ask boundary since
morec and rukn are both single-company clients (company_scope: single) --
no real multi-company client exists to prove this against end-to-end, so
this simulates one the same way test_agent.py mocks core.llm.complete.

C6c: resolution is also mocked at params.discover_profile -- the real fix
validates a reply against the client's REAL (id, name) company set, which
morec/rukn (both single-company) can't provide, so a synthetic multi-
company profile is injected here to exercise the actual matching logic."""
import os
import sys
from pathlib import Path
from unittest.mock import patch

os.environ.setdefault("CHATBOT_CLIENT", "morec")

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from fastapi.testclient import TestClient

from api import server
from api.server import app, SESSIONS
from core.sessions import record_session_turn
from core import agent

client = TestClient(app)

_MULTI_COMPANY_PROFILE = {
    "CompanyID": "MULTI",
    "CompanyID": "MULTI",
    "_companies": [{"id": 3, "name": "Alpha Trading"}, {"id": 7, "name": "Beta Foods"}],
    "_companies": [{"id": 3, "name": "Alpha Trading"}, {"id": 7, "name": "Beta Foods"}],
}

_PROFILE_PATCHES = (
    "api.server.params.discover_profile",
    "api.server.params.discover_profile",
)


def _patch_profile():
    return patch("api.server.params.discover_profile", return_value=_MULTI_COMPANY_PROFILE)


def test_ask_pins_dropdown_company_without_listing_companies_in_chat():
    sid = "test-session-pin-default"
    SESSIONS.pop(sid, None)
    with patch("api.server.agent.ask_stream") as mock_ask, _patch_profile():
        mock_ask.return_value = _stream_of({"answer": "42 customers.", "needs_ask": None})
        _ask("how many customers?", sid)
        conv = mock_ask.call_args.kwargs["conversation"]
        assert conv.get("CompanyID") == 3 or conv.get("CompanyID") == 3
    SESSIONS.pop(sid, None)


def test_ask_body_company_id_overrides_default():
    sid = "test-session-pin-body"
    SESSIONS.pop(sid, None)
    with patch("api.server.agent.ask_stream") as mock_ask, _patch_profile():
        mock_ask.return_value = _stream_of({"answer": "ok", "needs_ask": None})
        client.post("/ask", json={"question": "q", "session_id": sid, "company_id": 7}).read()
        conv = mock_ask.call_args.kwargs["conversation"]
        assert conv.get("CompanyID") == 7 or conv.get("CompanyID") == 7
    SESSIONS.pop(sid, None)


def test_a_number_in_the_question_does_not_override_pinned_company():
    sid = "test-session-c6c-bad-number"
    SESSIONS.pop(sid, None)
    with patch("api.server.agent.ask_stream") as mock_ask, _patch_profile():
        mock_ask.return_value = _stream_of({"answer": "ok", "needs_ask": None})
        _ask("how many invoices in 2024?", sid)
        conv = mock_ask.call_args.kwargs["conversation"]
        assert conv.get("CompanyID") == 3 or conv.get("CompanyID") == 3
        assert conv.get("CompanyID") != 2024 and conv.get("CompanyID") != 2024
    SESSIONS.pop(sid, None)

def _stream_of(result):
    """C7: api/server.py now calls agent.ask_stream() (a generator), not
    agent.ask(). A list (not a real generator) so a mocked return_value can
    be read more than once without exhausting."""
    return [{"type": "done", **result}]


def _ask(question, session_id):
    headers = {"X-Session-Id": session_id or "anon"} if session_id else {}
    resp = client.post("/ask", json={"question": question, "session_id": session_id}, headers=headers)
    resp.read()  # force the StreamingResponse generator to actually run
    return resp


def test_different_session_is_not_contaminated():
    sid_a, sid_b = "test-session-m8-b1", "test-session-m8-b2"
    SESSIONS.pop(sid_a, None)
    SESSIONS.pop(sid_b, None)
    with patch("api.server.agent.ask_stream") as mock_ask, _patch_profile():
        mock_ask.return_value = _stream_of({"answer": "ok", "needs_ask": None})
        client.post("/ask", json={"question": "q", "session_id": sid_a, "company_id": 7}).read()
        assert mock_ask.call_args.kwargs["conversation"].get("CompanyID") == 7

        _ask("some other question", sid_b)
        # B never sent company_id=7 — default pin is first profile company (3).
        assert mock_ask.call_args.kwargs["conversation"].get("CompanyID") == 3
    SESSIONS.pop(sid_a, None)
    SESSIONS.pop(sid_b, None)
    SESSIONS.pop(sid_a, None)
    SESSIONS.pop(sid_b, None)


def test_touch_session_bounds_total_size():
    """C9: SESSIONS is a bounded LRU (SESSION_MAX entries), not an unbounded
    dict -- a flood of distinct session_ids (real or garbage) must not grow
    memory without bound; the oldest entry evicts first."""
    saved = dict(SESSIONS)
    SESSIONS.clear()
    try:
        added = [f"zz_bound_test_{i}" for i in range(server.SESSION_MAX + 5)]
        for sid in added:
            server._touch_session(sid, lambda: {"conversation": {}})
        assert len(SESSIONS) == server.SESSION_MAX
        assert added[0] not in SESSIONS, "oldest entry must have been evicted first"
        assert added[-1] in SESSIONS, "newest entry must survive"
    finally:
        SESSIONS.clear()
        SESSIONS.update(saved)


def test_touch_session_sweeps_idle_entries(monkeypatch):
    """A session untouched for longer than SESSION_IDLE_SECONDS must be
    swept on the next _touch_session call, not linger forever."""
    saved = dict(SESSIONS)
    SESSIONS.clear()
    fake_now = [1_000_000.0]
    monkeypatch.setattr(server.time, "time", lambda: fake_now[0])
    try:
        server._touch_session("zz_idle", lambda: {"conversation": {}})
        assert "zz_idle" in SESSIONS
        fake_now[0] += server.SESSION_IDLE_SECONDS + 1
        server._touch_session("zz_fresh", lambda: {"conversation": {}})
        assert "zz_idle" not in SESSIONS, "idle-expired entry must be swept"
        assert "zz_fresh" in SESSIONS
    finally:
        SESSIONS.clear()
        SESSIONS.update(saved)


def test_no_session_id_is_fully_stateless():
    with patch("api.server.agent.ask_stream") as mock_ask, \
         patch("api.server.params.discover_profile", return_value=_MULTI_COMPANY_PROFILE):
        mock_ask.return_value = _stream_of({"answer": None, "needs_ask": "Which company?"})
        _ask("q", None)
        mock_ask.return_value = _stream_of({"answer": "ok", "needs_ask": None})
        _ask("company 3", None)
        # with no session_id, each request is independent -- the "company 3"
        # reply was never associated with the prior needs_ask, so it must NOT
        # have resolved CompanyID (there's no session to have remembered
        # pending_ask against).
        assert mock_ask.call_args.kwargs["conversation"].get("CompanyID") == 3
    assert None not in SESSIONS


def test_record_session_turn_whitespace_question_returns_none():
    session: dict = {"transcript": [], "history": []}
    turn_id = record_session_turn(
        session,
        question="   ",
        result={"answer": "hi", "answer_sql": "", "cache_key": "k"},
        client="morec",
        company_id=1,
        max_history=agent.MAX_HISTORY_TURNS,
    )
    assert turn_id is None
    assert session["transcript"] == []
    assert session["history"] == []


def test_transcript_index_block_empty_returns_none():
    assert agent._transcript_index_block(None) is None
    assert agent._transcript_index_block([]) is None


def test_transcript_index_block_six_questions():
    transcript = [{"q": f"question {i}"} for i in range(6)]
    block = agent._transcript_index_block(transcript)
    assert block is not None
    assert "question 0" in block.split("\n")[1]
    assert len(block) <= 800


def test_transcript_index_block_25_keeps_first_and_last():
    transcript = [{"q": f"q{i}"} for i in range(25)]
    block = agent._transcript_index_block(transcript)
    assert block is not None
    lines = [ln for ln in block.split("\n") if ln and not ln.startswith("##")]
    assert lines[0] == "1. q0"
    assert lines[-1] == "25. q24"
    assert len(lines) == 20
    assert "q1" not in [ln.split(". ", 1)[1] for ln in lines]
    assert "q4" not in [ln.split(". ", 1)[1] for ln in lines]


def test_record_session_turn_six_turns_caps_history_not_transcript():
    session: dict = {}
    full_answer = "A" * 500
    for i in range(6):
        record_session_turn(
            session,
            question=f"q{i}",
            result={
                "answer": full_answer if i == 0 else f"ans{i}",
                "answer_sql": f"SELECT {i}",
                "cache_key": f"k{i}",
            },
            client="morec",
            company_id=1,
            max_history=agent.MAX_HISTORY_TURNS,
        )
    assert len(session["history"]) == 4
    assert len(session["transcript"]) == 6
    assert session["transcript"][0]["a"] == full_answer
    assert len(session["transcript"][0]["a"]) == 500
    assert session["history"][0]["a"] == "ans2"
    assert len(session["history"][-1]["a"]) <= 400
    assert session["transcript"][0]["sql"] == "SELECT 0"
    assert session["transcript"][0]["company_id"] == 1
    assert session["transcript"][0]["client"] == "morec"


def test_company_switch_clears_transcript():
    session = {
        "conversation": {"CompanyID": 1},
        "history": [{"q": "x"}],
        "transcript": [{"id": "t1"}],
        "thread_head": {"tax": "incl"},
    }
    server._set_session_company(session, session["conversation"], 2)
    assert session["transcript"] == []
    assert session["history"] == []
    assert "thread_head" not in session
