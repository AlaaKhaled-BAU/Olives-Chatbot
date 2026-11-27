# Olives Client Chatbot

An Arabic-first, tenant-isolated AI copilot for **Olives_BO** (an enterprise FMCG distribution and van-sales ERP running on SQL Server and IIS). It answers operational "how-to" questions from indexed product documentation and executes verified, read-only natural-language-to-SQL (NL2SQL) queries against live customer databases.

> **Security Contract:** At runtime, the service connects exclusively through a restricted `chatbot_ro` SQL Server login with zero base-table grants and zero `EXECUTE` permissions. All data access is mediated by `t.*` views scoped via `SESSION_CONTEXT('CompanyID')` and validated through a `sqlglot` AST safety gate.

---

## Architecture

```
Browser / Embedded Widget (static/index.html + app.js, Arabic RTL)
  │  POST /ask (SSE + heartbeat), GET /context, POST /feedback, GET /metrics
  ▼
FastAPI Service (api/server.py)
  ├─ Env-pinned tenant (CHATBOT_CLIENT → clients/<name>.yaml; browser cannot switch)
  ├─ Per-session rate limiting (slowapi, 30 req/min) & LRU session state
  └─ SSE stream pump with keep-alive heartbeats & disconnect cancellation
  │
  ▼
Agent Pipeline (core/agent.py)
  ├─ 1. Scope & Guards     ──► CompanyID resolution (core/params.py) + empty-calendar guard
  ├─ 2. Routing & Memory   ──► Intent router (fast-count / report / how-to / NL2SQL)
  │                            SQLite plan, result & few-shot caches (core/memory.py)
  ├─ 3. Prompt Assembly    ──► Byte-stable static prefix (system + playbook + t.* schema + vault cards)
  │                            followed by dynamic per-turn context (KV-cache friendly)
  ├─ 4. Tool Loop (≤12)    ──► DeepSeek gears (f0 / t1 / t2 / p) via core/llm.py
  │                            Tools: run_select, run_metric, run_report, lookup_hot,
  │                                   search_docs, search_schema_notes, get_joins, analyze, ask_user
  └─ 5. Verification & Out ──► Header-vs-line grain check (core/verify.py), JSON envelope,
                               JSONL tracing & Prometheus metrics (core/trace.py)
  │
  ├─────────────────────────┬─────────────────────────┐
  ▼                         ▼                         ▼
SQL Safety & Exec        Knowledge & Schema        L1 / L2 Caches
core/gate.py (sqlglot)   core/docs.py (FTS5)       work/<client>/cache.sqlite
core/sql.py (pymssql)    core/vault.py (cards)     core/hot_cache.py (master TTL)
  │
  ▼
SQL Server (Olives_BO)
  └─ Login: chatbot_ro → Schema: t.* views → WHERE CompanyID = SESSION_CONTEXT('CompanyID')
```

---

## Key Engineering Highlights

### 1. Five-Layer Tenant Isolation & SQL Safety Wall
No single layer trusts another:
1. **Tenant Pinning:** `CHATBOT_CLIENT` in `.env` pins the deployment to a single `clients/<name>.yaml`; request bodies cannot override the tenant.
2. **Least-Privilege SQL Login:** `chatbot_ro` (`db/01_readonly_login.sql`) is intentionally **not** in `db_datareader` and holds zero base-table `SELECT` or `EXECUTE` grants.
3. **Engine-Enforced View Scoping:** `db/02_tenant_views.sql` generates `t.*` views filtered by `SESSION_CONTEXT('CompanyID')`. Unset session context evaluates to `NULL` and fails closed to zero rows.
4. **AST-Level SQL Gate (`core/gate.py`):** Parses every query with `sqlglot` (TSQL dialect). Enforces single `SELECT` statements, blocks DDL/DML/`EXEC`/`OPENROWSET`/`xp_*`, rejects cross-company literals, injects tenant predicates, N-prefixes Arabic string literals (`N'...'`), and caps results (`TOP 200`).
5. **Context & UI Caps:** Model context is capped at 50 rows and UI tables at 100 rows to prevent token bloat and OOMs.

### 2. Cost & Latency Optimization via DeepSeek Gears & Prefix Caching
- **Gear Routing (`core/llm.py`):** Maps task complexity to model/thinking profiles rather than hardcoding model names:
  - `f0` (`deepseek-v4-flash`, thinking off): docs Q&A, fast-count SQL, report paths, JSON envelope formatting.
  - `t1` (`deepseek-v4-flash`, thinking low): standard interactive NL2SQL.
  - `t2` (`deepseek-v4-flash`, thinking high): mid-turn escalation on gate/tool errors or analytical queries.
  - `p` (`deepseek-v4-pro`, thinking high): non-streaming rescue path for empty-final retries only.
- **Byte-Stable Prefix Caching:** System instructions, join playbook, queryable `t.*` schema, and compiled vault cards are placed in an immutable leading prefix (`messages[0..2]`) with a fixed tool list per turn, preserving DeepSeek's disk KV-cache across turns.
- **Thinking + Tool Echo:** Accumulates and echoes `reasoning_content` across multi-turn tool calls as required by DeepSeek's thinking API contract.

### 3. Domain-Specific Reliability & Arabic-First Design
- **Arabic Morphology & Normalization (`core/docs.py`, `core/locale_ar.py`):** FTS5 search handles Arabic normalization, singular/plural/prefixed forms, and bilingual schema preservation (schema identifiers stay in English; Arabic string literals receive `N'...'`).
- **Grain & Calendar Honesty (`core/verify.py`, `core/agent.py`):** Detects header-vs-line `COUNT` traps when joining `TransactionsHeaders` with `TransactionsDetails`, and intercepts relative-date queries (e.g., "this month") when the database's latest posting period is empty before spending LLM tokens.
- **Human-in-the-Loop Learning (`POST /feedback`):** Thumbs-up feedback re-validates the executed SQL through `core/gate.py` before promoting it to `verified_queries` few-shots; thumbs-down invalidates the plan cache and records a negative example.

