"""Phase 8 acceptance: the isolation release gate actually gates. Runs the
real isolation.jsonl against the live wall/gate/catalog (same as
evals/run_evals.py) and separately proves the leak-detection logic itself
would catch a real leak, so a future change that silently breaks detection
(not just breaks the wall) gets caught too."""
import json
import re
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "evals"))
import run_evals  # noqa: E402
from core import memory  # noqa: E402

EVALS_DIR = Path(__file__).resolve().parent.parent / "evals"


def test_isolation_corpus_fully_blocked_live():
    leaks = run_evals.run_isolation()
    assert leaks == [], f"isolation leak(s) detected: {leaks}"


def test_leak_detection_catches_an_entitled_proc(monkeypatch):
    """If catalog.for_client() ever mis-entitles a client-named proc, this
    must show up as a LEAK, not silently pass."""
    leaked_proc = "dbo.AX_Integ_SendPayments_AbuTawileh"  # the one isolation.jsonl probes
    monkeypatch.setattr(run_evals.catalog, "for_client", lambda *a, **k: {leaked_proc: []})
    leaks = run_evals.run_isolation()
    assert "client_named_proc_probe" in leaks


def test_leak_detection_catches_real_rows_from_wrong_tenant(monkeypatch):
    """If run_select ever returned rows for the wrong tenant, this must be
    reported as a LEAK, not silently pass."""
    monkeypatch.setattr(run_evals.sql, "run_select", lambda *a, **k: [{"leaked": True}])
    leaks = run_evals.run_isolation()
    assert len(leaks) >= 1


def test_passing_case_promotes_its_query_with_eval_source(monkeypatch, tmp_path):
    """C3a: a passing, non-refusal accuracy case with a real answer_sql
    must be promoted to verified_queries with source="eval" -- this is
    what keeps the few-shot pool alive now that C3 correctly stopped
    trusting raw agent traffic (users click thumbs-up rarely, so without
    this the pool would otherwise just stay empty)."""
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    monkeypatch.setattr(run_evals, "_load",
                         lambda name: [{"name": "t", "client": "morec", "question": "how many companies?",
                                        "expect_contains": ["1"]}])
    with patch.object(run_evals.agent, "ask", return_value={
        "answer": "There is 1 company.", "needs_ask": None,
        "answer_sql": "SELECT COUNT(*) FROM t.Companies",
    }):
        run_evals.run_accuracy()

    stored = memory.get_verified_query("morec", 1, "how many companies?")
    assert stored["proc_or_sql"] == "SELECT COUNT(*) FROM t.Companies"
    shots = memory.few_shots("morec", 1)
    assert len(shots) == 1, "an eval-promoted query must feed few_shots (source='eval' is in the trusted set)"


