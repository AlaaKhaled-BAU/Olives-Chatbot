#!/usr/bin/env python3.13
"""TRACK A: snapshot gold rows for execution-accuracy grading.

Reads evals/exec_golden.jsonl cases that have `gold_sql` but no stored
`gold_rows`, executes the gold SQL once through the real gated path
(chatbot_ro + t. views), and writes normalized rows back into the file.

Usage:
  set -a && source .env && set +a
  python3.13 evals/build_golden.py            # fill missing gold_rows
  python3.13 evals/build_golden.py --refresh  # re-snapshot everything
"""
import argparse
import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from core import sql  # noqa: E402
from evals.golden_rows import snapshot_rows  # noqa: E402

GOLDEN_PATH = BASE_DIR / "evals" / "exec_golden.jsonl"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true",
                        help="re-execute gold SQL even when gold_rows already stored")
    args = parser.parse_args()

    cases = [json.loads(l) for l in GOLDEN_PATH.read_text().splitlines() if l.strip()]
    changed = 0
    for case in cases:
        if case.get("gold_rows") and not args.refresh:
            continue
        try:
            rows = sql.run_select(case["gold_sql"], case.get("company_id", 1), case["client"])
        except Exception as exc:  # noqa: BLE001 — report and keep going
            print(f"[SKIP] {case.get('name')}: {type(exc).__name__}: {str(exc)[:100]}")
            continue
        case["gold_rows"] = snapshot_rows(rows)
        changed += 1
        print(f"[OK] {case['name']}: {len(rows)} rows snapshotted")
    GOLDEN_PATH.write_text(
        "\n".join(json.dumps(c, ensure_ascii=False) for c in cases) + "\n")
    print(f"{changed}/{len(cases)} cases (re)snapshotted -> {GOLDEN_PATH}")


if __name__ == "__main__":
    main()