---

## Repository Layout

| Path | Purpose |
|------|---------|
| `api/server.py` | FastAPI HTTP/SSE server, rate limiting, session store, `/health`, `/metrics`, `/feedback` |
| `core/agent.py` | Turn pipeline, intent router, tool loop, budget enforcement, answer contract |
| `core/gate.py` | `sqlglot` AST validator/rewriter (single `SELECT`, `TOP` injection, tenant predicates) |
| `core/sql.py` | `chatbot_ro` connection factory, `SESSION_CONTEXT` binding, `run_select` |
| `core/llm.py` | OpenAI-compatible DeepSeek adapter, gear table, retry policy, token/cache accounting |
| `core/memory.py` | SQLite caches (`verified_queries`, `negative_queries`, `plan_cache`, `result_cache`) scoped by `client + CompanyID + model + schema_version` |
| `core/docs.py` | FTS5 documentation search with Arabic morphology support |
| `core/vault.py` | Compiled Obsidian vault table/relation cards and join lookup |
| `core/metrics.py` & `core/reports.py` | Deterministic parameterized `SELECT` templates for KPIs and certified reports |
| `core/hot_cache.py` & `core/tenant_pack.py` | L1 master-table TTL cache and live per-company prompt facts |
| `core/verify.py` & `core/trace.py` | Header/line grain verifier, JSONL event tracing, Prometheus metrics |
| `db/` | Setup-time SQL (`01_readonly_login.sql`, `02_tenant_views.sql`) and table classification |
| `setup/` | SA bootstrap scripts: DB restore, schema introspection, `t.*` view creation, FTS indexing, vault card compilation |
| `clients/` | Per-tenant YAML configs (`_example.yaml` template; real client configs are gitignored) |
| `obsidian/olives/` | Domain knowledge vault (tables, procedures, relations, runbooks) |
| `knowledge/` | Curated user-guide and reference markdown sources for FTS5 indexing |
| `static/` | Arabic RTL web chat UI |
| `evals/` & `tests/` | Unit test suite (`pytest`) and offline accuracy/isolation evaluation batteries |
| `windows_packaging/` & `docker/` | PyInstaller standalone Windows `.exe` entry point and Docker build/compose helpers |

---

## Prerequisites

- **Python 3.13** (`python3.13` on Linux/macOS, `py -3.13` on Windows).
- **SQL Server** reachable from the host with `Olives_BO` (or target database) restored.
- **Environment & Client Config:** `.env` (from `.env.example`) and `clients/<name>.yaml` (from `clients/_example.yaml`).

---

## Quick Start

### 1. Install Dependencies

```bash
python3.13 -m pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
```

Set the required variables in `.env`:

| Variable | Description |
|----------|-------------|
| `CHATBOT_CLIENT` | Pinned tenant matching `clients/<name>.yaml` (**required**) |
| `DEEPSEEK_API_KEY` | DeepSeek API key (or `CHATBOT_LLM_API_KEY` + `CHATBOT_LLM_BASE_URL` for compatible endpoints) |
| `CHATBOT_MODEL_FAST` / `CHATBOT_MODEL_HEAVY` | Model IDs for interactive vs. rescue gears |
| `DB_HOST` / `DB_PORT` | SQL Server host and port (default `127.0.0.1:1433`) |
| `DB_SA_USER` / `DB_SA_PASSWORD` | SA credentials used **only** by `setup/` scripts |

### 3. Bootstrap Database & Indexes (Setup-Time SA)

Applies `chatbot_ro`, builds `t.*` tenant views, introspects live schema to `work/<client>/schema_cache.json`, and builds the FTS5 docs index:

```bash
set -a && source .env && set +a
python3.13 setup/native_bootstrap.py --client <client_name>
```

If restoring from a `.bak` snapshot first:

```bash
python3.13 setup/01_db_up.py --mode native --db-name Olives_BO --bak "<path-to.bak>"
python3.13 setup/native_bootstrap.py --client <client_name> --db-name Olives_BO
```

To refresh schema metadata and `t.*` views after customer schema changes:

```bash
python3.13 setup/refresh.py --client <client_name>
```

### 4. Run the Service

```bash
# Linux / macOS / WSL
./run.sh

# Windows (PowerShell)
.\run.ps1

# Or directly
python3.13 -m uvicorn api.server:app --host 127.0.0.1 --port 8100
```

Open `http://127.0.0.1:8100`.

---

## Testing & Evaluation

```bash
# Unit & integration tests (offline tests run without live DB; multi-client/isolation tests require bootstrapped clients)
python3.13 -m pytest -q

# Offline accuracy & isolation evaluation harness
python3.13 evals/run_evals.py
```

---

## Security & Operational Rules

- **Never** commit `.env`, `work/`, `.bak` files, or real `clients/*.yaml` configs.
- **Never** grant `db_datareader` or base-table `SELECT` to `chatbot_ro`, and never use SA or IIS `cds` credentials in `core/` or `api/`.
- **Never** return stored procedure bodies to the model or end users.
- **Always** route runtime SQL through `core/sql.py` + `core/gate.py` so `SESSION_CONTEXT` and AST checks cannot be bypassed.
- See [AGENTS.md](AGENTS.md) and [docs/SYSTEM_BLUEPRINT.md](docs/SYSTEM_BLUEPRINT.md) for the full architectural invariants and lifecycle documentation.
