#!/usr/bin/env python3.13
"""Phase 1/9: live schema introspection (as SA) -> work/<client>/schema_cache.json.
Structure only -- never fetches proc bodies (PLAN.md golden rule 5).
Also runs the two Phase-1 acceptance probes (Companies scope, ClientsActive)."""
import argparse
import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DRIFT_TOOL_ROOT = Path(
    os.environ.get("DRIFT_TOOL_ROOT", "/media/alaa/data/olives/apps/drift-tool")
)
sys.path.insert(0, str(DRIFT_TOOL_ROOT))
sys.path.insert(0, str(REPO_ROOT))

import pymssql  # noqa: E402
from drift import config  # noqa: E402
from core import config as client_config  # noqa: E402


def log(msg):
    print(msg, flush=True)


def connect(db_name):
    return pymssql.connect(
        server="127.0.0.1", port=config.HOST_PORT,
        user=config.SA_USER, password=config.SA_PASSWORD,
        database=db_name, autocommit=True, timeout=60, login_timeout=10,
        as_dict=True,
    )


# C0 (2026-07-26, see db/table_classification.md for the full per-table reasoning
# behind each name here -- keep both files in sync if this list ever changes).
# has_tenant_view is derived from this POLICY, not a live `sys.views` query --
# refresh.py always runs this script BEFORE 03_apply_db_sql.py (confirmed
# consistent everywhere this pair is sequenced), so the `t.` schema may not
# exist yet at introspection time; deriving from the same classification
# db/02_tenant_views.sql itself encodes is correct regardless of run order.
_COMPANY_COL_TABLES = {
    "CustomerChqList", "CustomerReceivablesInfo", "CustomerSalesByCategory",
    "DebitCreditNoteTrans", "DeliveryRoute", "InvoiceDeliveryDF", "InvoiceDeliveryHF",
    "InvoiceHistoryDF", "InvoiceHistoryHF", "LogActionTransaction", "LogActionTransaction_",
    "Pos_InvoiceOrderHF", "SalesOrderDeliveryDF", "SalesOrderDeliveryHF",
    "SalesOrderHistoryDF", "SalesOrderHistoryHF", "Themar", "TransactionsSuggestedItems",
}
_REFERENCE_TABLES = {
    "ActivityList", "CustomerLoginActions", "Currencies", "DeviceReportsList",
    "ExcelReports", "Language", "LanguageDictionary", "LogActions", "Menu",
    "MIMETypes", "MMS_MaintenanceTechnicianPermissions_Def", "MMS_OrderStatus",
    "OlivesMenu", "OlivesPages", "PromotionTypes", "SystemCodes",
    "TargetsTypes", "TransactionsTypes", "WF_Functions",
}


def _has_tenant_view(table_name: str, columns: list) -> bool:
    if table_name == "Companies":
        return True  # special-cased view on its own PK, see db/02_tenant_views.sql
    if any(c["column"].lower() == "companyid" for c in columns):
        return True
    if table_name in _COMPANY_COL_TABLES and any(c["column"].lower() == "compno" for c in columns):
        return True
    return table_name in _REFERENCE_TABLES


def fetch_tables(cur):
    cur.execute("""
        SELECT t.TABLE_SCHEMA, t.TABLE_NAME, c.COLUMN_NAME, c.DATA_TYPE,
               c.IS_NULLABLE, c.ORDINAL_POSITION
        FROM INFORMATION_SCHEMA.TABLES t
        JOIN INFORMATION_SCHEMA.COLUMNS c
          ON c.TABLE_SCHEMA = t.TABLE_SCHEMA AND c.TABLE_NAME = t.TABLE_NAME
        WHERE t.TABLE_TYPE = 'BASE TABLE'
        ORDER BY t.TABLE_SCHEMA, t.TABLE_NAME, c.ORDINAL_POSITION
    """)
    tables = {}
    for row in cur.fetchall():
        key = f"{row['TABLE_SCHEMA']}.{row['TABLE_NAME']}"
        tables.setdefault(key, []).append({
            "column": row["COLUMN_NAME"],
            "type": row["DATA_TYPE"],
            "nullable": row["IS_NULLABLE"] == "YES",
        })
    return tables


