#!/usr/bin/env python3.13
"""FIXPLAN M7: one command to recover from a client's schema drift (renamed
column, new CompanyID table, new/changed procedure) -- chains the two
existing setup scripts for one client, as SA:
  1. 02_introspect.py --client X --db-name Y  (rebuilds work/X/schema_cache.json)
  2. 03_apply_db_sql.py --db-name Y           (rebuilds the t. views, idempotent --
     db/02_tenant_views.sql already DROPs+recreates each view by name)
No new logic beyond that -- just sequences scripts that already exist. Not
auto-triggered (no drift detection here); run it by hand once you know the
client's schema changed.

Stress-tested live (simulated drift: added a real CompanyID-bearing table,
confirmed introspect+views pick it up AND the new view is correctly
tenant-scoped, confirmed idempotent on a second run) -- that surfaced one
real gap: db/02_tenant_views.sql only CREATEs/updates views for tables
that CURRENTLY qualify; it never drops a view whose backing table was
later removed (confirmed: dropping the test table left an orphaned
t.<name> view behind after a refresh). Not a security issue -- the orphan
just errors if ever queried, and schema_cache.json (the model's only
source of table knowledge) already stops listing the dropped table, so
nothing can reach it -- but it's real drift-recovery debt, so this script
cleans it up. db/02_tenant_views.sql itself is intentionally left
untouched (FIXPLAN.md's own rule: don't edit the wall file except where a
phase explicitly calls for it) -- the cleanup lives here instead."""
import argparse
import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "setup"))
import db_connect  # noqa: E402
import pymssql  # noqa: E402
from core import config as client_config  # noqa: E402
from core import memory  # noqa: E402


def _drop_orphaned_tenant_views(db_name: str):
    """A t.<name> view whose backing dbo.<name> table no longer exists is
    dead weight left by a table rename/removal -- 02_tenant_views.sql never
    cleans these up on its own (see module docstring)."""
    conn = db_connect.sa_connect(database=db_name, autocommit=True)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sys.views WHERE schema_id = SCHEMA_ID('t')")
    view_names = [row[0] for row in cur.fetchall()]
    dropped = []
    for name in view_names:
        cur.execute("SELECT OBJECT_ID(%s)", (f"dbo.{name}",))
        if cur.fetchone()[0] is None:
            cur.execute(f"DROP VIEW t.[{name}]")
            dropped.append(name)
    conn.close()
    return dropped


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--client", required=True)
    args = parser.parse_args()

    db_name = client_config.load_client(args.client)["db_name"]
    setup_dir = REPO_ROOT / "setup"

    print(f"[refresh] {args.client} -> {db_name}: re-introspecting schema...")
    subprocess.run(
        ["python3.13", str(setup_dir / "02_introspect.py"), "--client", args.client, "--db-name", db_name],
        check=True,
    )

    print(f"[refresh] {args.client} -> {db_name}: rebuilding tenant wall (t. views)...")
    subprocess.run(
        ["python3.13", str(setup_dir / "03_apply_db_sql.py"), "--db-name", db_name],
        check=True,
    )

    print(f"[refresh] {args.client} -> {db_name}: dropping orphaned t. views (removed tables)...")
    dropped = _drop_orphaned_tenant_views(db_name)
    print(f"[refresh] dropped {len(dropped)} orphaned view(s): {dropped}" if dropped else "[refresh] none orphaned")

    # C3: schema_version is already baked into the plan_cache key, so a
    # stale-shape entry can never be matched by a new query -- but it would
    # otherwise sit in the table forever with nothing to clean it up. This
    # is the "invalidated by setup/refresh.py" half of that fix.
    removed = memory.clear_plan_cache(args.client)
    print(f"[refresh] cleared {removed} stale plan_cache entr{'y' if removed == 1 else 'ies'} for {args.client}")

    print(f"[refresh] {args.client}: compiling vault schema cards...")
    subprocess.run(
        ["python3.13", str(setup_dir / "compile_vault_cards.py"), "--client", args.client],
        check=True,
    )

    print(f"[refresh] {args.client} done.")


if __name__ == "__main__":
    main()
