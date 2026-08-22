# Execution plan: generic Olives BO assistant

Branch: `feat/general-bo-assistant`  
Parent snapshot: `f8b73cb` on `main` (trust-slice: metrics, vault cards, Arabic evals)  
Vault: `obsidian/olives/` already tracked (~2659 files). Keep notes in git so a bad vault edit can roll back.  
Locked scope (eng review D1, 2026-08-15): **B — general assistant, SELECT-first; EXEC only for audited read-only `Rpt_*`.**  
Locked (D2): **SELECT templates first. No GRANT EXECUTE in the first implementation PR.** `setup/audit_rpt_readonly.py` may write a *candidate* allow-list; Grok signs it before any GRANT in a later PR.  
Supersedes (partial): `alaa-main-design-20260814-123430.md` “no EXEC of Rpt_*”. Money grains and no-proc-bodies still hold.

Python **3.13** only. Runtime login **`chatbot_ro`** + schema **`t.`** + `SESSION_CONTEXT('CompanyID')`. Never `cds` / SA from `core/` or `api/`. Never return procedure bodies.

---

## 0. What this product is

The chatbot is a Back Office accountant’s search engine over **Olives_BO** plus the **user guide**.

Two jobs, one session:

1. **How Olives works** — screens, system options, assignment, CFD, van stock, reports, Arabic names for English tables.
2. **This company’s numbers** — invoices, orders, receipts, stock, customers, salespersons, routes, collections. Always CompanyID-scoped.

Pilot tenant: client **105**, CompanyID **2**, ClientID **207**. Arabic is the product language. Company picker is live `SELECT ID, Name FROM t.Companies`. Do not mention IIS in UI copy.

**Generic, not hardcoded.** Seven `run_metric` grains exist so money questions do not invent `COUNT(*)` on `TransactionsHeaders` (261 headers ≠ 238 sales invoices). The long tail is **live schema + vault metadata + headed FTS + `run_select`**, not a 400-metric cookbook.

**Cache:** plan_cache and verified SQL templates, keyed by `client + CompanyID`. Never cache the numeric answer as truth. Re-run SQL.

---

## 1. Business model the agent must internalize

Olives BO is a van-sales / distribution ERP. Core loop:

```
Company ── SalesPersons (PositionID) ── CFD (customer assignment)
                │
                ├── SalesPersonItemsBalance (van stock)
                ├── OrdersHeaders/Details (طلبات, not invoices)
                └── TransactionsHeaders/Details (فواتير)
                        TransactionTypeID=1 sales, =2 returns
                        ISNULL(IsVoid,0)=0 required
                        Receipts are a different table (تحصيل)
```

Grain that already failed live:

| User said | Wrong SQL | Right grain |
|-----------|-----------|-------------|
| كم فاتورة مبيعات | `COUNT(*)` headers = 261 | type=1, non-void = **238** |
| طلبات | invoices | `OrdersHeaders` = **132** |
| أفضل مندوب | customer count / CFD rows | net sales by salesperson (**Imad**) |
| عملاء أسامة | 1 CFD join | `cfd.PositionsID = sp.PositionID` (6 rows) |
| هذا الشهر | calendar Aug 2026 | last posting **2025-07-15**; ask, do not silently use July |

System options, screen numbers (`knowledge/back-office/*.md`, ~215 files, almost no `#` headings), and `Rpt_*` (~593 vault notes) are how staff *name* work. The chatbot must map those names onto `t.` tables.

---

## 2. Architecture (strangler, not rewrite)

```
Browser POST /ask (SSE)
        │
        ▼
core/agent.py  (MAX_TURNS=12, MAX_QUERIES=4, MAX_DOC_SEARCHES=3)
        │
        ├── search_docs          → FTS5 docs.sqlite (how-to)
        ├── search_schema_notes  → vault metadata, no bodies
        ├── read_schema_note     → params / tables read
        ├── get_joins            → live FKs (schema_cache) + vault relations
        ├── lookup_hot           → names/IDs for this CompanyID
        ├── run_metric           → certified money grains
        ├── run_select           → t. views via gate + sql
        └── run_report (NEW)     → catalog match → SELECT clone OR audited EXEC
                │
                ▼
        core/sql.py + core/gate.py
                │
                ▼
        chatbot_ro  SESSION_CONTEXT  t.*
```

