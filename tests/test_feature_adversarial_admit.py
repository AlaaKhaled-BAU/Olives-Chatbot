"""Unit tests for C2 company-switch empty-session admit phrases (eval honesty)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from evals.run_feature_adversarial import _admits_empty_session
from evals.run_visit_battery import visit_eval


def test_admits_empty_session_phrases() -> None:
    honest = (
        "هذا هو أول سؤال في هذه المحادثة؛ لم يسبق أن طرحت أي سؤال قبله."
    )
    assert _admits_empty_session(honest)

    for phrase in (
        "لا يوجد سؤال سابق",
        "لم يكن هناك سؤال",
        "لم أسأل شيء قبل",
        "لا أسئلة في الجلسة",
        "محادثة جديدة",
        "لا ذاكرة عن سؤال",
        "session is empty",
    ):
        assert _admits_empty_session(phrase), phrase

    assert not _admits_empty_session("كم عدد المسارات المسجلة؟")
    assert not _admits_empty_session("")


def test_visit_eval_needs_ask_not_empty() -> None:
    case = {"style": "plan_explicit"}
    parsed = {
        "answer": "",
        "needs_ask": "أي مندوب تقصد؟ (مثل: يوسف عوض)",
        "answer_sql": "",
    }
    ev = visit_eval(case, parsed)
    assert ev["verdict"] != "fail"
    assert "empty" not in ev.get("flags", [])
    assert ev["score"] >= 6


def test_visit_eval_empty_when_both_missing() -> None:
    case = {"style": "plan_explicit"}
    parsed = {"answer": "", "needs_ask": "", "answer_sql": ""}
    ev = visit_eval(case, parsed)
    assert ev["verdict"] == "fail"
    assert ev["flags"] == ["empty"]


def test_visit_eval_penalizes_route_summary_on_plan() -> None:
    case = {"style": "plan_explicit"}
    parsed = {
        "answer": "خطة المسار",
        "needs_ask": "",
        "answer_sql": "EXEC Rpt_RouteSummaryBySalesman",
    }
    ev = visit_eval(case, parsed)
    assert "wrong_grain_route_summary_on_plan" in ev.get("flags", [])
