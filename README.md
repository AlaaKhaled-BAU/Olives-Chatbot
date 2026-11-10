# Olives Client Chatbot

Arabic-first assistant that answers from **indexed documentation** and **read-only SQL** against the customer’s **Olives_BO** database. This repository is the **pilot FastAPI service** (`api/server.py`) plus the agent stack in `core/`; a small static UI ships under `static/`.

**Operator’s contract:** the runtime uses a dedicated SQL login and tenant-scoped views (`t.*`). It does not use the IIS application login or SA at request time. Details and non-negotiables live in **[AGENTS.md](AGENTS.md)**.

---

## What you get

| Layer | Role |
|--------|------|
| **FastAPI** | `POST /ask` (SSE), `GET /context`, `GET /health`, `GET /metrics`, static UI |
| **Agent** | Tool loop: doc search, schema help, gated `SELECT` / metrics / reports |
| **SQL** | `pymssql` + `sqlglot` gate + `SESSION_CONTEXT('CompanyID')` via `core/sql.py` |
| **LLM** | OpenAI-compatible client; default provider is **DeepSeek** (`core/llm.py`) |
| **Memory** | SQLite: plan cache, verified queries, short result cache (`work/`, gitignored) |
| **Knowledge** | FTS over assembled corpus; large Obsidian vault under `obsidian/olives/` |

---

## Prerequisites

- **Python 3.13** (see `requirements.txt`; do not rely on older interpreters).
- **SQL Server** reachable from the app host, with **Olives_BO** (or your target DB) and scripts from `setup/` applied so **`chatbot_ro`** and **`t.`** views exist (`db/`, `setup/03_apply_db_sql.py`).
- **Tenant config:** `clients/<name>.yaml` (real files are gitignored; copy from `clients/_example.yaml`).
- **Secrets:** create `.env` from `.env.example` (never commit `.env`).

---

## Quick start

### 1. Install dependencies

```bash
python3.13 -m pip install -r requirements.txt
```

On Windows, if you use the launcher:

```powershell
py -3.13 -m pip install -r requirements.txt
```

### 2. Configure environment

```bash
cp .env.example .env
```

Set at minimum:

- `DEEPSEEK_API_KEY` — primary secret for the default DeepSeek endpoint (or set `CHATBOT_LLM_API_KEY` when using `CHATBOT_LLM_BASE_URL`).
- `CHATBOT_CLIENT` — must match a `clients/<name>.yaml` file on disk.
- `DB_SA_PASSWORD` — only for **setup** scripts that connect as SA (not used by the running API for chat SQL).

See **[.env.example](.env.example)** for DB host/port and optional LLM overrides.

### 3. Bootstrap against an existing database (SA)

Skip if `schema_cache`, `t.` views, and docs index are already in place for your client.

```bash
set -a && source .env && set +a   # Linux / WSL / Git Bash
python3.13 setup/native_bootstrap.py --client <client_name>
```

Restore from `.bak` first when needed (native SQL Server, snapshot path as in `AGENTS.md`):

```bash
python3.13 setup/01_db_up.py --mode native --db-name Olives_BO --bak "<path-to.bak>"
python3.13 setup/native_bootstrap.py --client <client_name> --db-name Olives_BO
```

### 4. Run the API

**Linux / macOS / WSL** (loads `.env`, enforces key presence):

```bash
./run.sh
```

**Windows** (PowerShell, same port convention):

```powershell
.\run.ps1
```

**Manual** (after exporting env vars):

```bash
python3.13 -m uvicorn api.server:app --host 127.0.0.1 --port 8100
```

Open **http://127.0.0.1:8100**. The UI expects the tenant pinned in `CHATBOT_CLIENT`; the browser does not switch YAML clients.

---

## Environment variables (reference)

| Variable | Purpose |
|----------|---------|
| `CHATBOT_CLIENT` | Pinned tenant; loads `clients/<name>.yaml` at startup (**required**) |
| `DEEPSEEK_API_KEY` | Default API key for DeepSeek (`https://api.deepseek.com`) |
| `CHATBOT_LLM_BASE_URL` | Optional alternate OpenAI-compatible base URL |
| `CHATBOT_LLM_API_KEY` | Optional key when not using `DEEPSEEK_API_KEY` alone |
| `CHATBOT_MODEL_FAST` / `CHATBOT_MODEL_HEAVY` | Model names for interactive vs rescue gears |
| `DB_HOST` / `DB_PORT` | SQL Server endpoint for runtime and setup tools (default `127.0.0.1:1433`) |
| `DB_SA_USER` / `DB_SA_PASSWORD` | Setup only — **not** the chatbot runtime login |

Runtime SQL uses **`chatbot_ro`** as described in `db/01_readonly_login.sql`; keep SA credentials out of `core/` and `api/`.

---

## When the customer schema changes

Introspection and `t.` views do not auto-heal in the pilot. Re-run as SA:

```bash
python3.13 setup/refresh.py --client <name>
```

This rebuilds `work/<client>/schema_cache.json` and reapplies tenant views. See **FIXPLAN.md** (e.g. M7) for edge cases that were live-tested.

---

## Tests and evals

```bash
python3.13 -m pytest
python3.13 evals/run_evals.py    # optional harness / gate
```

Eval assets and large result JSON under `evals/` are for quality gates and offline analysis, not required to boot the server.

---

## Repository layout (high level)

```
api/           FastAPI app and HTTP surface
core/          Agent, LLM adapter, SQL, gate, memory, metrics, tracing
static/        Chat UI (served by FastAPI)
setup/         DB bootstrap, introspection, docs corpus, refresh
db/            SQL for chatbot_ro and t.* tenant views
knowledge/     Source markdown for FTS corpus (via assemble + index scripts)
obsidian/      Customer vault (tables, relations, runbooks) — large, load-bearing
tests/         Pytest suite
evals/         Offline eval runners and fixtures
sqlmcp/        MCP-style SQL tooling (optional; see sqlmcp/README.md)
docker/        Optional container build helpers
```

Optional: **`obsidian-mcp-server.py`** for editor MCP integration; runtime chat uses FTS, not MCP, unless you wire it separately.

---

## Documentation map

| Document | Contents |
|----------|-----------|
| [AGENTS.md](AGENTS.md) | Golden rules, architecture, env, setup commands (**read first**) |
| [PLAN.md](PLAN.md) | Original phased plan (some paths superseded by DeepSeek-direct stack) |
| [FIXPLAN.md](FIXPLAN.md) | Known gaps and tested fixes |
| [TOOLS-REVIEW.md](TOOLS-REVIEW.md) | Tooling decisions |
| [plans/deepseek_swap_parallel_plan.md](plans/deepseek_swap_parallel_plan.md) | LLM gear semantics and API notes |

---

## Security notes

- Do not commit `.env`, `work/`, real `clients/*.yaml`, or database backups.
- Do not grant base-table `SELECT` to `chatbot_ro`; tenant access is through **`t.`** views and procedure allow-lists as defined in the gate and catalog.
- Procedure bodies are not returned to the model or end users (see **AGENTS.md**).

---

## License / upstream

Internal Olives pilot; coordinate with the repo owner for redistribution and customer deployments.
