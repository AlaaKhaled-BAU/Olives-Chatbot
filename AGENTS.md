# AGENTS.md — Olives Client Chatbot

Standalone repo at `/media/alaa/data/client-chatbot/`.  
**Goal:** embeddable IIS chatbot (circle widget) that answers docs questions and runs read-only SQL against the customer's **`Olives_BO`** database.  
**Today:** FastAPI full-page pilot (`api/server.py` + `static/`) — widget not built yet.

---

## Golden rules (read first)

1. **Python 3.13 only** — never `python3`.
2. **Never use SA or IIS `cds` from the running app** — only `chatbot_ro` + `t.` views + `SESSION_CONTEXT`.
3. **LLM keys never in `core/` or `api/`** — OmniRoute holds provider keys; app sends `GATEWAY_API_KEY` from `.env`.
4. **Tenant pinned in env** — `CHATBOT_CLIENT` selects `clients/*.yaml`; browser cannot switch yaml client.
5. **One SQL path:** `core/sql.py` + `core/gate.py` (shared by agent and `sqlmcp/`).
6. **Never return procedure bodies** to the model or user.
7. **Cache keys include client + CompanyID** — exact match only (`core/memory.py`).
8. **After query results enter model context, no more tool calls** (`core/agent.py` golden rule 6).
9. **Do not bypass the gate** or grant base-table access to `chatbot_ro`.
10. **Vault is load-bearing** — do not delete or gitignore `obsidian/olives/` (2659 files including `.obsidian/`).

---

## Architecture

```
Browser → static/ + api/server.py (POST /ask, SSE)
              → core/agent.py
                    ├─ search_docs → core/docs.py (FTS5 over work/<client>/docs.sqlite)
                    ├─ introspect_schema / run_select → core/sql.py + core/gate.py
                    └─ core/llm.py → OmniRoute (GATEWAY_URL) → provider models

Setup (SA, not runtime):
  native_bootstrap.py → 03_apply_db_sql → 02_introspect → 04_assemble → 05_index_docs

Future (not wired yet):
  obsidian-mcp-server.py → vault notes + vault_graph.json for join/schema reasoning
  Circle widget embed on customer IIS wwwroot
```

| Path | Role |
|------|------|
| `api/server.py` | FastAPI, env-pinned client, SSE `/ask`, `GET /context`, `/health`, `/metrics` |
| `core/agent.py` | Agent loop, tools, tenant scoping |
| `core/sql.py` | `chatbot_ro` connections, `SESSION_CONTEXT`, `run_select` |
| `core/gate.py` | `sqlglot` safety gate (defense-in-depth) |
| `core/docs.py` | FTS5 doc search (not vault MCP at runtime today) |
| `core/catalog.py` | Per-client proc allow-list metadata |
| `core/memory.py` | SQLite plan/result cache |
| `core/llm.py` | Thin OpenAI client → `GATEWAY_URL`, model from `CHATBOT_MODEL` |
| `db/01_readonly_login.sql` | Creates `chatbot_ro` (no base-table grants) |
| `db/02_tenant_views.sql` | Schema `t.` views scoped by `SESSION_CONTEXT('CompanyID')` |
| `obsidian/olives/` | Live Obsidian vault (tables, procs, relations, runbooks) |
| `obsidian-mcp-server.py` | 12-tool stdio MCP over vault + graph |
| `db/vault_graph.json` | Precomputed graph for `get_impact` / `get_proc_deps` |
| `knowledge/` | User-guide markdown sources for FTS corpus |
| `setup/` | Bootstrap scripts (see below) |
| `work/` | **Gitignored** — `ro_password.txt`, `schema_cache.json`, `docs.sqlite`, traces |

---

## Environment (`.env`, gitignored)

Copy from `.env.example`. Required for local dev:

| Variable | Purpose |
|----------|---------|
| `GATEWAY_URL` | OmniRoute OpenAI-compatible base (default `http://localhost:20128/v1`) |
| `GATEWAY_API_KEY` | Client key OmniRoute accepts (`Authorization: Bearer …`) |
| `CHATBOT_MODEL` | Model alias routed by OmniRoute (e.g. `auto/best-coding`) |
| `DB_HOST` | SQL Server host (default `127.0.0.1`) |
| `DB_PORT` | **1433** native / production-like; **14330** legacy drift-tool Docker only |
| `DB_SA_USER` | SA login for setup scripts only (default `sa`) |
| `DB_SA_PASSWORD` | SA password for setup scripts only |
| `SQL_SNAPSHOT_MOUNT` | Path SQL Server sees for `.bak` files (default `/snapshots`) |
| `CHATBOT_CLIENT` | Pinned tenant name matching `clients/<name>.yaml` (required at startup) |

Provider keys (Gemini, OpenRouter, etc.) live in **OmniRoute** (`omniroute keys list`), not in this repo.

---

## SQL Server

### Production (customer IIS)

