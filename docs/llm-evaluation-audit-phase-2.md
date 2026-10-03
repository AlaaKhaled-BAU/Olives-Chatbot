# Phase 2 — Component deep dive (evaluation lens)

Per subsystem: purpose, files, I/O, invariants, **evaluation quad** (spec / automated / human-judge / gap).

See: [index](./llm-evaluation-audit-index.md) · Phase 1 · Phase 3.

---

## 2.1 API & SSE

**Files:** `api/server.py`, `static/app.js`. **Quad:** `tests/test_api.py`, `test_rate_limit.py`, `test_feedback.py`. **Gap P1:** Lab DB not in default gate.

## 2.2 Agent loop

**Files:** `ask_stream`, `_active_tools`, `_run_tool`, `MAX_QUERIES=4`. **Quad:** `tests/test_agent.py`, comprehensive battery. **Gap P0:** No trace assert on tool-null after budget.

## 2.3 Prompts & prefix

**Files:** `prompts/system.md`, `_static_prefix`, `prefix_hash`. **Gap P1:** No CI on prefix_hash; cache hits not on `/metrics`.

## 2.4 LLM gears

**Files:** `core/llm.py` `GEARS`. **Quad:** `test_llm.py`, `test_trace_usage.py`. **Gap P1:** Token budgets not in eval artifacts.

## 2.5 Doc RAG

**Files:** `core/docs.py`, `setup/05_index_docs.py`. **Quad:** `docs_accuracy.jsonl`, `docs_105_ar.jsonl`, isolation docs case.

## 2.6 SQL & tenant

**Files:** `core/sql.py`. **Quad:** `test_tenant_wall.py`, `golden_rows`, `accuracy.jsonl`. **Gap P0:** Snapshot-bound numerics.

## 2.7 Gate

**Files:** `core/gate.py`. **Quad:** `test_gate.py`, `isolation.jsonl`.

## 2.8 Catalog / EXEC

**Files:** `core/catalog.py`. Metadata only; EXEC disabled.

## 2.9 Memory

**Files:** `core/memory.py` `cache_key`. **Quad:** `test_memory_company.py`, calendar guard tests.

## 2.10 Config & tenant

**Files:** `core/config.py`, `core/params.py`, `clients/_example.yaml`.

## 2.11 Trace / metrics / usage

**Files:** `core/trace.py`, `core/usage.py`, `core/metrics.py`. **Gap P1:** Evals don't ingest `trace.jsonl`.

## 2.12 Vault vs FTS

**Files:** `core/vault.py` vs `search_docs`. MCP server not per-turn.

## 2.13 Bootstrap

**Files:** `setup/native_bootstrap.py`. **Gap P0:** Stale `work/` breaks accuracy cases.

---

## Single-turn tool inventory

| Tool | MAX_QUERIES? | Gate | Eval |
|------|--------------|------|------|
| introspect_schema | No | UX | golden |
| run_select | Yes | **gate** | isolation, golden |
| ask_user | No | server | battery |
| analyze | No | — | unit |
| search_docs | No (cap 3) | index | docs suites |
| vault tools | No (cap 3) | no bodies | weak |
| run_metric | Yes | via SQL | wave5, test_metrics |
| run_report | Yes if SQL | certified | report_alias |
| lookup_hot | No | L1 | hot_cache tests |
| recall_turns | No | transcript | battery, recall_followup |

Post-loop: `_final_contract` (f0, no tools).
