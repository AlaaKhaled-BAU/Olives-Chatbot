"""A+ transcript recall: overlap ranker, digit-stripped hints, tool latch."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core import agent, docs


def _turns(*pairs):
    """pairs: (q, a, sql) """
    out = []
    for i, (q, a, sql) in enumerate(pairs, 1):
        out.append({"id": f"t{i}", "q": q, "a": a, "sql": sql})
    return out


def test_fold_tokens_strips_al():
    toks = docs.fold_tokens("المندوب أحمد")
    assert "مندوب" in toks
    assert "أحمد" in toks or "احمد" in toks


def test_recall_skips_last_four_and_ranks_older():
    transcript = _turns(
        ("مبيعات يوليو 2025 للمندوب أحمد القدسي", "المجموع 99999", "SELECT SUM(x) FROM t.Y WHERE SalesmanID=3003 AND d>='2025-07-01'"),
        ("كم عميل؟", "12", "SELECT COUNT(*) FROM t.Customers"),
        ("كم صنف؟", "3", "SELECT COUNT(*) FROM t.Items"),
        ("كم مسار؟", "4", "SELECT COUNT(*) FROM t.DeliveryRoute"),
        ("كم فاتورة؟", "5", "SELECT COUNT(*) FROM t.TransactionsHeaders"),
        ("كم طلب؟", "6", "SELECT COUNT(*) FROM t.SalesOrder"),
    )
    hits = agent.recall_turns(transcript, "نفس المندوب أحمد الشهر الحالي")
    assert hits
    assert hits[0]["i"] == 1
    assert "3003" in hits[0]["sql"]
    assert "99999" not in hits[0]["entities_hint"]
    assert hits[0]["i"] != 6


def test_recall_empty_on_no_overlap():
    transcript = _turns(
        ("كم عميل؟", "1", "SELECT 1"),
        ("كم صنف؟", "2", "SELECT 2"),
        ("كم مسار؟", "3", "SELECT 3"),
        ("كم فاتورة؟", "5", "SELECT 4"),
        ("كم طلب؟", "6", "SELECT 5"),
    )
    assert agent.recall_turns(transcript, "xyzzy-no-match-zzzz") == []


def test_entities_hint_strips_digits():
    assert "430" not in agent._entities_hint("صافي 12430 عبر 38 فاتورة")
    assert "فاتورة" in agent._entities_hint("صافي 12430 عبر 38 فاتورة")


def test_recall_hidden_after_business_rows():
    state = {
        "queries": ["SELECT 1"],
        "had_business_rows": True,
        "fast_count": False,
        "report_path": False,
        "howto_path": False,
        "doc_searches": 0,
        "vault_searches": 0,
        "docs_only": False,
        "question": "نفس المندوب",
    }
    names = {t["function"]["name"] for t in agent._active_tools(state)}
    assert "recall_turns" not in names
    assert "run_select" in names


def test_recall_offered_before_business_rows():
    state = {
        "queries": [],
        "had_business_rows": False,
        "fast_count": False,
        "report_path": False,
        "howto_path": False,
        "doc_searches": 0,
        "vault_searches": 0,
        "docs_only": False,
        "question": "نفس المندوب",
    }
    names = {t["function"]["name"] for t in agent._active_tools(state)}
    assert "recall_turns" in names


def test_run_tool_recall_uses_state_transcript():
    transcript = _turns(
        ("مبيعات يوليو للمندوب سامي", "100", "SELECT SalesmanID=7"),
        ("a", "1", "SELECT 1"),
        ("b", "2", "SELECT 2"),
        ("c", "3", "SELECT 3"),
        ("d", "4", "SELECT 4"),
    )
    state = {"transcript": transcript, "question": "نفس المندوب"}
    result = agent._run_tool(
        "recall_turns", {"query": "نفس المندوب سامي"},
        {}, {}, [], 1, "morec", state,
    )
    assert state["recall_used"] is True
    assert result["hits"][0]["sql"].find("7") >= 0


def test_needs_recall_nudge_when_history_has_no_overlap():
    history = [{"q": "كم عميل؟", "sql": "SELECT COUNT(*) FROM t.Customers"}] * 4
    assert agent._needs_recall_nudge("نفس المندوب قارن يوليو", history)
    history2 = [{"q": "مبيعات المندوب أحمد", "sql": "SELECT 1"}] * 4
    assert not agent._needs_recall_nudge("نفس المندوب أحمد", history2)
