# Memory, Analyst Mode & Review-Point Fixes — Implementation Plan

Scope: review points 1/3/4/5/6 + conversation memory + analyst behavior
(future expectations & recommendations). Branch target: `deepseek-swap`.
All designs respect golden rules 5/8/9 and the byte-stable-prefix economics.

---

## TRACK A — Execution-accuracy golden set (review point 1)

Grade by comparing **result rows**, not answer wording.

| # | Change | Detail | Test |
|---|---|---|---|
| A1 | `evals/golden_rows.py` | `normalize_rows()`: ISO-str values, numeric round(2), rows sorted → deterministic tuples; `rows_equal(a,b,tol)` set-compare with numeric tolerance | hermetic: «٢٣٨» vs 238.004 equal; row-order insensitive; missing-row mismatch fails |
| A2 | Snapshot builder `evals/build_golden.py` | Executes each case's `gold_sql` once via gated `sql.run_select`, stores `{question, company_id, gold_sql, gold_rows}` into `evals/exec_golden.jsonl`; refuses to snapshot when SQL errors or >200 rows | builder dry-run prints counts; refuses EXEC |
| A3 | Runner suite `--suite golden` in run_evals.py | For each case: agent.ask → take `answer_sql` → execute gated → compare vs stored gold_rows; PASS requires row-equality AND no refusal | live suite green on seed set |
| A4 | Seed data | Export 10–15 verified pairs (from comprehensive results.json answer_sql + verified_queries where source=eval) after eyeball review | n/a |
| A5 | CI wiring note | README/AGENTS: golden + isolation suites must pass before any prompt/model/gear change lands | doc only |

Effort M. Cost per full run ≈ 2 SQL executions/question — trivial.

## TRACK B — Table-usage counters (review point 3)

| # | Change | Detail | Test |
|---|---|---|---|
| B1 | `trace.record_table_uses(client, tables)` | Prometheus Counter `chatbot_table_uses_total{client,table}`; ≤~450 label values/client — bounded, acceptable | unit: counter increments, registry scrape contains series |
| B2 | Wire in agent.py done-path | Reuse `_SOURCE_TABLE_RE` over `state["queries"]+hot_sql` (already computed for sources) — zero new parsing | fake-LLM ask asserts record called with expected set |

Effort XS.

## TRACK C — Alef normalization A/B (review point 4)

Current: trigram tokenizer + diacritics strip + «ال» strip + synonyms. Missing: أإآ→ا, ى→ي folding.

| # | Change | Detail | Test |
|---|---|---|---|
| C1 | `_unify_alef(text)` in docs.py | fold `[أإآ]→ا`, `ى→ي` (NOT ة→ه — changes meaning too often) | pure-function table test incl. mixed strings |
| C2 | Apply at BOTH sides | `_fts_query()` :314 and indexing path (`05_index_docs` chunker) — behind env `DOCS_AR_NORM=1` default-on after A/B | index+query both normalized → match fires |
| C3 | A/B harness | rebuild tmp index from same corpus with/without flag; run `evals/docs_accuracy.jsonl` + «كيف أضيف عميل»→«إضافة زبون» probe set; adopt if recall strictly ≥ baseline | script outputs side-by-side table |

Effort S. Synonym gap (عميل vs زبون) is separate — extend synonym map only if probe shows need.

## TRACK D — SSE disconnect cancellation (review point 5)

Constraint: `/ask` is a sync generator in threadpool; LLM stream blocks between chunks.

| # | Change | Detail | Test |
|---|---|---|---|
| D1 | Cancel event plumbing | `_with_heartbeat(gen, cancel)` pumps gen in thread; new async wrapper checks `await request.is_disconnected()` every queue poll → sets `threading.Event` and raises GeneratorExit | hermetic: stalled pump + disconnected flag ⇒ event set, [DONE] skipped, exception contained |
| D2 | Cooperative checks | `agent._stream_turn` accepts optional `cancel: Event`; checked every chunk + before each tool dispatch → raise `TurnCancelled`; llm stream iterator closed (SDK aborts HTTP) | fake stream of N chunks, event pre-set at k ⇒ stops ≤k+1 chunks, upstream close called |
| D3 | Server wiring | wrap generator: disconnect ⇒ cancel.set(); except TurnCancelled → silent return (no error frame to nobody) | integration-style TestClient with aborting connection |

Effort M (async/sync bridge is the fiddly part).

## TRACK E — Sessions to SQLite + documented constraint (review point 6)

| # | Change | Detail | Test |
|---|---|---|---|
| E1 | `work/sessions.sqlite` | table sessions(sid PK, client, company_id, pending_ask, last_turn_json, conv_json, touched REAL); WAL + busy_timeout; SESSIONS dict stays as hot read-cache with write-through | restart-simulation: reopen file, state survives; concurrent writers don't corrupt (WAL) |
| E2 | Sweeper | existing idle-eviction deletes rows too | expired row gone |
| E3 | Constraint doc | AGENTS.md: multi-worker allowed on one machine (sqlite shared) — NOT across machines; document explicitly | doc |

Effort S. Prerequisite for F1 (memory must survive restarts).

## TRACK F — Conversation memory + analyst mode (the feature)

### F1 — Session memory store (depends E1)

