# Client Chatbot — Standalone Extraction Notes

**Scope:** `/media/alaa/data/olives/apps/client-chatbot/` as mapped for a future **standalone** project (embeddable widget on customer IIS sites; docs Q&A + NL2SQL against customer SQL Server).

**Generated:** 2026-08-13 (read-only survey; no code changes).

---

## 1. Directory tree (logical)

### 1.1 What exists today (by role)

```
client-chatbot/
├── PLAN.md, FIXPLAN.md, README.md          # design + post-review fix backlog + runbook
├── TOOLS-REVIEW.md, RESEARCH-RAW.md        # tool research (not runtime)
├── METABASE-EVAL.md                        # Phase 10 go/no-go note (Metabase)
├── requirements.txt                        # pinned Python deps (no `mcp` package)
├── run.sh                                  # dev launcher: Docker MSSQL + gateway + API :8100
├── .env.example, .env                      # app config + per-client bearer tokens (gitignored)
├── .gitignore
│
├── api/
│   └── server.py                           # FastAPI: POST /ask (SSE), /feedback, /health, /metrics; mounts static/
│
├── core/                                   # brain (no LLM API key, no web server)
│   ├── agent.py                            # agent loop + tools + streaming
│   ├── catalog.py                          # per-client proc entitlement filter
│   ├── config.py                           # YAML client loader + work/<client>/ paths
│   ├── docs.py                             # FTS5 docs search (NOT vault MCP)
│   ├── gate.py                             # sqlglot safety gate
│   ├── llm.py                              # OpenAI-compatible client → gateway
│   ├── memory.py                           # SQLite: verified_queries, plan_cache, result_cache
│   ├── params.py                           # CompanyID / ClientActive resolution
│   ├── procedure_match.py                  # TF-IDF proc matcher — **exists but unused**
│   ├── sql.py                              # pymssql + SESSION_CONTEXT tenant wall
│   └── trace.py                            # JSONL audit + Prometheus metrics
│
├── gateway/                                # LLM key custody ONLY
│   ├── litellm.config.yaml                 # Gemini primary, DeepSeek fallback
│   ├── .env.example, .env                  # GEMINI_KEY, DEEPSEEK_KEY, MASTER_KEY (gitignored)
│   └── README.md
│
├── clients/
│   ├── _example.yaml                       # template (tracked)
│   ├── morec.yaml, rukn.yaml               # real configs (gitignored per .gitignore)
│
├── db/
│   ├── 01_readonly_login.sql               # chatbot_ro login + db_datareader
│   ├── 02_tenant_views.sql                 # `t.` SESSION_CONTEXT-scoped views
│   └── table_classification.md             # which tables get `t.` views (C0 policy)
│
├── prompts/
│   └── system.md                           # system prompt ({{CLIENT}} placeholder)
│   # NOTE: PLAN.md lists verified_queries.seed.jsonl — **not present**
│
├── static/                                 # full-page chat UI (see §4)
│   ├── index.html, app.js, style.css
│
├── setup/
│   ├── 01_db_up.py                         # Docker MSSQL + restore .bak (via drift-tool)
│   ├── 02_introspect.py                    # SA introspection → work/<client>/schema_cache.json
│   ├── 03_apply_db_sql.py                  # apply db/*.sql as SA
│   ├── 04_assemble_docs_corpus.py          # symlinks parent-repo knowledge → docs_corpus/
│   ├── 05_index_docs.py                    # build work/<client>/docs.sqlite
│   └── refresh.py                          # chain 02+03 + orphan view cleanup (FIXPLAN M7)
│
├── evals/
│   ├── accuracy.jsonl          (12 cases)
│   ├── docs_accuracy.jsonl       (5 cases)
│   ├── isolation.jsonl         (11 cases)
│   └── run_evals.py            # release gate; calls live agent + DB
│
├── tests/                      (15 modules, 31 tests per FIXPLAN.md)
│   test_agent.py, test_api.py, test_auth.py, test_catalog.py,
│   test_docs.py, test_evals.py, test_feedback.py, test_gate.py,
│   test_gateway.py, test_llm.py, test_memory.py, test_multi_client.py,
│   test_params.py, test_rate_limit.py, test_session_memory.py, test_tenant_wall.py
│
├── sqlmcp/                     # optional gated SQL MCP (SSE); not used by agent in-process
│   ├── sql_server.py, prove_isolation.py, run_isolation_test.sh, Dockerfile, README.md
│
├── docs_corpus/                # gitignored; symlinks to parent `knowledge/` + support-agent
├── work/                       # gitignored runtime artifacts
│   ├── cache.sqlite, ro_password.txt, trace.jsonl, litellm.log
│   ├── morec/schema_cache.json, docs.sqlite, …
│   └── rukn/…
│
├── olives web pages/           # ~901 MB, 783 .aspx — bundled Olives ASP.NET site (reference only)
└── _extract_notes/             # this file
```

