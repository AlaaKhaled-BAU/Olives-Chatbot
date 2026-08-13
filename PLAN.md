# Client Chatbot — Pilot Implementation Plan (agent-executable)

> Builds the system in [PLAN-01-client-chatbot-poc.html](../PLAN-01-client-chatbot-poc.html), retargeted to **pilot tier** — between a bare MVP and full production. Tool choices: [TOOLS-REVIEW.md](TOOLS-REVIEW.md) (§ RECHECK, pilot tier).
> One central service on our servers. LLM via a **gateway** (key never touches app code). SQL Server in **Docker on Linux** by reusing the drift-tool. Read-only, multi-client by config, tenant-isolated server-side.
> Written for an agent to execute step by step. Reviewed with an eng lens; each phase has an acceptance gate.

---

## What "pilot tier" means (the bar every phase is held to)

**It IS (built here):**
- A real HTTP service (FastAPI + uvicorn) with `/health` and `/metrics`, not a script.
- **Key custody:** the API key lives only in the **gateway**, never in `core/` or logs.
- **Server-side tenant isolation:** the wall is a read-only login **plus tenant views / RLS** keyed on `SESSION_CONTEXT` — the engine enforces `CompanyID`, not a string check.
- **Memory + cache:** a SQLite module (verified queries, plan cache, result cache) and gateway response cache.
- **Structured tracing + metrics** from the first turn.
- **Multi-client by config** (`clients/*.yaml`), proven isolated across two live clients.
- **Accuracy AND isolation eval gates** that fail the build on a leak.

**It is NOT (deferred to production):**
- Full red-team hardening suite, per-user record-level permissions (pilot uses one read-only manager login — flagged), HA/redundant gateway, a secrets manager (an env file behind the gateway is acceptable for pilot), per-client on-prem installs, air-gapped / self-hosted-model tier, load/soak at scale.

The center does not change with the tier: **catalog-first proc execution + `sqlglot` gate + read-only login + server-side scoping.** Pilot adds *surrounding* machinery, not a new brain.

---

## 0. Golden rules (the executing agent reads these FIRST)

