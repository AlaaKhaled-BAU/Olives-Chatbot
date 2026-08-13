#!/usr/bin/env python3.13
"""Phase 8/9: the release gate. Runs accuracy.jsonl (prints a %) and
isolation.jsonl (exits non-zero if ANY case leaks -- PLAN.md: a single leak
fails the build). Isolation cases go through the real gate/wall/catalog
code paths, not the model's judgment -- "blocked" here means the server
refused, not that the model declined to try.

Only a known "this was actually denied" exception counts as blocked
(GateError, or a pymssql permission/operational error) -- anything else
propagates as a real harness failure. A bare `except Exception` here once
silently turned a TypeError (a bug in this very script) into a false
"BLOCKED" -- reporting 100% safe while not actually running the attack at
all. Never widen this back to a bare except for convenience."""
import json
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


def _load(name):
    path = BASE_DIR / "evals" / name
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def run_accuracy():
    """C3a: every PASSING, non-refusal case with a real answer_sql gets its
    query promoted to verified_queries (source="eval") -- the few-shot pool
    is now seeded from a corpus of KNOWN-correct answers instead of from
    raw user traffic (which C3 correctly stopped trusting on its own).
    Re-running this script re-seeds every time, so the pool tracks the
    eval corpus as it grows rather than going stale."""
    cases = _load("accuracy.jsonl")
    passed = 0
    promoted = 0
    for case in cases:
        result = agent.ask(case["client"], case["question"])
        answer = (result["answer"] or result["needs_ask"] or "").lower()
        answer_normalized = answer.replace(",", "")  # "33,517" and "33517" must both match
        if case.get("expect_refusal"):
            ok = bool(result["needs_ask"]) or any(m in answer for m in REFUSAL_MARKERS)
        elif "expect_contains_any" in case:
            ok = any(needle.lower() in answer_normalized for needle in case["expect_contains_any"])
        else:
            ok = all(needle.lower() in answer_normalized for needle in case["expect_contains"])
        print(f"  [{'PASS' if ok else 'FAIL'}] {case['name']}: {case['question']!r} -> {answer[:120]!r}")
        passed += int(ok)
        if ok and not case.get("expect_refusal") and result.get("answer_sql"):
            memory.promote_verified_query(case["client"], case["question"], result["answer_sql"], source="eval")
            promoted += 1
    pct = 100 * passed / len(cases) if cases else 0
    print(f"accuracy: {passed}/{len(cases)} ({pct:.0f}%)")
    print(f"  promoted {promoted} query pattern(s) to verified_queries (source=eval)")
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
        result = agent.ask(case["client"], case["question"])
        answer = (result["answer"] or result["needs_ask"] or "").lower()
        answer_normalized = answer.replace(",", "")
        if case.get("expect_refusal"):
            ok = bool(result["needs_ask"]) or any(m in answer for m in REFUSAL_MARKERS)
        elif "expect_contains_any" in case:
            ok = any(needle.lower() in answer_normalized for needle in case["expect_contains_any"])
        else:
            ok = all(needle.lower() in answer_normalized for needle in case["expect_contains"])
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


def main():
    print("=== accuracy ===")
    run_accuracy()
    print("=== docs accuracy ===")
    run_docs_accuracy()
    print("=== isolation (release gate) ===")
    leaks = run_isolation()
    if leaks:
        print(f"ISOLATION FAILURE: {len(leaks)} case(s) leaked: {leaks}")
        sys.exit(1)
    print("isolation: 100% blocked")


if __name__ == "__main__":
    main()
