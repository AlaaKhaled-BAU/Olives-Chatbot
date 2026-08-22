#!/usr/bin/env python3.13
"""Phase 8/9: the release gate. Runs accuracy.jsonl (prints a %) and
isolation.jsonl (exits non-zero if ANY case leaks -- PLAN.md: a single leak
fails the build). Isolation cases go through the real gate/wall/catalog
code paths, not the model's judgment -- "blocked" here means the server
refused, not that the model declined to try.

Wave 5 (evals/wave5_accuracy.jsonl): Arabic accuracy for client 105 /
CompanyID 2 — part of the default release gate, or runnable alone via
``--suite wave5``.

Only a known "this was actually denied" exception counts as blocked
(GateError, or a pymssql permission/operational error) -- anything else
propagates as a real harness failure. A bare `except Exception` here once
silently turned a TypeError (a bug in this very script) into a false
"BLOCKED" -- reporting 100% safe while not actually running the attack at
all. Never widen this back to a bare except for convenience."""
import argparse
import json
import statistics
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

import pymssql  # noqa: E402

from core import agent, catalog, config, docs, gate, memory, sql  # noqa: E402

BLOCKING_EXCEPTIONS = (gate.GateError, pymssql.OperationalError, pymssql.DatabaseError)

REFUSAL_MARKERS = [
    "can't", "cannot", "don't have", "no such", "unable", "not able", "no record",
    "impossible", "no information", "not possible", "insufficient", "not found",
    "doesn't exist", "does not exist", "no salesperson", "no customer", "limited to",
    "لا يمكن", "لا أستطيع", "لا توجد", "غير متوفر", "لا يوجد", "يقتصر", "لا تتوفر",
    # FIXPLAN adversarial pass (2026-07-25): a real query for a nonexistent ID
    # correctly answered "لم يتم العثور على مندوب مبيعات برقم معرف 999999" (=
    # "no salesperson found with ID 999999") -- a completely valid refusal the
    # model gave, that the OLD marker list didn't recognize (a checker gap,
    # not a chatbot bug -- the answer was already correct).
    "لم يتم العثور",
]

WAVE5_CASES_FILE = "wave5_accuracy.jsonl"
DOCS105_CASES_FILE = "docs_105_ar.jsonl"
HARD_EN_CASES_FILE = "hard_en_regression.jsonl"


def _load(name):
    path = BASE_DIR / "evals" / name
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def _normalize_answer(result):
    answer = (result["answer"] or result["needs_ask"] or "").lower()
    return answer, answer.replace(",", "")


def _case_passes(case, result):
    answer, answer_normalized = _normalize_answer(result)
    has_evidence = bool(result.get("answer_sql")) or bool(result.get("sources"))
    if has_evidence and not (result.get("answer") or "").strip() and not result.get("needs_ask"):
        return False
    if case.get("expect_refusal"):
        return bool(result["needs_ask"]) or any(m in answer for m in REFUSAL_MARKERS)
    if "expect_not_contains" in case:
        if any(needle.lower() in answer_normalized for needle in case["expect_not_contains"]):
            return False
    if case.get("answer_sql_must_contain"):
        sql_text = (result.get("answer_sql") or "").lower()
        for needle in case["answer_sql_must_contain"]:
            if needle.lower() not in sql_text:
                return False
    if case.get("source_must_match"):
        sources_blob = " ".join(result.get("sources") or []).lower()
        if not any(p.lower() in sources_blob for p in case["source_must_match"]):
            return False
    if case.get("gateway_ok"):
        if result.get("answer_sql"):
            return True
        gateway_markers = ("gateway", "unavailable", "502", "البوابة", "غير متاح")
        if any(m in answer for m in gateway_markers):
            return True
        return False
    if "expect_contains_any" in case:
        return any(needle.lower() in answer_normalized for needle in case["expect_contains_any"])
    return all(needle.lower() in answer_normalized for needle in case["expect_contains"])


def _ask_case(case):
    company_id = case.get("company_id")
    conversation = {"CompanyID": company_id} if company_id is not None else None
    return agent.ask(case["client"], case["question"], conversation=conversation)


