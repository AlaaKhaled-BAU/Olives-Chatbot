# Olives Client Chatbot — Full Blueprint

> System architecture + end-to-end prompt lifecycle.
> Current as of branch `deepseek-swap`, commit `e9e92c0` (2026-08-22).
> Line anchors refer to `core/agent.py`, `core/llm.py`, `api/server.py` at that commit.

---

# PART 0 — PRODUCT & DOMAIN CONTEXT

## 0.1 What Olives is

Olives is an **Arabic-language ERP suite for FMCG distribution and trading companies**.
It has a front-office side (field sales / orders) and the back-office system this
chatbot lives next to: database catalog **`Olives_BO`**, deployed on the customer's own
infrastructure — IIS web application + SQL Server. The Olives website authenticates
through SQL login `cds` with a session-bound `CompanyID`; several companies of one
group share the same instance, so every business table carries `CompanyID` and every
answer must be scoped to exactly one.

Back-office modules (official user guides under `knowledge/back-office/`):
customers · items · salespersons · routes · delivery · transactions (sales /
returns / purchases / transfers) · receipts & checks · promotions · agreements ·
**competitive items** (rival products tracked per customer store) · dashboards ·
reports · users & permissions · workflow · settings.

The operating model visible in the data and metric pack is **van-sales distribution**:
salesmen are assigned routes of shop-customers, vans carry stock (`van_stock`),
field reps get daily sales packs (`daily_sales_pack`), salesman↔customer assignment
is explicit (`cfd_assignment`), and orders placed in the field are invoiced back at
the office (hence the orders-vs-invoices gap reports).

## 0.2 What this chatbot is within it

A **read-only copilot over that estate**. It answers two kinds of Arabic questions:

1. **How-do-I / where-is-it** — from the official user guides only (FTS5 corpus).
   If the guides don't cover it, it says so («لا يوجد في دليل المستخدم»).
2. **Verified live-data questions** — generates a read-only `SELECT` against `t.*`
   views through the five-layer wall, shows its receipt (SQL + rows + freshness),
   and refuses rather than guesses when evidence is missing or grain is ambiguous.

It never writes to the ERP, never executes procedures, never crosses companies,
and is not a replacement for any screen — it is the fastest path from question to
defensible number.

## 0.3 Who uses it

| Persona | Typical asks | What they need |
|---|---|---|
| GM / group owner (multi-company) | «مبيعات شركة الاضواء هذا الشهر؟» | correct company scoping; honest "I only see company X" when asked cross-company |
| Back-office manager | «كم عدد الزبائن النشطين؟», net-sales totals | instant verified KPIs without opening dashboards |
| Receivables clerk | «سداديات العميل الفلاني خلال يوليو؟», checks status | collection lines per period/customer |
| Sales supervisor | «مبيعات كل مندوب», orders-vs-invoiced gap | per-salesman accountability numbers |
| Data-entry clerk | «حركة صنف كذا», transfers/van stock | item movement detail |
| Helpdesk / support agent | «كيف أضيف عميل؟», screen/option explanations | guide-grounded answers with section citations |

All personas are **Arabic-first RTL users who cannot write SQL**. The common thread:
they need numbers they can defend to a superior — which is why every number ships
with its executed query, row count, and data-freshness stamp instead of a bare answer.

## 0.4 Use-case catalog → mechanism map

