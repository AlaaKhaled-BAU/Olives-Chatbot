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
    s = str(v).strip().lower()
    # Type symmetry: a numeric STRING must land where the same NUMBER lands,
    # or snapshot-vs-candidate comparisons split on representation.
    try:
        return f"{float(s.replace(',', '')):.2f}"
    except ValueError:
        return s


def snapshot_rows(rows) -> list[dict]:
    """Build-time capture preserving COLUMN NAMES (projection needs them at
    grade time): [{'gross_amount': '432.58'}, ...] with values already
    normalized so grade-time normalization is idempotent."""
    if isinstance(rows, dict):
        rows = rows.get("rows", [])
    out = []
    for row in rows or []:
        if isinstance(row, dict):
            out.append({str(k): _norm_value(v) for k, v in row.items()})
        else:
            raise ValueError("cannot snapshot nameless rows — gold SQL must return dict rows")
    return out


def normalize_rows(rows) -> list[tuple]:
    """Robust over result shapes: {col: val} rows, bare [val] rows,
    driver oddities, and the capped {'rows': [...]} wrapper."""
    if isinstance(rows, dict):  # capped-shape wrapper
        rows = rows.get("rows", [])
    if rows is None:
        return []
    out = []
    for row in rows:
        if isinstance(row, dict):
            out.append(tuple(_norm_value(row[k]) for k in sorted(row.keys(), key=str)))
        elif isinstance(row, (list, tuple)):
            out.append(tuple(_norm_value(v) for v in row))
        else:
            out.append((_norm_value(row),))
    return sorted(out)


def _unwrap(rows):
    if isinstance(rows, dict):
        rows = rows.get("rows", [])
    return rows or []


def _ci_map(row: dict) -> dict:
    """Case-insensitive column lookup (SQL Server collations ignore case;
    driver-preserved casing must not decide pass/fail)."""
    return {_col_key(k): v for k, v in row.items()}


def _col_key(name):
    return str(name).strip().lower()


def rows_equal(gold_rows, candidate_rows) -> bool:
    """Column-projected comparison (TRACK A hardening): when both sides are
    dict-rows, grade ONLY the gold columns — candidates may return extra
    columns (e.g. the certified metric ships invoice_count alongside
    gross_amount) without failing, but every gold column must exist and
    match. Missing gold column in candidate = fail. Non-dict shapes fall
    back to strict whole-tuple comparison. Row order never matters."""
    gold = _unwrap(gold_rows)
    cand = _unwrap(candidate_rows)
    if not gold and not cand:
        return True
    if gold and all(isinstance(r, dict) for r in gold) \
            and cand and all(isinstance(r, dict) for r in cand):
        gold_cols = []
        seen = set()
        for r in gold:
            for k in r.keys():
                ck = _col_key(k)
                if ck not in seen:
                    seen.add(ck)
                    gold_cols.append(ck)
        cand_maps = [_ci_map(r) for r in cand]

        def proj(row_map):
            try:
                return tuple(_norm_value(row_map[c]) for c in gold_cols)
            except KeyError:
                return None

        try:
            gold_set = sorted(
                tuple(_norm_value(_ci_map(r)[c]) for c in gold_cols) for r in gold)
        except KeyError:
            gold_missing = True  # ragged/unmatched names — try value-tier below
        else:
            gold_missing = False

        cand_proj = []
        names_match = not gold_missing and all(
            all(c in m for c in gold_cols) for m in cand_maps)

        if names_match:
            for m in cand_maps:
                p = proj(m)
                if p is None:
                    return False  # candidate missing a required gold column
                cand_proj.append(p)
            return sorted(cand_proj) == gold_set

        # Value-tier fallback: aggregate aliases are model-invented
        # (COUNT(*) AS CustomerCount vs our AS n), so names legitimately
        # diverge. For SINGLE-column golds, pass iff every gold value exists
        # among the candidate cells and the candidate isn't missing rows.
        if len(gold_cols) == 1:
            needed = {_norm_value(r[gold_cols[0]]) for r in gold}
            have = {_norm_value(v) for r in cand for v in r.values()}
            return needed <= have and len(cand) >= len(gold)
        return False
    return normalize_rows(gold) == normalize_rows(cand)


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
        if not ok and verbose:
            from evals.golden_rows import normalize_rows as _nr
            print(f"    cand_sql: {cand_sql[:180]!r}")
            print(f"    gold={_nr(case.get('gold_rows'))[:5]} cand={_nr(cand_rows)[:5]}")
        passed += int(ok)
        if verbose:
            mark = "PASS" if ok else "FAIL"
            print(f"  [{mark}] {name}: {case['question']!r} -> {len(cand_rows)} rows")
    return passed, len(cases)