def test_failing_case_never_promotes(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    monkeypatch.setattr(run_evals, "_load",
                         lambda name: [{"name": "t", "client": "morec", "question": "how many companies?",
                                        "expect_contains": ["999"]}])
    with patch.object(run_evals.agent, "ask", return_value={
        "answer": "There is 1 company.", "needs_ask": None,
        "answer_sql": "SELECT COUNT(*) FROM t.Companies",
    }):
        run_evals.run_accuracy()

    assert memory.get_verified_query("morec", 1, "how many companies?") is None


def test_refusal_case_never_promotes_even_if_marked_ok(monkeypatch, tmp_path):
    """A refusal has no meaningful SQL to teach the model from -- must
    never be promoted even though it correctly counts as a PASS."""
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    monkeypatch.setattr(run_evals, "_load",
                         lambda name: [{"name": "t", "client": "morec", "question": "nonsense question",
                                        "expect_refusal": True}])
    with patch.object(run_evals.agent, "ask", return_value={
        "answer": "I cannot answer that.", "needs_ask": None, "answer_sql": "SELECT 1",
    }):
        run_evals.run_accuracy()

    assert memory.get_verified_query("morec", 1, "nonsense question") is None


def test_wave5_corpus_is_arabic_with_company_id():
    cases = run_evals._load(run_evals.WAVE5_CASES_FILE)
    assert len(cases) >= 14
    for case in cases:
        assert case["lang"] == "ar", f"{case['name']} must be Arabic"
        assert case["company_id"] == 2, f"{case['name']} must scope CompanyID=2"
        assert case["client"] == "105"
        # Arabic script present in every question
        assert re.search(r"[\u0600-\u06FF]", case["question"]), case["question"]


def test_wave5_sales_ground_truth_is_238_not_261():
    yaml_text = (EVALS_DIR / "wave5.yaml").read_text()
    assert "sales_invoices_non_void: 238" in yaml_text
    assert "transactions_headers_all_types: 261" in yaml_text

    cases = run_evals._load(run_evals.WAVE5_CASES_FILE)
    sales_case = next(c for c in cases if c["name"] == "w5_non_void_sales_invoices_ar")
    assert sales_case["expect_contains"] == ["238"]
    assert "261" in sales_case["expect_not_contains"]


def test_expect_not_contains_rejects_all_transactions_total():
    case = {
        "expect_contains": ["238"],
        "expect_not_contains": ["261"],
    }
    ok_answer = {"answer": "يوجد 238 فاتورة مبيعات غير ملغاة.", "needs_ask": None}
    bad_answer = {"answer": "يوجد 261 فاتورة مبيعات.", "needs_ask": None}
    assert run_evals._case_passes(case, ok_answer)
    assert not run_evals._case_passes(case, bad_answer)


def test_wave5_ask_passes_conversation_company_id(monkeypatch):
    seen = {}

    def fake_ask(client, question, conversation=None, **kwargs):
        seen["conversation"] = conversation
        return {"answer": "238", "needs_ask": None, "answer_sql": "SELECT 1"}

    monkeypatch.setattr(run_evals.agent, "ask", fake_ask)
    monkeypatch.setattr(run_evals, "_load", lambda name: [{
        "name": "w5_non_void_sales_invoices_ar",
        "client": "105",
        "company_id": 2,
        "question": "كم عدد فواتير المبيعات غير الملغاة؟",
        "expect_contains": ["238"],
    }])
    run_evals.run_wave5_accuracy()
    assert seen["conversation"] == {"CompanyID": 2}


def test_this_month_case_requires_temporal_context():
    case = run_evals._load(run_evals.WAVE5_CASES_FILE)
    temporal = next(c for c in case if c["name"] == "w5_this_month_sales_context_ar")
    assert temporal["question"] == "كم مبيعات هذا الشهر؟"
    assert "2025" in temporal["expect_contains_any"] or "يوليو" in temporal["expect_contains_any"]

    bare_zero = {"answer": "مبيعات هذا الشهر صفر.", "needs_ask": None}
    contextual = {"answer": "أغسطس 2026 فارغ؛ آخر بيانات في يوليو 2025.", "needs_ask": None}
    assert not run_evals._case_passes(temporal, bare_zero)
    assert run_evals._case_passes(temporal, contextual)


def test_wave5_in_default_release_gate():
    assert "wave5" in run_evals._DEFAULT_SUITES
    assert "wave5" in run_evals._SUITE_RUNNERS


def test_argparse_suite_wave5_only(monkeypatch):
    ran = []

    def _recorder(name):
        def _run():
            ran.append(name)
            return [] if name == "isolation" else None
        return _run

    patched = {
        k: (hdr, _recorder(k)) for k, (hdr, _) in run_evals._SUITE_RUNNERS.items()
    }
    monkeypatch.setattr(run_evals, "_SUITE_RUNNERS", patched)
    monkeypatch.setattr(sys, "argv", ["run_evals.py", "--suite", "wave5"])
    run_evals.main()
    assert ran == ["wave5"]


def test_source_must_match_passes_when_any_pattern_hits():
    case = {
        "expect_contains_any": ["approval"],
        "source_must_match": ["user_guide", "back-office"],
    }
    ok = {"answer": "See screen 7.1.3 for approval.", "needs_ask": None,
          "sources": ["user_guide.md › Transactions › back-office approve"]}
    bad = {"answer": "See screen 7.1.3 for approval.", "needs_ask": None, "sources": ["random.md › X"]}
    assert run_evals._case_passes(case, ok)
    assert not run_evals._case_passes(case, bad)


def test_answer_sql_must_contain():
    case = {"expect_contains_any": ["total"], "answer_sql_must_contain": ["ISNULL(IsVoid,0)=0"]}
    ok = {"answer": "totals shown", "needs_ask": None, "answer_sql": "SELECT SUM(x) FROM t.R WHERE ISNULL(IsVoid,0)=0"}
    bad = {"answer": "totals shown", "needs_ask": None, "answer_sql": "SELECT SUM(x) FROM t.R"}
    assert run_evals._case_passes(case, ok)
    assert not run_evals._case_passes(case, bad)


def test_docs105_and_hard_en_not_in_default_gate():
    assert "docs105" not in run_evals._DEFAULT_SUITES
    assert "hard_en" not in run_evals._DEFAULT_SUITES
    assert "docs105" in run_evals._SUITE_RUNNERS
    assert "hard_en" in run_evals._SUITE_RUNNERS


def test_hard_en_never_promotes_verified_query(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    cases = run_evals._load(run_evals.HARD_EN_CASES_FILE)
    assert len(cases) == 11
    with patch.object(run_evals.agent, "ask", return_value={
        "answer": "238 invoices", "needs_ask": None,
        "answer_sql": "SELECT COUNT(*) FROM t.TransactionsHeaders",
        "sources": [], "doc_search_count": 0,
    }), patch.object(memory, "promote_verified_query") as mock_promote:
        run_evals.run_hard_en_regression()
    mock_promote.assert_not_called()


def test_empty_answer_with_sql_evidence_hard_fails():
    case = {"expect_contains": ["9"]}
    bad = {"answer": "   ", "needs_ask": None, "answer_sql": "SELECT COUNT(*) AS n FROM t.X", "sources": []}
    good = {"answer": "النتيجة: 9.", "needs_ask": None, "answer_sql": "SELECT COUNT(*) AS n FROM t.X", "sources": []}
    assert not run_evals._case_passes(case, bad)
    assert run_evals._case_passes(case, good)


def test_empty_answer_with_doc_sources_hard_fails():
    case = {"expect_contains_any": ["customers"]}
    bad = {"answer": "", "needs_ask": None, "answer_sql": None, "sources": ["customers.md › 4.8"]}
    good = {"answer": "see customers.md 4.8", "needs_ask": None, "answer_sql": None, "sources": ["customers.md › 4.8"]}
    assert not run_evals._case_passes(case, bad)
    assert run_evals._case_passes(case, good)