| Need | Example (ar) | Served by |
|---|---|---|
| Daily KPI counts | كم عدد الزبائن النشطين؟ | fast-count path → metric pack / master terms, gear `f0` |
| Charged sales for a period | صافي مبيعات يوليو 2025؟ | `net_sales`: line `Price` after discounts, tax already inside `Price`. قبل الضريبة and بعد المرتجعات are playbook readings on `run_select`, not extra metrics. |
| Salesman performance | مبيعات كل مندوب هذا الشهر | `net_sales_by_salesperson` metric + report template |
| Returns control | نسبة المرتجعات إلى المبيعات غير الملغاة؟ | returns-ratio NL→SQL (+ `analyze` for arithmetic) |
| Collections & receipts | سداديات عميل خلال فترة | receipt-collection report templates |
| Item movement | مبيعات ومرتجعات صنف معين | invoice-line-by-item template |
| Field-to-office gap | الأوامر مقابل الفواتير لكل مندوب | orders-vs-invoices template |
| Van / route ops | جرد فان معين، توزيع المناديب على المسارات | `van_stock`, `routes` module knowledge, hot_cache snapshots |
| Date honesty | كم مبيعات هذا الشهر؟ (period empty) | deterministic calendar guard ask — no model judgment involved |
| Grain honesty | كم فاتورة عندنا؟ (which type?) | grain-trap disclosure requirement in system prompt + scorer |
| How-to guidance | كيف أضيف عميل جديد؟ أين خيار كذا؟ | FTS5 over headed user-guide corpus with section citations |
| Multi-company disambiguation | any question when CompanyID unresolved | `needs_ask` listing REAL companies; pending-answer binding |

## 0.5 Non-goals

No writes to the ERP · no EXEC (allow-list empty until signed audit) · no
cross-company leakage (the wall, not politeness) · no guessing without sources
(refusal is a feature) · not a dashboard replacement (Olives has one) · English UI
is future work (`locale: ar` today).

---

# PART 1 — SYSTEM ARCHITECTURE

## 1.1 Bird's-eye view

```
                                ┌────────────────────────────┐
                                │  Customer browser / widget │
                                │  static/index.html+app.js  │
                                └───────────┬────────────────┘
                                            │ POST /ask (SSE), /context, /feedback
                                            ▼
┌───────────────────────────────────────────────────────────────────────────────┐
│ api/server.py — FastAPI (uvicorn :8100)                                       │
│  • env-pinned tenant: CHATBOT_CLIENT → clients/<name>.yaml   (server.py:51)   │
│  • rate limit 30/min keyed on x-session-id / IP              (server.py:31)   │
│  • SESSIONS OrderedDict: per-session CompanyID + pending_ask (server.py:80)   │
│  • SSE relay: _with_heartbeat pump + X-Accel-Buffering:no     (server.py:87)  │
│    every stream ends with data: [DONE], including error paths                 │
└───────────┬───────────────────────────────────────────────────────────────────┘
            │ agent.ask_stream(client, question, conversation, subject)
            ▼
┌───────────────────────────────────────────────────────────────────────────────┐
│ core/agent.py — the turn pipeline (~1540 LOC)                                 │
│                                                                               │
│  intent router ─► plan/result cache ─► calendar guard ─► message assembly     │
│       │                                                    │                  │
│       │            STATIC PROMPT PREFIX (byte-stable)      ▼                  │
│       │   [system.md+playbook] [full t. schema] [all vault cards]             │
│       │                                                    │                  │
│       ▼                                                    ▼                  │
│  tool loop (MAX_TURNS=12) ◄──────────────────── core/llm.py gears             │
│       │                        f0 flash·no-think | t1 think-low               │
│       │                        t2 think-high | p pro (rescue only)            │
│       ▼                                        https://api.deepseek.com       │
│  JSON answer contract (E1): final call has NO tools                           │
│  envelope: table/chart/sources/followups/confidence                           │
└──────┬──────────────┬──────────────┬──────────────┬──────────────────────────┘
       │              │              │              │
       ▼              ▼              ▼              ▼
┌────────────┐ ┌─────────────┐ ┌────────────┐ ┌──────────────────┐
│ core/sql   │ │ core/docs   │ │ core/vault │ │ work/<client>/   │
│ + gate     │ │ FTS5 search │ │ cards/joins│ │ cache.sqlite     │
│ chatbot_ro │ │ docs.sqlite │ │ vault_cards│ │ (plans/results/  │
│ + t.views  │ │ knowledge/  │ │ obsidian/  │ │  few-shot pools) │
└─────┬──────┘ └─────────────┘ └────────────┘ └──────────────────┘
      ▼
SQL Server Olives_BO
login: chatbot_ro (NO base-table grants)
schema: t.* views filtered by SESSION_CONTEXT('CompanyID')
gate: sqlglot single-SELECT, TOP-inject, tenant predicates, EXEC blocked
```