### 1.2 PLAN.md vs actual code

| PLAN item | Status | Notes |
|-----------|--------|-------|
| Phases 0–9 (pilot service) | **Mostly built** | FIXPLAN.md claims M1–M9 largely done (2026-07-25 baseline) |
| `core/schema.py` | **Missing** | Introspection lives in `setup/02_introspect.py`, output in `work/<client>/schema_cache.json` |
| `prompts/verified_queries.seed.jsonl` | **Missing** | Seeding via eval promotion + `/feedback` thumbs-up instead |
| `run_proc` tool | **Removed** | FIXPLAN M6 Path B: `chatbot_ro` has no EXECUTE; tool dict deleted from `agent.py` lines 133–211 |
| Docs via vault MCP | **Not wired** | Implemented as local FTS5 (`core/docs.py` + `setup/05_index_docs.py`) |
| `procedure_match.py` | **Orphan** | File exists; not imported by `agent.py` |
| Phase 10 docs corpus | **Partial** | `04_assemble_docs_corpus.py` + FTS index; MinerU not needed per script comments |
| Phase 10 Metabase | **Eval only** | `METABASE-EVAL.md` go/no-go recorded; no Metabase code |
| Central Docker pilot | **Current design** | Not IIS/on-prem per customer |
| Per-client on-prem installs | **Explicitly deferred** | PLAN.md line 21 |
| Vault universal schema (M11) | **Not started** | FIXPLAN.md separate track |
| Redis gateway cache | **Deferred** | `litellm.config.yaml` uses `type: local` |
| `core/agent.py` streaming | **Built** | C7: real SSE progress + answer chunks (`api/server.py` lines 188–236) |

---

## 2. Runtime: `/ask`, agent loop, paths, tenant isolation, gateway

