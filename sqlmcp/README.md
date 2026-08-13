# sqlmcp — SQL Server MCP + isolated test harness

Thin MCP over `core/sql.py`. Same gate, same `chatbot_ro` read-only login, same
`set_tenant` tenant scoping as the in-process path — it *calls* `core/sql.py`, so the
wall holds identically. **Not** a generic mssql MCP (that would bypass the gate).

Dir is `sqlmcp/`, not `mcp/`, on purpose: a local `mcp/` package would shadow the pip
`mcp` SDK and break `from mcp.server.fastmcp import FastMCP`.

## Transport

**SSE (HTTP)** — `http://<host>:9000/sse`. Chosen because the chatbot may live on a
different host/network than the DB. stdio is a local pipe (same-host only); SSE lets a
remote chatbot reach the MCP over the network. Set `MCP_HOST` / `MCP_PORT` to change
the bind.

## Isolation test — "DB reachable ONLY via the MCP"

```bash
bash sqlmcp/run_isolation_test.sh     # exit 0 = proven
```

What it does (reuses the running `drift-tool-mssql`; host `:14330` + in-process pymssql
stay up as the **fallback**, untouched):

```
olives_dbnet  (internal, no host route):  DB  +  MCP
olives_appnet (internal, no host route):  MCP +  test-client
```

The test-client sits on `appnet` only — it has **no route to the DB**. The MCP is on
both nets and is the only bridge. The proof (`prove_isolation.py`) hard-fails unless:
1. the DB port is **unreachable** directly from the test-client (real isolation), AND
2. a gated `SELECT COUNT(*) FROM t.Customers` **still returns rows** through the MCP.

Verified mechanism (already run): a container on `dbnet` reaches the DB; the same
image on `appnet` cannot. So "only via MCP" is enforced by the network, not by trust.

## Run the MCP for real (behind the API, not raw)

```bash
DB_HOST=127.0.0.1 DB_PORT=14330 MCP_PORT=9000 python3.13 sqlmcp/sql_server.py
```

**SECURITY.** This MCP trusts its caller for `client`/`company_id`. It is a
server-side tool that MUST sit behind the API auth (FIXPLAN M1) — never exposed raw to
an end user or an untrusted network. Even if a caller lies about the tenant, the wall
holds (read-only login + `t.` views + gate): worst case they read only rows for the
`company_id` they pass, only via `t.` views, only SELECT. Do not add auth *inside* this
MCP for the pilot — put it in front (the API layer owns identity→tenant).

## Product path (later)

Runtime `pip install` on each container start is fine for a test, slow for prod. Add a
`Dockerfile` (`FROM python:3.12-slim`, `pip install mcp pymssql sqlglot pyyaml`, copy
`core/`+`sqlmcp/`) and a small compose once this graduates from test to a running
service. For the chatbot's own same-host DB, the in-process `core/sql.py` call is still
simpler and identically safe — build/run this MCP only when an external/remote consumer
needs the gated path.

## Teardown / restore

The test removes the MCP container itself. To fully restore the DB's networking:
```bash
docker network disconnect olives_dbnet drift-tool-mssql
docker network rm olives_dbnet olives_appnet
```