## 1.2 Component inventory

| Component | Role | Key entry points |
|---|---|---|
| `api/server.py` | HTTP surface; SSE streaming with keep-alive; session store; feedback endpoint | `ask()` server.py:216, `_with_heartbeat()` :87, `health()` |
| `core/agent.py` | Turn pipeline: intent routing, caching, guards, tool loop, contract, envelope | `ask_stream()` ~:1160, `_run_tool()` :958 |
| `core/llm.py` | Thin DeepSeek client. GEARS table = model × thinking × effort × timeout. SDK retries=0; one app-level retry layer; ProviderUnavailableError mapping; usage logging incl. cache-hit tokens | `complete()` llm.py:88, `provider_health()` |
| `core/gate.py` | sqlglot safety gate — THE only SQL door. Single SELECT, row-cap TOP injection, cross-company literal rejection, tenant predicate injection, EXEC deny-by-default | `validate()` gate.py:199 |
| `core/sql.py` | Only runtime connection factory (`chatbot_ro`); sets SESSION_CONTEXT per connection | `run_select()`, `set_tenant()` |
| `core/docs.py` | FTS5 over `work/<client>/docs.sqlite`; corpus from `knowledge/` via symlinked `docs_corpus/` | `search()` |
| `core/vault.py` | Compiled vault cards (table/relation knowledge), join lookups, proc-body sanitization | `retrieve_cards()` :625, `_load_cards()` :573 |
| `core/memory.py` | SQLite: verified_queries (+FTS few-shots), negative_queries, plan_cache, result_cache. Keys always include client+CompanyID+model+schema_version | `cache_key()` :87, `promote_verified_query()` :98 |
| `core/reports.py` | Report catalog matcher + certified SELECT templates (never EXEC) | `run_report()` :175 |
| `core/metrics.py` | Named metric registry (fast-count questions) | `question_mentions_metric()` |
| `core/hot_cache.py` | L1 master-data snapshots (salespersons/items/routes) — free tool budget-wise | `lookup_hot` tool |
| `core/tenant_pack.py` | Live per-company facts injected into every dynamic prompt block | `build()` |
| `core/params.py` | CompanyID resolution: NEEDS_ASK / MULTI / concrete id | `resolve()`, `discover_profile()` |
| `core/catalog.py` | Proc metadata per client (deny-by-default; `allowed_procs=[]` shipped) | `for_client()` |
| `core/trace.py` | JSONL event trace + Prometheus metrics (requests, gate rejections, latency histogram) | `log_event()`, `observe_latency()` |
| `db/01_readonly_login.sql` | Creates `chatbot_ro`: no db_datareader, no base-table grants, no EXECUTE | setup-time only |
| `db/02_tenant_views.sql` | Creates `t.*` views scoped by `SESSION_CONTEXT('CompanyID')` | setup-time only |
| `obsidian/olives/` | Source vault → compiled by `setup/compile_vault_cards.py` into `work/<client>/vault_cards.sqlite` | build-time |
| `db/vault_graph.json` | Precomputed relation graph for MCP impact/deps tools | offline |

## 1.3 The security wall (five independent layers)

```
L1  Tenant pinning        CHATBOT_CLIENT env → one yaml; browser cannot switch
L2  Login privileges      chatbot_ro: zero base-table grants, zero EXECUTE
L3  View scoping          t.* views filter rows by SESSION_CONTEXT('CompanyID'),
                          set per-connection inside core/sql.set_tenant()
L4  Gate                  sqlglot parse → exactly one SELECT → tenant predicates
                          injected/cross-company literals rejected → TOP cap 200
L5  Row/context caps      gate DEFAULT_ROW_CAP=200; model context _cap_for_context
                          shows 50; UI table caps 100 (_TABLE_ROW_CAP)
```
Defense-in-depth rule: no layer trusts another. The wall held all 36 adversarial probes in the production review; EXEC is structurally dead (`DEFAULT_ALLOWED_PROCS = ()`, agent hardcodes `[]`, and thumbs-up promotion re-validates through the gate before writing a few-shot).