**Do not add:** LangChain, vector DB, embeddings, a second SQL path, IIS identity.

**Reuse:** `core/reports.py` + `setup/build_report_catalog.py`, `core/vault.py`, `core/docs.py`, `core/metrics.py`, `core/gate.py` (already parses `EXEC` if the name is allow-listed), `core/memory.py`.

### Intent router (code, not a new service)

Cheap regex + tenant_pack dates, already partly in `agent.py`:

| Intent | Tools offered | Skip |
|--------|---------------|------|
| How-to / option / screen | `search_docs` only first | schema + SQL |
| Count/sum of known metric | `run_metric` | docs |
| Named report | `run_report` | docs thrash |
| Ad-hoc analyst | vault notes + `get_joins` + `run_select` | |
| Identity / كل الشركات | `ask_user` | |

After a **business** rowset from `run_select` / `run_metric` / `run_report`, the model may still use remaining `MAX_QUERIES` (today 4) for a second grain or check — that is current code (C4), not the old “golden rule 6 latch”. Plan text must not restore the latch. `analyze` stays free. Docs/vault stay on their own caps.

---

## 3. Workstreams (parallel Composer lanes)

Lanes share `core/agent.py` at the end. Merge lane A/B/C first; lane D last (agent wiring).

### Lane A — Headed user guide + FTS (docs)

**Problem:** `knowledge/back-office/*.md` and the 4079-line `OLIVES USER GUIDE_2021Updated2025.md` have almost **zero** `#` headings. `docs.py` chunks by heading then paragraph. Retrieval returns `user_guide.md › ` empty titles and TOC noise.

**Build:**

1. Split the monolith guide into one file per numbered screen / chapter under `knowledge/back-office/` (or `knowledge/guide-headed/`). Keep originals; generate headed copies. Do not invent screens that are not in the source.
2. Inject `#` headings from existing numeric prefixes (`4.8 Assign customers…`) where the file already has a number-title line.
3. Re-run `setup/04_assemble_docs_corpus.py` + `setup/05_index_docs.py --client 105`.
4. Keep synonym expand + 4.8 boost + assign card. Cap `search_docs` at 3 (already). Cap vault tools (`search_schema_notes` / `read_schema_note` / `get_joins`) at **MAX_VAULT_SEARCHES=3** (D6). Do not share one budget with docs.
5. Filter TOC / empty-heading hits in `_search_docs` (already intended; finish if incomplete).

**Vault sync while building:** if a screen names a table that is missing from vault or from `schema_cache.json`, log `vault_drift` and fix the note from **live** `INFORMATION_SCHEMA`, not from memory.

**Tests:** `tests/test_docs.py` — headed chunks exist; assign-customers ranks top-3; TOC chunks never in top-5.

**Eval:** `evals/docs_105_ar.jsonl` must stay green.

### Lane B — Live joins + module map (schema)

**Problem:** 440 tables, 30 relation notes. Vault graph is incomplete. `schema_cache.json` already has `foreign_keys` from introspect.

**Build:**

1. `get_joins` must prefer **live FKs** from `schema_cache` over vault relation notes. Vault is a hint; live wins.
2. Compile a **module map** JSON (cached, not per-turn LLM): tables grouped by domain (sales, orders, receipts, CFD, van, items, routes, system options). Source: vault tags + `reads_from` of high-support procs + tables-summary.md.
3. Inject a short module card into tenant_pack for the matched domain (not the whole 440-table dump).
4. Join playbook (`prompts/join_playbook.md`) stays; extend with live FK examples that failed in Arabic evals (CFD PositionsID, SalesPersonItemsBalance).

**Vault sync:** for each table the agent actually queries, compare vault columns vs `schema_cache` columns. If mismatch: patch the vault note (frontmatter + column list only, **never** paste proc bodies). Commit vault fixes on this branch so they are rollback-able.

**Tests:** `tests/test_vault.py` — get_joins returns live FK even when relation note is missing; body strip still holds.

### Lane C — Reports: catalog → SELECT clone → audited EXEC

