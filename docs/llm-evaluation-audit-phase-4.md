# Phase 4 — LLM-evaluation synthesis (full system)

Read-only. Phases 1–3: sibling docs in this folder.

---

## 4.1 Executive summary

**Architecture health:** Control flow is layered (HTTP → agent → gate → `t.*` views). Safety-critical paths are **code-enforced** (gate, tenant views, empty EXEC allow-list, catalog deny-by-default, docs index entitlement). Model behavior is **shaped** by routers, tool caps, and prompts—but up to **four** business queries per turn remain possible (C4), so “single SQL then answer” is not a hard invariant.

**Eval maturity vs surface:** Strong on **isolation** (design) and **substring/row-golden** NL2SQL for pinned DB snapshots; weak on **trace-driven regression**, **gear/cost**, **vault tool order**, and **HTTP vs in-process parity**. Many `*_results.json` files are **partial or stale** relative to their jsonl corpora.

**Top 3 P0 risks:** (1) Eval/ops assume frozen `work/` + DB—silent accuracy drift. (2) `isolation` not stored as artifact—security posture unknown without fresh run. (3) Doc drift (blueprint CompanyID `needs_ask` vs UI pin) misleads operators and eval authors.

**Top 3 quick wins:** (1) Commit baseline `run_evals.py` log + `git_sha` in CI. (2) Export `Usage.totals()` + `prefix_hash` into eval result JSON. (3) Pre-merge watchlist in CI (agent, gate, llm, prompts, isolation.jsonl).

---

## 4.2 Automated metrics — system-wide

**BLEU/ROUGE/BERTScore:** **Reject** for this product (Arabic ERP, numeric grounding). Prefer structured checks.

| Capability | Measure | Existing | Missing |
|------------|---------|----------|---------|
| Docs RAG | `expect_contains`, `source_must_match`, Precision@K on chunk id | docs suites | chunk-id metric |
| NL2SQL | `rows_equal`, `answer_sql_must_contain` | golden, wave5 | per-table grain rules in harness |
| Routing | `tools_prefer`, `expect_report`, `doc_search_max` | comprehensive battery | default gate |
| Memory | `must_recall`, transcript length | battery, adversarial | — |
| Gate | block rate, 0 rows | isolation | taxonomy in trace |
| Locale AR | per-lang pass in docs | docs_accuracy | morphology beyond probes |
| Gears | gear per call | `Usage.calls` in trace | Prometheus / eval rollup |
| Cost/latency | tokens, `tools_ms`, turn latency | trace, histogram | dashboard |

**Custom metrics to add:** groundedness vs doc chunk ids; SQL allow-list compliance; row-hash match (golden); tool-sequence legality (`queries` count ≤4, no tools after budget); `prefix_hash` regression; `doc_search_count` ≤3.

---

## 4.3 Human evaluation playbook

Stratified sampling: docs-only, metric path, ad-hoc SQL, report, visit past/plan, analyst forecast, multi-turn recall, company switch.

Rubrics (1–5): factual correctness, grain honesty, Arabic fluency, citation quality, refusal appropriateness.

Journeys: Arabic ERP manager (wave5-like), company scope via dropdown, follow-up pronouns (`والمقارنة؟`).

---

## 4.4 LLM-as-judge (design only)

| Subsystem | Judge helps | Forbidden inputs |
|-----------|-------------|------------------|
| Docs | Citation supports claim | Full schema, SQL rows |
| NL2SQL prose | Grounded in table | Other companies’ data |
| Analyst | Estimate labeled | Raw proc bodies |

Pairwise: t1 vs t2 on same question. Pointwise: refusal vs hallucination. No judge execution in audit session.

---

## 4.5 Security & isolation first-class

P0 metrics: isolation pass rate 100%; cross-tenant row count 0; `GateError` on EXEC; docs cross-client retrieval 0; cache key includes `company_id`.

Map: `SESSION_CONTEXT` + gate tenant preds + `memory.cache_key` ↔ `isolation.jsonl` cases.

---

## 4.6 Observability → eval loop

Today: `work/trace.jsonl` + Prometheus (`chatbot_requests_total`, latency, cache hits, gate rejections, table uses). Gap: evals do not consume traces; no `cache_hit_tokens` on `/metrics`.

```mermaid
flowchart LR
  T[trace.jsonl] -.->|not wired| E[eval regression]
  P[/metrics] -.->|not wired| E
  E --> R[run_evals + golden]
```

---

## 4.7 Release gate (humans run later)

Ordered:

1. `python3.13 -m pytest tests/test_gate.py tests/test_tenant_wall.py`
2. `python3.13 evals/run_evals.py --suite isolation`
3. `python3.13 evals/run_evals.py` (accuracy, docs, wave5)
4. `python3.13 evals/run_evals.py --suite golden`
5. Optional: comprehensive battery, adversarial (uvicorn), stress70

**P0:** any isolation leak; gate/tenant test fail. **P1:** wave5/docs regression; golden row mismatch.

**Pre-merge watchlist:** `core/agent.py`, `core/gate.py`, `core/llm.py`, `core/sql.py`, `prompts/`, `evals/isolation.jsonl`, `evals/wave5_accuracy.jsonl`.

---

## 4.8 Baseline & backlog

| Suite | Baseline (stored) | Capability |
|-------|-------------------|------------|
| isolation | run required | security |
| wave5 | re-run | AR NL2SQL |
| golden | 5 cases client 105 | row truth |
| feature_adversarial | 24 PASS 2026-08-29 | HTTP+session |
| comprehensive battery | 9/69 partial | memory/routing |
| stress70 | ~94% per report | stress |

**P0 backlog:** trace-ingest eval; snapshot id in results; fix blueprint CompanyID narrative.

**P1:** tool-budget legality assert; gear/token gate; vault sequence cases.

**P2:** KV metric; chunk-id docs metric.

---

## 4.9 Doc/code drift

| Doc | Code today | Eval impact |
|-----|------------|-------------|
| AGENTS.md golden rule 6 “no tools after results” | C4: up to 4 queries, then tools=None | Tests should assert budget not boolean latch |
| AGENTS.md “FTS not vault at runtime” | `core/vault.py` tools wired | Evals should cover vault path |
| SYSTEM_BLUEPRINT Phase 1 CompanyID needs_ask | UI dropdown + block company ask_user | Battery `must_not_ask_company` not blueprint flow |
| FIXPLAN M1 bearer auth | `CHATBOT_CLIENT` pin only | Pilot threat model doc vs code |
| isolation 10 vs 11 lines | jsonl has 11 cases | FIXPLAN count stale |