## 1.4 Gears (core/llm.GEARS)

| Gear | Model | Thinking | Effort | Timeout | Used for |
|---|---|---|---|---|---|
| `f0` | deepseek-v4-flash | **off** | — | 30s | doc answers, needs_ask text, fast-count SQL, report paths, E1 contract formatting |
| `t1` | deepseek-v4-flash | on | low | 60s | standard NL→SQL turns (default interactive gear) |
| `t2` | deepseek-v4-flash | on | high | 90s | escalation after first failed tool attempt (joins/compound) |
| `p` | deepseek-v4-pro | on | high | 300s | rescue only: empty-final retry completion. Never streamed to users |

Routing entry: `_initial_gear()` agent.py:73; escalation inline in the tool loop; rescue in `_retry_empty_final()` :912.

## 1.5 DeepSeek API contracts honored

| Contract | Where handled |
|---|---|
| Thinking ON by default (effort high) → explicit toggle every request | `extra_body.thinking.type` llm.py |
| tools+thinking ⇒ echo `reasoning_content` back each request or HTTP 400 | `_stream_turn()` accumulates & attaches to assistant message agent.py:276 |
| temperature/top_p ignored in thinking mode → never relied upon | gears never set sampling params |
| KV disk-cache: full prefix-unit match; eviction hours–days; best-effort | byte-stable static prefix `_static_prefix()` agent.py:132; hit-rate logged per call |
| `user_id` regex `[A-Za-z0-9_-]{32}` via extra_body | `_user_id()` agent.py:65 = sha256(client\|company\|subject) |
| Streaming `: keep-alive` comments during inference | SDK drops comments ⇒ server synthesizes heartbeats `_with_heartbeat()` |

---

# PART 2 — END-TO-END PROMPT LIFECYCLE (one `/ask` turn)

## Phase 0 — HTTP entry (api/server.py)

```
POST /ask {question, session_id?}
  ├─ rate limit 30/min  bucket=x-session-id or client IP        (slowapi)
  ├─ pinned_client()          → CHATBOT_CLIENT env, fail-fast if unset/unknown yaml
  ├─ subject = sha256(session_id)[:12]        audit identity for this turn
  ├─ _touch_session()         → SESSIONS OrderedDict (LRU 500 / idle 3600s)
  ├─ _apply_pending_answer()  → if last turn was needs_ask(CompanyID), try to bind
  │                             the user's reply to a REAL company id/name match
  └─ stream() generator wrapped in _with_heartbeat(15s) + anti-buffer headers
```

## Phase 1 — Scope resolution (before any tokens are spent)

```python
company_id = params.resolve("CompanyID", conversation, profile)
```
- `NEEDS_ASK`/`MULTI` → done-frame `needs_ask` listing REAL companies from live `t.Companies` (agent.py C6c). Zero LLM calls. `[DONE]`.
- Concrete id → continue. Every later DB operation runs inside this scope.

## Phase 2 — Cache keys + schema version

```python
cache          = _schema_cache(client)                       # work/<client>/schema_cache.json
schema_version = sha256(tables+procs)[:16]                   # stale-plan immunity
key            = sha256(client|company|role|MODEL_ALIAS|question|schema_version)
```
Model name participates in the key ⇒ swapping models invalidates old plans automatically (this is how the DeepSeek swap cleanly orphaned OmniRoute-era plans).

## Phase 3 — Calendar guard BEFORE cache replay  *(live-proven ordering fix)*

`_empty_calendar_needs_ask(question, client, company_id)` (agent.py:743):
- «هذا الشهر» style question + live MAX(TransactionDate) says the period is empty
- → deterministic Arabic ask: «أغسطس 2026 فارغ. آخر قيد: يوليو 2025. هل أحسب آخر شهر قيد؟»
- fires for ALL questions; short-circuits before any LLM call.