**593** `Rpt_*` notes. Catalog builder already writes `work/<client>/report_catalog.json` (name, purpose, params, tables, when_to_run). Matcher is token overlap (`core/reports.py`) **plus `aliases[]` on each card** (D4). First-wave 10 templates get hand Arabic/English aliases and unit tests (`match_reports("تقرير مبيعات المندوب")`). **Never EXEC from the catalog alone.** Vault `writes_to:` is often empty **and AUTO-GENERATED**. That is not a write-free proof.

```
Question "تقرير مبيعات المندوب"
        │
        ▼
match_reports() → Rpt_SalesmanSalesSummary
        │
        ▼
SA audit script (setup, not runtime)
  sys.sql_modules definition
  reject if INSERT/UPDATE/DELETE/MERGE/TRUNCATE/DROP/CREATE/ALTER
          EXEC of non-allow-listed callee, xp_, OPENROWSET
  reject if writes_to non-empty in LIVE sys.dm_sql_referenced_entities
        │
        ├── FAIL → SELECT clone on t. using params + tables read
        │            OR "افتح شاشة التقرير في Olives" if uncloneable
        └── PASS → add to work/<client>/rpt_exec_allowlist.json
                     GRANT EXECUTE ON dbo.Rpt_X TO chatbot_ro  (setup/03 only)
                     agent tool run_report → EXEC with bound params
```

**Parameters:** from vault Parameters section **and** live `sys.parameters`. Bind `@CompanyID` / `@CompNo` to session company always. Refuse other companies. Dates from tenant_pack (last posting vs calendar — same honesty as metrics). Optional salesman/item from `lookup_hot`.

**`run_report` tool:**

- Input: `name` (catalog) + `params` dict.
- Path 1: if a **SELECT template** exists in `work/<client>/rpt_select_templates.json`, run through `sql.run_select`.
- Path 2 (later PR only): existing `sql.run_proc` after signed GRANT. Do not add `run_exec`. First PR never calls this path.
- Path 3: else return catalog purpose + “equivalent SELECT not certified yet”.

**T0 (P0, first commit in Lane C/D):** `allowed_proc_names` passed to `gate.validate` / `run_select` must **not** be `catalog.for_client().keys()` (that is every entitled `Rpt_*`). Until a signed allow-list exists, pass `allowed_procs=[]` so EXEC in model SQL is always GateError. Templates live in-repo (`knowledge/report_templates/` or `prompts/report_templates/`), not only gitignored `work/`.

**T0b:** Remove or rewrite the agent injection that says “never EXEC” so it matches D1 (no EXEC in *this* PR; later signed `run_proc` only). Do not leave contradictory system text.

**Setup:** `setup/audit_rpt_readonly.py` (SA, one-shot). Output: allow-list JSON + reject reasons. Human (Grok supervisor) reads the reject file before any GRANT.

**Tests:** gate still denies EXEC of non-allow-listed names; allow-listed EXEC with wrong CompanyID is rewritten/refused; SELECT template path never calls EXEC; xp_ still denied.

**AGENTS.md:** update the EXEC sentence to match D1 (allow-listed read-only Rpt only). Keep “never return procedure bodies”.

### Lane D — Agent loop + prompts (after A/B/C merge)

1. Add `run_report` to TOOLS.
2. Split tool offering by intent (already partial `_FAST_PATH_SKIP_TOOLS`).
3. `prompts/system.md`: generic analyst rules — assume-and-confirm for grain, never invent TransactionTypeID, prefer run_metric for the seven grains, use get_joins before joining, search_docs for how-to only.
4. Widget: keep SQL + as-of. Show report name when `run_report` fired.
5. Empty-answer stub stays.

**Tests:** `tests/test_agent.py` — docs-only never calls run_select; metric questions skip docs; report questions call run_report not 8× search_docs.

### Lane E — Evals + real-world loop (continuous)

Coverage matrix (~120), not 7 happy paths:

| Band | Count | Source |
|------|-------|--------|
| Certified money (metrics) | ~15 | existing comprehensive_ar + daily pack |
| How-to / options / assignment | ~20 | docs_105_ar + new headed-guide Qs |
| Ad-hoc SQL (items, customers, routes) | ~30 | new; ground truth from live SELECT |
| Named reports | ~20 | catalog names in Arabic |
| Honesty (this month, all companies, void) | ~10 | existing |
| English regression | 11 | hard_en — do not few-shot |