1. **Python = `python3.13`**, never `python3`.
2. **Reuse the drift-tool** for Docker + restore (`from drift import docker_mgmt, restore, config`). Do not rewrite it.
3. **The wall is server-side:** read-only login **+ tenant views/RLS**. The `sqlglot` gate is defense-in-depth, never the only check.
4. **The API key lives ONLY in `gateway/`.** Never in `core/`, `api/`, `.env` at the repo root after Phase 3, or any log line. `core/` reaches the LLM only through the gateway's `base_url`.
5. **Never write. Never EXEC a non-allow-listed proc. Never return a proc body to a user** (leaks other clients' `@ClientActive` branches).
6. **After query results enter the model context, make NO more tool calls.**
7. **Cache keys MUST include `client + CompanyID + role + model`.** A cache-key bug here is a tenant leak, not a stale answer. **Exact-match keys only — never semantic/embedding cache** (it confuses customer 4022 with 4023).
8. **Never translate schema names or data values.** Arabic literals get an `N'…'` prefix.
9. **One SQL implementation** (`core/sql.py` + `core/gate.py`), shared by the agent and the MCP.
10. **This box OOMs.** Summarize introspection, cap rows, stream.
11. **Commit per phase**, each green on its acceptance gate. Branch `feature/chatbot-pilot`.

---

## 1. Folder structure (create exactly this under `olives/client-chatbot/`)

```
client-chatbot/
├── PLAN.md  README.md  RESEARCH-RAW.md  TOOLS-REVIEW.md
├── requirements.txt          # fastapi, uvicorn, anthropic-or-openai(gateway client), sqlglot, pyyaml, prometheus-client
├── .env.example              # non-secret defaults (GATEWAY_URL, DB host/port/name); NO key
├── .gitignore                # .env  work/  __pycache__/  docs_corpus/
├── clients/                  # MULTI-CLIENT BY CONFIG
│   ├── _example.yaml         # template: db, company_scope, catalog, locale
│   └── morec.yaml            # the first real pilot client
├── core/                     # THE BRAIN — no API key, no direct LLM network
│   ├── config.py             # env + per-client YAML loader
│   ├── schema.py             # live introspection + on-disk cache (built at setup as SA)
│   ├── catalog.py            # per-client proc catalog: entitlement + confidentiality filter
│   ├── gate.py               # sqlglot safety gate
│   ├── sql.py                # pymssql read-only exec; sets SESSION_CONTEXT tenant; row cap + timeout
│   ├── params.py             # resolution order + multi-value guard + profile
│   ├── memory.py             # SQLite: verified queries + plan cache + result cache
│   ├── llm.py                # thin client → gateway base_url (NO key)
│   ├── trace.py              # structured JSONL + Prometheus counters
│   └── agent.py              # the loop
├── api/
│   └── server.py             # FastAPI: POST /ask (SSE), GET /health, GET /metrics; serves static/
├── gateway/                  # KEY LIVES ONLY HERE
│   ├── README.md             # run LiteLLM (preferred) or OmniRoute; Claude primary + fallback
│   ├── litellm.config.yaml   # Claude primary, Gemini fallback, Redis cache
│   └── .env.example          # LLM_API_KEY=  (the ONLY place the key goes)
├── db/
│   ├── 01_readonly_login.sql # db_datareader login (the app login)
│   └── 02_tenant_views.sql   # SESSION_CONTEXT tenant scoping / RLS (the wall)
├── prompts/
│   ├── system.md             # schema rules, resolution order, Arabic rule, no-proc-bodies
│   └── verified_queries.seed.jsonl  # procedural-memory seed (question -> proc/SQL)
├── static/                   # chat UI, Arabic RTL, streaming  (served by FastAPI)
│   ├── index.html  app.js  style.css
├── setup/
│   ├── 01_db_up.py           # reuse drift-tool: docker + restore .bak
│   ├── 02_introspect.py      # build schema cache + param profiles + catalog (as SA)
│   └── 03_apply_db_sql.py    # apply 01_readonly_login.sql + 02_tenant_views.sql (as SA)
├── evals/
│   ├── accuracy.jsonl        # known-answer Qs, >=30% Arabic, incl the 2 use cases
│   ├── isolation.jsonl       # cross-client leak / tenant-bypass / client-named-proc corpus
│   └── run_evals.py          # runs both; exits non-zero if ANY isolation case leaks
├── tests/
│   ├── test_gate.py          # red-team-lite
│   └── test_params.py        # resolution order + multi-value guard
├── docs_corpus/              # MinerU output (markdown from the PDF/DOCX guides)  [gitignored]
└── work/                     # gitignored: cache.sqlite, profiles, traces, schema_cache.json
```

Layout logic: `core/` is a pure library (no key, no web server); `api/` exposes it; `gateway/` isolates the secret; `db/` holds the server-side wall; `clients/` makes it multi-tenant by config. One SQL implementation, one brain.

---

## 1.5 · Repo inventory — what already exists in `olives/` and where it goes

A name-first pass over the whole `olives/` tree, opening a file only when its name didn't say enough. Two names lied: `Inventory-Master.csv` sounds like business data but is actually a DB object catalog; `procedures.md` sounds like documentation but is raw proc bodies. Listed here so nothing gets moved on a guess. **Move timing is the user's call** — this only says what's relevant and why.

### A. Docs-corpus material (feeds Phase 10's `docs_corpus/` and `prompts/system.md`)

| Path | What it actually is | Note |
|---|---|---|
| `OLIVES USER GUIDE_2021Updated2025.md` (206K) | Full user guide, **already converted** from the 50.6MB PDF | MinerU not needed for this one — a markdown version already exists. Keep the PDF only as a citation/fallback source. |
| `Olives SQL_Documentation.md` (710K) | Full SQL doc, **already converted** from the 1.6MB DOCX | Same — already converted, MinerU not needed here either. |
| `tables summary.md` (15.5K) | Clean, curated **OSFA ↔ Olives_BO table-mapping** doc (verified by reading it) | Directly documents the "BO = source of truth, OSFA/OT_ = replica" rule the system prompt needs. |
| `support-agent/system_options_guide.md` (47.9K) | OP_ID 1–754 reference (system options) | Prefer this one — it's the larger of two near-duplicates (see below). |
| `system option explained.md` (41.2K, top level) | Same OP_ID table, smaller | Verified by reading — same shape (`OP_ID\|OP_Desc\|Notes`) as the support-agent version. Likely an earlier/partial export. Keep as a cross-check, don't ingest both as if independent. |
| `support-agent/database_mapping.md` (50.0K) | Table schemas + ready diagnostic SQL queries | Direct input to `prompts/system.md`'s schema-conventions section. |
| `back-office/*.md` (15 files) | Per-topic BO feature docs: `promotions`, `transactions`, `routes`, `work_flow`, `users_permissions`, `salespersons`, `customers`, `reports`, `dashboards`, `settings`, `items`, `delivery`, `agreements`, `competitive_items`, `intro` | Business-process "how do I do X" layer — complements the vault (which covers schema/procs, not user workflow). Likely the topic-split source the USER GUIDE was drawn from (not confirmed, not diffed). |
| `front-office/*.md` (16 files) | Same, for OSFA (the Android tablet app): `add_customer`, `view_customers`, `transaction_list`, `upload_order`, `unload_order`, `collect_gps`, `salesman_reports`, `data_updates`, `settings`, etc. | Same value as back-office/, for the field-salesman side. |

**Checked and excluded from docs-corpus (name suggested docs, content didn't hold up):**
- `procedures.md` (769K, top level) — opened it: first lines are bare T-SQL (`AS` on its own line). This is a **raw dump of procedure bodies**, not prose. Wrong shape for a docs corpus, and returning proc bodies to users is already banned (§0 rule 5) — this file shouldn't feed anything user-facing.
- `db/bo_procedures_A.md` … `_E.md`, `db/bo_tables.md`, `db/osfa_procedures.md`, `db/osfa_tables.md` — flat markdown bundles of the same per-object content already in the Obsidian vault, just chunked differently. Redundant with the vault; skip rather than ingest a second, divergent copy.

### B. Schema/catalog seed material (cross-check input for `core/schema.py` / `core/catalog.py` — NOT a replacement for live introspection, which is the design choice)

| Path | What it actually is | Note |
|---|---|---|
| `Inventory-Master.csv` (top level, 8,472 rows) | **Misleading name.** Opened it: columns are `object_type, database, schema, name, parent_object, column_name, data_type, nullable, is_pk, is_fk, fk_ref_table, fk_ref_column, procedure_params, procedure_tables_read, procedure_tables_write, estimated_size, business_purpose, status` — a full column-grain inventory of every table and procedure across both DBs. | Genuinely useful, previously unlisted. A single flat file is far cheaper to seed `core/catalog.py` from than parsing ~1,900 separate vault notes. **Caveat:** spot-checked rows had `business_purpose` blank (a basic table) — check real fill-rate before depending on that column for catalog descriptions. |
| `db/tables.json` (1.5M), `db/procs_csv.json` (860K), `db/procs_sql.json` (679K), `db/name_index.json` (469K) | Structured JSON exports of the same schema | Optional offline fallback only. The plan's whole point is **live introspection to avoid drift** (this is the same staleness problem that got `vault_graph.json` rejected) — don't wire these into the running pilot; at most, useful for writing prompts by hand without a DB connection open. |
| `db/OSFA_DB.sql`, `db/Olives_BO.sql` (+ `*6-8-2026.sql` dated pair, 115–190MB each) | Raw DDL dumps (structure + proc bodies) of the master/105 image | Same as above — optional offline reference only, not part of the running pilot. |

### C. Relevant later, not blocking (named so they aren't lost, not needed for Phases 0–9)

- **`backup test/105/olives_bo.bak` + `osfa.bak`** (the master/105 pair, ~1.2–1.6GB each) — useful once the plan builds the "drift overlay" idea from the architecture doc (flag an answer as lower-confidence when the client's proc has diverged from 105). Not needed to run the pilot.
- **`backup test/morec/Olives_BO.bak`** — byte-identical in size to `drift-tool/reference-databases/morec_original.bak`; it's the same file, already relocated there. Nothing to do here — don't re-import a second copy.

### D. Do NOT move (would break something already working)

- **`obsidian/olives/`** (the live vault) and **`obsidian-mcp-server.py`** — the MCP server hardcodes `VAULT = "/media/alaa/data/olives/obsidian/olives"` and `GRAPH_PATH = "/media/alaa/data/olives/db/vault_graph.json"`. Moving either breaks the currently-running docs MCP. Reference it in place (as the plan already does); don't relocate it under `client-chatbot/`.
- **`drift-tool/reference-databases/morec_original.bak`** — shared with the drift-tool's own validation suite. The plan already imports it by relative path (`setup/01_db_up.py`); moving it duplicates a multi-GB file and risks breaking drift-tool's tests. Leave in place, reference only.

### E. Checked and not relevant to this project

- **`Olives.rar`** (648MB) — listed its contents (no extraction): it's the actual .NET web app source (`Account/Login.aspx`, `App_GlobalResources/*.resx`, JS chart libs). This is application source code; the chatbot is a read-only DB consumer and doesn't touch or need app code.
- **`db/*.py`** (`bulk_edit.py`, `csv_to_graph.py`, `merge_graph.py`, `normalize_frontmatter.py`, `parse_osfa_writes_to.py`, `regenerate_body.py`, `sql_to_deps.py`, `update_osfa_vault.py`) and **`db/vault_graph.json`** — the vault/graph regeneration pipeline. A separate, already-tracked concern (see `TODOS.md`), and `vault_graph.json` was already rejected earlier in this project for being dirty (callers/callees swapped, junk tokens). Not chatbot code.
- **`support-agent/AGENT.md`, `orchestrator.md`, `workflow_guide.md`, `diagram.md`, `tickets/`** — these belong to the *other* platform idea (the technical support assistant), not this client chatbot.
- **`support-agent/Salah AlBakri.zip` + `support-agent/AlBakri/`** (1.9GB) — opened the listing: a specific client support engagement bundle — live `Olives_BO.bak`/`OSFA_DB.bak`/image/log backups, a "Fix Config File" folder, and installer EXEs (AnyDesk, Chrome, WinRAR). This is a support technician's case file, not project source material — flagging only because it's live client backups + remote-access tooling sitting in a project folder, not because it needs any action from this plan.
- **`backup test/morec/Osfa_DB.bak`** — the client's OSFA_DB (sync replica) backup; the plan already treats OSFA_DB as non-authoritative and never queries it for real answers.
- **`obsidian-vault/`** and **`obsidian/olives.BAK.20260714-005041/`** — a secondary mirror (no `.obsidian` config, so not the live one) and a dated snapshot backup of the vault. Redundant with `obsidian/olives/`; no separate action needed.
- **`route-optimizer-app/`, `test-db/`** — confirmed by content (Tauri app, `route_optimizer.py`, `visits.csv`) to be a separate, unrelated project (per-route TSP optimizer). Not part of this system.
- **`ROUTING_TABLE.md`** — a meta-index of *this coding repo's* own file/route structure for `codebase-memory-mcp`, not Olives business content.

---

## PHASE 0 — Manual setup (YOU; the agent cannot). 3 items.

1. **API key** → **`cp gateway/.env.example gateway/.env`** and paste `LLM_API_KEY=...`. The key goes **only** here. (For quick Phase 1–2 testing before the gateway exists, a root `.env` may hold it temporarily; **Phase 3 moves it behind the gateway and deletes it from root**.)
2. **Docker** works without sudo: `docker ps` prints a table.
3. **Approve the pilot client(s):** default `drift-tool/reference-databases/morec_original.bak` (client "morec") restored **locally**. Reply "ok" or name another `.bak` under `/media/alaa/data`.

Acceptance: `gateway/.env` has a key; `docker ps` clean.

---

## PHASE 1 — Database up + introspection (reuse the drift-tool)

**This is how SQL Server runs on Linux:** the drift-tool's container `drift-tool-mssql` (image `mcr.microsoft.com/mssql/server:2022-latest`, host port `14330`). Reuse it.

- `setup/01_db_up.py`: `from drift import docker_mgmt, restore` → `docker_mgmt.ensure_running(log)` → `restore.restore_backup(Path(".../morec_original.bak"), "chatbot_db", log)`.
- `setup/02_introspect.py` (runs as **SA** — metadata read): build `work/schema_cache.json` (tables+cols, procs+params from `INFORMATION_SCHEMA` + `sys.parameters` + `sys.sql_expression_dependencies`), discover the per-client param profile (§Phase 5), and build the per-client catalog (§Phase 4). Summaries only.

**Acceptance:**
- `docker ps` shows `drift-tool-mssql`; SA `SELECT @@VERSION` returns SQL 2022.
- `SELECT COUNT(*) FROM chatbot_db..Companies` > 0; record `SELECT DISTINCT CompanyID FROM Companies` count.
- `SELECT ClientID FROM ClientsActive` returns the ClientActive value (missing → mark "ask", don't crash).
- `work/schema_cache.json` written.

---

## PHASE 2 — The wall: read-only login + tenant views (server-side)

- `db/01_readonly_login.sql` (run as SA): `CREATE LOGIN chatbot_ro` + user + `db_datareader`. No writer, no ddl. Random password → `work/ro_password.txt` (gitignored).
- `db/02_tenant_views.sql`: enforce `CompanyID` in the engine, not in Python. Pilot approach: **`SESSION_CONTEXT`-scoped tenant views** — a schema `t.` whose views read `WHERE CompanyID = CONVERT(int, SESSION_CONTEXT(N'CompanyID'))`; grant `chatbot_ro` SELECT on `t.` views only, not base tables. (If the edition/time allows true RLS security policies, use those; views are the pilot-simple equivalent.)
- `core/sql.py` sets the tenant on every connection: `EXEC sp_set_session_context 'CompanyID', @id` before any query.

**Acceptance (the isolation proof):**
- As `chatbot_ro`, a query through a `t.` view with `SESSION_CONTEXT CompanyID=1` returns only company 1's rows.
- Setting `CompanyID=2` returns only company 2's rows. No session context → zero rows (fail closed).
- `INSERT` fails (permission). Direct base-table `SELECT` denied (only `t.` views granted).

---

## PHASE 3 — Gateway + key custody  ← the key moves behind the gateway here

Stand up a local **LiteLLM** proxy (preferred; mature, Python, self-hosted, OpenAI-compatible). OmniRoute is the alternative if you want its compression/free-tier extras. Either way: **Claude pinned as primary, a fallback model only on outage, Redis cache.**

> **"Gateway" ≠ "free-tier routing."** The gateway exists for key custody + outage failover, not to cut cost by routing through free-tier model pools (freellmapi, or OmniRoute's own Tier-4 free models). Real client DB rows flow into the model's context to format every answer — sending that through ~30 barely-vetted free backends is a confidentiality leak, not a savings. Drift-tool's own validation already proved this class of model unreliable here (free Qwen rate-limited; Nemotron leaked chain-of-thought before the JSON, twice). Free tier is fine for dev/test traffic that touches zero real data; never in the path where a query result becomes model context. See [TOOLS-REVIEW.md](TOOLS-REVIEW.md) (§10/11) for the full argument.

- `gateway/litellm.config.yaml`:
  ```yaml
  model_list:
    - model_name: chatbot            # the only name core/ knows
      litellm_params: { model: claude-sonnet-5, api_key: os.environ/LLM_API_KEY }
    - model_name: chatbot            # fallback, same alias
      litellm_params: { model: gemini/gemini-2.5-flash, api_key: os.environ/GEMINI_KEY }
  router_settings: { fallbacks: [{ chatbot: ["chatbot"] }], num_retries: 2 }
  litellm_settings: { cache: true, cache_params: { type: redis } }
  ```
- Run: `litellm --config gateway/litellm.config.yaml --port 4000` (Redis via `docker run -p 6379:6379 redis` or LiteLLM in-memory for pilot).
- `core/llm.py`: OpenAI-compatible client pointed at `http://localhost:4000`, model `"chatbot"`, **no key**. Delete the key from any root `.env`.

**Acceptance:**
- `grep -ri "sk-\|api_key\|LLM_API_KEY" core/ api/` → nothing (key only in `gateway/`).
- A `core/llm.py` call returns a completion via the gateway.
- Stop the primary (bad key sim) → the fallback answers (prove failover).
- Two identical calls → the second is a cache hit (check gateway logs).

---

## PHASE 4 — Core SQL + gate + catalog (+ tests)

- `core/gate.py` `validate(sql)->str`: `sqlglot` tsql parse; allow one `SELECT` or allow-listed `EXEC`; reject INSERT/UPDATE/DELETE/DDL, `SELECT…INTO`, `OPENROWSET/OPENQUERY`, multi-statement, `xp_`/`sp_OA*`; inject `TOP(n)`; `N'…'`-prefix Arabic literals; raise `GateError(reason)`.
- `core/sql.py`: `get_conn()` (chatbot_ro, port 14330, UTF-8), `set_tenant(conn, company_id)` (SESSION_CONTEXT), `run_select(sql, company_id)` (gate → set tenant → execute via `t.` views → row cap + timeout), `run_proc(name, args, company_id)` (allow-list only).
- `core/catalog.py`: per-client proc catalog from the schema cache, with the **confidentiality filter** — exclude client-named procs (`*_Sokhtian`, `*_Jebrene`, …) and any proc not entitled to this client. Deny-by-default.
- `tests/test_gate.py`: rejects the bad corpus, allows a clean SELECT + `TOP`, N-prefixes Arabic.

**Acceptance:** `python3.13 -m pytest tests/test_gate.py -q` green; `catalog.for_client('morec')` excludes other clients' named procs (paste the excluded count).

---

## PHASE 5 — Params + memory + cache (SQLite)

- `core/params.py`: `discover_profile()` (distinct-count `CompanyID` → value or `MULTI`; `ClientActive` from `ClientsActive` → static; guard: never store static until distinct-count proves single); `resolve(param, conversation)` → (1) conversation, (2) profile if single, (3) `NEEDS_ASK`.
- `core/memory.py` — one SQLite file `work/cache.sqlite`, three tables:
  - `verified_queries(client, question_norm, proc_or_sql, ok_count)` — procedural memory; retrieved as few-shots by normalized question.
  - `plan_cache(key, plan)` — `key = hash(client, CompanyID, role, model, question_norm)`; **exact match only**.
  - `result_cache(key, rows, ts)` — closed-period questions only, short TTL.
- `tests/test_params.py`: multi-value guard; resolution order; **cache-key isolation** (same question, different client → different key, no bleed).

**Acceptance:** `pytest tests/test_params.py -q` green; a verified query feeds a few-shot; the cache-key isolation test passes.

---

## PHASE 6 — Agent loop

`core/agent.py`: load `prompts/system.md`; tools = `introspect_schema`, `run_select`, `run_proc`, `ask_user`; loop: user msg → check `verified_queries`/`plan_cache` → pick a catalog proc or generate SQL → `gate` + `run_select` (tenant set from resolved `CompanyID`) → results to model → **format only, no more tools** → Arabic/English (schema names verbatim) → write `core/trace.py` line + bump counters → on success, upsert `verified_queries`.

`prompts/system.md` includes: BO vs OSFA/OT_ rules, CompanyID scoping, case-insensitive table lookup, catalog-first-then-generate, the resolution order, the Arabic rule, no-proc-bodies, and the "I can't answer confidently" fallback.

**Acceptance (as CLI `python3.13 -m core.agent --client morec "…"`):**
- "كم عدد الشركات؟" → correct count, Arabic answer, schema names in English.
- Use case 1 (salesman permissions, `SalesPersons`→`SalesPersonsDevicePermissions`) and 2 (best-seller per pricelist) → correct.
- `CompanyID` MULTI → asks which; single → doesn't ask.
- Unanswerable → refuses, no fabricated number. Trace written.

---

## PHASE 7 — API service + UI (FastAPI, uvicorn)

`api/server.py`:
- `POST /ask` → SSE stream of the agent's answer (body: `{client, question, session_id}`).
- `GET /health` → pings DB (`SELECT 1`) + gateway; returns `{db, gateway, ok}`.
- `GET /metrics` → Prometheus (`prometheus-client`): request count, latency histogram, cache-hit ratio, gate rejections, refusals, per-client counters.
- serves `static/` (Arabic RTL, streamed answers).

Run: `uvicorn api.server:app --host 0.0.0.0 --port 8000`.

**Acceptance:** `/health` returns ok; `/metrics` counters increment after a request; a browser question streams a correct Arabic RTL answer.

---

## PHASE 8 — Evals: accuracy AND isolation (the release gate)

- `evals/accuracy.jsonl` — known-answer questions, ≥30% Arabic, both use cases, some "should refuse".
- `evals/isolation.jsonl` — the security corpus: a client-A session asking for client-B data; `OR 1=1`; wrong-alias predicate; predicate only true after a join; a request that would hit a client-named proc. **Every one must be blocked server-side** (tenant views + gate + catalog), not by the model's goodwill.
- `evals/run_evals.py` — runs both; prints accuracy %; **exits non-zero if ANY isolation case leaks** (wire into a pre-deploy check).

**Acceptance:** accuracy number printed; **isolation corpus 100% blocked** (a single leak fails the build).

---

## PHASE 9 — Multi-client by config (prove isolation across two live clients)

- `clients/morec.yaml` + a second client config (restore a second `.bak` as `chatbot_db2`, or a second CompanyID scope).
- `core/config.load_client(name)` selects DB + company scope + catalog + locale.
- Run the service against both; a client-A request can **never** return client-B data, and each client's catalog differs.

**Acceptance:** cross-client probe from `evals/isolation.jsonl` returns only own-client data for both; catalogs differ per client.

---

## PHASE 10 — (parallel, optional) Docs corpus + Metabase eval

- **Assemble `docs_corpus/` from what already exists** (see §1.5.A — most of this needs no conversion): `OLIVES USER GUIDE_2021Updated2025.md`, `Olives SQL_Documentation.md`, `tables summary.md`, `support-agent/system_options_guide.md`, `support-agent/database_mapping.md`, all of `back-office/*.md` and `front-office/*.md`. Copy or symlink into `docs_corpus/`.
- **MinerU** is now a smaller job than originally scoped: only needed to (a) re-extract the two big files if the existing `.md` conversions prove lossy on spot-check, or (b) handle any future PDF/DOCX-only doc that has no `.md` sibling yet. Not a blocking step given the conversions already exist.
- Feed the assembled corpus into the docs path (vault MCP now; **wire qmd** if regex retrieval proves weak). *Acceptance:* a docs question ("why is a salesman blocked?") is answerable from the assembled corpus.
- **Metabase**: evaluate self-hosted Metabase (SQL Server driver) as the **reports/dashboard/push** surface — scheduled reports + permission-gated dashboards — a **parallel delivery layer**, not the chat brain. *Acceptance:* a go/no-go note recorded (does its proc/permission model fit, or do we hand-build the push channel?).

---

## Files & folders checklist (everything needed to run)

| Path | Purpose | Phase |
|---|---|---|
| `setup/01_db_up.py` | SQL Server + restore (reuse drift-tool) | 1 |
| `setup/02_introspect.py`, `work/schema_cache.json` | schema + profile + catalog (as SA) | 1 |
| `db/01_readonly_login.sql`, `db/02_tenant_views.sql` | the server-side wall | 2 |
| `gateway/` (litellm.config.yaml, .env, README) | LLM gateway + key custody | 3 |
| `core/gate.py`, `core/sql.py`, `core/catalog.py`, `tests/test_gate.py` | SQL layer + gate + confidentiality | 4 |
| `core/params.py`, `core/memory.py`, `tests/test_params.py` | resolution + memory + cache | 5 |
| `core/agent.py`, `core/llm.py`, `core/trace.py`, `prompts/` | the loop + tracing | 6 |
| `api/server.py`, `static/` | FastAPI service + UI | 7 |
| `evals/` | accuracy + isolation gate | 8 |
| `clients/*.yaml`, `core/config.py` | multi-client | 9 |
| `docs_corpus/` (MinerU) | docs enrichment | 10 |
| `requirements.txt`, `.env.example`, `.gitignore`, `work/` | deps, config, runtime | 1 |

Reused, not rebuilt: `../drift-tool/drift/{docker_mgmt,restore,config}.py`, `../obsidian-mcp-server.py` (docs path + MCP boilerplate), `../drift-tool/reference-databases/morec_original.bak`.

---

## Eng-review notes folded in (must-not-skip)

- **Cache-key = tenant boundary.** Include `client + CompanyID + role + model`; exact-match only. Test it (Phase 5). A semantic cache is banned here.
- **Tenant views are the wall; the gate is defense-in-depth.** Both required. Fail closed with no session context.
- **Key custody:** grep `core/`/`api/` for secrets in CI; the key lives only in `gateway/`.
- **RCSI** on any real client before prod-read (pilot restores a private copy, so not blocking here).
- **Arabic:** `charset="UTF-8"`, `NVARCHAR`, `N'…'` — a missing `N` returns zero rows silently.
- **Gateway single point of failure:** health-check it; fallback model is the mitigation; `/health` surfaces it.
- **OOM:** summarize introspection, cap rows, stream.
- **Deferred to production (named, not forgotten):** full red-team suite, per-user record permissions (pilot = manager login), HA gateway, secrets manager, per-client on-prem, air-gapped tier, load/soak.

---

## Commit sequence

`P1 db+introspect` → `P2 wall` → `P3 gateway` → `P4 gate+sql+catalog` → `P5 params+memory` → `P6 agent` → `P7 api+ui` → `P8 evals` → `P9 multi-client` → `P10 docs+metabase`. One commit per phase, green on its acceptance gate before the next.
