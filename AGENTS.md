# AGENTS.md — Olives Client Chatbot (standalone)

This repository is a **standalone extract** of the Olives client chatbot pilot from the olives monorepo. It is intended to become an **IIS circle-widget** on customer Windows servers; the current code is a **FastAPI full-page pilot** (`api/server.py` + `static/`).

## Runtime

- **Python 3.13 only** (`python3.13`). Do not run under 3.12 or earlier.
- Install deps: `pip install -r requirements.txt`
- App entry: `uvicorn api.server:app` (after setup phases in README / PLAN.md)

## Layout (this repo)

| Path | Purpose |
|------|---------|
| `api/`, `core/`, `static/` | FastAPI app, SQL gate, UI |
| `clients/` | Per-client yaml (`clients/_example.yaml` template); **no secrets in yaml** |
| `db/*.sql` | Read-only login + tenant `t.` views (server-side wall) |
| `gateway/` | OmniRoute client config docs; optional LiteLLM `litellm.config.yaml` |
| `knowledge/` | FTS corpus sources (reference, back-office, front-office, support-agent) |
| `docs_corpus/` | **Derived** — gitignored symlinks; regenerate with `setup/04_assemble_docs_corpus.py` |
| `obsidian/olives/` | Obsidian vault (schema notes, tables, procedures, relations) — **2659 files, track as-is** |
| `obsidian-mcp-server.py` | Vault MCP (stdio JSON-RPC) |
| `db/vault_graph.json` | Precomputed vault link graph for MCP |
| `sqlmcp/` | Optional SSE MCP over `core/sql.py` |
| `setup/` | Bootstrap scripts (DB, introspect, corpus, index) |
| `work/` | **Gitignored** — per-client schema cache, ro password, sqlite indexes |

## Vault and MCP

- **Vault:** `/media/alaa/data/client-chatbot/obsidian/olives`
- **Graph:** `/media/alaa/data/client-chatbot/db/vault_graph.json`
- **Run MCP (stdio):** `python3.13 obsidian-mcp-server.py`
- Vault MCP is for **schema / join understanding** (to be wired into the agent loop). Today, end-user doc answers use **FTS over `docs_corpus/`** built from `knowledge/`.

## Secrets and tenant wall

- **Tenant bearer tokens:** only in `.env` (gitignored). Each `clients/*.yaml` names its var via `api_token_env`; never put token values in yaml.
- **LLM:** OmniRoute at `GATEWAY_URL` (default `http://localhost:20128/v1`). App key in `.env` as `GATEWAY_API_KEY`. Provider keys in `~/.omniroute` via `omniroute keys`.
- **Never commit:** `.env`, `gateway/.env`, `work/`, real `clients/*.yaml`, `*.bak`, gateway keys, `MASTER_KEY`, `GATEWAY_API_KEY`.
- **Tenant wall:** app connects as **`chatbot_ro`** + tenant-scoped **`t.` views** + `SESSION_CONTEXT` (`CompanyID`). **Never** use IIS `cds` credentials from customer `Web.config`.
- **One SQL implementation:** `core/sql.py` + `core/gate.py`. All SQL paths go through the gate.
- **Never return procedure bodies** to the model or client (structure/metadata only).
- **Cache keys** (`core/memory.py`) must include **client name + CompanyID** so tenants never share cache rows.

## SQL Server / IIS target

- Production: customer **Windows IIS** host with **Olives_BO** + **OSFA_DB** on their SQL Server instance.
- The **circle widget is not built yet**; this repo is the service backend + pilot UI.
- Local dev: Docker SQL Server via **drift-tool** (see below) — not the production path.

## Local Docker / drift-tool (dev only)

Setup scripts `setup/01_db_up.py`, `02_introspect.py`, `03_apply_db_sql.py`, and `setup/refresh.py` still import **`drift-tool`** from the olives monorepo layout. They are **not rewritten in this extract**.

**Main DB backups** (gitignored): `data/db-snapshots/backup test/` — copied from olives (`105/` master pair + `morec/` pilot client). Default restore: `morec/Olives_BO.bak`.

For local restore and introspection, either:

- Keep olives `apps/drift-tool` on disk and set:
  `export DRIFT_TOOL_ROOT=/media/alaa/data/olives/apps/drift-tool`
  (scripts currently resolve `../drift-tool` relative to olives `apps/` — you may need to symlink or adjust paths until a follow-up normalizes this), **or**
- Point `CHATBOT_TEST_BAK` / `--bak` at a `.bak` on disk (multi-GB; never in git).

Shared dev container name: `drift-tool-mssql` on host port **14330**.

## Docs corpus regeneration

```bash
python3.13 setup/04_assemble_docs_corpus.py   # symlinks knowledge/ -> docs_corpus/
python3.13 setup/05_index_docs.py --client <name>  # FTS sqlite in work/<client>/docs.sqlite
```

## Setup order

Follow README.md and PLAN.md phase order:

1. `.env` + `gateway/.env` from examples
2. `python3.13 setup/01_db_up.py` (Docker + restore — needs drift-tool)
3. `python3.13 setup/02_introspect.py --client <name>`
4. `python3.13 setup/03_apply_db_sql.py --db-name <db>`
5. `python3.13 setup/04_assemble_docs_corpus.py`
6. `python3.13 setup/05_index_docs.py --client <name>`
7. Start gateway, then `uvicorn api.server:app`
8. `python3.13 evals/run_evals.py`

Schema drift on a client: `python3.13 setup/refresh.py --client <name>`.

## Do not

- Commit secrets or real client configs
- Bypass `core/gate.py` for SQL
- Grant base-table access to `chatbot_ro`
- Copy IIS `cds` SQL credentials into this app
- Gitignore or omit vault files under `obsidian/olives/` (including `.obsidian/`)