**Loop (Composer builds, Grok validates):**

```
for each failing eval or live Arabic usecase:
  1. Composer reproduces with python3.13 evals/run_evals.py or /ask
  2. If SQL wrong: fix grain / join / template; if vault wrong: patch note from live schema
  3. Add regression jsonl case (never auto-promote to verified_queries)
  4. Re-run unit tests + the failed band
  5. Grok reads the trace + SQL + numbers; only Grok marks the band DONE
```

Stop adding metrics unless a money grain is repeatedly wrong after generic SQL. Prefer join cards and report templates.

---

## 4. Permissions the model actually needs

| Need | How |
|------|-----|
| SELECT on tenant data | already: `t.` views + SESSION_CONTEXT |
| Company list | already: `t.Companies` |
| Schema names | `schema_cache` + vault metadata tools |
| How-to | FTS docs.sqlite |
| Named reports as SQL | SELECT templates on `t.` |
| Named reports as EXEC | **only** after SA write-free audit + GRANT EXECUTE on that proc to `chatbot_ro` |
| Functions used by reports | if EXEC path needs them, GRANT EXECUTE on **read-only** functions too, same audit |
| Proc bodies | **never** |

`chatbot_ro` stays without `db_datareader` and without base-table SELECT.

---

## 5. Vault ↔ database sync (mandatory while building)

Live schema is truth. Vault is a search index.

On every SQL error `Invalid column` / `Invalid object`:

1. Introspect live (setup/02 or INFORMATION_SCHEMA via existing introspect tool).
2. Diff vault note.
3. Patch vault (columns, FKs, params). Commit on this branch.
4. Rebuild vault cards / report catalog if the note was a Rpt_*.
5. Retry the question.

Batch job (Composer, once): `setup/refresh.py --client 105` then a script that lists vault tables missing from schema_cache and schema_cache tables missing from vault. Do not auto-delete notes; flag them.

---

## 6. Files expected (right-sized; strangler)

Touch, do not explode:

- `core/agent.py`, `core/docs.py`, `core/reports.py`, `core/vault.py`, `core/gate.py`, `core/sql.py`, `core/metrics.py` (only if a certified grain is still wrong)
- `setup/audit_rpt_readonly.py` (new), `setup/05_index_docs.py` / assemble if needed
- `prompts/system.md`, `prompts/join_playbook.md`
- `AGENTS.md` EXEC sentence
- `knowledge/` headed copies (generated + reviewed)
- `obsidian/olives/` only when live schema disagrees
- `evals/*.jsonl`, `tests/test_*.py`
- `static/app.js` if report name must show

Avoid new frameworks and a second agent runtime.

---

## 7. Acceptance gates

1. `python3.13 -m pytest tests/` green.
2. Wave 5 Arabic + docs_105_ar no regressions.
3. comprehensive_ar 105: keep ≥ 64/69; new generic band ≥ 80% on first 30 ad-hoc questions with **paid** model (not OmniRoute free `auto/*`).
4. Gate denies EXEC of non-allow-listed proc (unit test).
5. No procedure body in any tool result (existing vault tests).
6. Empty SSE still impossible (P0).
7. Company isolation: CompNo/CompanyID injection still on.

---

## 8. NOT in scope

- IIS widget / cds / cookie identity
- LangChain, Pinecone, embeddings
- GRANT EXECUTE on all 593 Rpt_*
- Returning CREATE PROCEDURE text
- Caching numeric answers
- Multi-company “كل الشركات” answers
- Writes, posting, approvals
- OSFA field-salesman product
- English as product voice (English-11 is regression only)

---

## 9. What already exists (do not rebuild)

| Piece | Status |
|-------|--------|
| FastAPI `/ask` SSE, company dropdown | ship |
| Gate + t. views + SESSION_CONTEXT + CompNo inject | ship |
| 7 metrics | ship |
| Vault tools without bodies | ship |
| Report catalog from vault (metadata only) | ship, unused as EXEC |
| FTS docs, assign boost | ship, headingless corpus |
| plan_cache / verified_queries | ship |
| Arabic 69-q eval harness | ship |

---

## 10. Failure modes

