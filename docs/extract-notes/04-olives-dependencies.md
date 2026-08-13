# Olives-root dependencies for a standalone `client-chatbot` repo

> Inventory date: 2026-08-13. Source: `README.md`, `apps/client-chatbot/{PLAN,FIXPLAN,README}.md`, setup-script imports, `core/docs.py`, `obsidian-mcp-server.py`, `sqlmcp/`, and `git ls-files` across the monorepo.

## Executive summary

The **running pilot** (`uvicorn api.server:app` + `gateway/` + `core/*`) is largely self-contained under `apps/client-chatbot/`. What still reaches outside that folder today is:

1. **Setup/bootstrap** — `apps/drift-tool/drift/{docker_mgmt,restore,config}.py` and a `.bak` restore file (gitignored).
2. **Docs corpus assembly** — `knowledge/{reference,back-office,front-office}/` plus one file from `apps/support-agent/`.
3. **Shared Docker infra** — container name `drift-tool-mssql` on host port `14330` (owned by drift-tool config).
4. **Future / not wired** — Obsidian vault + `obsidian-mcp-server.py` + `db/vault_graph.json` (editor/agent MCP path; the shipped agent uses `core/docs.py` FTS over `docs_corpus/` instead).

A standalone repo must either **vendor/copy** (1)–(2), **submodule** drift-tool, or **rewrite paths** in setup scripts. The vault/MCP stack can stay in olives unless you adopt FIXPLAN M11 (vault-as-universal-schema).

---

## Path-resolution trap (fix on extract)

Setup scripts disagree on what “repo root” means:

| Script | `REPO_ROOT` resolves to | Expects sibling |
|--------|-------------------------|-----------------|
| `setup/01_db_up.py`, `02_introspect.py`, `03_apply_db_sql.py`, `05_index_docs.py` | `apps/` (`parents[2]`) | `drift-tool/`, `client-chatbot/` under `apps/` |
| `setup/04_assemble_docs_corpus.py` | olives root (`parents[3]`) | `knowledge/`, `apps/support-agent/`, `apps/client-chatbot/` |
| `setup/refresh.py` | `apps/client-chatbot/` (`parent.parent`) | `../drift-tool/` |

`obsidian-mcp-server.py` hardcodes absolute paths:

```python
VAULT = "/media/alaa/data/olives/obsidian/olives"
GRAPH_PATH = "/media/alaa/data/olives/db/vault_graph.json"
```

`apps/drift-tool/drift/config.py` hardcodes `BACKUP_BROWSE_ROOT = Path("/media/alaa/data")` and `REPO_ROOT = olives/`.

Any extraction must normalize these to env vars (e.g. `OLIVES_ROOT`, `DRIFT_TOOL_ROOT`, `BACKUP_BROWSE_ROOT`) or a single `REPO_ROOT` inside the new repo layout.

---

## Asset table

