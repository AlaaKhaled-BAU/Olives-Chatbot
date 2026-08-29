#!/usr/bin/env python3.13
"""Comprehensive system battery — memory, routing, NL2SQL, docs, reports, session, adversarial.

Runs against live agent.ask_stream (direct, no HTTP). Maintains per-session state
for multi-turn chains. Supervised heuristic scoring per category.

Usage:
  set -a && source .env && set +a
  python3.13 evals/run_comprehensive_system_battery.py
  python3.13 evals/run_comprehensive_system_battery.py --self-check
  python3.13 evals/run_comprehensive_system_battery.py --ids mem6-07,visit-chainA-03
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
import uuid
from collections import Counter, defaultdict
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core import agent  # noqa: E402
from core.sessions import record_session_turn  # noqa: E402

EVALS = Path(__file__).resolve().parent
CASES_FILE = EVALS / "comprehensive_system_battery.jsonl"
OUT = EVALS / "comprehensive_system_battery_results.json"
CLIENT = __import__("os").environ.get("CHATBOT_CLIENT", "105")
DEFAULT_COMPANY_ID = 1

_DENIAL_PHRASES = (
    "لم أجد",
    "لا يوجد",
    "لم يكن في سياق",
    "غير موجود في المحادثة",
    "لا أتذكر",
    "لم يكن هناك",
    "لا أملك",
    "لم أسأل",
    "لا أسئلة سابقة",
    "لم يسبق أن",
    "أول سؤال في هذه المحادثة",
    "لا ذاكرة",
)
_EMPTY_ADMIT_PHRASES = _DENIAL_PHRASES + (
    "empty",
    "لا محادثة",
    "بداية",
    "لا توجد أسئلة سابقة",
)
_GAP_PHRASES = ("لا يوجد", "لم يعثر", "لا يشرح", "لم أجد", "لا يغطي", "غير متوفر")
_AR_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
_NUM_RE = re.compile(r"\d+(?:\.\d+)?")

# Expected transcript lengths after each session completes (self-check).
_SESSION_TRANSCRIPT_EXPECT: dict[str, int] = {
    "mem-6turn": 7,   # 6 answered turns + 1 recall (thanks may be short)
    "mem-index": 9,   # 7 substantive + thanks + 2 recalls (8 setup if thanks counts)
    "visit-chain-a": 3,
    "visit-chain-b": 3,
}


def load_cases(path: Path = CASES_FILE) -> list[dict]:
    cases = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            cases.append(json.loads(line))
    return cases


def _subject(session_key: str) -> str:
    return hashlib.sha256(session_key.encode()).hexdigest()[:12]


def _switch_company(session_state: dict, company_id: int, *, force_clear: bool = False) -> None:
    conv = session_state.setdefault("conversation", {})
    prev = conv.get("CompanyID")
    conv["CompanyID"] = company_id
    if force_clear or (prev is not None and int(prev) != int(company_id)):
        session_state["history"] = []
        session_state["transcript"] = []
        session_state.pop("last_turn", None)


def run_one(
    client: str,
    session_state: dict,
    case: dict,
    session_key: str,
) -> dict:
    company_id = int(case.get("company_id") or DEFAULT_COMPANY_ID)
    conv = session_state.setdefault("conversation", {})
    conv["CompanyID"] = company_id
    history = session_state.setdefault("history", [])
    transcript_before = len(session_state.get("transcript") or [])

    question = case.get("question", "")
    if case.get("action") == "switch_company":
        _switch_company(session_state, company_id, force_clear=True)
        return {
            "elapsed_s": 0.0,
            "answer": "",
            "answer_sql": "",
            "confidence": None,
            "sources": [],
            "steps": [],
            "needs_ask": None,
            "tools_ms": {},
            "report_name": None,
            "doc_search_count": 0,
            "transcript_before": transcript_before,
            "transcript_after": len(session_state.get("transcript") or []),
            "action": "switch_company",
        }

    answer_chunks: list[str] = []
    steps: list[str] = []
    result: dict = {}
    t0 = time.perf_counter()
    for event in agent.ask_stream(
        client,
        question,
        conversation=conv,
        subject=_subject(session_key),
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

    if str(question or "").strip() and (result.get("answer") or "").strip():
        record_session_turn(
            session_state,
            question=question,
            result=result,
            client=client,
            company_id=company_id,
            max_history=agent.MAX_HISTORY_TURNS,
        )

    return {
        "elapsed_s": elapsed,
        "answer": result.get("answer") or "".join(answer_chunks),
        "answer_sql": result.get("answer_sql") or "",
        "confidence": result.get("confidence"),
        "sources": result.get("sources") or [],
        "steps": steps,
        "needs_ask": result.get("needs_ask"),
        "tools_ms": result.get("tools_ms") or {},
        "report_name": result.get("report_name"),
        "doc_search_count": result.get("doc_search_count", 0),
        "transcript_before": transcript_before,
        "transcript_after": len(session_state.get("transcript") or []),
        "action": None,
    }


def _blob(parsed: dict) -> str:
    answer = (parsed.get("answer") or "").strip()
    needs = (parsed.get("needs_ask") or "").strip()
    src = json.dumps(parsed.get("sources") or [], ensure_ascii=False)
    return (answer + " " + needs + " " + src).lower().translate(_AR_DIGITS)


def _sql_blob(parsed: dict) -> str:
    return (parsed.get("answer_sql") or "").lower()


def _has_denial(text: str, *, window: int | None = 300) -> bool:
    chunk = text[:window] if window else text
    return any(p in chunk for p in _DENIAL_PHRASES)


def _has_numeric(text: str) -> bool:
    return bool(_NUM_RE.search(text.translate(_AR_DIGITS)))


def _table_hit(sql: str, table: str) -> bool:
    t = table.lower()
    return t in sql or f"t.{t}" in sql or f"[{t}]" in sql


def score_case(case: dict, parsed: dict) -> dict:
    """Supervised heuristic scoring → verdict strong|ok|weak|fail, score 1-10."""
    expect = case.get("expect") or {}
    notes: list[str] = []
    flags: list[str] = []
    score = 5
    criteria = expect.get("min_score_criteria", "")

    if case.get("action") == "switch_company":
        cleared = int(parsed.get("transcript_after") or 0) == 0
        if expect.get("transcript_cleared") and not cleared:
            score -= 3
            flags.append("transcript_not_cleared_on_switch")
        elif cleared:
            score += 3
            notes.append("transcript cleared on company switch")
        score = max(1, min(10, score))
        verdict = _verdict_from_score(score)
        return {"verdict": verdict, "score": score, "notes": notes, "flags": flags}

    answer = (parsed.get("answer") or "").strip()
    needs = (parsed.get("needs_ask") or "").strip()
    combined = answer or needs
    blob = _blob(parsed)
    sql = _sql_blob(parsed)
    tools_ms = parsed.get("tools_ms") or {}

    if not combined and not expect.get("transcript_no_growth"):
        return {"verdict": "fail", "score": 1, "notes": ["empty answer"], "flags": ["empty"]}

    # --- generic expect checks ---
    if expect.get("transcript_no_growth"):
        before = parsed.get("transcript_before", 0)
        after = parsed.get("transcript_after", 0)
        if after > before:
            score -= 4
            flags.append("whitespace_grew_transcript")
        else:
            score += 3
            notes.append("whitespace did not grow transcript")

    if expect.get("prior_transcript_len") is not None:
        if parsed.get("transcript_before") != expect["prior_transcript_len"]:
            score -= 1
            flags.append("unexpected_prior_transcript_len")

    for table in expect.get("must_use_table") or []:
        if _table_hit(sql, table) or table.lower() in blob:
            score += 1
            notes.append(f"uses {table}")
        else:
            score -= 2
            flags.append(f"missing_table_{table}")

    for table in expect.get("must_not_use_table") or []:
        if _table_hit(sql, table):
            score -= 3
            flags.append(f"forbidden_table_{table}")
        else:
            score += 1
            notes.append(f"avoided {table}")

    if expect.get("must_have_sql"):
        if sql.strip():
            score += 1
            notes.append("has SQL")
        else:
            score -= 2
            flags.append("missing_sql")

    for needle in expect.get("answer_sql_must_contain") or []:
        if needle.lower() in sql:
            score += 1
        else:
            score -= 2
            flags.append(f"sql_missing_{needle}")

    if expect.get("expect_contains_any"):
        if any(needle.lower() in blob for needle in expect["expect_contains_any"]):
            score += 1
        elif criteria not in ("recall_setup",):
            score -= 1
            flags.append("no_needle_match")

    if expect.get("expect_report"):
        got = parsed.get("report_name") or ""
        if got == expect["expect_report"]:
            score += 2
            notes.append(f"report {got}")
        elif expect["expect_report"].lower() in sql or expect["expect_report"].lower() in blob:
            score += 1
            notes.append("report grain in SQL/answer")
        else:
            score -= 2
            flags.append(f"wrong_report_want_{expect['expect_report']}")

    if expect.get("must_not_report_path"):
        if parsed.get("report_name"):
            score -= 3
            flags.append("unexpected_report_path")
        elif "run_report" in json.dumps(tools_ms):
            score -= 2
            flags.append("run_report_in_tools")

    if expect.get("must_recall"):
        if _has_denial(answer) and not any(n.lower() in blob for n in expect["must_recall"]):
            score -= 3
            flags.append("denied_memory")
        hits = sum(1 for n in expect["must_recall"] if n.lower() in blob)
        if hits:
            score += 2
            notes.append(f"recall hit {hits}/{len(expect['must_recall'])}")
        else:
            score -= 2
            flags.append("recall_miss")

    if expect.get("must_not_deny") and _has_denial(answer) and not any(
        n.lower() in blob for n in (expect.get("must_recall") or [])
    ):
        score -= 3
        flags.append("denial_when_should_recall")

    if expect.get("must_admit_empty"):
        admits = any(p in answer for p in _EMPTY_ADMIT_PHRASES)
        if admits:
            score += 3
            notes.append("admits empty session")
        else:
            score -= 2
            flags.append("no_empty_admission")

    if expect.get("must_not_recall"):
        leaked = any(n.lower() in blob for n in expect["must_not_recall"])
        if leaked:
            score -= 3
            flags.append("leaked_prior_after_switch")
        else:
            score += 1
            notes.append("no leak after switch")

    if expect.get("must_not_ask_company"):
        if needs and any(w in needs for w in ("شركة", "company", "CompanyID")):
            score -= 2
            flags.append("asked_company")

    if expect.get("must_need_ask_or_clarify"):
        if needs or any(w in blob for w in ("مندوب", "salesman", "sales person", "أي مندوب", "حدد")):
            score += 2
            notes.append("clarifying ask for salesman")
        else:
            score -= 2
            flags.append("no_clarifying_ask")

    if expect.get("tools_must_include"):
        for tool in expect["tools_must_include"]:
            if tools_ms.get(tool, 0) > 0:
                score += 2
                notes.append(f"tools_ms.{tool}")
            else:
                score -= 2
                flags.append(f"tools_ms_missing_{tool}")

    if expect.get("tools_prefer"):
        for tool in expect["tools_prefer"]:
            if tools_ms.get(tool, 0) > 0:
                score += 1
                notes.append(f"used {tool}")

    if expect.get("doc_search_max") is not None:
        dc = parsed.get("doc_search_count", 0)
        if dc <= expect["doc_search_max"]:
            score += 1
            notes.append("low doc thrash")
        else:
            score -= 1
            flags.append(f"doc_search_count_{dc}")

    if expect.get("expect_numeric") and _has_numeric(combined):
        score += 1
        notes.append("numeric follow-up")

    if expect.get("must_not_exec"):
        if "exec " in sql or sql.strip().startswith("exec"):
            score -= 4
            flags.append("executed_proc")
        elif any(w in blob for w in ("exec", "إجراء مخزن", "stored procedure", "لا أنفذ", "لا يمكن تنفيذ")):
            score += 2
            notes.append("exec refused or explained")

    # --- criteria-specific tuning ---
    if criteria == "recall_setup":
        if combined:
            score = max(score, 6)
            notes.append("setup turn recorded")
    elif criteria == "visit_past":
        if "actionid" in sql and ("'0'" in sql or "n'0'" in sql):
            score += 1
            notes.append("ActionID 0 filter")
    elif criteria == "visit_plan":
        if "salespersonsroutes" in sql:
            score += 2
        if "routesummary" in sql:
            score -= 3
            flags.append("route_summary_on_plan")
    elif criteria == "visit_plan_or_ask":
        asked = (parsed.get("needs_ask") or "") + combined
        if parsed.get("needs_ask") or any(w in asked for w in ("أي مندوب", "which salesman")):
            score += 2
            notes.append("asked which salesman")
        elif "salespersonsroutes" in sql:
            score += 1
            notes.append("plan sql without ask")
        if "routesummary" in sql:
            score -= 3
            flags.append("route_summary_on_plan")
    elif criteria == "visit_compare":
        if "logactiontransaction" in sql and "salespersonsroutes" in sql:
            score += 2
        elif "logactiontransaction" in sql or "salespersonsroutes" in sql:
            score += 1
    elif criteria == "visit_forecast":
        if any(w in blob for w in ("تقدير", "estimate", "forecast", "اتجاه", "trend")):
            score += 1
    elif criteria == "bait_table":
        if "salesmanvisitssummary" not in sql:
            score += 2
    elif criteria == "docs_gap":
        admits = any(p in answer for p in _GAP_PHRASES)
        honest = any(n in blob for n in ("تابلت", "tablet", "new invoice")) and any(
            n in blob for n in ("اعتماد", "approve", "7.3", "عرض")
        )
        if admits or honest:
            score += 2
            notes.append("honest docs gap or routing")
        else:
            score -= 2
            flags.append("docs_gap_not_honest")
    elif criteria == "not_certified_unlock":
        if parsed.get("report_name") == "Rpt_FooBarUnknown" and not sql:
            score -= 1
        if any(w in blob for w in ("غير معتمد", "not certified", "run_metric", "مبيعات")):
            score += 2
            notes.append("not_certified handled")
    elif criteria == "grain_trap" or criteria == "grain_honesty":
        if any(m in blob for m in ("transactiontypeid", "isvoid", "261", "238", "نوع", "type")):
            score += 2
            notes.append("grain awareness")
    elif criteria == "dual_rail":
        if sql.count("select") >= 1 and (parsed.get("report_name") or "تقرير" in blob):
            score += 1
            notes.append("addressed dual ask")

    score = max(1, min(10, score))
    verdict = _verdict_from_score(score)
    return {"verdict": verdict, "score": score, "notes": notes, "flags": flags}


def _verdict_from_score(score: int) -> str:
    if score >= 8:
        return "strong"
    if score >= 6:
        return "ok"
    if score >= 4:
        return "weak"
    return "fail"


def _summarize(results: list[dict]) -> dict:
    by_verdict: Counter[str] = Counter()
    by_category: dict[str, dict[str, int]] = defaultdict(lambda: Counter())
    by_difficulty: dict[str, dict[str, int]] = defaultdict(lambda: Counter())
    all_flags: list[str] = []

    for r in results:
        ev = r["evaluation"]
        v = ev["verdict"]
        by_verdict[v] += 1
        by_category[r["category"]][v] += 1
        by_difficulty[r.get("difficulty", "unknown")][v] += 1
        all_flags.extend(ev.get("flags", []))

    total = len(results)
    strong_ok = by_verdict.get("strong", 0) + by_verdict.get("ok", 0)
    return {
        "total": total,
        "by_verdict": dict(by_verdict),
        "by_category": {k: dict(v) for k, v in sorted(by_category.items())},
        "by_difficulty": {k: dict(v) for k, v in sorted(by_difficulty.items())},
        "avg_score": round(sum(r["evaluation"]["score"] for r in results) / max(1, total), 2),
        "pass_rate_strong_ok_pct": round(100.0 * strong_ok / max(1, total), 1),
        "hallucination_flags": sorted(set(all_flags)),
        "total_elapsed_s": round(sum(r.get("elapsed_s", 0) for r in results), 1),
    }


def self_check(cases: list[dict] | None = None) -> None:
    cases = cases or load_cases()
    assert len(cases) >= 40, f"expected >=40 cases, got {len(cases)}"
    ids = [c["id"] for c in cases]
    assert len(ids) == len(set(ids)), "duplicate case ids"
    for c in cases:
        assert c.get("category"), f"missing category: {c.get('id')}"
        assert c.get("difficulty") in ("easy", "medium", "hard"), c["id"]
        assert c.get("session"), c["id"]
    chains = [c for c in cases if c.get("chain")]
    for c in chains:
        assert any(x["id"] == c["chain"] for x in cases), f"chain ref missing: {c['id']} -> {c['chain']}"
    sessions = defaultdict(list)
    for c in cases:
        sessions[c["session"]].append(c["id"])
    assert len(sessions) >= 10, "expected diverse sessions"
    print(f"self-check OK: {len(cases)} cases, {len(sessions)} sessions, {len(chains)} chained", flush=True)


def run_battery(
    cases: list[dict] | None = None,
    *,
    client: str = CLIENT,
) -> list[dict]:
    cases = cases or load_cases()
    sessions: dict[str, dict] = {}
    results: list[dict] = []

    for case in cases:
        sid_key = case["session"]
        if sid_key not in sessions:
            sessions[sid_key] = {}
        print(f"Running {case['id']} [{case['category']}/{case['difficulty']}]...", flush=True)
        parsed = run_one(client, sessions[sid_key], case, sid_key)
        ev = score_case(case, parsed)
        row = {
            **case,
            "client": client,
            "company_id": case.get("company_id", DEFAULT_COMPANY_ID),
            **parsed,
            "evaluation": ev,
        }
        results.append(row)
        time.sleep(0.2)

    # Post-run session assertions
    for sess, expected in _SESSION_TRANSCRIPT_EXPECT.items():
        actual = len((sessions.get(sess) or {}).get("transcript") or [])
        if actual < expected - 1:  # allow thanks-turn skip
            print(f"WARN: session {sess} transcript={actual} expected>={expected-1}", flush=True)

    payload = {
        "run_at": datetime.now(UTC).isoformat(),
        "mode": "direct_agent",
        "client": client,
        "company_id": DEFAULT_COMPANY_ID,
        "cases_file": str(CASES_FILE),
        "results": results,
        "summary": _summarize(results),
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Comprehensive system eval battery")
    parser.add_argument("--self-check", action="store_true", help="Validate case file only")
    parser.add_argument("--ids", type=str, default="", help="Comma-separated case ids")
    args = parser.parse_args()

    cases = load_cases()
    self_check(cases)
    if args.self_check:
        return 0

    if args.ids:
        wanted = {x.strip() for x in args.ids.split(",") if x.strip()}
        cases = [c for c in cases if c["id"] in wanted]
        if not cases:
            print("No matching cases", file=sys.stderr)
            return 1

    results = run_battery(cases)
    summary = _summarize(results)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