| Path | Failure | User sees | Test |
|------|---------|-----------|------|
| EXEC allow-list miss | proc writes | must never run; audit reject | audit script + gate unit |
| Vault stale column | Invalid column | Arabic error + retry after patch | vault sync loop |
| Headingless FTS | empty/TOC answer | stub already; headed corpus | docs tests |
| Free OmniRoute 502 | empty SSE | stub; operator switches paid model | eval skip/retry |
| Generic SQL counts headers | 261 vs 238 | run_metric still preferred | grain tests + eval q07 |

---

## 11. Parallelization

| Lane | Modules | Depends |
|------|---------|---------|
| A headed docs | `knowledge/`, `core/docs.py`, `setup/05_*` | — |
| B joins/module map | `core/vault.py`, `prompts/join_playbook.md` | — |
| C report audit/templates | `setup/audit_rpt_readonly.py`, `core/reports.py`, `core/sql.py`, `core/gate.py` | — |
| D agent wiring | `core/agent.py`, `prompts/system.md` | A, B, C merged |
| E evals loop | `evals/`, `tests/` | D |

Launch A+B+C in parallel Composer worktrees. Merge. Then D. Then E loop with Grok as supervisor.

Conflict flag: A and D both eventually touch `core/docs.py` / `core/agent.py`. Keep A’s agent edits to `_search_docs` only until merge.

---

## 12. Implementation tasks

- [ ] **T0 (P0)** — Pass `allowed_procs=[]` into the gate until a signed list exists. Stop using full `catalog.for_client()` as EXEC allow-list.
- [ ] **T0b (P1)** — Rewrite agent “never EXEC” injection; templates in-repo not only `work/`.
- [ ] **T2 (P1)** — `get_joins` live FK first. Tests.
- [ ] **T3 (P1)** — `setup/audit_rpt_readonly.py` + empty allow-list until Grok signs rejects.
- [ ] **T4 (P1)** — SELECT templates for the first 10 Arabic-asked reports.
- [ ] **T5 (P2, later PR)** — Wire `run_report` to existing `sql.run_proc` only after signed allow-list + GRANT. No `run_exec`.
- [ ] **T6 (P1)** — Intent split in agent; no docs thrash on counts.
- [ ] **T7 (P1)** — Vault drift script + patch notes from live schema.
- [ ] **T8 (P1)** — 30 new ad-hoc Arabic evals + regression cases from live fails.
- [ ] **T9 (P2)** — AGENTS.md EXEC sentence; widget report name if `run_report` fired.
- [ ] **T10 (P1)** — `MAX_VAULT_SEARCHES=3` in `core/agent.py` + unit test that the 4th vault tool is refused.

---

## 13. Supervisor vs builders

**Grok (this chat / parent):** architecture, security (EXEC grants), acceptance, reading traces, marking lanes DONE, writing vault policy. Does not grind pytest or split 215 markdown files.

**Composer agents (parallel):** implement T1–T9, write tests, run evals, patch vault notes, reindex FTS, propose allow-list entries with audit evidence.

Paid LLM for live `/ask` (Gemini 2.5 Flash primary). Free OmniRoute `auto/*` 502s are not product bugs.

---

## GSTACK REVIEW REPORT

- Branch: `feat/general-bo-assistant` (from `main` @ `f8b73cb`)
- Design doc: `alaa-main-design-20260814-123430.md` (Approach B trust slice). This plan supersedes “no EXEC” with D1=B + D2=no GRANT in first PR.
- D1 B general assistant SELECT-first
- D2 A SELECT templates first, no GRANT
- D3 A reuse `sql.run_proc`
- D4 A catalog `aliases[]`
- D5 A full eval bar
- D6 A `MAX_VAULT_SEARCHES=3`
- D7 A thin Lane C (10 in-repo templates)
- D8 A keep `MAX_QUERIES=4`
- D9 A TODO gate-wrap `run_proc`
- T0: `allowed_procs=[]` until signed list (catalog keys are not an EXEC allow-list)
- Outside voice: Composer subagent (Codex CLI not installed). Tensions resolved D7/D8; remaining holes folded as T0 + TODOS.
- Unresolved decisions: 0
- Critical gaps flagged: 1 mitigated (EXEC via catalog keys) — T0 is P0