| Asset | Path | Needed in standalone? | Why | Copy vs submodule vs leave-path |
|-------|------|----------------------|-----|----------------------------------|
| **client-chatbot app tree** | `/media/alaa/data/olives/apps/client-chatbot/` (api, core, static, tests, evals, db/*.sql, clients, requirements.txt, gateway, prompts, sqlmcp, setup, PLAN*.md) | **Yes** | The product. 65 paths tracked in olives git; runtime is self-contained under `BASE_DIR = core/..`. | **Copy** (or `git filter-repo` subtree). Fix setup `REPO_ROOT` while moving. |
| **drift-tool (Python package)** | `/media/alaa/data/olives/apps/drift-tool/drift/{docker_mgmt,restore,config}.py` (+ `drift/__init__.py`) | **Yes** (setup/dev) | `setup/01_db_up.py` imports `docker_mgmt`, `restore`, `config`. `02/03/refresh` import `drift.config` for SA creds + port 14330. API runtime does **not** import drift. | **Submodule** at `vendor/drift-tool` (keeps parity with olives) **or copy** minimal 3-module slice. Do not reimplement (PLAN golden rule 2). |
| **drift-tool (full app)** | `/media/alaa/data/olives/apps/drift-tool/` (Flask UI, compare pipeline, tests, desktop) | **No** (for chatbot runtime) | Only the three modules above are imported. Full tool is a separate product (PLAN-03). | **Leave in olives** unless you want one “platform” monorepo. Optional **submodule** for developers who run drift UI alongside chatbot. |
| **Reference `.bak` (default test DB)** | `/media/alaa/data/olives/apps/drift-tool/reference-databases/morec_original.bak` (documented; `*.bak` gitignored — not present on disk in this workspace) | **Yes** (local dev/evals) | `setup/01_db_up.py` default `--bak` points here. Shared with drift-tool validation suite (PLAN §1.5). Multi-GB; never in git. | **Leave on disk outside git** — document `CHATBOT_TEST_BAK` env var. Same file can be referenced from `data/db-snapshots/` (`/media/alaa/data/olives/data/`, gitignored). Do **not** duplicate inside standalone repo. |
| **Other reference `.bak` files** | e.g. `morec_surgical_v2.bak`, client backups under `/media/alaa/data/olives/data/client-archives/`, `/data/db-snapshots/` | **No** (chatbot) / **Yes** (drift-tool QA) | Drift-tool surgical battery only. Chatbot pilot needs one restoreable client image. | **Leave-path** under `data/` or host backup tree; widen `BACKUP_BROWSE_ROOT` in drift `config.py` if needed. |
| **Shared SQL Server container** | Docker name `drift-tool-mssql`, image `mcr.microsoft.com/mssql/server:2022-latest`, host `127.0.0.1:14330` | **Yes** (local dev) | `run.sh`, `sqlmcp/run_isolation_test.sh`, all setup scripts assume this container. Password in `apps/drift-tool/work/.mssql_pw` (gitignored). | **Leave shared** if both repos on same machine; **document** container name/port in standalone README. Standalone could rename container only after forking drift `config.CONTAINER_NAME`. |
| **knowledge/reference/** (3 guides) | `/media/alaa/data/olives/knowledge/reference/OLIVES USER GUIDE_2021Updated2025.md`, `Olives SQL_Documentation.md`, `tables summary.md` | **Yes** | `setup/04_assemble_docs_corpus.py` symlinks these into `docs_corpus/`. `core/docs.py` indexes them via FTS. | **Copy** into standalone `docs/source/reference/` (preferred — breaks symlink dependency) **or submodule** olives `knowledge/` **or leave-path** with `OLIVES_ROOT` env (fragile). |
| **knowledge/back-office/** | `/media/alaa/data/olives/knowledge/back-office/*.md` (15 files) | **Yes** | Same assembly path; primary “how do I do X” user docs. | **Copy** with reference docs (2.2M total for all `knowledge/`). |
| **knowledge/front-office/** | `/media/alaa/data/olives/knowledge/front-office/*.md` (16 files) | **Yes** | Same. | **Copy** with back-office. |
| **support-agent/system_options_guide.md** | `/media/alaa/data/olives/apps/support-agent/system_options_guide.md` | **Yes** | Only support-agent file wired into `04_assemble_docs_corpus.py` (754 system options; chunked headings for FTS). | **Copy** one file into `docs/source/` (or vendor `support-agent/docs/` slice). |
| **support-agent (rest)** | `/media/alaa/data/olives/apps/support-agent/{AGENT,orchestrator,workflow_guide,tickets,...}` | **No** | PLAN §1.5: belongs to Plan-02 support assistant, not client chatbot. `database_mapping.md` was considered but excluded from corpus (staff runbook). | **Leave in olives** |
| **knowledge/reference (excluded)** | `procedures.md`, `system option explained.md`, `ROUTING_TABLE.md` | **No** (runtime) | Not in `04_assemble` mapping. `procedures.md` = raw proc bodies (golden rule 5). `system option explained.md` duplicate of system_options_guide. | **Leave**; optional copy for human authors only. |
| **docs_corpus/** | `/media/alaa/data/olives/apps/client-chatbot/docs_corpus/` (gitignored) | **Yes** (derived) | Symlinked view assembled by `04_assemble_docs_corpus.py`; indexed to `work/<client>/docs.sqlite` by `05_index_docs.py`. `core/docs.search()` reads the sqlite index, not symlinks directly at query time. | **Regenerate** in standalone after copying sources (`python3.13 setup/04_assemble_docs_corpus.py` then `05_index_docs.py`). Do not treat as source of truth. |
| **Obsidian vault (live)** | `/media/alaa/data/olives/obsidian/olives/` (~2,600 notes, 12M tracked) | **No** (current pilot) | Shipped agent uses `search_docs` → `core/docs.py` FTS, not vault MCP. FIXPLAN M11 (future) would use vault for schema structure. PLAN-04 §8: blocked on vault/graph cleanup. | **Leave in olives**; reference via MCP config if/when needed. Optional **submodule** only if standalone operators need vault offline. |
| **obsidian-mcp-server.py** | `/media/alaa/data/olives/obsidian-mcp-server.py` | **No** (current pilot) | 12-tool stdio MCP for editors/other agents; hardcoded absolute `VAULT` + `GRAPH_PATH`. Not imported by client-chatbot Python code. Deps: stdlib + `pyyaml`. | **Leave in olives** (or copy + parameterize paths if standalone team runs Cursor/Claude against vault). |
| **db/vault_graph.json** | `/media/alaa/data/olives/db/vault_graph.json` (2.8M, tracked) | **No** (current pilot) | Loaded only by `obsidian-mcp-server.py` (`get_impact`, `get_proc_deps`). Known dirty (`called_by` semantics, PLAN-04). Rejected for live chatbot schema (PLAN §1.5). | **Leave in olives** |
| **db/ vault regen pipeline** | `/media/alaa/data/olives/db/{bulk_edit,csv_to_graph,merge_graph,...}.py`, `db/{tables,procs_*}.json`, `db/bo_*.md`, `db/osfa_*.md` | **No** | Separate concern (vault regeneration, TODOS.md). Redundant with vault notes per PLAN. | **Leave in olives** |
| **knowledge/planning/** | `/media/alaa/data/olives/knowledge/planning/PLAN-*.md`, `TODOS.md` | **No** (runtime) | Platform/architecture docs. `PLAN-01`/`PLAN-04` inform design; `apps/client-chatbot/PLAN.md` is the operative build doc inside the app. | **Leave in olives**; optionally copy `PLAN-01` + `PLAN-04` into standalone `docs/history/` for context. |
| **gateway/** | `/media/alaa/data/olives/apps/client-chatbot/gateway/` | **Yes** | LiteLLM config + key custody (golden rule 4). Already inside client-chatbot. | **Already in tree** — moves with copy. |
| **prompts/** | `/media/alaa/data/olives/apps/client-chatbot/prompts/system.md` | **Yes** | Loaded by `core/agent.py` for system prompt. | **Already in tree**. |
| **sqlmcp/** | `/media/alaa/data/olives/apps/client-chatbot/sqlmcp/` | **Yes** (if external SQL MCP consumers) | Thin SSE MCP over `core/sql.py` (FIXPLAN M9). Self-contained under client-chatbot; Docker test harness expects `drift-tool-mssql`. | **Already in tree**. Rename collision avoided (`sqlmcp/` not `mcp/`). |
| **olives web pages** | `/media/alaa/data/olives/apps/client-chatbot/olives web pages/` (~901M, **untracked**, `??` in git status) | **No** | ASP.NET BO/OSFA UI snapshot. **Zero** Python/JS imports in chatbot code; only incidental CKEditor README mentions “web pages”. Likely manual reference dump. | **Leave out of standalone** (or optional `reference/asp/` git-LFS). Do not add to olives git as-is (size). |
| **data/** (disk-only) | `/media/alaa/data/olives/data/{client-archives,db-snapshots,exports,dev-scratch}/` | **No** (in repo) | Gitignored per root `.gitignore`. Real `.bak`/exports live here. README: “Only DBs kept in git: none.” | **Leave on disk**; document mount paths for restore. |
| **Inventory-Master.csv** | Referenced in `PLAN.md §1.5` at olives root; **not present** in workspace | **No** (optional seed) | Could seed `core/catalog.py` descriptions; not wired in code today. | **Leave** if it appears; optional copy for catalog authoring. |
| **Olives README / conventions** | `/media/alaa/data/olives/README.md` | **No** (runtime) | Documents monorepo layout, vault path load-bearing rule, `docs_corpus` symlink convention. | Extract relevant bullets into standalone `README.md`; **leave** monorepo file. |
| **AGENTS.md / CLAUDE.md** | Not present at olives root | — | — | — |
| **.claude/** | `/media/alaa/data/olives/.claude/` | **No** | Editor launch configs per README. | **Leave** |
| **Untracked local-only in client-chatbot** | `run.sh`, `core/procedure_match.py`, `.env`, `work/`, `clients/{morec,rukn}.yaml`, `gateway/.env` | **Mixed** | `run.sh` orchestrates docker+gateway+uvicorn (useful). `procedure_match.py` has **no imports** anywhere (dead code). Secrets gitignored per C2. | Copy `run.sh`; drop or finish `procedure_match.py`; never commit `.env` / `work/`. |

---

## What the running stack actually calls

```
Browser → static/ + api/server.py
              → core/agent.py → core/{sql,gate,catalog,docs,memory,llm}.py
              → core/llm.py → gateway/ (LiteLLM :4000)
              → pymssql → 127.0.0.1:14330 (drift-tool-mssql) as chatbot_ro

Setup chain (not runtime):
  01_db_up.py      → drift.docker_mgmt + drift.restore + .bak file
  02_introspect.py → drift.config (SA) → work/<client>/schema_cache.json
  03_apply_db_sql.py → drift.config + db/*.sql
  04_assemble_docs_corpus.py → olives knowledge/ + support-agent file → docs_corpus/ symlinks
  05_index_docs.py → core/docs.build_index → work/<client>/docs.sqlite
  refresh.py       → chains 02+03
```

**Not in the call graph today:** `obsidian-mcp-server.py`, `db/vault_graph.json`, `obsidian/olives/`, drift compare pipeline, `olives web pages/`.

---

## Nested git vs sibling directory

### Option A — `git init` inside `apps/client-chatbot` (nested repo)

| Pros | Cons |
|------|------|
| Smallest filesystem move | Parent `olives` must **stop tracking** the folder (`git rm -r --cached apps/client-chatbot`) or use **git submodule** — otherwise nested `.git` is painful |
| Can keep symlinks to `../../knowledge/` temporarily | `04_assemble_docs_corpus.py` symlinks **outside** the nested repo → broken on standalone clone |
| | `parents[2]` = `apps/` breaks if drift-tool isn't sibling at `../drift-tool` from `apps/` |
| | CI clones of “just chatbot” still need olives knowledge paths or copied docs |
| | `olives web pages/` (901M untracked) moves with folder unless deleted first |

### Option B — Copy/move to sibling directory (recommended)

Example: `/media/alaa/data/client-chatbot` next to `/media/alaa/data/olives`.

| Pros | Cons |
|------|------|
| Clean repo boundary; no `.git` inside `.git` | One-time path rewrites in `setup/*.py` and drift `config.py` |
| Vendor `docs/source/` from `knowledge/` + `system_options_guide.md` — no symlink hop | Parent olives keeps or removes `apps/client-chatbot/` explicitly |
| `vendor/drift-tool` git submodule at fixed path | Two repos to coordinate for shared container name / port |
| Matches PLAN intent: chatbot is “between bare MCP and production,” drift/vault are platform | |

**Recommendation:** **Option B (sibling copy)** + `git submodule add` for `drift-tool` at `vendor/drift-tool` (or document `DRIFT_TOOL_PATH`). Copy knowledge docs into `docs/source/` and change `04_assemble` to symlink/copy from there instead of `parents[3]`. Keep vault, `vault_graph.json`, and `obsidian-mcp-server.py` in olives unless M11 ships.

If you must stay inside olives tree short-term: nested git **only** works if olives adds `apps/client-chatbot/` to `.gitignore` and treats it as a submodule — not as continued monorepo tracking.

---

## Open questions

| Question | Notes |
|----------|-------|
| **Destination path** | Sibling (`/media/alaa/data/client-chatbot`) vs nested (`olives/apps/client-chatbot/.git`). Sibling is cleaner. If nested, decide submodule vs full untrack from parent. |
| **Remove from parent git?** | If extracting: `git rm -r --cached apps/client-chatbot` in olives + add submodule pointer **or** leave a stub README redirect. Untracked `olives web pages/` can simply be deleted or moved before extract. |
| **Secrets handling** | Never commit: `apps/client-chatbot/.env`, `gateway/.env`, `work/ro_password.txt`, `clients/*.yaml` (real tokens), `drift-tool/work/.mssql_pw`, `data/*` backups. Standalone needs fresh `OLIVES_TOKEN_*`, `GEMINI_KEY`/`DEEPSEEK_KEY`, `MASTER_KEY`, `GATEWAY_API_KEY`. C2 pattern: tokens in `.env`, `clients/*.yaml` only names `api_token_env`. |
| **`.bak` location** | Default path missing on this machine. Point `01_db_up.py --bak` at a file under `data/db-snapshots/` or client archives; keep out of git. |
| **`BACKUP_BROWSE_ROOT`** | Hardcoded `/media/alaa/data` in drift `config.py` — must match where `.bak` files live for Docker RESTORE. Parameterize per deployment. |
| **Docs: copy vs symlink** | Symlinks break on Windows clones and standalone boundaries. Prefer **copy** or git submodule of `knowledge/` at extract time. |
| **Shared Docker container** | `drift-tool-mssql` is shared infra. Renaming requires coordinated drift-tool + chatbot config change. |
| **Vault MCP later (M11)** | If adopted, standalone either keeps MCP server in olives with network access, or copies parameterized `obsidian-mcp-server.py` + submodule vault + regen pipeline — large scope, explicitly deferred. |
| **`run.sh` / `procedure_match.py`** | Not in olives git today. Decide whether to track `run.sh` in standalone; delete or wire `procedure_match.py`. |

---

## Minimal standalone file checklist

**Must have in new repo (copy or submodule):**

- Everything currently tracked under `apps/client-chatbot/` (65 files)
- `vendor/drift-tool/` — at least `drift/{__init__,docker_mgmt,restore,config}.py`
- `docs/source/` — vendored from `knowledge/{reference,back-office,front-office}/` + `system_options_guide.md`
- Rewritten `setup/04_assemble_docs_corpus.py` pointing at `docs/source/`
- Rewritten `setup/{01,02,03,05}_*.py` with single `REPO_ROOT = Path(__file__).resolve().parents[1]`

**Keep only in olives:**

- `obsidian/olives/`, `obsidian-mcp-server.py`, `db/vault_graph.json`, `db/*.py` regen pipeline
- `apps/drift-tool/` full compare UI (optional submodule)
- `apps/support-agent/` (except one copied guide file)
- `knowledge/planning/`, `data/`, `apps/route-optimizer-app/`
- `olives web pages/` (unless explicitly wanted as reference blob)

**On disk, outside any git repo:**

- `*.bak` database backups
- `work/` runtime state, `docs_corpus/` symlinks, `.env` secrets
