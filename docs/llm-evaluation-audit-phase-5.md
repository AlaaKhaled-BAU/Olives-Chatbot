# Phase 5 — Targeted recommendations (no implementation)

Read-only recommendations spanning **architecture + measurement**. Full narrative and diagrams: chat 2026-10-03.

Index: [llm-evaluation-audit-index.md](./llm-evaluation-audit-index.md).

---

## Top 5 gaps (summary)

| # | Gap | Change types | Phase 2 subsystems |
|---|-----|--------------|-------------------|
| 1 | No reproducible eval baseline (DB/schema/git) | harness + metric | 13 bootstrap, 3 eval map |
| 2 | Query-budget / tool-null invariants not in release gate | harness + trace | 2 agent, 11 observability |
| 3 | Trace/Prometheus not wired to regression | metric + harness | 11 trace/usage |
| 4 | Doc drift (CompanyID, tool-budget story) | doc + harness cases | 1 API, 10 config |
| 5 | NL2SQL semantics (sign/grain) beyond row-hash | metric + prompt + golden | 6 SQL, 7 gate, metrics |

---

## Gap 1 — Reproducible eval baseline

**Problem:** Numeric suites bind to a specific DB snapshot; `comprehensive_system_battery_results.json` ran 9/69 cases with no recorded schema id — false confidence.

**Subsystems:** 13 setup/bootstrap, Phase 3 eval map.

**Changes:** harness — `eval_manifest` in battery/`run_evals` output: `git_sha`, `prefix_hash`, `schema_version`, client, optional DB fingerprint.

**Patterns:** Extend `comprehensive_system_battery_results.json` summary; mirror `trace.GIT_SHA`.

**Validation:** Re-run battery twice on same snapshot → identical pass set; after `setup/refresh.py` → manifest `schema_version` changes.

---

## Gap 2 — Query-budget legality in CI

**Problem:** C4 allows 4 queries then `tools=None`; not asserted in default gate (AGENTS.md still says single-latch story).

**Subsystems:** 2 agent, 11 trace.

**Changes:** harness — parse `queries` from trace or instrument `ask_stream` done payload; metric `tool_sequence_legal`.

**Patterns:** New `evals/tool_budget.jsonl` with `expect_max_queries`, `expect_tools_ms_keys`; or pytest on mocked multi-`run_select` trace.

**Validation:** Case with 5th `run_select` must fail harness; golden path ≤4 passes.

---

## Gap 3 — Trace → regression loop

**Problem:** Rich `trace.jsonl` unused by evals; no SLO on refusal/gate/latency.

**Subsystems:** 11 trace/metrics/usage.

**Changes:** harness `evals/aggregate_trace.py`; metric — optional Prometheus `cache_hit_tokens` sum.

**Patterns:** Read JSONL like stress report aggregates; compare to baseline file in `evals/baselines/`.

**Validation:** Inject synthetic trace lines → aggregator flags regression; `/metrics` scrape after one `/ask`.

---

## Gap 4 — Doc/operator drift (CompanyID + vault)

**Problem:** Blueprint describes `needs_ask` company list; code uses UI pin. AGENTS says FTS-only runtime; vault tools wired.

**Subsystems:** 1 API, 3 prompts, 10 config, 12 vault.

**Changes:** doc — SYSTEM_BLUEPRINT Phase 0–1; harness — battery `must_not_ask_company` in default wave5 sample.

**Patterns:** `comprehensive_system_battery.jsonl` `sess-co-*`, `nl2sql-scope-01`.

**Validation:** Manual test from updated blueprint only dropdown; adversarial company-ask case PASS.

---

## Gap 5 — NL2SQL semantics (sign / grain / presentation)

**Problem:** stress70 B02: SQL correct-ish, negative qty as “top sellers”; substring/golden miss presentation.

**Subsystems:** 6 SQL, 7 gate, metrics, 3 prompts.

**Changes:** metric — `top_items` certified template; prompt guard on quantity sign; golden row + answer rubric flag.

**Patterns:** `exec_golden.jsonl` + `golden_rows`; `stress70` category B; `gate.invoice_grain_error` pattern.

**Validation:** Re-run stress B02 + new golden; human rubric on ABS/sort direction.

---

## Follow-up prompts

- **A** — Implement highest-impact measurability (eval manifest + battery metadata).
- **B** — Run live batteries mapped to architecture steps.
- **C** — Deep dive agent loop + eval traceability.