Why first: q13 proved a July-dated cached plan replaying as "this month" when cache was checked first.

## Phase 4 — Plan-cache replay (cheap path)

Eligible only when: plan exists AND not a report-path question AND question has NO relative-date/all-companies phrases (`_needs_honesty_preamble` false — cached SQL bakes dates from a past day).
Replay = re-run each cached query through `sql.run_select` (full gate) → hand results to ONE `f0` streaming completion ("answer from these results only") → envelope → done. `trace.record_cache_hit`.

## Phase 5 — Message assembly (the prompt itself)

**Static prefix** — byte-identical across turns for a client (DeepSeek disk-caches these units at ~3% of miss price):

| msg | content | built by |
|---|---|---|
| [0] | `prompts/system.md` with `{{CLIENT}}`,`{{MAX_QUERIES}}` substituted + full `join_playbook.md` | `_static_prefix()` agent.py:132 |
| [1] | **Full schema of queryable tenant views**: every `t.*` table with `col:type?...` — 412 views, ~59k tokens shipped per turn | `_schema_block()` :79 (only tables where `has_tenant_view=true`) |
| [2] | **All compiled vault cards**: TBL lines (purpose/PK/FK) + REL lines (parent→referenced, business meaning) | `_all_cards_block()` :101 |

**Dynamic suffix** (changes per question/day — must stay AFTER the stable units):

| order | block | source |
|---|---|---|
| [3] | Previously-verified query patterns (≤3 FTS-ranked few-shots, this client+CompanyID only) | `memory.few_shots()` |
| [4] | Known bad patterns (≤2 negatives with reasons) | `memory.negative_shots()` |
| [5] | Matching report catalog cards (≤2) | `reports.match_reports()` |
| [6] | Vault card retrieval hits (≤3; skipped on fast_count/report paths) | `vault.retrieve_cards()` |
| [7] | Path directives: fast-count / report / howto behavioral notes | intent router |
| [8] | Honesty preamble (only for relative-date/all-companies questions): `calendar_today`, live `MAX(TransactionDate)`, `MAX(OrderDate)`, "views return only CompanyID=N" | `_honesty_preamble()` :647 — 2 gated live SQL probes |
| [9] | Calendar confirm note (if user just approved last-posting-period) | `_calendar_confirm_system_note()` |
| [10] | **user message: the question** | — |

## Phase 6 — The tool loop (`MAX_TURNS = 12`)

Each iteration:

```
tools = _active_tools(state)         # None once MAX_QUERIES=4 spent → golden rule 9
                                     # also strips doc/vault/schema tools per path caps
_stream_turn(messages, tools, gear, user_id)
  ├─ llm.complete(..., stream=True, extra_body={thinking, reasoning_effort?, user_id})
  ├─ reasoning_content deltas → accumulated, NEVER yielded
  ├─ content buffered until malformed-tool-syntax markers ruled out,
  │    then forwarded as answer_chunk SSE events
  └─ tool_call fragments reconstructed into complete calls
malformed markup in content → drop the turn silently, retry
no tool_calls → this is the FINAL answer → exit loop
else, per tool call:
  ask_user            → needs_ask done-frame, turn ends (no further LLM calls)
  run_select          → gate.validate(sql, company_id, schema_cache)
                          TOP-inject · tenant predicates · reject cross-company literals
                        sql.run_select → chatbot_ro conn w/ SESSION_CONTEXT
                        rows capped for context (50) with explicit partial-note
  run_metric/run_report/lookup_hot/introspect_schema/search_docs/
  search_schema_notes/read_schema_note/get_joins/analyze → their modules
  error (GateError or exception) → {"error": …} fed BACK to the model;
                        gate rejection counted; gear escalates t1 → t2
budget nudges injected once: "last query", doc-search cap, vault-search cap
```

Tool inventory (11): `introspect_schema, run_select, analyze, ask_user, search_docs, search_schema_notes, read_schema_note, get_joins, run_metric, run_report, lookup_hot`.