def fetch_primary_keys(cur):
    cur.execute("""
        SELECT tc.TABLE_SCHEMA, tc.TABLE_NAME, kcu.COLUMN_NAME
        FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc
        JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu
          ON tc.CONSTRAINT_NAME = kcu.CONSTRAINT_NAME AND tc.TABLE_SCHEMA = kcu.TABLE_SCHEMA
        WHERE tc.CONSTRAINT_TYPE = 'PRIMARY KEY'
    """)
    pks = {}
    for row in cur.fetchall():
        key = f"{row['TABLE_SCHEMA']}.{row['TABLE_NAME']}"
        pks.setdefault(key, []).append(row["COLUMN_NAME"])
    return pks


def fetch_foreign_keys(cur):
    cur.execute("""
        SELECT fk.name AS fk_name,
               SCHEMA_NAME(po.schema_id) + '.' + po.name AS table_name,
               COL_NAME(fkc.parent_object_id, fkc.parent_column_id) AS column_name,
               SCHEMA_NAME(ro.schema_id) + '.' + ro.name AS ref_table,
               COL_NAME(fkc.referenced_object_id, fkc.referenced_column_id) AS ref_column
        FROM sys.foreign_keys fk
        JOIN sys.foreign_key_columns fkc ON fk.object_id = fkc.constraint_object_id
        JOIN sys.objects po ON po.object_id = fk.parent_object_id
        JOIN sys.objects ro ON ro.object_id = fk.referenced_object_id
    """)
    return cur.fetchall()


def fetch_procs(cur):
    cur.execute("""
        SELECT SCHEMA_NAME(p.schema_id) AS proc_schema, p.name AS proc_name,
               par.name AS param_name, TYPE_NAME(par.user_type_id) AS data_type,
               par.is_output
        FROM sys.procedures p
        LEFT JOIN sys.parameters par ON par.object_id = p.object_id
        ORDER BY proc_schema, proc_name, par.parameter_id
    """)
    procs = {}
    for row in cur.fetchall():
        key = f"{row['proc_schema']}.{row['proc_name']}"
        params = procs.setdefault(key, [])
        if row["param_name"]:
            params.append({
                "param": row["param_name"],
                "type": row["data_type"],
                "output": bool(row["is_output"]),
            })
    return procs


def find_nullable_companyid_rows(cur, tables: dict) -> dict:
    """C0: a CompanyID column being NULLABLE (schema metadata, already known)
    doesn't mean any row actually HAS a NULL there -- that needs a real
    COUNT. Run once here (SA, introspection-time) rather than on every
    /health hit: SESSION_CONTEXT(NULL) semantics already make a NULL-
    CompanyID row correctly invisible through every t. view (fail-closed,
    no leak) -- but invisible also means the row's data silently never
    shows up in an answer, which is safe but not trustworthy if the count
    is non-zero. Only checks tables that are BOTH already tenant-scoped
    (has a CompanyID column at all) AND that column is nullable -- a table
    with NOT NULL CompanyID can never have this problem, skip the query."""
    out = {}
    for key, columns in tables.items():
        col = next((c for c in columns if c["column"].lower() == "companyid" and c["nullable"]), None)
        if not col:
            continue
        schema, bare = key.split(".", 1)
        try:
            cur.execute(f"SELECT COUNT(*) AS cnt FROM [{schema}].[{bare}] WHERE CompanyID IS NULL")
            n = cur.fetchone()["cnt"]
            if n:
                out[key] = n
        except Exception:  # noqa: BLE001 - diagnostic only, one bad table must not abort introspection
            continue
    return out


