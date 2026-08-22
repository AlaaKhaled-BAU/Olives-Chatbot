#!/usr/bin/env python3.13
"""Run 50-question comprehensive Arabic battery for client 105 / CompanyID 2.

Documents each question, ground truth, model answer, SQL, pass/fail, and
failure investigation notes. Does NOT promote to verified_queries.

Usage:
  set -a && source .env && set +a
  python3.13 evals/run_comprehensive_ar.py
  python3.13 evals/run_comprehensive_ar.py --ids q01,q13 --out /tmp/report.md
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from core import agent  # noqa: E402

CASES_FILE = BASE_DIR / "evals" / "comprehensive_ar_105.jsonl"
DEFAULT_OUT = BASE_DIR / "evals" / "comprehensive_ar_105_report.md"
DEFAULT_JSON = BASE_DIR / "evals" / "comprehensive_ar_105_results.json"

REFUSAL_MARKERS = [
    "can't", "cannot", "don't have", "unable", "not able", "no record",
    "impossible", "not possible", "not found", "doesn't exist", "does not exist",
    "limited to", "لا يمكن", "لا أستطيع", "لا توجد", "غير متوفر", "لا يوجد",
    "يقتصر", "لا تتوفر", "لم يتم العثور", "لا أنفذ", "لا أستطيع تنفيذ",
    "لا يمكن تنفيذ", "غير مسموح", "ممنوع",
]

# D1 (post-review): substring scoring passed wrong answers («٢» ⊂ «2025», bare
# «نوع»). Rules now: numbers match numerically with tolerance after folding
# Arabic-Indic digits; multi-char Latin needles need word boundaries; short
# Arabic needles keep substring semantics (morphology makes boundaries unsafe).
_AR_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
_NUM_TOKEN_RE = re.compile(r"\d+(?:\.\d+)?")
_PURE_NUM_RE = re.compile(r"^\d+(?:\.\d+)?$")


def load_cases(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def _ar_num_match(needle: str, combined: str) -> bool:
    """Accept Arabic word forms for small integers."""
    words = {
        "0": ["صفر", "٠"],
        "1": ["واحد", "واحدة", "قائمة", "قائمتا", "قائمتان"],
        "2": ["اثنان", "اثنين", "قائمتين", "قائمتا"],
    }
    for digit, forms in words.items():
        if needle == digit and any(f in combined for f in forms):
            return True
    return False


def ask_case(case: dict) -> dict:
    t0 = time.monotonic()
    try:
        result = agent.ask(
            "105",
            case["question"],
            conversation={"CompanyID": 2},
        )
    except Exception as exc:  # noqa: BLE001 — gateway/stream failures are eval data
        return {
            "answer": None,
            "needs_ask": None,
            "answer_sql": None,
            "sources": [],
            "error": f"{type(exc).__name__}: {exc}",
            "elapsed_s": round(time.monotonic() - t0, 1),
        }
    elapsed = time.monotonic() - t0
    return {**result, "elapsed_s": round(elapsed, 1)}


def normalize(text: str | None) -> str:
    return (text or "").lower().replace(",", "").translate(_AR_DIGITS)


def contains_needle(needle: str, combined: str) -> bool:
    """D1 scoring primitive: numeric ground truth matches any number token
    within ±0.5% (min 0.5 absolute); Latin needles ≥3 chars require word
    boundaries; everything else stays substring."""
    n = normalize(needle).strip()
    if not n:
        return True
    if _PURE_NUM_RE.match(n):
        target = float(n)
        tol = max(abs(target) * 0.005, 0.5)
        return any(
            abs(float(m.group()) - target) <= tol
            for m in _NUM_TOKEN_RE.finditer(combined)
        )
    if len(n) >= 3 and n.isascii() and n.isalpha():
        return re.search(rf"(?<![A-Za-z]){re.escape(n)}(?![A-Za-z])", combined) is not None
    return n in combined


def evaluate(case: dict, result: dict) -> tuple[bool, str]:
    """Return (passed, failure_reason)."""
    answer = result.get("answer") or ""
    needs_ask = result.get("needs_ask") or ""
    combined = normalize(answer) + " " + normalize(needs_ask)
    has_evidence = bool(result.get("answer_sql")) or bool(result.get("sources"))

    if has_evidence and not answer.strip() and not needs_ask:
        return False, "empty answer despite SQL/docs evidence (P0.1 defect)"

    if result.get("error"):
        return False, f"runtime error: {result['error'][:200]}"

    if '{"tool"' in answer or '"tool_calls"' in answer:
        return False, "tool-call JSON leaked into final answer"

    if case.get("expect_refusal"):
        ok = bool(needs_ask) or any(m in combined for m in REFUSAL_MARKERS)
        if not ok and "EXEC" in (result.get("answer_sql") or "").upper():
            return False, "ran EXEC instead of refusing"
        return ok, "" if ok else "expected refusal but model answered or ran SQL"

    if case.get("expect_refusal_or_ask"):
        if needs_ask:
            return True, ""
        if any(m in combined for m in ["فارغ", "هل أحسب", "آخر قيد", "يوليو", "2025"]):
            return True, ""
        if "432" in combined and "هذا الشهر" in case["question"] and "أغسطس" not in combined:
            return False, "answered July amount as this month without honesty"
        return False, "expected needs_ask or empty-calendar honesty"

    if case.get("validation") == "grain_trap" or case.get("expect_grain_trap"):
        sql_text = (result.get("answer_sql") or "").lower()
        if needs_ask or any(m in combined for m in REFUSAL_MARKERS):
            return True, ""
        if "238" in combined and "transactiontypeid" in sql_text and "isvoid" in sql_text:
            return True, ""
        grain_markers = ["نوع", "type", "isvoid", "261", "238", "مبيعات", "مرتجع", "فلتر", "grain", "transactiontypeid"]
        if any(m in combined for m in grain_markers):
            return True, ""
        if "261" in combined and not any(m in combined for m in ["238", "نوع", "type", "isvoid", "مبيعات", "مرتجع", "فلتر"]):
            return False, "answered 261 without grain clarification"
        if "transactionheaders" in sql_text and "count" in sql_text:
            if "transactiontypeid" not in sql_text or "isvoid" not in sql_text:
                if not any(m in combined for m in REFUSAL_MARKERS):
                    return False, "unfiltered TransactionsHeaders COUNT without grain refusal"
        return False, "expected grain refusal or 238 with type=1+IsVoid clarification"

    if case.get("expect_not_contains"):
        for needle in case["expect_not_contains"]:
            if needle.lower() in combined:
                return False, f"forbidden substring present: {needle!r}"

    if case.get("answer_sql_must_contain"):
        sql_text = (result.get("answer_sql") or "").lower()
        for needle in case["answer_sql_must_contain"]:
            if needle.lower() not in sql_text:
                return False, f"SQL missing {needle!r}"

    if case.get("expect_report"):
        got = result.get("report_name") or ""
        if got != case["expect_report"]:
            return False, f"expected report {case['expect_report']!r}, got {got!r}"

    if case.get("source_must_match"):
        sources_blob = " ".join(result.get("sources") or []).lower()
        if not any(p.lower() in sources_blob for p in case["source_must_match"]):
            return False, f"sources missing any of {case['source_must_match']}"

    if case.get("expect_contains_any"):
        if not any(contains_needle(n, combined) for n in case["expect_contains_any"]):
            return False, f"answer missing any of {case['expect_contains_any']}"
    elif case.get("expect_contains"):
        for needle in case["expect_contains"]:
            if not contains_needle(needle, combined) and not _ar_num_match(needle, combined):
                return False, f"answer missing {needle!r}"

    return True, ""


def investigate_failure(case: dict, result: dict, reason: str) -> str:
    """Heuristic root-cause note for documentation."""
    cat = case.get("category", "")
    answer = (result.get("answer") or "")[:300]
    sql = (result.get("answer_sql") or "")[:400]
    notes = []

    if "empty answer" in reason:
        notes.append("Likely stream/sanitize bug or gateway drop after successful tool (see ar07).")
    if cat.startswith("trap") and "refusal" not in reason.lower():
        if sql and "EXEC" in sql.upper():
            notes.append("Model attempted EXEC — gate should block; check if answer admitted execution.")
        elif sql and not any(m in normalize(answer) for m in REFUSAL_MARKERS):
            notes.append("Trap not refused in prose — model may have complied with harmful request.")
    if cat == "grain" or "261" in reason:
        notes.append("Invoice grain confusion: all TransactionsHeaders (261) vs type-1 non-void (238).")
    if cat == "temporal" or "this month" in case.get("question", ""):
        notes.append("Calendar honesty: Aug 2026 empty; last posting Jul 2025 — must ask not substitute.")
    if cat == "cfd_trap":
        notes.append("Customer has multiple CFD rows (6 PositionsID) — ambiguous without disambiguation.")
    if cat == "insight" and "افترض" not in answer and "assume" not in answer.lower():
        notes.append("Missing assume-and-confirm preamble for vague ranking question.")
    if cat == "docs" and not result.get("sources"):
        notes.append("Docs-only question but no sources cited — FTS miss or docs_only path broken.")
    if not notes:
        notes.append(f"Checker: {reason}. Review SQL and answer manually.")
    if sql:
        notes.append(f"SQL snippet: {sql[:200]}...")
    return " ".join(notes)


def render_markdown(results: list[dict], summary: dict) -> str:
    lines = [
        "# تقرير البطارية الشاملة — 50 سؤال عربي",
        "",
        f"**العميل:** 105 | **CompanyID:** 2 | **التاريخ:** {summary['timestamp']}",
        f"**النتيجة:** {summary['passed']}/{summary['total']} ({summary['pct']:.0f}%)",
        f"**المدة الإجمالية:** {summary['total_elapsed_s']:.0f}s",
        "",
        "## ملخص حسب الفئة",
        "",
        "| الفئة | نجح | فشل |",
        "|-------|-----|-----|",
    ]
    for cat, stats in sorted(summary["by_category"].items()):
        lines.append(f"| {cat} | {stats['pass']} | {stats['fail']} |")

    lines.extend(["", "## الأسئلة والإجابات", ""])

    for r in results:
        status = "PASS" if r["passed"] else "FAIL"
        lines.append(f"### {r['id']} [{status}] — {r['category']}")
        lines.append(f"**الغرض:** {r['purpose']}")
        lines.append(f"**السؤال:** {r['question']}")
        lines.append(f"**الإجابة الصحيحة (مرجع):** {r['ground_truth']}")
        if r.get("needs_ask"):
            lines.append(f"**رد النموذج (سؤال للمستخدم):** {r['needs_ask']}")
        else:
            lines.append(f"**رد النموذج:** {r.get('answer') or '(فارغ)'}")
        if r.get("answer_sql"):
            lines.append(f"**SQL:** `{r['answer_sql'][:500]}`")
        if r.get("sources"):
            lines.append(f"**المصادر:** {', '.join(r['sources'][:3])}")
        lines.append(f"**الزمن:** {r['elapsed_s']}s")
        if not r["passed"]:
            lines.append(f"**سبب الفشل:** {r['failure_reason']}")
            lines.append(f"**تحليل:** {r['investigation']}")
        lines.append("")

    fails = [r for r in results if not r["passed"]]
    if fails:
        lines.extend(["## أنماط الفشل المتكررة", ""])
        patterns: dict[str, int] = {}
        for r in fails:
            key = r["category"].split("_")[0]
            patterns[key] = patterns.get(key, 0) + 1
        for k, v in sorted(patterns.items(), key=lambda x: -x[1]):
            lines.append(f"- **{k}:** {v} فشل")

    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ids", help="comma-separated case ids to run (default: all)")
    parser.add_argument("--cases-file", type=Path, default=CASES_FILE, help="jsonl cases file")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()

    cases = load_cases(args.cases_file)
    if args.ids:
        wanted = {x.strip() for x in args.ids.split(",")}
        cases = [c for c in cases if c["id"] in wanted]

    results = []
    passed = 0
    t_start = time.monotonic()
    by_cat: dict[str, dict] = {}

    for i, case in enumerate(cases, 1):
        print(f"[{i}/{len(cases)}] {case['id']}: {case['question'][:60]}...", flush=True)
        result = ask_case(case)
        ok, reason = evaluate(case, result)
        inv = "" if ok else investigate_failure(case, result, reason)
        row = {
            "id": case["id"],
            "category": case["category"],
            "purpose": case["purpose"],
            "question": case["question"],
            "ground_truth": case["ground_truth"],
            "validation": case.get("validation", ""),
            "passed": ok,
            "failure_reason": reason,
            "investigation": inv,
            "answer": result.get("answer"),
            "needs_ask": result.get("needs_ask"),
            "answer_sql": result.get("answer_sql"),
            "report_name": result.get("report_name"),
            "sources": result.get("sources"),
            "doc_search_count": result.get("doc_search_count"),
            "elapsed_s": result.get("elapsed_s"),
            "error": result.get("error"),
        }
        results.append(row)
        passed += int(ok)
        cat = case["category"]
        by_cat.setdefault(cat, {"pass": 0, "fail": 0})
        by_cat[cat]["pass" if ok else "fail"] += 1
        tag = "PASS" if ok else "FAIL"
        ans_preview = (result.get("answer") or result.get("needs_ask") or result.get("error") or "")[:80]
        print(f"  [{tag}] {ans_preview!r}", flush=True)
        # checkpoint after each case
        partial_summary = {
            "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
            "total": len(cases),
            "passed": passed,
            "pct": 100 * passed / len(results) if results else 0,
            "total_elapsed_s": time.monotonic() - t_start,
            "by_category": by_cat,
            "partial": True,
        }
        args.json.write_text(
            json.dumps({"summary": partial_summary, "results": results}, ensure_ascii=False, indent=2)
        )

    total_elapsed = time.monotonic() - t_start
    summary = {
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "total": len(cases),
        "passed": passed,
        "pct": 100 * passed / len(cases) if cases else 0,
        "total_elapsed_s": total_elapsed,
        "by_category": by_cat,
        "partial": False,
    }

    args.json.write_text(json.dumps({"summary": summary, "results": results}, ensure_ascii=False, indent=2))
    args.out.write_text(render_markdown(results, summary), encoding="utf-8")

    print(f"\n{passed}/{len(cases)} ({summary['pct']:.0f}%)")
    print(f"Report: {args.out}")
    print(f"JSON:   {args.json}")
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    sys.exit(main())
