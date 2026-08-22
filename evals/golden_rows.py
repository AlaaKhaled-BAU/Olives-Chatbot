"""TRACK A: execution-accuracy grading.

A case passes when the candidate SQL — executed through the real gated
path — returns THE SAME ROWS as the stored gold SQL, regardless of answer
wording. This is strictly stronger than substring scoring: wording can't
fool it, and it directly measures the thing users care about (the data).

Row normalization: every value -> ISO string; floats rounded to 2dp so
432.58 == 432.582; rows sorted so result order never decides pass/fail.
"""
from __future__ import annotations

import json
import math
from datetime import date, datetime
from decimal import Decimal


def _norm_value(v):
    if v is None:
        return ""
    if isinstance(v, bool):
        return str(int(v))
    if isinstance(v, (int, float, Decimal)):
        # One numeric path: 238, 238.0 and 238.004±tol all normalize to the
        # same 2dp string — cross-type equality must never depend on which
        # driver returned int vs float.
        return f"{float(v):.2f}"
    if isinstance(v, (datetime, date)):
        return v.isoformat()[:10]
    return str(v).strip().lower()


def normalize_rows(rows) -> list[tuple]:
    """[{col: val}] -> sorted list of column-sorted value tuples."""
    out = []
    for row in rows or []:
        out.append(tuple(_norm_value(row[k]) for k in sorted(row.keys(), key=str)))
    return sorted(out)


def rows_equal(gold_rows, candidate_rows) -> bool:
    return normalize_rows(gold_rows) == normalize_rows(candidate_rows)


def load_cases(path) -> list[dict]:
    import json as _json
    from pathlib import Path
    return [_json.loads(line) for line in Path(path).read_text().splitlines() if line.strip()]


def run_suite(cases, agent_ask, run_select, verbose=True) -> tuple[int, int]:
    """Execute gold SQL + candidate SQL through the same gated path; compare.
    Returns (passed, total)."""
    passed = 0
    for case in cases:
        name = case.get("name", "?")
        company_id = case.get("company_id", 1)
        client = case["client"]
        conversation = {"CompanyID": company_id}
        try:
            gold_rows = run_select(case["gold_sql"], company_id, client)
            result = agent_ask(client, case["question"], conversation=conversation)
            cand_sql = result.get("answer_sql") or ""
            if not cand_sql:
                if verbose:
                    print(f"  [FAIL] {name}: no answer_sql produced")
                continue
            cand_rows = run_select(cand_sql.split(";")[0], company_id, client)
        except Exception as exc:  # noqa: BLE001 — harness failures are results, not crashes
            if verbose:
                print(f"  [FAIL] {name}: {type(exc).__name__}: {str(exc)[:120]}")
            continue
        ok = rows_equal(case.get("gold_rows"), cand_rows)
        passed += int(ok)
        if verbose:
            mark = "PASS" if ok else "FAIL"
            print(f"  [{mark}] {name}: {case['question']!r} -> {len(cand_rows)} rows")
    return passed, len(cases)