- Same SQL Server instance as the Olives website (`Web.config` → `CNNStr` → **`Olives_BO`**).
- IIS app uses SQL login **`cds`** + session/cookie `CompanyID` — **do not reuse `cds` in this app**.
- Chatbot uses **`chatbot_ro`** + schema **`t.`** views; tenant isolation is server-side via `SESSION_CONTEXT`.

### Local dev (default)

Native instance on **port 1433** (local `mssql` Docker container or Azure Data Studio target).  
Typical databases on this machine: `Olives_BO`, `OSFA_DB`, `olives_PEEK`.

`.bak` restore path: host folder mounted into SQL Server as `/snapshots`  
(e.g. `/media/alaa/data/olives/data/db-snapshots` → `/snapshots`).

### Setup scripts

| Script | Purpose |
|--------|---------|
| `setup/native_bootstrap.py` | **Primary.** Wall + introspect + docs index on existing DB |
| `setup/03_apply_db_sql.py` | SA: `chatbot_ro` login + `t.` views |
| `setup/02_introspect.py` | SA: live schema → `work/<client>/schema_cache.json` |
| `setup/04_assemble_docs_corpus.py` | Symlink `knowledge/` → `docs_corpus/` |
| `setup/05_index_docs.py` | FTS index → `work/<client>/docs.sqlite` |
| `setup/refresh.py` | Re-run 02+03 after client schema drift |
| `setup/01_db_up.py --mode native` | RESTORE `.bak` into native instance |
| `setup/01_db_up.py --mode docker` | Legacy: drift-tool container on port 14330 |
| `setup/db_connect.py` | Shared SA connection helpers (env-based) |
| `setup/restore_native.py` | Native RESTORE implementation |

**One-shot bootstrap** (when `Olives_BO` already exists):

```bash
set -a && source .env && set +a
python3.13 setup/native_bootstrap.py --client morec
```

**Restore then bootstrap:**

```bash
python3.13 setup/01_db_up.py --mode native --db-name Olives_BO \
  --bak "data/db-snapshots/backup test/morec/Olives_BO.bak"
python3.13 setup/native_bootstrap.py --client morec --db-name Olives_BO
```

**Schema changed on client:**

```bash
python3.13 setup/refresh.py --client morec
```

`work/ro_password.txt` holds the shared `chatbot_ro` password (one per SQL Server instance).

---

## Clients (`clients/*.yaml`)

Template: `clients/_example.yaml`. Real configs are **gitignored** (`clients/*.yaml` except `_example.yaml`).

```yaml
db_name: Olives_BO          # catalog on the SQL Server instance
company_scope: single       # informational; live probe in schema_cache is authoritative
name_aliases: [morec]       # client-specific proc name suffixes
locale: ar
```

Multi-company clients: user must specify `CompanyID`; session memory resolves aliases via `schema_cache.json` → `profile_probe.companies`.

---

## LLM gateway (OmniRoute)

```bash
omniroute serve --port 20128          # or: omniroute serve --daemon --no-open
```

App calls `GATEWAY_URL` with `GATEWAY_API_KEY`. Model name from `CHATBOT_MODEL`.  
See `gateway/README.md`. LiteLLM (`gateway/litellm.config.yaml`) is an optional fallback.

---

## Vault and MCP

| Item | Path |
|------|------|
| Vault | `obsidian/olives/` (2659 files) |
| Graph | `db/vault_graph.json` |
| MCP server | `obsidian-mcp-server.py` |

```bash
python3.13 obsidian-mcp-server.py    # stdio JSON-RPC for editors/agents
```

**Runtime today:** agent uses `search_docs` (FTS), not vault MCP.  
**Planned:** vault MCP for join/schema understanding in NL2SQL (FIXPLAN M11).

Excluded from FTS corpus (by design): raw proc bodies, staff runbooks, duplicate system-option dumps.

---

## Run the app

```bash
set -a && source .env && set +a
./run.sh
# or: uvicorn api.server:app --host 0.0.0.0 --port 8100
```

Chat UI: `http://localhost:8100` — no login; tenant pinned via `CHATBOT_CLIENT` in `.env`.

Eval gate (optional):

```bash
python3.13 evals/run_evals.py
```

---

## Do not

- Commit `.env`, `work/`, `*.bak`, real `clients/*.yaml`, or API keys
- Use IIS `cds` credentials or SA from `core/` at runtime
- Grant `db_datareader` or base-table SELECT to `chatbot_ro`
- Bypass `core/gate.py` or duplicate SQL execution elsewhere
- Return procedure bodies to the model
- Remove or gitignore vault files under `obsidian/olives/`
- Assume `vault_graph.json` is clean schema truth (use live introspection for SQL; graph for MCP impact/deps only)

---

## Related docs

| File | Contents |
|------|----------|
| `README.md` | Quick start |
| `PLAN.md` | Full pilot build plan |
| `FIXPLAN.md` | Known gaps and live-tested fixes |
| `TOOLS-REVIEW.md` | Tool adoption decisions |

Legacy olives monorepo (drift-tool Docker only): `/media/alaa/data/olives/apps/drift-tool` — needed only for `setup/01_db_up.py --mode docker`.
