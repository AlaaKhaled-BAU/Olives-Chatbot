#!/usr/bin/env python3.13
"""Stress-70 evaluation driver (plan: user-requested large model eval).

Runs every case through the real agent loop against the local instance,
times it, auto-validates numeric/date answers against reference SQL, keeps
chain history so multi-turn cases exercise conversation memory, and writes
evals/stress70_results.jsonl for manual grading.

Parallelized: 5 workers; chains hold one worker until their last turn.
"""
from __future__ import annotations

import concurrent.futures as cf
import json
import re
import sys
import threading
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from core import agent  # noqa: E402

CASES_PATH = BASE_DIR / "evals" / "stress70.jsonl"
OUT_PATH = BASE_DIR / "evals" / "stress70_results.jsonl"
AR_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
_NUM_RE = re.compile(r"-?\d[\d,]*(?:\.\d+)?")


def ask_once(client: str, q: str, company_id, history=None) -> dict:
    conv = {"CompanyID": company_id} if company_id is not None else {}
    done = None
    for ev in agent.ask_stream(client, q, conversation=conv,
                               subject=f"stress-{threading.get_ident()}",
                               history=history or None):
        if ev["type"] == "done":
            done = {k: v for k, v in ev.items() if k != "type"}
    return done or {"answer": None, "needs_ask": "NO_DONE_EVENT", "answer_sql": None}


def numbers_in(text: str) -> list[float]:
    flat = (text or "").translate(AR_DIGITS).replace(",", "")
    out = []
    for m in _NUM_RE.finditer(flat):
        try:
            out.append(float(m.group()))
        except ValueError:
            pass
    return out


def close(a: float, b: float) -> bool:
    return abs(a - b) <= max(abs(b) * 0.008, 0.51)


def validate(case: dict, result: dict, gold_rows: list | None) -> dict:
    """Auto-grading where possible; everything else left for manual review."""
    if result.get("needs_ask"):
        return {"auto": "NEEDS_ASK"}
    ans = result.get("answer") or ""
    if not ans.strip():
        return {"auto": "FAIL_EMPTY"}
    if gold_rows is not None:
        want = []
        for row in gold_rows:
            for v in row.values():
                try:
                    want.append(float(str(v).translate(AR_DIGITS).replace(",", "")))
                except ValueError:
                    pass
        got = numbers_in(ans)
        ok = all(any(close(g, x) for x in got) for g in want)
        return {"auto": "PASS_NUMBER" if ok else "FAIL_NUMBER",
                "expected": want}
    return {"auto": "MANUAL"}


def run_case(case: dict, gold_cache: dict) -> dict:
    t0 = time.perf_counter()
    rec = {"id": case["id"], "cat": case["cat"], "note": case.get("note", "")}
    try:
        if "turns" in case:  # chain
            turns_out, hist = [], []
            for i, q in enumerate(case["turns"], 1):
                tq0 = time.perf_counter()
                res = ask_once("105", q, case.get("company"), hist)
                dt = round(time.perf_counter() - tq0, 1)
                turns_out.append({"turn": i, "q": q, "elapsed_s": dt,
                                  "answer": (res.get("answer") or "")[:600],
                                  "needs_ask": res.get("needs_ask"),
                                  "answer_sql": (res.get("answer_sql") or "")[:200],
                                  "followups": len(res.get("followups") or [])})
                a = res.get("answer")
                if a:
                    hist.append({"q": q, "a": str(a)[:400],
                                 "sql": (res.get("answer_sql") or "")[:200]})
                    del hist[:-agent.MAX_HISTORY_TURNS]
            rec.update(mode="chain", turns=turns_out,
                       elapsed_s=round(time.perf_counter() - t0, 1))
            rec["final_answer"] = turns_out[-1]["answer"][:300] if turns_out else ""
            rec["validation"] = {"auto": "MANUAL_CHAIN"}
        else:
            res = ask_once("105", case["q"], case.get("company"))
            rec.update(mode="single",
                       q=case["q"],
                       elapsed_s=round(time.perf_counter() - t0, 1),
                       answer=(res.get("answer") or "")[:700],
                       needs_ask=res.get("needs_ask"),
                       answer_sql=(res.get("answer_sql") or "")[:250],
                       sources=res.get("sources") or [],
                       followups=len(res.get("followups") or []),
                       confidence=res.get("confidence"))
            gold = gold_cache.get(case["id"])
            rec["validation"] = validate(case, res, gold)
    except Exception as exc:  # noqa: BLE001 — harness failures are findings
        rec["validation"] = {"auto": f"HARNESS_ERROR: {type(exc).__name__}: {str(exc)[:120]}"}
        rec["elapsed_s"] = round(time.perf_counter() - t0, 1)
    print(f"[{rec['id']}] {rec['validation'].get('auto', '')} {rec.get('elapsed_s', '?')}s", flush=True)
    return rec


def main() -> None:
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    cases = [json.loads(l) for l in CASES_PATH.read_text().splitlines() if l.strip()]
    # Pre-compute gold rows once (main thread, before fan-out).
    from core import sql
    gold_cache: dict[str, list] = {}
    for c in cases:
        g = c.get("gold_sql")
        if g:
            try:
                gold_cache[c["id"]] = sql.run_select(g, c.get("company") or 2, "105")
            except Exception as exc:  # noqa: BLE001
                print(f"[gold-skip {c['id']}] {exc}", flush=True)

    t0 = time.perf_counter()
    records = []
    with cf.ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(run_case, c, gold_cache) for c in cases]
        for f in cf.as_completed(futures):
            records.append(f.result())

    # Stable output order matching input file.
    order = {c["id"]: i for i, c in enumerate(cases)}
    records.sort(key=lambda r: order.get(r["id"], 999))
    OUT_PATH.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in records) + "\n")
    wall = round(time.perf_counter() - t0, 1)
    total_turns = sum(len(r.get("turns", [])) or 1 for r in records)
    print(f"\nDONE {len(records)} cases / {total_turns} graded turns "
          f"in {wall}s wall ({OUT_PATH.name})")


if __name__ == "__main__":
    main()
