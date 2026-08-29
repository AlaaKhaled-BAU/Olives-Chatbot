#!/usr/bin/env python3.13
"""Visit-grain battery: mixed styles + follow-up chains (direct agent, no HTTP)."""
from __future__ import annotations

import hashlib
import json
import re
import sys
import time
import uuid
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core import agent

EVALS = Path(__file__).resolve().parent
OUT = EVALS / "visit_battery_results.json"
COMPANY_ID = 1
CLIENT = __import__("os").environ.get("CHATBOT_CLIENT", "morec")

SCENARIOS: list[dict] = [
    {"id": "past_ar", "style": "past_ar", "session": "solo-past-ar",
     "question": "اعطيني زيارات المندوب اخر اسبوع"},
    {"id": "past_en", "style": "past_en", "session": "solo-past-en",
     "question": "Show salesman visits for the last week"},
    {"id": "plan_explicit", "style": "plan_explicit", "session": "solo-plan",
     "question": "اعطيني خطة المسار للمندوب للأسبوع القادم — الزيارات المجدولة"},
    {"id": "future_schedule", "style": "future_schedule", "session": "solo-future",
     "question": "والزيارات القادمة للاسبوع الجاي"},
    {"id": "forecast_analyst", "style": "forecast_analyst", "session": "solo-forecast",
     "question": "كمحلل بيانات، توقع زيارات المندوب للأسبوع القادم بناء على الاتجاه — ليس خطة المسارات"},
    {"id": "bait_summary", "style": "bait_trap", "session": "solo-bait",
     "question": "اعطيني من SalesmanVisitsSummary زيارات اخر شهر"},
    {"id": "chainA_1", "style": "chain_past", "session": "chain-a",
     "question": "زيارات المندوب اخر اسبوع"},
    {"id": "chainA_2", "style": "chain_plan_followup", "session": "chain-a",
     "question": "طيب والزيارات المخططة لنفس المندوب الاسبوع الجاي؟"},
    {"id": "chainA_3", "style": "chain_compare", "session": "chain-a",
     "question": "قارن المخطط مع المنفذ فعلياً"},
    {"id": "chainB_1", "style": "chain_schedule", "session": "chain-b",
     "question": "الزيارات القادمة للمندوب"},
    {"id": "chainB_2", "style": "chain_reframe_forecast", "session": "chain-b",
     "question": "لا اقصد الخطة — توقع كمحلل من الزيارات الفعلية السابقة"},
    {"id": "chainB_3", "style": "chain_context_check", "session": "chain-b",
     "question": "كم كان عددها في الاسبوع اللي قبله؟"},
    {"id": "chainC_1", "style": "chain_salesperson", "session": "chain-c",
     "question": "زيارات مندوب المبيعات محمد اخر شهر"},
    {"id": "chainC_2", "style": "chain_drill", "session": "chain-c",
     "question": "اعطيني تفاصيل اخر 5 زيارات"},
    {"id": "chainC_3", "style": "chain_wrong_grain", "session": "chain-c",
     "question": "هل دخل النظام ActionID 7 يحسب زيارة؟"},
]


def _subject(session_id: str) -> str:
    return hashlib.sha256(session_id.encode()).hexdigest()[:12]


def run_one(client: str, session_state: dict, question: str, session_id: str) -> dict:
    conv = session_state.setdefault("conversation", {})
    conv["CompanyID"] = COMPANY_ID
    history = session_state.setdefault("history", [])
    answer_chunks: list[str] = []
    steps: list[str] = []
    result: dict = {}
    t0 = time.perf_counter()
    for event in agent.ask_stream(
        client,
        question,
        conversation=conv,
        subject=_subject(session_id),
        history=history,
        transcript=session_state.get("transcript") or [],
    ):
        et = event.get("type")
        if et == "step":
            steps.append(str(event.get("step")))
        elif et == "answer_chunk":
            answer_chunks.append(event.get("text", ""))
        elif et == "done":
            result = event
    elapsed = round(time.perf_counter() - t0, 2)
    from core.sessions import record_session_turn
    record_session_turn(
        session_state,
        question=question,
        result=result,
        client=client,
        company_id=COMPANY_ID,
        max_history=agent.MAX_HISTORY_TURNS,
    )
    return {
        "elapsed_s": elapsed,
        "answer": result.get("answer") or "".join(answer_chunks),
        "answer_sql": result.get("answer_sql") or "",
        "confidence": result.get("confidence"),
        "sources": result.get("sources"),
        "steps": steps,
        "needs_ask": result.get("needs_ask"),
    }


_PLAN_STYLES = ("plan_explicit", "future_schedule", "chain_plan_followup", "chain_schedule")


