#!/usr/bin/env python3.13
"""Patch obsidian/olives table notes from work/<client>/schema_cache.json.

Setup / maintenance only — NOT called at runtime. The FastAPI /ask path and
core/agent.py must never write vault files; live schema wins at query time via
get_joins (read-only). Run this script after introspect or refresh when vault
column lists drift from live INFORMATION_SCHEMA.

Usage:
  python3.13 setup/sync_vault_from_cache.py --client morec
  python3.13 setup/sync_vault_from_cache.py --client morec --table Customers
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from core import config, vault  # noqa: E402


def _tables_with_drift(client: str, database: str = "Olives_BO") -> list[str]:
    cache_path = config.work_dir(client) / "schema_cache.json"
    if not cache_path.exists():
        return []
    cache = json.loads(cache_path.read_text(encoding="utf-8"))
    drifted: list[str] = []
    for key in cache.get("tables", {}):
        bare = key.split(".")[-1]
        note_path = vault.VAULT / database / "Tables" / f"{bare}.md"
        if not note_path.exists():
            continue
        live_names = [c.get("column") for c in cache["tables"][key]]
        vault_cols = vault._parse_vault_column_names(note_path.read_text(encoding="utf-8"))
        if vault_cols != live_names:
            drifted.append(bare)
    return sorted(drifted)


def sync_client(client: str, table: str | None = None, database: str = "Olives_BO") -> list[dict]:
    targets = [table] if table else _tables_with_drift(client, database)
    results: list[dict] = []
    for name in targets:
        results.append(vault.sync_vault_table_from_cache(name, client, database=database))
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Patch vault table notes from schema_cache (setup only, not runtime)",
    )
    parser.add_argument("--client", required=True)
    parser.add_argument("--table", help="Single table name; default = all drifted tables")
    parser.add_argument("--database", default="Olives_BO")
    args = parser.parse_args()

    results = sync_client(args.client, table=args.table, database=args.database)
    patched = [r for r in results if r.get("status") == "patched"]
    skipped = [r for r in results if r.get("status") == "skipped"]
    ok = [r for r in results if r.get("status") == "ok" and not r.get("patched")]

    print(f"Checked {len(results)} table(s): {len(patched)} patched, {len(ok)} already in sync, {len(skipped)} skipped")
    for r in patched:
        print(f"  patched {r['table']}: {r['vault_cols']} -> {r['live_cols']} cols ({r['path']})")
    for r in skipped:
        print(f"  skipped {r.get('table') or args.table}: {r.get('reason')}")


if __name__ == "__main__":
    main()
