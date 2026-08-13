"""The one shared SQL implementation (PLAN.md golden rule 9), used by both
the agent and (later) the MCP. chatbot_ro has no base-table grants -- only
the `t.` schema (db/02_tenant_views.sql). Every connection must call
set_tenant() before querying; SESSION_CONTEXT is NULL on a fresh connection,
which the tenant views treat as zero rows (fail closed).

Every function takes an explicit `client` -- there is no default, so a
caller can't accidentally hit the wrong client's database by omission
(PLAN.md Phase 9)."""
import os
from pathlib import Path

import pymssql

from . import config, gate

_SHARED_WORK_DIR = Path(__file__).resolve().parent.parent / "work"


def _ro_password() -> str:
    # chatbot_ro is a SERVER-level login (one per SQL Server instance, not
    # per client database) -- its password is shared, not per-client.
    return (_SHARED_WORK_DIR / "ro_password.txt").read_text().strip()


def get_conn(client: str):
    db_name = config.load_client(client)["db_name"]
    return pymssql.connect(
        server=os.environ.get("DB_HOST", "127.0.0.1"),
        port=int(os.environ.get("DB_PORT", 14330)),
        user="chatbot_ro",
        password=_ro_password(),
        database=db_name,
        timeout=30, login_timeout=10,
    )


def set_tenant(conn, company_id: int):
    """Scope every subsequent query on this connection to one CompanyID.
    Connections are not pooled across tenants -- always a fresh connection
    per request, never reused across a different CompanyID."""
    cur = conn.cursor()
    cur.execute("EXEC sp_set_session_context %s, %s", ("CompanyID", company_id))


def run_select(raw_sql: str, company_id: int, client: str, allowed_procs=None, row_cap: int = gate.DEFAULT_ROW_CAP):
    """gate -> set tenant -> execute via the t. views. raw_sql is untrusted
    (model-generated); the gate is the only thing standing between it and
    the database, on top of the server-side wall."""
    safe_sql = gate.validate(raw_sql, allowed_procs=allowed_procs, row_cap=row_cap)
    conn = get_conn(client)
    try:
        set_tenant(conn, company_id)
        cur = conn.cursor(as_dict=True)
        cur.execute(safe_sql)
        return cur.fetchall()
    finally:
        conn.close()


def run_proc(proc_name: str, args: dict, company_id: int, client: str, allowed_procs):
    """Allow-list only -- proc_name must be a key in the caller's
    catalog.for_client() result. NOTE: granting chatbot_ro EXECUTE on any
    real proc still needs the sys.sql_expression_dependencies write-free
    audit (ownership chaining means EXEC isn't automatically read-only,
    per PLAN.md/memory) -- that grant doesn't exist yet, so this is
    mechanically complete but not yet wired to a live permission."""
    allowed = {p.lower() for p in allowed_procs}
    if proc_name.lower() not in allowed:
        raise gate.GateError(f"{proc_name} is not an allow-listed procedure")
    args = args or {}
    for key in args:
        gate.safe_identifier(key)

    placeholders = ", ".join(f"@{k}=%s" for k in args)
    exec_sql = f"EXEC {proc_name} {placeholders}" if args else f"EXEC {proc_name}"
    conn = get_conn(client)
    try:
        set_tenant(conn, company_id)
        cur = conn.cursor(as_dict=True)
        cur.execute(exec_sql, tuple(args.values()))
        try:
            return cur.fetchall()
        except pymssql.OperationalError:
            return []  # the proc had no result set
    finally:
        conn.close()