def probe_profile(cur):
    probe = {}
    try:
        # Companies' own PK is `ID`, not `CompanyID` -- verified via live introspection
        # (PLAN.md's literal "SELECT DISTINCT CompanyID FROM Companies" doesn't match
        # this schema). `CompanyID` is the FK column name on the 344 business tables
        # that reference Companies.ID -- that's what Phase 2's SESSION_CONTEXT scoping
        # targets, unaffected by this correction.
        cur.execute("SELECT COUNT(*) AS cnt FROM Companies")
        probe["companies_count"] = cur.fetchone()["cnt"]
        cur.execute("SELECT COUNT(DISTINCT ID) AS cnt FROM Companies")
        probe["companies_distinct_count"] = cur.fetchone()["cnt"]
        if probe["companies_distinct_count"] == 1:
            # Single-company client: params.py's discover_profile() (Phase 5)
            # needs the actual value, not just the count, to store CompanyID
            # as a static profile param -- chatbot_ro can't read this itself
            # (Companies has no t. view, see core/catalog.py note), so it has
            # to come from this SA-run probe.
            cur.execute("SELECT ID FROM Companies")
            probe["company_id"] = cur.fetchone()["ID"]
        # C6c: captured unconditionally (not just the single-valued case) --
        # a multi-company client's CompanyID-resolution reply ("company 7",
        # or the company's name) can only be matched against a REAL set of
        # (id, name) pairs, never a bare regex over the message text (that
        # bug once let "how many invoices in 2024" silently resolve
        # CompanyID=2024). No real multi-company client exists yet to
        # validate this against live -- morec and rukn are both
        # company_scope: single -- so this is honestly untested against
        # real multi-company data, only against the mechanism itself.
        cur.execute("SELECT ID, Name FROM Companies")
        probe["companies"] = [{"id": r["ID"], "name": r["Name"]} for r in cur.fetchall()]
    except Exception as e:  # noqa: BLE001 - acceptance probe, must not crash the run
        probe["companies_count"] = None
        probe["companies_error"] = str(e)

    try:
        cur.execute("SELECT ClientID FROM ClientsActive")
        rows = cur.fetchall()
        if len(rows) == 1:
            probe["client_active"] = rows[0]["ClientID"]
        else:
            probe["client_active"] = "ASK"
            probe["client_active_note"] = f"expected exactly 1 row, got {len(rows)}"
    except Exception as e:  # noqa: BLE001 - missing table is a valid outcome, not a crash
        probe["client_active"] = "ASK"
        probe["client_active_note"] = str(e)
    return probe


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--client", default="morec")
    parser.add_argument("--db-name", default="chatbot_db")
    args = parser.parse_args()

    work_dir = client_config.work_dir(args.client)
    conn = connect(args.db_name)
    cur = conn.cursor()

    cur.execute("SELECT @@VERSION AS v")
    version = cur.fetchone()["v"]
    log(f"engine: {version.splitlines()[0]}")

    tables = fetch_tables(cur)
    pks = fetch_primary_keys(cur)
    for key, cols in pks.items():
        for col in cols:
            for c in tables.get(key, []):
                if c["column"] == col:
                    c["is_pk"] = True
    fks = fetch_foreign_keys(cur)
    procs = fetch_procs(cur)
    profile = probe_profile(cur)
    nullable_companyid_rows = find_nullable_companyid_rows(cur, tables)
    conn.close()

    # C0: keyed the same schema-qualified way as `tables` itself, so
    # agent._introspect can check it inline with the loop it already runs
    # rather than re-deriving the bare name a second time.
    has_tenant_view = {key: _has_tenant_view(key.split(".", 1)[-1], cols) for key, cols in tables.items()}
    no_view_count = sum(1 for v in has_tenant_view.values() if not v)

    cache = {
        "engine_version": version,
        "db_name": args.db_name,
        "table_count": len(tables),
        "proc_count": len(procs),
        "tables": tables,
        "has_tenant_view": has_tenant_view,
        "foreign_keys": fks,
        "procs": procs,
        "profile_probe": profile,
        "nullable_companyid_rows": nullable_companyid_rows,
    }
    out_path = work_dir / "schema_cache.json"
    out_path.write_text(json.dumps(cache, indent=2, default=str))

    log(f"tables: {len(tables)}, procs: {len(procs)}, foreign keys: {len(fks)}")
    log(f"  {no_view_count}/{len(tables)} table(s) have no t. view (see db/table_classification.md) "
        f"-- introspect_schema refuses these before the agent wastes a turn on a doomed query")
    if nullable_companyid_rows:
        log(f"  WARNING: {sum(nullable_companyid_rows.values())} row(s) across "
            f"{len(nullable_companyid_rows)} table(s) have CompanyID IS NULL -- invisible through "
            f"every t. view (fail-closed, not a leak) but silently missing from any answer that "
            f"touches them: {nullable_companyid_rows}")
    log(f"profile probe: {profile}")
    log(f"wrote {out_path}")


if __name__ == "__main__":
    main()
