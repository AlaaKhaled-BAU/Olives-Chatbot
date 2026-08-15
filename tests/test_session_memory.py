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

client = TestClient(app)

_MULTI_COMPANY_PROFILE = {
    "CompanyID": "MULTI",
    "_companies": [{"id": 3, "name": "Alpha Trading"}, {"id": 7, "name": "Beta Foods"}],
}

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


def test_needs_ask_then_number_resolves_then_sticks():
    sid = "test-session-m8-a"
    SESSIONS.pop(sid, None)
    with patch("api.server.agent.ask_stream") as mock_ask, \
         patch("api.server.params.discover_profile", return_value=_MULTI_COMPANY_PROFILE):
        # turn 1: simulate a MULTI-company client asking which company
        mock_ask.return_value = _stream_of({"answer": None, "needs_ask": "Which company should I look at? Options: Alpha Trading (3)، Beta Foods (7)"})
        _ask("how many customers?", sid)
        assert mock_ask.call_args.kwargs["conversation"] == {}  # nothing resolved yet

        # turn 2: user answers with a REAL company id -- must be resolved
        # INTO conversation before this call, and the clarifying loop must end.
        mock_ask.return_value = _stream_of({"answer": "42 customers.", "needs_ask": None})
        _ask("company 7", sid)
        assert mock_ask.call_args.kwargs["conversation"] == {"CompanyID": 7}

        # turn 3: same session, unrelated question -- must NOT be re-asked;
        # CompanyID must still be there without the user repeating it.
        mock_ask.return_value = _stream_of({"answer": "some answer", "needs_ask": None})
        _ask("and how many salespersons?", sid)
        assert mock_ask.call_args.kwargs["conversation"] == {"CompanyID": 7}
    SESSIONS.pop(sid, None)


def test_a_number_that_is_not_a_real_company_id_never_resolves():
    """C6c's actual measured bug: "how many invoices in 2024" was
    previously accepted as CompanyID=2024 because the old resolver grabbed
    ANY digit in the message. 2024 is not one of this client's real
    company IDs -- must be rejected, leaving the clarifying loop open
    rather than silently scoping every later answer to a nonexistent
    company."""
    sid = "test-session-c6c-bad-number"
    SESSIONS.pop(sid, None)
    with patch("api.server.agent.ask_stream") as mock_ask, \
         patch("api.server.params.discover_profile", return_value=_MULTI_COMPANY_PROFILE):
        mock_ask.return_value = _stream_of({"answer": None, "needs_ask": "Which company should I look at?"})
        _ask("how many customers?", sid)

        mock_ask.return_value = _stream_of({"answer": None, "needs_ask": "Which company should I look at?"})
        _ask("how many invoices in 2024?", sid)
        assert mock_ask.call_args.kwargs["conversation"] == {}, \
            "2024 must never be accepted as a CompanyID just because it's a number in the message"
    SESSIONS.pop(sid, None)


def test_company_name_also_resolves():
    """The plan's stated fix isn't just 'a real ID' -- a name match must
    work too, case-insensitively."""
    sid = "test-session-c6c-name"
    SESSIONS.pop(sid, None)
    with patch("api.server.agent.ask_stream") as mock_ask, \
         patch("api.server.params.discover_profile", return_value=_MULTI_COMPANY_PROFILE):
        mock_ask.return_value = _stream_of({"answer": None, "needs_ask": "Which company?"})
        _ask("q", sid)
        mock_ask.return_value = _stream_of({"answer": "ok", "needs_ask": None})
        _ask("beta foods please", sid)
        assert mock_ask.call_args.kwargs["conversation"] == {"CompanyID": 7}
    SESSIONS.pop(sid, None)


def test_different_session_is_not_contaminated():
    sid_a, sid_b = "test-session-m8-b1", "test-session-m8-b2"
    SESSIONS.pop(sid_a, None)
    SESSIONS.pop(sid_b, None)
    with patch("api.server.agent.ask_stream") as mock_ask, \
         patch("api.server.params.discover_profile", return_value=_MULTI_COMPANY_PROFILE):
        mock_ask.return_value = _stream_of({"answer": None, "needs_ask": "Which company?"})
        _ask("q", sid_a)
        mock_ask.return_value = _stream_of({"answer": "ok", "needs_ask": None})
        _ask("company 3", sid_a)
        assert mock_ask.call_args.kwargs["conversation"] == {"CompanyID": 3}

        # session B has never been told a company -- must start empty, not
        # inherit session A's CompanyID=3.
        _ask("some other question", sid_b)
        assert mock_ask.call_args.kwargs["conversation"] == {}
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
        assert mock_ask.call_args.kwargs["conversation"] == {}
    assert None not in SESSIONS
