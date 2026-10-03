#!/usr/bin/env python3.13
"""Accountant holdout battery — multi-session dialogue eval (not in default suites).

Calls agent.ask_stream directly (same session wiring as api/server.py).
Never promotes verified queries. Refuses production DeepSeek unless --allow-deepseek.

Usage:
  set -a && source .env && set +a
  python3.13 evals/run_accountant_holdout.py --self-check
  python3.13 evals/run_accountant_holdout.py --allow-deepseek   # only if intentional
  python3.13 evals/run_accountant_holdout.py --ids ah-001,ah-002
  python3.13 evals/run_accountant_holdout.py --repeat 3       # pass^3 numeric stability
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from collections import Counter, defaultdict
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core import agent  # noqa: E402
from core.sessions import record_session_turn  # noqa: E402

EVALS = Path(__file__).resolve().parent
CASES_FILE = EVALS / "accountant_holdout.jsonl"
OUT = EVALS / "accountant_holdout_results.json"
CLIENT = os.environ.get("CHATBOT_CLIENT", "105")

_DEEPSEEK_HOST = "https://api.deepseek.com"
_AR_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
_NUM_RE = re.compile(r"\d+(?:\.\d+)?")
_BENCHMARK_INVENT_RE = re.compile(
    r"(هدف|target|benchmark|يجب أن|must reach|KPI|مقارنة مع\s+\d|better than\s+\d)",
    re.I,
)
_PERIOD_ASK_RE = re.compile(
    r"(أي\s+فتر|which\s+period|what\s+month|what\s+date|من\s+متى|لأي\s+شهر|حدد\s+الفتر|specify)",
    re.I,
)


def _llm_base_url() -> str:
    return (os.environ.get("CHATBOT_LLM_BASE_URL") or _DEEPSEEK_HOST).rstrip("/")


def _assert_provider_allowed(*, allow_deepseek: bool) -> None:
    base = _llm_base_url()
    if base.rstrip("/") == _DEEPSEEK_HOST.rstrip("/") and not allow_deepseek:
        print(
            json.dumps(
                {
                    "error": "refused_deepseek",
                    "detail": (
                        "CHATBOT_LLM_BASE_URL is DeepSeek (production). "
                        "Set Composer endpoint in .env for battery runs, or pass --allow-deepseek."
                    ),
                    "CHATBOT_LLM_BASE_URL": base,
                },
                ensure_ascii=False,
            ),
            file=sys.stderr,
        )
        sys.exit(2)


def load_cases(path: Path = CASES_FILE) -> list[dict]:
    cases: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        row = json.loads(line)
        if "expect_tool" in row:
            raise ValueError(f"{row.get('id')}: expect_tool forbidden in holdout jsonl")
        cases.append(row)
    return cases


def self_check(cases: list[dict] | None = None) -> None:
    cases = cases or load_cases()
    assert len(cases) >= 60, f"expected >=60 turns, got {len(cases)}"
    ids = [c["id"] for c in cases]
    assert len(ids) == len(set(ids)), "duplicate case ids"
    sessions = {c["session"] for c in cases}
    assert len(sessions) >= 30, f"expected >=30 sessions, got {len(sessions)}"
    for c in cases:
        exp = c.get("expects") or {}
        assert exp.get("type") in ("number", "label", "howto", "opinion", "clarify"), c["id"]
        assert c.get("turn") is not None, c["id"]
    print(
        f"self-check OK: {len(cases)} turns, {len(sessions)} sessions",
        flush=True,
    )


def _subject(session_key: str) -> str:
    return hashlib.sha256(session_key.encode()).hexdigest()[:12]


def run_one(
    client: str,
    session_state: dict,
    case: dict,
    session_key: str,
) -> dict:
    company_id = int(case.get("company_id") or 1)
    conv = session_state.setdefault("conversation", {})
    conv["CompanyID"] = company_id
    history = session_state.setdefault("history", [])
    question = case.get("question", "")

    answer_chunks: list[str] = []
    steps: list[str] = []
    result: dict = {}
    t0 = time.perf_counter()
    error: str | None = None
    try:
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
    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"[:500]
    elapsed = round(time.perf_counter() - t0, 2)

    answer = result.get("answer") or "".join(answer_chunks)
    if str(question or "").strip() and str(answer or "").strip():
        record_session_turn(
            session_state,
            question=question,
            result=result,
            client=client,
            company_id=company_id,
            max_history=agent.MAX_HISTORY_TURNS,
        )

    queries = result.get("queries")
    if not queries and result.get("answer_sql"):
        queries = [s.strip() for s in str(result["answer_sql"]).split(";") if s.strip()]
    return {
        "elapsed_s": elapsed,
        "answer": answer,
        "answer_sql": result.get("answer_sql") or "",
        "queries": queries or [],
        "query_log": result.get("query_log") or [],
        "needs_ask": result.get("needs_ask"),
        "sources": result.get("sources") or [],
        "steps": steps,
        "error": error,
        "tools_ms": result.get("tools_ms") or {},
        "llm_calls": result.get("llm_calls"),
        "prompt_tokens": result.get("prompt_tokens"),
        "completion_tokens": result.get("completion_tokens"),
        "cache_hit_tokens": result.get("cache_hit_tokens"),
        "cache_miss_tokens": result.get("cache_miss_tokens"),
        "vault_search_count": result.get("vault_search_count"),
        "doc_search_count": result.get("doc_search_count"),
        "thread_head": result.get("thread_head"),
    }


def _normalize_numbers(text: str) -> list[str]:
    t = (text or "").translate(_AR_DIGITS)
    return _NUM_RE.findall(t)


def _score_case(case: dict, parsed: dict) -> dict:
    exp = case.get("expects") or {}
    kind = exp.get("type")
    answer = (parsed.get("answer") or "").strip()
    needs = (parsed.get("needs_ask") or "").strip()
    combined = answer or needs
    notes: list[str] = []
    flags: list[str] = []
    status = "skipped"

    run_error = parsed.get("error")
    if run_error:
        return {
            "status": "fail",
            "kind": kind,
            "notes": [run_error],
            "flags": ["agent_error"],
        }

    if kind == "number":
        gold = exp.get("gold")
        if gold == "pending" or gold is None:
            status = "skipped_pending_gold"
            notes.append("gold pending — human must fill from read-only SQL")
        elif not combined:
            status = "fail"
            flags.append("empty_answer")
        else:
            nums = _normalize_numbers(combined)
            if not nums:
                status = "fail"
                flags.append("no_numeric_in_answer")
            else:
                try:
                    target = float(gold)
                except (TypeError, ValueError):
                    status = "fail"
                    flags.append("bad_gold")
                else:
                    tol = 0.02 if not exp.get("gold_int") else 0.5
                    matched = any(abs(float(n) - target) <= tol for n in nums)
                    if matched:
                        status = "pass"
                        notes.append(f"matched gold {gold}")
                    else:
                        status = "fail"
                        flags.append(f"numeric_mismatch_want_{gold}_got_{nums[:3]}")
        if exp.get("no_single_headline_total") and combined:
            if re.search(r"إجمالي\s+الشركة|company total|total sales for july", combined, re.I):
                flags.append("collapsed_to_single_total")
                if status == "pass":
                    status = "weak"

    elif kind == "howto":
        if not combined:
            status = "fail"
            flags.append("empty_answer")
        else:
            blob = combined.lower()
            phrases = exp.get("phrases") or []
            hits = sum(1 for p in phrases if p.lower() in blob)
            if hits >= max(1, len(phrases) // 3):
                status = "pass"
                notes.append(f"howto cues {hits}/{len(phrases)}")
            else:
                status = "weak"
                flags.append("thin_howto_citation")

    elif kind == "label":
        if not combined:
            status = "fail"
            flags.append("empty_answer")
        else:
            blob = combined.lower()
            phrases = exp.get("phrases") or []
            if any(p.lower() in blob for p in phrases):
                status = "pass"
            else:
                status = "weak"
                flags.append("missing_label_phrase")

    elif kind == "opinion":
        if not combined:
            status = "fail"
            flags.append("empty_answer")
        elif exp.get("must_not_invent_target") and _BENCHMARK_INVENT_RE.search(combined):
            status = "fail"
            flags.append("invented_benchmark")
        else:
            status = "pass"
            notes.append("opinion without invented target")

    elif kind == "clarify":
        asks = bool(needs) or bool(_PERIOD_ASK_RE.search(combined))
        if exp.get("asks_period") and not asks:
            status = "weak"
            flags.append("did_not_ask_period")
        elif exp.get("must_not_reuse_yesterday") and combined:
            if re.search(r"نفس\s+(رقم|مبلغ|total)|same\s+amount", combined, re.I) and not asks:
                status = "fail"
                flags.append("reused_yesterday_without_clarify")
            else:
                status = "pass" if asks else "weak"
        elif exp.get("needs_salesman_or_report"):
            if needs or "مندوب" in combined or "salesman" in combined.lower():
                status = "pass"
                notes.append("clarified report params")
            else:
                status = "weak"
        elif exp.get("asks_basis_or_period"):
            status = "pass" if asks or "ضريب" in combined or "tax" in combined.lower() else "weak"
        else:
            status = "pass" if asks else "weak"

    return {"status": status, "kind": kind, "notes": notes, "flags": flags}


def _flake_report(run_rows: list[list[dict]]) -> dict:
    """Compare numeric tokens across repeated full-battery runs (pass^3)."""
    by_id: dict[str, list[list[str]]] = defaultdict(list)
    for run in run_rows:
        for row in run:
            exp = row.get("expects") or {}
            if exp.get("type") != "number" or exp.get("gold") == "pending":
                continue
            nums = _normalize_numbers(row.get("answer") or "")
            by_id[row["id"]].append(nums)
    flakes = []
    for cid, runs in by_id.items():
        if len(runs) < 2:
            continue
        sigs = [tuple(r) for r in runs]
        if len(set(sigs)) > 1:
            flakes.append({"id": cid, "runs": runs})
    return {"flake_count": len(flakes), "flakes": flakes}


def run_battery(
    *,
    client: str = CLIENT,
    cases: list[dict] | None = None,
    case_ids: set[str] | None = None,
    repeat: int = 1,
) -> dict:
    cases = cases or load_cases()
    if case_ids:
        cases = [c for c in cases if c["id"] in case_ids]
        if not cases:
            raise SystemExit(f"no cases matched ids: {case_ids}")

    all_runs: list[list[dict]] = []
    for run_idx in range(repeat):
        sessions: dict[str, dict] = {}
        results: list[dict] = []
        for case in cases:
            sid_key = case["session"]
            if sid_key not in sessions:
                sessions[sid_key] = {}
            print(f"[run {run_idx + 1}/{repeat}] {case['id']} session={sid_key} turn={case['turn']}...", flush=True)
            parsed = run_one(client, sessions[sid_key], case, sid_key)
            ev = _score_case(case, parsed)
            results.append({**case, "client": client, **parsed, "evaluation": ev})
        all_runs.append(results)

    final_results = all_runs[-1]
    status_counts = Counter(r["evaluation"]["status"] for r in final_results)
    payload = {
        "run_at": datetime.now(UTC).isoformat(),
        "client": client,
        "llm_base_url": _llm_base_url(),
        "llm_model_fast": os.environ.get("CHATBOT_MODEL_FAST", ""),
        "battery_note": (
            "Representative 16-turn subset only; full 67-turn holdout not run in this session."
            if case_ids and len(cases or []) < 67
            else None
        ),
        "cases_file": str(CASES_FILE.name),
        "repeat": repeat,
        "turns": len(final_results),
        "sessions": len({c["session"] for c in cases}),
        "status_counts": dict(status_counts),
        "flake": _flake_report(all_runs) if repeat > 1 else None,
        "results": final_results,
        "promote_verified_query": False,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Run accountant holdout battery")
    parser.add_argument("--self-check", action="store_true", help="Validate jsonl only")
    parser.add_argument("--allow-deepseek", action="store_true", help="Allow production DeepSeek endpoint")
    parser.add_argument("--ids", type=str, default="", help="Comma-separated case ids")
    parser.add_argument("--repeat", type=int, default=1, help="Full battery repeats for pass^3")
    args = parser.parse_args()

    if args.self_check:
        self_check()
        return

    _assert_provider_allowed(allow_deepseek=args.allow_deepseek)
    ids = {x.strip() for x in args.ids.split(",") if x.strip()} or None
    payload = run_battery(case_ids=ids, repeat=max(1, args.repeat))
    print(json.dumps({k: payload[k] for k in ("run_at", "turns", "sessions", "status_counts", "flake", "promote_verified_query")}, ensure_ascii=False, indent=2))
    print(f"Wrote {OUT}", flush=True)


if __name__ == "__main__":
    main()