### 2.1 HTTP surface (`api/server.py`)

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/ask` | POST | SSE stream; body `{question, session_id?, client?}` — **`client` ignored** |
| `/feedback` | POST | Thumbs up/down on last turn (session-bound) |
| `/health` | GET | Gateway liveness + per-client DB ping + token config + nullable CompanyID stats |
| `/metrics` | GET | Prometheus from `core/trace.py` |
| `/` | GET | Serves `static/` (full-page UI) |

**Auth (FIXPLAN M1, implemented):** Bearer token → client name via `TOKEN_MAP` built at startup from `clients/*.yaml` `api_token_env` + environment (lines 44–86). Missing/invalid token → 401/403.

**Rate limit (M3):** `@limiter.limit("30/minute")` keyed on `Authorization` header (lines 32–36, 177).

**Session memory (M8):** In-process `OrderedDict` `SESSIONS` (max 500, 1h idle) stores `conversation` + `pending_ask` + `last_turn` for `/feedback` (lines 95–129, 207–220).

### 2.2 `/ask` SSE event shapes

From `api/server.py` lines 196–236:

- `{"step": "searching schema"}` — progress only; never SQL text
- `{"answer_chunk": "..."}` — streamed final answer tokens
- `{"needs_ask": "..."}` — clarifying question (e.g. CompanyID)
- `{"answer", "table", "chart", "followups", "sources"}` — final envelope
- `{"error": "..."}` — mid-stream failure
- `data: [DONE]`

### 2.3 Agent loop (`core/agent.py`)

**Entry:** `ask_stream()` (line 434) / `ask()` wrapper (line 639).

**Flow:**

1. Load client config, `schema_cache.json`, entitled proc catalog (`catalog.for_client`).
2. Resolve `CompanyID` via `params.discover_profile` + `params.resolve` + session `conversation` (lines 458–474). `MULTI`/`NEEDS_ASK` → return `needs_ask` without LLM.
3. **Plan cache hit:** Re-run cached SQL list, stream formatted answer (lines 481–527).
4. **Full turn:** System prompt + verified-query few-shots → LLM with tools (max **12** turns, max **4** business queries per turn — lines 29–38, 550–609).
5. **Tools** (lines 133–211): `introspect_schema`, `run_select`, `ask_user`, `analyze`, `search_docs`. No `run_proc`.
6. After `MAX_QUERIES` business `run_select` calls, tools withheld (golden rule 6 variant).
7. On success: write `plan_cache` only — **not** `verified_queries` (lines 617–626). Promotion via eval or `/feedback` only.
8. Build envelope: table/chart/sources/followups (`_build_envelope`, line 420).

**Docs vs SQL routing** (`prompts/system.md` lines 13–26; `agent.py` lines 304–313):

- Conceptual/how-to → `search_docs` (FTS5, no query budget).
- Counts/lists/this client's data → `introspect_schema` + `run_select` on `t.*` views.
- Both allowed in one turn.

**LLM:** `core/llm.py` → `GATEWAY_URL` (default `http://localhost:4000`), model alias `"chatbot"`, optional `GATEWAY_API_KEY` (line 31).

### 2.4 SQL path

```
run_select(sql) → gate.validate() → pymssql chatbot_ro → set_tenant(CompanyID)
                → execute on t.* views only → row cap (200 via gate)
```

- `core/sql.py` lines 26–58: per-client `db_name` from YAML; shared `work/ro_password.txt`.
- `db/02_tenant_views.sql` lines 4–9: `SESSION_CONTEXT(N'CompanyID')`; unset → zero rows (fail closed).
- `core/gate.py`: single SELECT or allow-listed EXEC in SQL text; blocks writes, `xp_*`, `OPENROWSET`, multi-statement; injects `TOP(n)`; `N'…'` Arabic literals.

### 2.5 Tenant isolation layers

| Layer | Mechanism | File |
|-------|-----------|------|
| API | Bearer token → client; body `client` ignored | `api/server.py` 79–86, 179 |
| Catalog | Deny-by-default proc names with other clients' tokens | `core/catalog.py` 72–78 |
| DB login | `chatbot_ro` — SELECT on `t.` only | `db/01_readonly_login.sql`, `db/02_tenant_views.sql` |
| Session | `sp_set_session_context 'CompanyID', @id` per connection | `core/sql.py` 38–43 |
| Gate | sqlglot allow-list | `core/gate.py` |
| Cache keys | `client+CompanyID+role+model+question+schema_version` | `core/memory.py` 74–80 |
| Docs index | Per-client `docs.sqlite`; chunks naming other clients excluded at index time | `core/docs.py` 155–184 |

### 2.6 Gateway

- **Process:** LiteLLM proxy (`gateway/litellm.config.yaml`).
- **Models:** `chatbot` = Gemini 2.5 Flash; fallback `chatbot-fallback` = DeepSeek v4 Flash (lines 33–45).
- **Keys:** `GEMINI_KEY`, `DEEPSEEK_KEY` in `gateway/.env` only. `LLM_API_KEY` (Claude) placeholder empty in `.env.example`.
- **Auth to gateway:** `general_settings.master_key: os.environ/MASTER_KEY`; app sends `GATEWAY_API_KEY` (`litellm.config.yaml` lines 29–32, `core/llm.py` line 31).
- **Cache:** Local in-memory (`litellm_settings.cache_params.type: local`).
- **Health check:** `api/server.py` line 282 → `http://localhost:4000/health/liveliness`.

---

## 3. Configuration

### 3.1 Root `.env.example` (lines 1–13)

```env
GATEWAY_URL=http://localhost:4000
DB_HOST=127.0.0.1
DB_PORT=14330
DB_NAME=chatbot_db          # informational; per-client db_name in YAML overrides
OLIVES_TOKEN_MOREC=
OLIVES_TOKEN_RUKN=
```

**Not in `.env.example` but required at runtime:**

- `GATEWAY_API_KEY` — must match gateway `MASTER_KEY` (`core/llm.py` line 31).
- Actual values in gitignored `.env`.

### 3.2 `gateway/.env.example` (lines 1–3)

```env
LLM_API_KEY=
DEEPSEEK_KEY=
```

**Also used (from `litellm.config.yaml`):** `GEMINI_KEY`, `MASTER_KEY` — not documented in `.env.example`.

### 3.3 `clients/*.yaml`

**Template** (`clients/_example.yaml` lines 1–14):

- `db_name` — SQL Server database for this client
- `company_scope` — informational; real value from live probe in `schema_cache.json`
- `name_aliases` — for catalog + docs confidentiality filter
- `locale`
- `api_token_env` — name of env var holding bearer token (**token never in YAML**)

**Live examples:**

- `morec.yaml`: `db_name: chatbot_db`, aliases `[morec, morek]`, `api_token_env: OLIVES_TOKEN_MOREC`
- `rukn.yaml`: `db_name: chatbot_db2`, aliases `[rukn, alalmas, "ركن الالماس"]`, `api_token_env: OLIVES_TOKEN_RUKN`

**Git:** `.gitignore` ignores `clients/*.yaml` except `_example.yaml` (lines 11–12).

### 3.4 `core/config.py` (lines 1–24)

- `BASE_DIR` = parent of `core/` (project root)
- `CLIENTS_DIR` = `clients/`
- `load_client(name)` → parsed YAML
- `work_dir(client)` → `work/<client>/` (schema cache, docs index, etc.)

### 3.5 Connection string summary

| Setting | Source | Default |
|---------|--------|---------|
| SQL host | `DB_HOST` env | `127.0.0.1` |
| SQL port | `DB_PORT` env | `14330` |
| Database | `clients/<name>.yaml` `db_name` | per client |
| User | hardcoded | `chatbot_ro` |
| Password | `work/ro_password.txt` | written by `03_apply_db_sql.py` |
| Tenant | `CompanyID` int per request | `SESSION_CONTEXT` |

Multi-client = multiple YAML files + multiple restored DBs on **one** SQL Server instance (pilot: `chatbot_db`, `chatbot_db2`).

---

## 4. Static widget vs full page

### 4.1 What exists

**Full-page chat app**, not an embeddable circle-button widget.

- `static/index.html` lines 10–24: header with title "مساعد بيانات Olives", token login bar, message area, bottom form.
- `static/style.css` lines 6–14: `max-width: 720px`, `height: 100vh` — centered standalone page.
- `static/app.js`: posts to **same-origin** `/ask` and `/feedback`; token in `sessionStorage` (lines 14–15, 75–78).
- `api/server.py` line 334: `app.mount("/", StaticFiles(..., html=True))` — FastAPI serves UI and API together.

**No:** iframe embed script, floating launcher button, `postMessage` bridge, or CORS config for cross-origin embed.

### 4.2 What IIS / wwwroot would need for user's intent

For a **circle-button widget on customer IIS sites** (separate from API host):

1. **Widget assets** in wwwroot: launcher button + panel JS/CSS (new work).
2. **API base URL** config pointing to chatbot service (not hardcoded `/ask`).
3. **CORS** on FastAPI if widget origin ≠ API origin.
4. **Bearer token** delivery: how end users get `OLIVES_TOKEN_*` without exposing in page source (likely server-side session or reverse-proxy injection).
5. **Optional:** static-only wwwroot + API on Linux/cloud; or full stack on Windows (see §7).

Current design assumes user opens `http://localhost:8100` (`run.sh` line 27) as a dedicated chat page.

---

## 5. Dependencies on parent `olives` repo

### 5.1 Hard imports (will break if moved without replacement)

| Dependency | Where | Path assumption |
|------------|-------|-----------------|
| **drift-tool** | `setup/01_db_up.py` lines 10–13 | `REPO_ROOT = parents[2]` → **`apps/`**; imports `apps/drift-tool/drift/{docker_mgmt,restore,config}` |
| **drift-tool** | `setup/02_introspect.py` lines 10–16 | Same `apps/drift-tool` |
| **drift-tool** | `setup/03_apply_db_sql.py` lines 20–27 | Same |
| **drift-tool** | `setup/refresh.py` lines 33–35 | `REPO_ROOT.parent / "drift-tool"` (= `apps/drift-tool`) |
| **`.bak` backup** | `setup/01_db_up.py` line 15 | `apps/drift-tool/reference-databases/morec_original.bak` |
| **Docker container** | `run.sh` line 10 | Shared `drift-tool-mssql` on port **14330** |
| **knowledge docs** | `setup/04_assemble_docs_corpus.py` lines 9–29 | `parents[3]` → **olives root**; symlinks to `knowledge/reference/`, `knowledge/back-office/`, `knowledge/front-office/`, `apps/support-agent/system_options_guide.md` |
| **support-agent** | `04_assemble` line 22 | `apps/support-agent/system_options_guide.md` |

**Path inconsistency:** `04_assemble_docs_corpus.py` uses `parents[3]` (olives root); other setup scripts use `parents[2]` (`apps/`). Both work today because `client-chatbot` lives at `apps/client-chatbot`.

### 5.2 Referenced but NOT imported at runtime

| Asset | Mentioned in | Runtime use |
|-------|--------------|-------------|
| `obsidian/olives/` vault | PLAN.md §1.5.D lines 134–135; FIXPLAN M11 | **Not wired** — docs use copied/symlinked markdown + FTS5 |
| `obsidian-mcp-server.py` | PLAN.md line 313 | **Not wired** |
| `db/vault_graph.json` | PLAN.md lines 124, 140 | **Rejected** — dirty graph; not used |
| `db/*.json` (tables, procs) | PLAN.md line 124 | Optional offline reference only; not in running pilot |
| `db/*.py` vault pipeline | PLAN.md line 140 | Separate concern |
| `Inventory-Master.csv` | PLAN.md line 123 | Not wired |
| `backup test/*.bak` | PLAN.md §1.5.C | Manual restore inputs only |
| `olives web pages/` (783 .aspx) | Bundled in tree | **Not referenced by Python** — 901 MB reference copy of ASP.NET UI |

### 5.3 Absolute paths

No `/media/alaa/data/olives` in **Python runtime** code. Absolute paths appear only in **PLAN.md** documentation (e.g. line 154).

### 5.4 MCP

- **sqlmcp/** — optional standalone MCP over `core/sql.py`; agent does **not** call it (FIXPLAN.md line 17: "direct pymssql, NOT an MCP").
- **`mcp` pip package** — only in `sqlmcp/Dockerfile` line 6; **not** in `requirements.txt`.
- **Vault MCP** — planned (TOOLS-REVIEW.md, PLAN Phase 10); **not implemented** in agent.

---

## 6. Tests / evals — breakage if extracted

### 6.1 Unit tests (`tests/`)

Most tests use `sys.path.insert(0, project_root)` only — **portable**.

**Integration-dependent (need live Docker MSSQL + setup):**

| Module | Requires |
|--------|----------|
| `test_tenant_wall.py` | `chatbot_db` + wall applied; `morec` fixture (lines 1–3) |
| `test_multi_client.py` | Both `morec` and `rukn` DBs |
| `test_params.py` | May use `work/` profile data |
| `test_catalog.py` | `work/morec/schema_cache.json` |

**Gateway-dependent (skip if down):**

- `test_gateway.py` lines 29–34: `pytest.skip` if gateway unreachable

**Mocked (portable):**

- `test_agent.py` — mocks `llm.complete` at boundary (lines 1–11)
- `test_docs.py` — synthetic corpus in `tmp_path` (lines 1–5)
- `test_auth.py`, `test_api.py`, `test_rate_limit.py`, `test_feedback.py`, `test_session_memory.py` — FastAPI TestClient + env

### 6.2 Evals (`evals/run_evals.py`)

**Fully live:** calls `agent.ask()` → real LLM gateway + real SQL Server + real `work/` caches.

| Corpus | Cases | Failure mode if extracted |
|--------|-------|---------------------------|
| `accuracy.jsonl` | 12 | Wrong DB contents → wrong counts (expects e.g. 33517 customers, line 2) |
| `docs_accuracy.jsonl` | 5 | Missing `docs_corpus/` + `work/<client>/docs.sqlite` → doc answers fail |
| `isolation.jsonl` | 11 | Needs both clients' DBs + docs index; **must be 100% blocked** |

Evals also **mutate** `work/cache.sqlite` (promote verified queries, line 69).

### 6.3 sqlmcp isolation test

`sqlmcp/run_isolation_test.sh` assumes `drift-tool-mssql` container and Docker networks — parent drift-tool coupling.

---

## 7. Gaps vs stated standalone / on-prem intent

| User intent | Current pilot reality |
|-------------|----------------------|
| **Circle-button embed on customer IIS wwwroot** | Full-page Arabic RTL chat; same host as API |
| **Docs from Obsidian vault via MCP** | Symlinked markdown from `knowledge/` + per-client FTS5 SQLite; no live vault |
| **Complex NL2SQL with joins via vault MCP** | Joins inferred by LLM from `introspect_schema` + `schema_cache.json`; vault graph unused; `procedure_match.py` unused |
| **Direct SQL Server on customer Windows IIS** | Linux Docker `drift-tool-mssql` :14330; pymssql from app host; ASP.NET pages in `olives web pages/` are **not** integrated |
| **Per-customer on-prem install** | Explicitly deferred (PLAN.md line 21); central multi-tenant service design |
| **Proc execution (`run_proc`)** | Removed from agent; no EXECUTE grants |
| **Claude primary + Redis** | Gemini primary per `litellm.config.yaml` lines 34–37; local cache only |

**Architecture contrast:**

```
CURRENT (pilot):
  Browser → FastAPI (:8100) → LiteLLM (:4000) → cloud LLM
           ↘ pymssql → Docker MSSQL (:14330) ← .bak via drift-tool

USER INTENT (standalone/on-prem):
  Customer IIS wwwroot (widget) → ??? → LLM
                               ↘ pymssql → Customer's native SQL Server (Windows)
  Vault MCP → schema/docs for NL2SQL
```

---

## 8. Files: MUST stay, MUST NOT copy, AGENTS.md guidance

### 8.1 MUST stay (source of truth)

```
api/server.py
core/*.py          (except consider dropping unused procedure_match.py)
gateway/litellm.config.yaml, gateway/README.md
db/*.sql, db/table_classification.md
prompts/system.md
static/*           (or replace with widget — but current UI is here)
clients/_example.yaml
setup/*.py
evals/*.jsonl, evals/run_evals.py
tests/*
requirements.txt
.env.example
.gitignore
README.md, PLAN.md, FIXPLAN.md  (historical context)
sqlmcp/*           (if external MCP consumers needed)
```

### 8.2 MUST NOT copy / commit

| Path | Reason |
|------|--------|
| `.env`, `gateway/.env` | Secrets: tokens, API keys, `MASTER_KEY` |
| `work/` | `cache.sqlite`, `ro_password.txt`, `trace.jsonl`, per-client caches — derived + sensitive |
| `docs_corpus/` | Gitignored symlinks to parent repo; regenerate via `04_assemble` |
| `clients/morec.yaml`, `clients/rukn.yaml` | Gitignored; contain deployment-specific `db_name`/aliases |
| `.pytest_cache/`, `__pycache__/`, `evals/__pycache__/` | Build artifacts |
| `prompts/.~lock.system.md#` | Editor lock file |
| `olives web pages/` | 901 MB ASP.NET reference; not runtime dependency |
| `gateway/litellm.log`, `work/litellm.log` | Logs |
| Parent `.bak` files | Multi-GB; reference by path or customer-provided backup |
| `db/vault_graph.json` (parent) | Explicitly rejected as schema source |

**Lock files:** `requirements.txt` has pinned versions — **keep** for reproducibility. No `poetry.lock`/`uv.lock` in tree.

### 8.3 Suggested `AGENTS.md` content (does not exist today)

An `AGENTS.md` for a standalone repo should state:

1. **Python 3.13 only** (`python3.13`, never `python3`) — PLAN.md rule 1, README line 16.
2. **Never put LLM API keys in `core/` or `api/`** — gateway only (`PLAN.md` rule 4).
3. **Tenant bearer tokens in `.env` only** — `clients/*.yaml` names `api_token_env`, never the value (`api/server.py` lines 49–57).
4. **The wall is server-side** — `t.` views + `SESSION_CONTEXT`; gate is defense-in-depth (`db/02_tenant_views.sql`, `core/sql.py`).
5. **One SQL implementation** — `core/sql.py` + `core/gate.py`; sqlmcp must call these, not bypass (`sqlmcp/sql_server.py` lines 1–16).
6. **Never return proc bodies** to users (`PLAN.md` rule 5).
7. **Cache keys include client + CompanyID** — exact match only (`core/memory.py` lines 74–79).
8. **Setup order:** `01_db_up` → `02_introspect` → `03_apply_db_sql` → `04_assemble_docs_corpus` → `05_index_docs` per client; `refresh.py` on schema change.
9. **Eval gate:** `python3.13 evals/run_evals.py` — isolation corpus must be 100% blocked.
10. **If extracting standalone:** vendor or reimplement `apps/drift-tool` Docker restore **or** replace with native Windows SQL connection; fix `04_assemble_docs_corpus.py` paths or vendor `knowledge/` corpus into the standalone repo.
11. **Do not edit `db/02_tenant_views.sql` casually** — FIXPLAN.md line 10–11.

---

## 9. Open questions for the human

1. **Deployment target:** Central hosted service (current) vs true per-customer Windows/IIS on-prem vs hybrid (widget on IIS, API elsewhere)?

2. **Widget UX:** Should the embed be a floating circle button + slide-out panel, iframe, or something matching existing Olives ASP.NET chrome?

3. **Docs source of truth:** Keep symlinked `knowledge/` markdown + FTS5, migrate to live Obsidian vault MCP, or ship a frozen corpus inside the standalone repo?

4. **Schema source for NL2SQL:** Stay on per-client live introspection (`schema_cache.json`), or invest in FIXPLAN M11 vault-universal schema (prerequisite: clean vault graph)?

5. **SQL Server hosting:** Continue Docker/`drift-tool` for dev only and connect to customer production SQL Server in deployment, or run SQL Server locally on each customer Windows box?

6. **`.bak` / restore workflow:** Will each customer provide their own `Olives_BO.bak`, or only live connection strings to an existing instance?

7. **LLM routing:** Restore Claude as primary (PLAN intent) vs keep Gemini/DeepSeek? Budget for paid keys on every deployment?

8. **Gateway placement:** Co-located with API on customer network, or shared central gateway (data leaves customer site)?

9. **`olives web pages/` (901 MB):** Include in standalone repo, drop, or replace with a link to customer's deployed Olives site for UI context?

10. **`procedure_match.py`:** Wire into agent, delete, or keep for future catalog-first routing?

11. **`run_proc` / EXECUTE grants:** Is Path A (audited allow-list + grants) required for production, or is generated SELECT-only SQL sufficient?

12. **Multi-company clients:** Any real client with `CompanyID` MULTI to validate session memory (`api/server.py` lines 156–173)?

13. **CORS / token issuance:** How should IIS-hosted pages obtain bearer tokens without exposing secrets in static HTML?

14. **Extract boundary:** Should standalone repo include a minimal vendored `drift-tool` subset, or declare SQL Server + corpus as external prerequisites?

15. **`database_mapping.md`:** Present in `docs_corpus/` on disk but excluded in `04_assemble_docs_corpus.py` lines 23–25 — intentional to keep out of end-user docs, or should it be indexed for staff/diagnostic questions?

---

## Appendix: Key file line references

| Topic | File:lines |
|-------|------------|
| Token auth | `api/server.py:44-86, 176-179` |
| SSE streaming | `api/server.py:188-236` |
| Agent tools | `core/agent.py:133-211` |
| Query budget | `core/agent.py:29-38, 550-609` |
| Docs search | `core/docs.py:213-244` |
| SQL + tenant | `core/sql.py:26-58` |
| Gate | `core/gate.py:34-50` |
| Tenant views SQL | `db/02_tenant_views.sql:4-9, 21-37` |
| Client YAML | `clients/_example.yaml:1-14` |
| Env template | `.env.example:1-13` |
| Gateway models | `gateway/litellm.config.yaml:33-45` |
| Drift-tool import | `setup/01_db_up.py:10-15` |
| Parent knowledge symlinks | `setup/04_assemble_docs_corpus.py:9-29` |
| Full-page UI | `static/index.html:10-24` |
| PLAN deferrals | `PLAN.md:20-21` |
| Vault not wired | `FIXPLAN.md:487-509` |
