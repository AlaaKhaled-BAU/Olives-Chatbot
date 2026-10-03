#!/usr/bin/env python3.13
"""DeepSeek logged battery: time, tokens, path checks, balance floor.

Usage:
  set -a && source .env && set +a
  unset CHATBOT_LLM_BASE_URL CHATBOT_LLM_API_KEY
  export CHATBOT_CLIENT=morec   # or 105
  python3.13 evals/run_deepseek_logged_battery.py
"""
from __future__ import annotations

import argparse
import json
import os
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

# Pin DeepSeek before core/llm.py load_dotenv (composer vars may be in .env for battery).
load_dotenv(ROOT / ".env")
os.environ["CHATBOT_LLM_BASE_URL"] = _DEEPSEEK
if os.environ.get("DEEPSEEK_API_KEY"):
    os.environ["CHATBOT_LLM_API_KEY"] = os.environ["DEEPSEEK_API_KEY"]
# .env may still say composer-2.5 from the temporary battery — force DeepSeek models.
os.environ["CHATBOT_MODEL_FAST"] = os.environ.get("CHATBOT_MODEL_FAST_DEEPSEEK", "deepseek-v4-flash")
os.environ["CHATBOT_MODEL_HEAVY"] = os.environ.get("CHATBOT_MODEL_HEAVY_DEEPSEEK", "deepseek-v4-pro")
if "composer" in os.environ["CHATBOT_MODEL_FAST"].lower():
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

SUBSET = EVALS / "deepseek_battery_subset.jsonl"
OUT = EVALS / "deepseek_logged_battery_results.json"
TRACE_PATH = ROOT / "work" / "trace.jsonl"
MIN_BALANCE_USD = 0.5

# Off-peak flash $/1M (plans/deepseek_swap_parallel_plan.md) — conservative stop estimate
_PRICE_HIT = float(os.environ.get("DEEPSEEK_PRICE_HIT_M", "0.007"))
_PRICE_MISS = float(os.environ.get("DEEPSEEK_PRICE_MISS_M", "0.22"))
_PRICE_OUT = float(os.environ.get("DEEPSEEK_PRICE_OUT_M", "0.66"))

_VAULT_TOOLS = frozenset({"search_schema_notes", "read_schema_note", "get_joins"})
_DOC_TOOLS = frozenset({"search_docs"})
_SQL_TOOLS = frozenset({"run_select", "run_metric", "lookup_hot", "introspect_schema"})


def _load_subset() -> list[dict]:
    cases = []
    for line in SUBSET.read_text(encoding="utf-8").splitlines():
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
    """Bill hit/miss split when miss unknown: attribute (prompt-hit) to miss."""
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


def _verify_paths(parsed: dict, trace_row: dict | None) -> dict:
    tools = set((parsed.get("tools_ms") or {}).keys())
    checks = {
        "used_sql_path": bool(tools & _SQL_TOOLS or parsed.get("answer_sql")),
        "used_docs_fts": "search_docs" in tools,
        "used_vault_notes": bool(tools & _VAULT_TOOLS),
        "used_hot_lookup": "lookup_hot" in tools,
        "plan_cache_shortcut": (trace_row or {}).get("source") == "plan_cache",
        "trace_path_flags": (trace_row or {}).get("path"),
        "prefix_hash": (trace_row or {}).get("prefix_hash"),
        "playbook_in_prefix": True,  # static prefix always includes join_playbook.md
        "vault_cards_in_prefix": True,  # _all_cards_block in prefix
    }
    if parsed.get("error"):
        checks["agent_error"] = parsed["error"]
    # How-to should hit docs or vault; data should hit SQL
    exp = parsed.get("expects") or {}
    kind = exp.get("type")
    if kind == "howto":
        checks["howto_ok"] = checks["used_docs_fts"] or checks["used_vault_notes"]
    elif kind in ("number", "label"):
        checks["data_ok"] = checks["used_sql_path"] or checks["plan_cache_shortcut"]
    else:
        checks["path_ok"] = True
    return checks