## Phase 7 — Final-answer resolution

```
blank final text AND evidence exists?
  ├─ rescue completion: gear p (pro think-high), tools=None   ← only place p may run
  ├─ still blank → deterministic Arabic stub from last_rows   (_build_arabic_stub :889)
never whitespace-with-evidence leaves the pipeline.
```

## Phase 8 — JSON answer contract (E1)

One extra `f0` completion — **`response_format={"type":"json_object"}`, NO tools param** (golden rule 9 made structural):

```json
{"answer_md": "...", "refusal": false, "confidence": "high|medium|low",
 "followups": ["سؤال متابعة؟", "..."]}
```
- `answer_md` never replaces evidence-derived text shown to the user — numbers stay verbatim from tool output.
- Parse failure → legacy envelope, followups=[] — cosmetic, can never break a turn.
- Replaces the old serial followups round-trip: net-zero LLM calls, better UX.

## Phase 9 — Envelope + persistence

```
envelope = table(_build_table from last_rows) · chart(1-label×1-numeric heuristic)
           · sources(t.* names parsed from executed SQL + doc citations)
           · followups/confidence (from contract)
persist:
  memory.set_plan(key, queries)            unless report path
  trace.log_event(answer, subject, company_id)
  trace.observe_latency histogram
  [llm] log line: gear, in/out tokens, prompt_cache_hit_tokens / cache_miss
done event → server frames: steps… answer_chunks… final envelope frame… data: [DONE]
```

## Phase 10 — Feedback loop (human-in-the-loop learning)

```
POST /feedback {session_id, helpful, reason}
  thumbs-up  → gate.validate(last answer_sql) MUST pass → promote_verified_query
                (lands in next turns' few-shot block, Phase 5 [3])
  thumbs-down → delete_plan(cache_key) + promote_negative_query (Phase 5 [4])
Unverifiable SQL is logged as feedback_invalid_sql and discarded — the pool cannot be poisoned by an unauthenticated thumbs-up alone.
```

## Prompt economics (why the layout is load-bearing)

| State | Input cost / turn (flash, off-peak) | Latency |
|---|---|---|
| Cold prefix (first turn / post-eviction) | ~59k tok × $0.22 ≈ **$0.013** | ~2–3 s provider time |
| Warm prefix (measured steady state) | 58,752 hit × $0.007 + ~160 miss ≈ **$0.0005** | **0.7–1.0 s** |

Rules that protect this: nothing dated/timestamped/count-random enters messages[0..2]; dynamic blocks strictly after; any refactor breaking byte-stability fails `test_static_prefix_is_byte_stable_across_calls`.

---

# PART 3 — INVARIANTS MAP (who enforces what)

| Golden rule | Enforcing mechanism |
|---|---|
| 1 Python 3.13 only | shebangs, run.sh, requirements header |
| 2 No SA/cds at runtime | SA creds confined to `setup/db_connect.py`; runtime factory is `core/sql.get_conn` only |
| 3 Keys never in core/api | `.env` gitignored; `DEEPSEEK_API_KEY` read solely in `core/llm.py` |
| 4 Browser cannot switch tenant | body `client` field ignored (server.py AskRequest); env pin validated at import |
| 5 One SQL path | every execution funnels `sql.run_select` → `gate.validate`; server-side raw cursors flagged for removal |
| 6 No procedure bodies returned | vault sanitizer + corpus hygiene + catalog metadata-only |
| 7 EXEC blocked | `DEFAULT_ALLOWED_PROCS=()` + regex + allow-list check in gate; templates raise on EXEC |
| 8 Cache keys include client+CompanyID | `memory.cache_key()` composition |
| 9 No tools after results | budget latch `_active_tools`→None **and** structural: contract call carries no tools |
| 10 No base-table grants | `01_readonly_login.sql`; live test `test_base_table_denied` |

---

*Generated from the post-migration codebase; regenerate line anchors after large refactors.*
