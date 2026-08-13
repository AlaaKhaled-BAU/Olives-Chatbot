"""Thin SQL Server MCP over core/sql.py.

SAME gate, SAME chatbot_ro read-only login, SAME set_tenant tenant scoping as the
in-process path -- it literally calls core/sql.py, so the wall (db/02_tenant_views.sql
+ gate.py) holds identically. This is NOT a generic mssql MCP; a stock one connects
with its own creds and runs arbitrary SQL, bypassing the gate and the tenant views.

Transport = SSE (HTTP). Reason: the chatbot may run on a different host/network than
the DB. stdio is a local pipe only; SSE lets a remote chatbot reach this over the
network. Endpoint: http://<host>:<MCP_PORT>/sse

SECURITY: this MCP trusts its caller for `client`/`company_id`. It is a SERVER-SIDE
tool that must sit behind the API's auth (FIXPLAN M1) -- never exposed raw to an end
user or an untrusted network. Even if a caller lies about the tenant, the wall still
holds: read-only login + t. views + gate = worst case they read only rows for the
company_id they pass, only through t. views, only SELECT.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # repo root

from mcp.server.fastmcp import FastMCP  # noqa: E402
from mcp.server.transport_security import TransportSecuritySettings  # noqa: E402

from core import catalog, config, sql  # noqa: E402

# The SDK's own DNS-rebinding guard checks the Host: header against an allowlist
# (default = localhost only) and 421s anything else. Real deployments reach this
# over a Docker service name / real hostname, never localhost, so that name MUST
# be added here -- MCP_ALLOWED_HOSTS is comma-separated, e.g. "olives-sql-mcp:*"
# or the real host:port the chatbot will dial. Widen it per-deployment, not by
# disabling the check.
_allowed_hosts = ["127.0.0.1:*", "localhost:*", "[::1]:*"] + [
    h for h in os.environ.get("MCP_ALLOWED_HOSTS", "").split(",") if h
]

mcp = FastMCP(
    "olives-sql",
    transport_security=TransportSecuritySettings(
        allowed_hosts=_allowed_hosts,
        allowed_origins=_allowed_hosts,
    ),
)
mcp.settings.host = os.environ.get("MCP_HOST", "0.0.0.0")
mcp.settings.port = int(os.environ.get("MCP_PORT", "9000"))


def _allowed(client: str):
    cfg = config.load_client(client)
    return list(catalog.for_client(client, cfg.get("name_aliases", [client])))


@mcp.tool()
def run_select(sql_text: str, company_id: int, client: str) -> str:
    """One gated, tenant-scoped read-only SELECT via the t. views. Returns JSON rows."""
    rows = sql.run_select(sql_text, company_id, client, allowed_procs=_allowed(client))
    return json.dumps(rows, default=str)


@mcp.tool()
def introspect(name: str, client: str) -> str:
    """Columns for a table (case-insensitive), from this client's schema cache."""
    cache = json.loads((config.work_dir(client) / "schema_cache.json").read_text())
    low = name.strip().lower()
    # C0: same has_tenant_view gate as core/agent.py's _introspect -- None on
    # a pre-C0 cache never refuses (the t. wall is the real boundary either
    # way); present-but-False means genuinely no client-facing view.
    has_view = cache.get("has_tenant_view")
    for table_name, cols in cache["tables"].items():
        if table_name.split(".")[-1].lower() == low:
            if has_view is not None and not has_view.get(table_name, False):
                return json.dumps({"error": f"{name!r} exists in the schema but has no "
                                             f"client-facing t. view -- not queryable"})
            return json.dumps({"kind": "table", "name": table_name, "columns": cols}, default=str)
    return json.dumps({"error": f"{name!r} not found or not entitled to this client"})


if __name__ == "__main__":
    mcp.run(transport="sse")
