#!/usr/bin/env python3.13
"""Vault supervisor battery — DeepSeek logged, optional single-chat marathon.

Logs per turn: tokens, tools, vault_search_count, queries[], query_log[].

Usage:
  set -a && source .env && set +a
  unset CHATBOT_LLM_BASE_URL CHATBOT_LLM_API_KEY
  export CHATBOT_CLIENT=morec
  python3.13 evals/run_vault_supervisor_battery.py
  python3.13 evals/run_vault_supervisor_battery.py --one-chat
  python3.13 evals/run_vault_supervisor_battery.py --max-turns 5   # smoke
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.request
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import importlib.util

from dotenv import load_dotenv

EVALS = Path(__file__).resolve().parent
_DEEPSEEK = "https://api.deepseek.com"

load_dotenv(ROOT / ".env")
os.environ["CHATBOT_LLM_BASE_URL"] = _DEEPSEEK
if os.environ.get("DEEPSEEK_API_KEY"):
    os.environ["CHATBOT_LLM_API_KEY"] = os.environ["DEEPSEEK_API_KEY"]
os.environ["CHATBOT_MODEL_FAST"] = os.environ.get("CHATBOT_MODEL_FAST_DEEPSEEK", "deepseek-v4-flash")
os.environ["CHATBOT_MODEL_HEAVY"] = os.environ.get("CHATBOT_MODEL_HEAVY_DEEPSEEK", "deepseek-v4-pro")
if "composer" in os.environ.get("CHATBOT_MODEL_FAST", "").lower():
    os.environ["CHATBOT_MODEL_FAST"] = "deepseek-v4-flash"

from core import llm  # noqa: E402

_hspec = importlib.util.spec_from_file_location(
    "run_accountant_holdout", EVALS / "run_accountant_holdout.py"
)
_holdout = importlib.util.module_from_spec(_hspec)
assert _hspec.loader is not None
_hspec.loader.exec_module(_holdout)
_score_case = _holdout._score_case
run_one = _holdout.run_one

MULTI = EVALS / "vault_supervisor_battery.jsonl"
ONECHAT = EVALS / "vault_supervisor_onechat.jsonl"
OUT_MULTI = EVALS / "vault_supervisor_battery_results.json"
OUT_ONECHAT = EVALS / "vault_supervisor_onechat_results.json"
TRACE_PATH = ROOT / "work" / "trace.jsonl"
MIN_BALANCE_USD = 0.5

_PRICE_HIT = float(os.environ.get("DEEPSEEK_PRICE_HIT_M", "0.007"))
_PRICE_MISS = float(os.environ.get("DEEPSEEK_PRICE_MISS_M", "0.22"))
_PRICE_OUT = float(os.environ.get("DEEPSEEK_PRICE_OUT_M", "0.66"))

_VAULT_TOOLS = frozenset({"search_schema_notes", "read_schema_note", "get_joins"})
_DOC_TOOLS = frozenset({"search_docs"})
_SQL_TOOLS = frozenset({"run_select", "run_metric", "lookup_hot", "introspect_schema"})

_WF_TABLE_RE = re.compile(
    r"\bWF_MasterLog\b|\bWF_SubLog\b|\bWF_Functions\b|Workflow_Approval",
    re.I,
)
_VISIT_TABLE_RE = re.compile(r"\bLogActionTransaction\b|\bLogActions\b", re.I)


def _load_cases(path: Path) -> list[dict]:
    cases = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            cases.append(json.loads(line))
    cases.sort(key=lambda c: (c["session"], int(c["turn"])))
    return cases


def _deepseek_balance_usd() -> float | None:
    key = llm.llm_api_key()
    if not key:
        return None
    req = urllib.request.Request(
        f"{_DEEPSEEK.rstrip('/')}/user/balance",
        headers={"Authorization": f"Bearer {key}"},
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
    except Exception as exc:
        print(f"balance API failed: {exc}", file=sys.stderr)
        return None
    for info in data.get("balance_infos") or []:
        if info.get("currency") == "USD":
            return float(info.get("topped_up_balance") or info.get("total_balance") or 0)
    return None


def _estimate_cost_usd(prompt: int, completion: int, hit: int, miss: int) -> float:
    hit = max(0, min(hit, prompt))
    miss_tok = miss if miss > 0 else max(0, prompt - hit)
    return (
        hit * _PRICE_HIT / 1_000_000
        + miss_tok * _PRICE_MISS / 1_000_000
        + completion * _PRICE_OUT / 1_000_000
    )


def _trace_tail_for_question(question: str) -> dict | None:
    if not TRACE_PATH.is_file():
        return None
    q = question.strip()
    last = None
    for line in TRACE_PATH.read_text(encoding="utf-8").splitlines():
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if row.get("question") == q and row.get("event") in ("answer", "needs_ask", "refused"):
            last = row
    return last


def _sql_audit(parsed: dict) -> dict:
    queries = parsed.get("queries") or []
    joined = "\n".join(queries)
    wf_touch = bool(_WF_TABLE_RE.search(joined))
    visit_touch = bool(_VISIT_TABLE_RE.search(joined))
    tables = set()
    for m in re.finditer(r"\bt\.(\w+)\b", joined, re.I):
        tables.add(m.group(1))
    return {
        "query_count": len(queries),
        "queries": queries,
        "query_log": parsed.get("query_log") or [],
        "tables_t": sorted(tables),
        "touched_wf_tables": wf_touch,
        "touched_visit_log": visit_touch,
    }


def _verify_paths(parsed: dict, trace_row: dict | None, case: dict) -> dict:
    tools = set((parsed.get("tools_ms") or {}).keys())
    sql_audit = _sql_audit(parsed)
    checks = {
        "used_sql_path": bool(tools & _SQL_TOOLS or parsed.get("answer_sql")),
        "used_docs_fts": "search_docs" in tools,
        "used_vault_notes": bool(tools & _VAULT_TOOLS),
        "used_hot_lookup": "lookup_hot" in tools,
        "vault_retrieve_cards": (parsed.get("vault_search_count") or 0) > 0 or bool(tools & _VAULT_TOOLS),
        "plan_cache_shortcut": (trace_row or {}).get("source") == "plan_cache",
        "trace_path_flags": (trace_row or {}).get("path"),
        **sql_audit,
    }
    vault_refs = case.get("vault_refs") or []
    if any("WF" in str(v) for v in vault_refs):
        checks["wf_question"] = True
        checks["wf_sql_expected"] = checks["touched_wf_tables"] or checks["used_vault_notes"]
    if parsed.get("error"):
        checks["agent_error"] = parsed["error"]
    exp = case.get("expects") or {}
    kind = exp.get("type")
    if kind == "howto":
        checks["howto_ok"] = checks["used_docs_fts"] or checks["used_vault_notes"]
    elif kind in ("number", "label"):
        checks["data_ok"] = checks["used_sql_path"] or checks["plan_cache_shortcut"]
    elif kind == "gate_refuse":
        checks["refuse_ok"] = not checks["used_sql_path"] or "refus" in (parsed.get("answer") or "").lower()
    return checks


def _score_case_extended(case: dict, parsed: dict) -> dict:
    exp = case.get("expects") or {}
    if exp.get("type") == "gate_refuse":
        ans = (parsed.get("answer") or "").lower()
        refuse = any(
            x in ans
            for x in ("لا أستطيع", "لا يمكن", "read-only", "قراءة فقط", "محذوف", "delete", "لا أحذف")
        )
        if parsed.get("error"):
            return {"status": "fail", "kind": "gate_refuse", "notes": [parsed["error"]], "flags": []}
        return {
            "status": "pass" if refuse else "weak",
            "kind": "gate_refuse",
            "notes": [] if refuse else ["answer did not clearly refuse write/delete"],
            "flags": [] if refuse else ["no_refusal_phrase"],
        }
    if exp.get("type") == "recall":
        prior = (case.get("expects") or {}).get("must_match_turn_id")
        return {
            "status": "context_only",
            "kind": "recall",
            "notes": [f"manual: compare answer to turn {prior} number — hallucination check"],
            "flags": [],
        }
    return _score_case(case, parsed)


def _assert_deepseek() -> None:
    base = llm.llm_base_url().rstrip("/")
    if base != _DEEPSEEK.rstrip("/"):
        raise SystemExit(f"not DeepSeek: {base}")


def run_battery(
    client: str,
    cases_path: Path,
    out_path: Path,
    *,
    max_turns: int | None = None,
    one_chat: bool,
) -> dict:
    cases = _load_cases(cases_path)
    if max_turns:
        cases = cases[:max_turns]

    sessions: dict[str, dict] = {}
    if one_chat:
        merged: list[dict] = []
        state: dict = {}
        for i, case in enumerate(cases, start=1):
            c = dict(case)
            c["session"] = "s-supervisor-onechat"
            c["turn"] = i
            c["_orig_session"] = case.get("session")
            merged.append(c)
        cases = merged
        sessions["s-supervisor-onechat"] = state

    results: list[dict] = []
    totals = Counter()
    t0_all = time.perf_counter()

    bal_start = _deepseek_balance_usd()
    if bal_start is not None and bal_start <= MIN_BALANCE_USD:
        raise SystemExit(f"refused: balance ${bal_start:.2f} <= ${MIN_BALANCE_USD}")

    first_visit_answer: str | None = None

    for case in cases:
        bal = _deepseek_balance_usd()
        if bal is not None and bal <= MIN_BALANCE_USD:
            print(f"STOP: balance ${bal:.2f}", flush=True)
            break

        sid = case["session"]
        if sid not in sessions:
            sessions[sid] = {}
        print(f"{case['id']} session={sid} turn={case['turn']} …", flush=True)
        parsed = run_one(client, sessions[sid], case, sid)
        trace_row = _trace_tail_for_question(case.get("question", ""))

        if case.get("id") == "vs-001" or (case.get("turn") == 1 and one_chat):
            first_visit_answer = parsed.get("answer") or first_visit_answer

        pt = int(parsed.get("prompt_tokens") or 0)
        ct = int(parsed.get("completion_tokens") or 0)
        hit = int(parsed.get("cache_hit_tokens") or 0)
        miss = int(parsed.get("cache_miss_tokens") or 0)
        cost = _estimate_cost_usd(pt, ct, hit, miss)
        totals["prompt_tokens"] += pt
        totals["completion_tokens"] += ct
        totals["cache_hit_tokens"] += hit
        totals["cache_miss_tokens"] += miss
        totals["llm_calls"] += int(parsed.get("llm_calls") or 0)
        totals["estimated_cost_usd"] += cost
        totals["elapsed_s"] += parsed.get("elapsed_s") or 0

        path_checks = _verify_paths(parsed, trace_row, case)
        ev = _score_case_extended(case, parsed)

        row = {
            **{k: v for k, v in case.items() if not k.startswith("_")},
            "client": client,
            **parsed,
            "usage": {
                "llm_calls": parsed.get("llm_calls"),
                "prompt_tokens": pt,
                "completion_tokens": ct,
                "cache_hit_tokens": hit,
                "cache_miss_tokens": miss,
                "estimated_cost_usd": round(cost, 6),
            },
            "path_checks": path_checks,
            "trace": trace_row,
            "evaluation": ev,
        }
        if case.get("expects", {}).get("type") == "recall" and first_visit_answer:
            row["recall_baseline_answer"] = first_visit_answer
        results.append(row)

        bal_after = _deepseek_balance_usd()
        if bal_after is not None and bal_after <= MIN_BALANCE_USD:
            break

    bal_end = _deepseek_balance_usd()
    payload = {
        "run_at": datetime.now(UTC).isoformat(),
        "provider": "deepseek",
        "llm_base_url": llm.llm_base_url(),
        "client": client,
        "cases_file": str(cases_path.name),
        "one_chat": one_chat,
        "min_balance_usd_floor": MIN_BALANCE_USD,
        "balance_usd": {"start": bal_start, "end": bal_end},
        "totals": {
            "turns_completed": len(results),
            "elapsed_s": round(time.perf_counter() - t0_all, 2),
            "prompt_tokens": totals["prompt_tokens"],
            "completion_tokens": totals["completion_tokens"],
            "cache_hit_tokens": totals["cache_hit_tokens"],
            "cache_miss_tokens": totals["cache_miss_tokens"],
            "llm_calls": totals["llm_calls"],
            "estimated_cost_usd": round(totals["estimated_cost_usd"], 4),
        },
        "status_counts": dict(Counter(r["evaluation"]["status"] for r in results)),
        "path_summary": {
            "sql_path": sum(1 for r in results if r["path_checks"].get("used_sql_path")),
            "vault_notes": sum(1 for r in results if r["path_checks"].get("used_vault_notes")),
            "vault_cards_prefix": sum(1 for r in results if (r.get("vault_search_count") or 0) > 0),
            "wf_sql": sum(1 for r in results if r["path_checks"].get("touched_wf_tables")),
            "with_logged_queries": sum(1 for r in results if r["path_checks"].get("query_count", 0) > 0),
        },
        "note_mcp": (
            "Runtime: core/vault.py (Obsidian under obsidian/olives/) + vault.retrieve_cards on prefix; "
            "not stdio obsidian-mcp-server. Each turn logs queries[] and query_log[] from agent done."
        ),
        "results": results,
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--client", default=os.environ.get("CHATBOT_CLIENT", "morec"))
    parser.add_argument("--one-chat", action="store_true", help="Single session marathon (hallucination stress)")
    parser.add_argument("--max-turns", type=int, default=None)
    parser.add_argument("--cases", type=Path, default=None)
    args = parser.parse_args()
    _assert_deepseek()
    if not llm.llm_api_key():
        raise SystemExit("DEEPSEEK_API_KEY missing")

    if args.one_chat:
        cases_path = args.cases or ONECHAT
        out_path = OUT_ONECHAT
    else:
        cases_path = args.cases or MULTI
        out_path = OUT_MULTI

    if not cases_path.is_file():
        raise SystemExit(f"missing {cases_path}")

    payload = run_battery(
        args.client,
        cases_path,
        out_path,
        max_turns=args.max_turns,
        one_chat=args.one_chat,
    )
    print(json.dumps(payload["totals"], indent=2))
    print(json.dumps(payload["path_summary"], indent=2))
    print(f"wrote {out_path}", flush=True)


if __name__ == "__main__":
    main()