def _assert_deepseek() -> None:
    base = llm.llm_base_url().rstrip("/")
    if base != _DEEPSEEK.rstrip("/"):
        print(
            json.dumps(
                {
                    "error": "not_deepseek",
                    "CHATBOT_LLM_BASE_URL": base,
                    "hint": "unset CHATBOT_LLM_BASE_URL and CHATBOT_LLM_API_KEY",
                },
                indent=2,
            ),
            file=sys.stderr,
        )
        sys.exit(2)


def run_battery(client: str) -> dict:
    cases = _load_subset()
    sessions: dict[str, dict] = {}
    results: list[dict] = []
    totals = Counter()
    t0_all = time.perf_counter()

    bal_start = _deepseek_balance_usd()
    if bal_start is not None and bal_start <= MIN_BALANCE_USD:
        raise SystemExit(f"refused: topped_up_balance ${bal_start:.2f} <= floor ${MIN_BALANCE_USD}")

    for case in cases:
        bal = _deepseek_balance_usd()
        if bal is not None and bal <= MIN_BALANCE_USD:
            print(f"STOP: balance ${bal:.2f} <= ${MIN_BALANCE_USD}", flush=True)
            break

        sid = case["session"]
        if sid not in sessions:
            sessions[sid] = {}
        print(f"{case['id']} session={sid} turn={case['turn']} …", flush=True)
        parsed = run_one(client, sessions[sid], case, sid)
        trace_row = _trace_tail_for_question(case.get("question", ""))

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

        path_checks = _verify_paths({**parsed, "expects": case.get("expects")}, trace_row)
        ev = _score_case(case, parsed) if case.get("score", True) else {
            "status": "context_only",
            "kind": (case.get("expects") or {}).get("type"),
            "notes": ["setup turn for same-chat continuity"],
            "flags": [],
        }

        row = {
            **case,
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
        results.append(row)

        bal_after = _deepseek_balance_usd()
        if bal_after is not None and bal_after <= MIN_BALANCE_USD:
            print(f"STOP after {case['id']}: balance ${bal_after:.2f}", flush=True)
            break

    bal_end = _deepseek_balance_usd()
    payload = {
        "run_at": datetime.now(UTC).isoformat(),
        "provider": "deepseek",
        "llm_base_url": llm.llm_base_url(),
        "client": client,
        "cases_file": str(SUBSET.name),
        "min_balance_usd_floor": MIN_BALANCE_USD,
        "balance_usd": {"start": bal_start, "end": bal_end},
        "totals": {
            "turns_completed": len(results),
            "elapsed_s": round(time.perf_counter() - t0_all, 2),
            "wall_elapsed_s": round(time.perf_counter() - t0_all, 2),
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
            "docs_fts": sum(1 for r in results if r["path_checks"].get("used_docs_fts")),
            "vault_notes": sum(1 for r in results if r["path_checks"].get("used_vault_notes")),
            "plan_cache": sum(1 for r in results if r["path_checks"].get("plan_cache_shortcut")),
            "hot_lookup": sum(1 for r in results if r["path_checks"].get("used_hot_lookup")),
        },
        "note_mcp": (
            "Runtime uses core/vault.py (local Obsidian vault files), not stdio obsidian-mcp-server. "
            "search_docs uses FTS on knowledge corpus; join rules live in prompts/join_playbook.md prefix."
        ),
        "results": results,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--client", default=os.environ.get("CHATBOT_CLIENT", "morec"))
    args = parser.parse_args()
    _assert_deepseek()
    if not llm.llm_api_key():
        raise SystemExit("DEEPSEEK_API_KEY missing from .env")
    payload = run_battery(args.client)
    print(json.dumps(payload["totals"], indent=2))
    print(f"wrote {OUT}", flush=True)


if __name__ == "__main__":
    main()
