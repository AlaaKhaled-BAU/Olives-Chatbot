"""Live-proven regression (q13, post-swap extreme test): plan-cache replay
MUST NOT precede the empty-calendar guard, and relative-date questions must
never replay plans whose SQL bakes in dates from a previous day."""
import sys
import types
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core import agent, memory


def _plain(content):
    return types.SimpleNamespace(choices=[types.SimpleNamespace(message=types.SimpleNamespace(content=content))])


def _chunk(text):
    delta = types.SimpleNamespace(content=text, tool_calls=None, reasoning_content=None)
    return types.SimpleNamespace(choices=[types.SimpleNamespace(delta=delta)])


def _fake_llm(final_text, contract_json='{"followups": [], "confidence": null, "refusal": false}'):
    """stream=True -> chunk iterable (the turn); otherwise the E1 contract call."""
    def _complete(messages, **kwargs):
        if kwargs.get("stream"):
            return iter([_chunk(final_text)])
        return _plain(contract_json)
    return _complete


def _seed_plan(client, company_id, question, queries):
    cache = agent._schema_cache(client)
    key = agent.memory.cache_key(client, company_id, "manager", agent.MODEL_ALIAS,
                                 question, agent._schema_version(cache))
    agent.memory.set_plan(key, client, {"queries": queries})


RELATIVE_Q = "كم مبيعات هذا الشهر؟"
STALE_SQL = "SELECT 999 AS stale_from_july"


def test_relative_date_question_never_replays_cached_plan(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    _seed_plan("morec", 1, RELATIVE_Q, [STALE_SQL])
    ran = []
    monkeypatch.setattr(agent.sql, "run_select",
                        lambda sql_text, *a, **k: (ran.append(sql_text), [{"d": None, "x": 1}])[1])
    monkeypatch.setattr(agent.llm, "complete", _fake_llm("إجابة كاملة من النموذج."))

    events = list(agent.ask_stream("morec", RELATIVE_Q, conversation={"CompanyID": 1}))
    done = [e for e in events if e["type"] == "done"][0]

    assert STALE_SQL not in ran, "cached July-dated SQL was replayed for a relative-date question"
    assert done["answer"] == "إجابة كاملة من النموذج.", "expected the full-turn path, not a replay"


def test_calendar_guard_fires_even_when_a_cached_plan_exists(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    _seed_plan("morec", 1, "كم عدد الفواتير هذا الشهر؟", [STALE_SQL])
    monkeypatch.setattr(agent, "_empty_calendar_needs_ask", lambda *a, **k: "GUARD_MSG")
    llm_calls = []
    monkeypatch.setattr(agent.llm, "complete", lambda *a, **k: llm_calls.append(1))

    events = list(agent.ask_stream("morec", "كم عدد الفواتير هذا الشهر؟",
                                   conversation={"CompanyID": 1}))
    done = [e for e in events if e["type"] == "done"][0]

    assert done["needs_ask"] == "GUARD_MSG" and done["answer"] is None
    assert llm_calls == [], "guard must short-circuit before any LLM call"


def test_absolute_date_question_still_replays_cached_plan(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    q = "كم عدد الزبائن الإجمالي حتى تاريخ 2025-07-15؟"
    _seed_plan("morec", 1, q, ["SELECT COUNT(*) AS n FROM t.Customers"])
    monkeypatch.setattr(agent, "_empty_calendar_needs_ask", lambda *a, **k: None)
    monkeypatch.setattr(agent.sql, "run_select", lambda sql_text, *a, **k: [{"n": 7}])
    monkeypatch.setattr(agent.llm, "complete", _fake_llm("يوجد 7 عملاء."))

    events = list(agent.ask_stream("morec", q, conversation={"CompanyID": 1}))
    done = [e for e in events if e["type"] == "done"][0]

    assert "7" in (done["answer"] or "")
    assert done["answer_sql"] == "SELECT COUNT(*) AS n FROM t.Customers"
