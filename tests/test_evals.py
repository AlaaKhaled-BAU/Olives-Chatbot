"""Phase 8 acceptance: the isolation release gate actually gates. Runs the
real isolation.jsonl against the live wall/gate/catalog (same as
evals/run_evals.py) and separately proves the leak-detection logic itself
would catch a real leak, so a future change that silently breaks detection
(not just breaks the wall) gets caught too."""
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "evals"))
import run_evals  # noqa: E402
from core import memory  # noqa: E402


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

    stored = memory.get_verified_query("morec", "how many companies?")
    assert stored["proc_or_sql"] == "SELECT COUNT(*) FROM t.Companies"
    shots = memory.few_shots("morec")
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

    assert memory.get_verified_query("morec", "how many companies?") is None


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

    assert memory.get_verified_query("morec", "nonsense question") is None