What the model sees per turn — ONE bounded system block injected AFTER static prefix, BEFORE user message:

```
## سياق المحادثة الحالية (آخر 4 أسئلة)
س1: كم مبيعات هذا الأسبوع؟ → صافي المبيعات 12,430.50 عبر 38 فاتورة.
    SQL: SELECT SUM(...) WHERE TransactionDate >= '2026-08-16' ...
س2: ... (≤220 حرف لكل سطر، أرقام رئيسية فقط)
```

| # | Change | Detail | Test |
|---|---|---|---|
| F1a | Builder `_conversation_block(session)` | last ≤4 turns: question, compressed answer (deterministic trim), executed-SQL text (≤160ch), top-3 key numbers extracted from envelope table rows (no model call) | block ≤1200 chars hard cap; empty history → omitted entirely (byte-stability of fresh sessions preserved) |
| F1b | Extraction helper | key numbers = first 3 numeric cells of envelope table + answer's own figures regex | deterministic given same envelope |
| F1c | Server wiring | append block into messages via new `agent.ask_stream(..., history=...)` param fed from session store; store turns back post-done | SSE e2e: two-turn flow, second request messages contain س1 line |
| F1d | Cache safety | block sits after all stable units → DeepSeek caches previous-turn prefix naturally (their multi-round example) — hit-rate logged to prove | soak: turn-3 hit tokens ≥ turn-2 prefix size |

### F2 — Analyst intent + gear

| # | Change | Detail | Test |
|---|---|---|---|
| F2a | `_is_analysis_intent(q)` | regexes: توقع|المتوقعة|القادم|المقبل|تحليل|اتجاه|نمو|انصحني|ماذا تفعل|خطة | table-driven unit tests ar/en |
| F2b | Gear mapping | analysis intent → initial gear t2 (think-high) even without tool errors | extends _initial_gear table |
| F2c | Series-friendly budget | analysis questions typically need GROUP BY week buckets — still 1–2 queries, MAX_QUERIES unchanged; system directive tells model to prefer bucketed series over many single-number queries | prompt-content test |

### F3 — Deterministic trend helpers (extend `analyze` tool)

Same philosophy as existing arithmetic offload (agent.py C4 comment): model never does statistics in prose.

| op | input | output |
|---|---|---|
| `trend_direction` | numeric series (oldest→newest) | up/down/flat + slope % + simple 3-point moving-average projection for next bucket, labeled ESTIMATE |
| `growth_compare` | two period sums | delta abs/% |
| `top_movers` | {label: value} dict | ranked movers vs prior dict |

Tests: known series → expected slope/projection; flat series → "flat"; division-by-zero guards. Effort S.

### F4 — Analyst prompt pack (`prompts/analyst.md`, appended only when F2a fires)

Rules baked into the pack (Arabic):
1. التوقعات مبنية على السلسلة المسترجعة فقط — اذكر الأساس («بناءً على آخر 8 أسابيع»).
2. كل رقم متوقع يُسبق بـ«تقديري» ويُذكر اتجاهه لا دقّته الزائفة.
3. الثقة في العقد: confidence ∈ {low, medium} إجباري لأي توقع؛ high ممنوع للتوقعات.
4. التوصيات بصيغة: «الملاحظة ← الدليل ← الإجراء المقترح» ولا توصية بلا دليل مسترجع.
5. إذا كانت البيانات غير كافية للاتجاه (<3 نقاط) → قل ذلك واعرض ما يمكن حسابه.

Contract call gains nothing structurally — confidence field already exists; scorer later penalizes forecast+confidence=high (add to golden runner as soft-fail note). Effort S.

### F5 — Example flow (acceptance scenario from client)

```
U1: كم مبيعات هذا الأسبوع؟        → t1 SQL (week-bucket) → 12,430 / 38 فاتورة   [stored]
U2: وأكثر صنف مبيعاً الأسبوع القادم؟
    guard order ✓ → cache skip? (relative date «القادم») ✓ honesty preamble ✓
    conversation block shows U1 context → t2
    → run_select(items grouped by week, last 6 weeks) → analyze.trend_direction
    → contract(refusal=false, confidence=low|medium, followups)
    → «تقديري بناءً على آخر 6 أسابيع: الصنف X يقود باتجاه صاعد (+9%/أسبوع)...»
```

Golden-runner addition A3 covers U1-style exactness; U2 gets a dedicated eval case with expect_contains_any + sql_must_contain(GROUP BY) — not execution-matched (it's an estimate by design).

### Residency note
Conversation blocks carry business numbers already covered by the existing cloud-egress stance — no NEW class of data leaves premises; volume grows ~1KB/turn.

## Sequencing

```
Week-shape (parallelizable lanes):
Lane 1: E (sessions sqlite) ──► F1 ──► F2/F4 ──► F5 acceptance
Lane 2: A (golden rows) standalone ──► A5 doc
Lane 3: B (counters) XS anytime
Lane 4: C (alef A/B) standalone
Lane 5: D (cancellation) standalone
```

Definition of done: pytest green incl. new suites; live two-turn analyst demo recorded; golden suite passes ≥ seed set; docs updated (blueprint Part 2 gains Phase 3.5 "conversation block", AGENTS env table gains DOCS_AR_NOLR flags).