def _run_accuracy_corpus(cases, label: str, promote: bool = True):
    passed = 0
    promoted = 0
    for case in cases:
        result = _ask_case(case)
        answer, _ = _normalize_answer(result)
        ok = _case_passes(case, result)
        lang = case.get("lang", "")
        lang_tag = f" ({lang})" if lang else ""
        print(f"  [{'PASS' if ok else 'FAIL'}] {case['name']}{lang_tag}: {case['question']!r} -> {answer[:120]!r}")
        passed += int(ok)
        if promote and ok and not case.get("expect_refusal") and result.get("answer_sql"):
            # D2: verify-before-promote — a passing eval must never write SQL
            # into the live few-shot pool that the gate itself would reject
            # (EXEC, multi-statement, cross-company literals, stale tables).
            sql_text = result["answer_sql"]
            company = case.get("company_id", 1)
            try:
                cache = json.loads(
                    (BASE_DIR / "work" / case["client"] / "schema_cache.json").read_text())
                gate.validate(
                    sql_text,
                    allowed_procs=gate.DEFAULT_ALLOWED_PROCS,
                    company_id=company,
                    schema_cache=cache,
                )
            except Exception as exc:  # noqa: BLE001 — any validation failure blocks promotion
                print(f"  [SKIP-PROMOTE] {case['name']}: answer_sql failed gate validation ({exc})")
            else:
                memory.promote_verified_query(
                    case["client"], company, case["question"], sql_text, source="eval",
                )
                promoted += 1
    pct = 100 * passed / len(cases) if cases else 0
    print(f"{label}: {passed}/{len(cases)} ({pct:.0f}%)")
    if promote:
        print(f"  promoted {promoted} query pattern(s) to verified_queries (source=eval)")
    return pct


def run_accuracy():
    """C3a: every PASSING, non-refusal case with a real answer_sql gets its
    query promoted to verified_queries (source="eval") -- the few-shot pool
    is now seeded from a corpus of KNOWN-correct answers instead of from
    raw user traffic (which C3 correctly stopped trusting on its own).
    Re-running this script re-seeds every time, so the pool tracks the
    eval corpus as it grows rather than going stale."""
    return _run_accuracy_corpus(_load("accuracy.jsonl"), "accuracy")


def run_wave5_accuracy():
    """T4: Arabic Wave 5 release gate for client 105 / CompanyID 2.
    Ground-truth sales invoices (type=1, non-void) = 238 — NOT 261 (all
    TransactionsHeaders including returns). Every case passes conversation
    CompanyID so multi-company client 105 scopes to the right tenant."""
    cases = _load(WAVE5_CASES_FILE)
    return _run_accuracy_corpus(cases, "wave5 accuracy", promote=True)


def run_docs105_accuracy():
    """P0: Arabic how-to corpus for client 105 / CompanyID 2 — promote never."""
    cases = _load(DOCS105_CASES_FILE)
    passed = 0
    doc_counts: list[int] = []
    for case in cases:
        result = _ask_case(case)
        answer, _ = _normalize_answer(result)
        ok = _case_passes(case, result)
        doc_count = result.get("doc_search_count", 0)
        doc_counts.append(doc_count)
        print(
            f"  [{'PASS' if ok else 'FAIL'}] {case['name']}: {case['question']!r} "
            f"-> {answer[:120]!r} (doc_search_count={doc_count})"
        )
        passed += int(ok)
    pct = 100 * passed / len(cases) if cases else 0
    print(f"docs105 accuracy: {passed}/{len(cases)} ({pct:.0f}%)")
    if doc_counts:
        median = statistics.median(doc_counts)
        print(f"  doc_search_count median: {median:.1f}")
        if median > 3:
            print("  WARNING: doc_search_count median > 3 (not a release-gate exit)")
    return pct


def run_hard_en_regression():
    """English-11 regression net — informational only, promote never."""
    cases = _load(HARD_EN_CASES_FILE)
    passed = 0
    for case in cases:
        result = _ask_case(case)
        answer, _ = _normalize_answer(result)
        ok = _case_passes(case, result)
        print(f"  [{'PASS' if ok else 'FAIL'}] {case['name']}: {case['question']!r} -> {answer[:120]!r}")
        passed += int(ok)
    pct = 100 * passed / len(cases) if cases else 0
    print(f"hard_en regression (informational): {passed}/{len(cases)} ({pct:.0f}%)")
    return pct


def run_docs_accuracy():
    """C5: reported separately from run_accuracy() (SQL) per the plan --
    a docs question exercises search_docs + citation, not the tenant wall
    or the gate, so blending it into one percentage would hide which half
    of the "data master" use case is actually working. No verified_queries
    promotion here -- these questions have no SQL to promote at all."""
    cases = _load("docs_accuracy.jsonl")
    by_lang = {}  # lang -> [ok, ok, ...]
    for case in cases:
        result = _ask_case(case)
        answer, _ = _normalize_answer(result)
        ok = _case_passes(case, result)
        print(f"  [{'PASS' if ok else 'FAIL'}] {case['name']} ({case['lang']}): {case['question']!r} -> {answer[:120]!r}")
        by_lang.setdefault(case["lang"], []).append(ok)

    total = sum(len(v) for v in by_lang.values())
    passed = sum(sum(v) for v in by_lang.values())
    pct = 100 * passed / total if total else 0
    print(f"docs accuracy: {passed}/{total} ({pct:.0f}%)")
    # Per the plan: don't blend a materially worse Arabic recall into one
    # number that looks fine on average -- this corpus is English-only
    # prose, so a purely conceptual Arabic question (no shared digit/proper
    # noun) has a real, measured recall gap that a blended % would hide.
    for lang in sorted(by_lang):
        n, k = len(by_lang[lang]), sum(by_lang[lang])
        print(f"  {lang}: {k}/{n} ({100 * k / n:.0f}%)")
    return pct


