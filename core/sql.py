"""The one shared SQL implementation (PLAN.md golden rule 9), used by both
the agent and (later) the MCP. chatbot_ro has no base-table grants -- only
the `t.` schema (db/02_tenant_views.sql). Every connection must call
set_tenant() before querying; SESSION_CONTEXT is NULL on a fresh connection,
which the tenant views treat as zero rows (fail closed).

Every function takes an explicit `client` -- there is no default, so a
caller can't accidentally hit the wrong client's database by omission
(PLAN.md Phase 9)."""
import json
import os
from pathlib import Path

import pymssql

from . import config, gate, memory

def _shared_work_dir() -> Path:
    env_work = os.environ.get("CHATBOT_WORK_DIR")
    if env_work:
        return Path(env_work)
    return Path(__file__).resolve().parent.parent / "work"


def _ro_password() -> str:
    # chatbot_ro is a SERVER-level login (one per SQL Server instance, not
    # per client database) -- its password is shared, not per-client.
    return (_shared_work_dir() / "ro_password.txt").read_text().strip()


def get_conn(client: str):
    """Connection target precedence (operator console, core/dblink.py):
    runtime override (UI-entered server) > .env snapshot. The tenant wall
    is NOT bypassable from this console — chatbot_ro/t.* views still apply
    unless the operator deliberately connects with a different login."""
    db_name = config.load_client(client)["db_name"]
    override = None
    try:
        from . import dblink  # local import: optional module, never a hard dep
        override = dblink.raw_override()
    except Exception:  # noqa: BLE001
        override = None
    if override:
        conn_kwargs = dict(
            server=override["host"],
            port=int(override.get("port") or 1433),
            database=override.get("database") or db_name,
            timeout=30, login_timeout=10,
        )
        if override.get("trusted"):
            conn_kwargs["trusted"] = {"yes"}  # Windows auth, best-effort on Linux
        else:
            conn_kwargs["user"] = override.get("user", "")
            conn_kwargs["password"] = override.get("password", "")
        return pymssql.connect(**conn_kwargs)
    user = os.environ.get("DB_USER") or "chatbot_ro"
    password = os.environ.get("DB_PASSWORD")
    if not password:
        try:
            password = _ro_password()
        except Exception:
            password = ""
    return pymssql.connect(
        server=os.environ.get("DB_HOST", "127.0.0.1"),
        port=int(os.environ.get("DB_PORT", "1433")),
        user=user,
        password=password,
        database=db_name,
        timeout=30, login_timeout=10,
    )


_TENANT_VIEW_SUPPORT: dict[str, bool] = {}


def has_tenant_views(conn) -> bool:
    """Check if the connected database has the t schema created."""
    server_key = getattr(conn, "_server_key", None)
    if server_key and server_key in _TENANT_VIEW_SUPPORT:
        return _TENANT_VIEW_SUPPORT[server_key]
    try:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM sys.schemas WHERE name = 't'")
        res = cur.fetchone()
        has_t = bool(res and res[0] > 0)
    except Exception:
        has_t = True
    if server_key:
        _TENANT_VIEW_SUPPORT[server_key] = has_t
    return has_t


def set_tenant(conn, company_id: int):
    """Scope every subsequent query on this connection to one CompanyID.
    Connections are not pooled across tenants -- always a fresh connection
    per request, never reused across a different CompanyID."""
    cur = conn.cursor()
    cur.execute("EXEC sp_set_session_context %s, %s", ("CompanyID", company_id))


RESULT_CACHE_TTL = 45


def _schema_cache(client: str) -> dict:
    return json.loads((config.work_dir(client) / "schema_cache.json").read_text())


def run_select(
    raw_sql: str,
    company_id: int,
    client: str,
    allowed_procs=gate.DEFAULT_ALLOWED_PROCS,
    row_cap: int = gate.DEFAULT_ROW_CAP,
):
    """gate -> set tenant -> execute via the t. views. raw_sql is untrusted
    (model-generated); the gate is the only thing standing between it and
    the database, on top of the server-side wall."""
    safe_sql = gate.validate(
        raw_sql,
        allowed_procs=allowed_procs,
        row_cap=row_cap,
        company_id=company_id,
        schema_cache=_schema_cache(client),
    )
    rc_key = memory.result_cache_key(client, company_id, safe_sql)
    cached = memory.get_result(rc_key, ttl_seconds=RESULT_CACHE_TTL)
    if cached is not None:
        return cached
    conn = get_conn(client)
    try:
        set_tenant(conn, company_id)
        exec_sql = safe_sql
        if not has_tenant_views(conn):
            # Remote server connected with base tables (e.g. direct cds login)
            import re
            exec_sql = re.sub(r"(?i)\bfrom\s+t\.", "FROM dbo.", exec_sql)
            exec_sql = re.sub(r"(?i)\bjoin\s+t\.", "JOIN dbo.", exec_sql)
        cur = conn.cursor(as_dict=True)
        cur.execute(exec_sql)
        rows = cur.fetchall()
    finally:
        conn.close()
    memory.set_result(rc_key, rows)
    return rows


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

    gate.safe_identifier(proc_name.split(".")[-1])
    placeholders = ", ".join(f"@{k}=%s" for k in args)
    exec_sql = f"EXEC {proc_name} {placeholders}" if args else f"EXEC {proc_name}"
    try:
        schema_cache = _schema_cache(client)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        schema_cache = {}
    gate.validate(
        f"EXEC {proc_name}",
        allowed_procs=allowed_procs,
        company_id=company_id,
        schema_cache=schema_cache or None,
    )
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