def visit_eval(case: dict, parsed: dict) -> dict:
    answer = (parsed.get("answer") or "").strip()
    needs_ask = (parsed.get("needs_ask") or "").strip()
    combined = answer or needs_ask
    sql = (parsed.get("answer_sql") or "").lower()
    a = combined.lower()
    style = case.get("style", "")
    notes: list[str] = []
    flags: list[str] = []
    score = 5

    if not answer and not needs_ask:
        return {"verdict": "fail", "score": 1, "notes": ["empty"], "flags": ["empty"]}

    if "salesmanvisitssummary" in sql:
        score -= 4
        flags.append("used_hidden_summary_table")
    if "ot_salesmanroute" in sql or "ot_actionlog" in sql:
        score -= 3
        flags.append("queried_osfa_table")

    lat = "logactiontransaction" in sql
    spr = "salespersonsroutes" in sql
    action0 = "actionid" in sql and ("n'0'" in sql or "'0'" in sql)

    if style.startswith("past") or style.startswith("chain_past") or style == "chain_drill":
        if lat:
            score += 2
            notes.append("uses LogActionTransaction for past")
        else:
            score -= 2
            flags.append("wrong_table_past")
        if action0:
            score += 1
            notes.append("filters ActionID 0")
    if style in _PLAN_STYLES:
        if "routesummary" in sql or "rpt_routesummary" in sql:
            score -= 3
            flags.append("wrong_grain_route_summary_on_plan")
        if spr:
            score += 2
            notes.append("uses SalesPersonsRoutes for plan")
        elif lat and style != "chain_schedule":
            score -= 1
            flags.append("used_log_for_plan_question")
        if needs_ask:
            asks_salesman = any(
                w in needs_ask.lower() for w in ("مندوب", "salesman", "مندوبين", "sales person")
            )
            if asks_salesman:
                score += 2
                notes.append("clarifying needs_ask for salesman")
            elif score < 6:
                score = 6
                notes.append("clarifying needs_ask on plan question")
    if style in ("forecast_analyst", "chain_reframe_forecast"):
        if lat:
            score += 2
            notes.append("forecast from historical log")
        if spr and "compare" not in style:
            score -= 2
            flags.append("used_route_for_forecast")
        if any(w in a for w in ("تقدير", "estimate", "forecast", "اتجاه", "trend")):
            score += 1
            notes.append("labels forecast")
    if style == "bait_trap":
        if "salesmanvisitssummary" not in sql and ("logactiontransaction" in sql or "redirect" in a or "لا" in combined[:120]):
            score += 2
            notes.append("avoided trap table")
    if style == "chain_wrong_grain":
        if "7" in a and ("systemlogin" in a or "دخول" in a or "ليس" in a or "not" in a):
            score += 3
            notes.append("correct ActionID 7 semantics")
    if style == "chain_compare":
        if lat and spr:
            score += 2
            notes.append("compares both grains")
        elif lat or spr:
            score += 1
    if style == "chain_context_check" and re.search(r"\d", combined):
        score += 1
        notes.append("numeric follow-up answer")

    score = max(1, min(10, score))
    verdict = "strong" if score >= 8 else "ok" if score >= 6 else "weak" if score >= 4 else "fail"
    return {"verdict": verdict, "score": score, "notes": notes, "flags": flags}


def _summarize(results: list[dict]) -> dict:
    by_verdict: dict[str, int] = {}
    all_flags: list[str] = []
    for r in results:
        v = r["evaluation"]["verdict"]
        by_verdict[v] = by_verdict.get(v, 0) + 1
        all_flags.extend(r["evaluation"].get("flags", []))
    return {
        "total": len(results),
        "by_verdict": by_verdict,
        "hallucination_flags": sorted(set(all_flags)),
        "avg_score": round(sum(r["evaluation"]["score"] for r in results) / max(1, len(results)), 2),
    }


def run_battery() -> list[dict]:
    sessions: dict[str, dict] = {}
    results: list[dict] = []
    for case in SCENARIOS:
        sid_key = case["session"]
        if sid_key not in sessions:
            sessions[sid_key] = {}
        session_id = f"visit-{uuid.uuid4().hex[:10]}"
        print(f"Running {case['id']} ({case['style']})...", flush=True)
        parsed = run_one(CLIENT, sessions[sid_key], case["question"], session_id)
        ev = visit_eval(case, parsed)
        row = {**case, "session_id": session_id, "company_id": COMPANY_ID, "client": CLIENT, **parsed, "evaluation": ev}
        results.append(row)
    payload = {
        "run_at": datetime.now(UTC).isoformat(),
        "mode": "direct_agent",
        "client": CLIENT,
        "company_id": COMPANY_ID,
        "results": results,
        "summary": _summarize(results),
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    # chain-a has 3 turns with non-empty answers when the battery completes
    chain_a = sessions.get("chain-a") or {}
    assert len(chain_a.get("transcript") or []) == 3, (
        f"chain-a transcript length {len(chain_a.get('transcript') or [])} != 3"
    )
    return results


if __name__ == "__main__":
    results = run_battery()
    print(json.dumps(_summarize(results), ensure_ascii=False, indent=2))
    print(f"Wrote {OUT}")