def _attempt_no_tenant(case):
    conn = sql.get_conn(case["client"])
    try:
        cur = conn.cursor()
        cur.execute(case["sql"])
        try:
            rows = cur.fetchall()
        except pymssql.Error:  # a write statement has no result set to fetch
            rows = []
        return len(rows) == 0, f"{len(rows)} rows returned"
    finally:
        conn.close()


def run_isolation():
    cases = _load("isolation.jsonl")
    leaks = []
    for case in cases:
        blocked, detail = True, ""
        try:
            if case["attack"] == "catalog":
                aliases = config.load_client(case["client"])["name_aliases"]
                entitled = catalog.for_client(case["client"], aliases)
                blocked = case["proc"] not in entitled
                detail = "excluded from catalog" if blocked else "LEAKED: proc entitled"
            elif case["attack"] == "no_tenant":
                blocked, detail = _attempt_no_tenant(case)
            elif case["attack"] == "docs":
                # C5: a chunk excluded at INDEX time (core.docs.build_index)
                # must be unreachable via search too -- this is the
                # end-to-end proof, not just a unit test of the exclusion
                # function in isolation.
                hits = docs.search(case["client"], case["query"])
                blocked = len(hits) == 0
                detail = "no results" if blocked else f"LEAKED: {hits}"
            else:  # run_select -- the real gate + tenant-scoped path
                rows = sql.run_select(case["sql"], case["company_id"], case["client"], allowed_procs=[])
                blocked = len(rows) == 0
                detail = f"{len(rows)} rows returned"
        except BLOCKING_EXCEPTIONS as e:
            blocked, detail = True, f"{type(e).__name__}: {str(e)[:100]}"

        print(f"  [{'BLOCKED' if blocked else 'LEAKED'}] {case['name']}: {detail}")
        if not blocked:
            leaks.append(case["name"])
    return leaks


def run_golden_exec():
    """TRACK A: execution accuracy — candidate SQL's RESULT ROWS must equal
    the stored gold rows. Wording-proof; the strongest signal we have."""
    from evals.golden_rows import load_cases, run_suite
    cases = load_cases(BASE_DIR / "evals" / "exec_golden.jsonl")
    if not cases:
        print("  (no golden cases — run evals/build_golden.py first)")
        return
    passed, total = run_suite(
        cases,
        agent_ask=lambda client, question, conversation: agent.ask(
            client, question, conversation=conversation),
        run_select=lambda sql_text, company, client: sql.run_select(sql_text, company, client),
    )
    pct = 100 * passed / total if total else 0
    print(f"golden exec-accuracy: {passed}/{total} ({pct:.0f}%)")


_SUITE_RUNNERS = {
    "accuracy": ("=== accuracy ===", run_accuracy),
    "docs": ("=== docs accuracy ===", run_docs_accuracy),
    "docs105": ("=== docs105 accuracy (ar, client 105 / CompanyID 2) ===", run_docs105_accuracy),
    "wave5": ("=== wave5 accuracy (ar, client 105 / CompanyID 2) ===", run_wave5_accuracy),
    "hard_en": ("=== hard_en regression (en, client 105 / CompanyID 2, informational) ===", run_hard_en_regression),
    "isolation": ("=== isolation (release gate) ===", run_isolation),
    "golden": ("=== golden execution-accuracy (TRACK A release gate) ===", run_golden_exec),
}

_DEFAULT_SUITES = ("accuracy", "docs", "wave5", "isolation")


def main():
    parser = argparse.ArgumentParser(description="Run eval suites (release gate).")
    parser.add_argument(
        "--suite",
        choices=["all", *list(_SUITE_RUNNERS)],
        default="all",
        help="Suite to run (default: all — accuracy, docs, wave5, isolation)",
    )
    args = parser.parse_args()

    suites = list(_DEFAULT_SUITES) if args.suite == "all" else [args.suite]
    leaks = []

    for name in suites:
        header, runner = _SUITE_RUNNERS[name]
        print(header)
        if name == "isolation":
            leaks = runner()
        else:
            runner()

    if "isolation" in suites:
        if leaks:
            print(f"ISOLATION FAILURE: {len(leaks)} case(s) leaked: {leaks}")
            sys.exit(1)
        print("isolation: 100% blocked")


if __name__ == "__main__":
    main()
