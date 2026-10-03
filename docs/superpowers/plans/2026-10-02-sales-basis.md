# Sales money: fix the default, teach the variants in the playbook

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Certified sales totals stop using `Quantity * Price`. Other readings (before tax, after returns) come from a short paragraph in the join playbook the model already has in cache.

**Architecture:** `core/metrics.py` owns one charged-line expression and the four builders call it. `prompts/join_playbook.md` is appended into the stable system prefix (`core/agent.py` `_static_prefix`). That paragraph is how the model learns to vary `run_select` when the user names another reading. No phrase table, no new `basis` tool argument, no vault edit. The Obsidian vault is not on the answer path. Runtime docs search is FTS over `knowledge/`, and schema SQL turns already carry the playbook.

**Tech Stack:** Python 3.13, pytest. No DeepSeek calls. No new services.

## Global Constraints

- Python 3.13 only. SQL through `core/metrics.py` and the existing gate. No `dbo`, no `EXEC`.
- Do not add `resolve_basis`, a phrase tuple, or a `basis` parameter. Decision 2026-10-02: plan A.
- `Price` is the extended line amount and already includes tax. Do not multiply by `Quantity`. Do not add `TaxAmount` on top of `Price`.
- Charged line, the new default for `net_sales` and the other three builders:

`ABS(td.Price) - ABS(td.DiscountAmount) - ABS(td.VoucherDiscount) - ABS(ISNULL(td.CustomerDiscountAmount,0))`

- Type 1, `ISNULL(IsVoid,0) = 0` stays as it is.
- `432.58` is the old July product. Recompute the golden charged total with a read-only query. Do not keep the old number.
- Do not read `CompanyParameters.PriceWithTax` or system option 499.

## Decision

```
question ──► run_metric (مبيعات) ──► charged line SQL     (code, one formula)
         └─► run_select            ──► model reads playbook paragraph
                                      before tax: also subtract ABS(TaxAmount)
                                      after returns: type 1 charged minus type 2 charged
```

Vault notes stay out. A note there is not read on a normal sales question.

---

### Task 1: One charged expression, four call sites

**Files:** `core/metrics.py`, `tests/test_metrics.py`

Call sites today, all `Quantity * Price`:

- `net_sales` (~line 157)
- `net_sales_by_salesperson` (~line 172)
- `sales_pipeline` invoiced amount (~line 234)
- `daily_sales_pack` sales value, returns value, top item by value (~lines 266, 268, 287)

- [ ] Failing test: `build_sql("net_sales", company_id=2)` contains `ABS(td.Price)`, `ABS(td.DiscountAmount)`, `ABS(td.VoucherDiscount)`, `CustomerDiscountAmount`, and does not contain `Quantity *`.
- [ ] Add `line_amount_sql(alias)` and use it in all four builders. Keep the output column name `gross_amount` so existing readers of that key still parse. `daily_sales_pack` quantity ranking stays `ABS(Quantity)`. Its value columns use `line_amount_sql`.
- [ ] `python3.13 -m pytest tests/test_metrics.py -q`

### Task 2: Playbook paragraph

**Files:** `prompts/join_playbook.md`

- [ ] Under the Invoice section, add one short block, no new file:

`TransactionsDetails.Price` is the line total, tax included. Do not multiply `Price` by `Quantity`.

Charged total (default, what `run_metric` `net_sales` returns): `ABS(Price)` minus `ABS(DiscountAmount)` minus `ABS(VoucherDiscount)` minus `ABS(ISNULL(CustomerDiscountAmount,0))`, type 1, not void.

Before tax, only when the user says قبل الضريبة / بدون ضريبة / before tax: that charged total minus `ABS(TaxAmount)`. Do not add `TaxAmount1` or `TaxAmount2`.

After returns, only when the user says بعد المرتجعات / net of returns: type 1 charged minus the same expression on type 2.

«صافي» alone means the charged total, not "minus returns".

- [ ] Do not duplicate this arithmetic in `prompts/system.md`. The playbook is already concatenated into the cached prefix.

### Task 3: Golden number

**Files:** `evals/exec_golden.jsonl`, `tests/test_memory_analyst.py`, `docs/SYSTEM_BLUEPRINT.md`

- [ ] Read-only: company 2, July 2025, type 1, not void, sum of the charged expression. Replace the `g03` gold SQL and the `432.58` row with that result.
- [ ] Point `tests/test_memory_analyst.py` at the new literal, or drop the literal if the test is only about tolerance.
- [ ] Blueprint row for net sales: one sentence that the default is the charged line (after discounts, tax inside the price). Variants are playbook readings, not extra metrics.
- [ ] `python3.13 -m pytest tests/test_metrics.py tests/test_agent.py tests/test_memory_analyst.py -q`
- [ ] Do not run the 69-question battery. Do not call DeepSeek.

## Out of scope

- Phrase resolver, `basis` argument, new metric names.
- Obsidian vault edits.
- `dbo.Rpt_*` procedure bodies.
- Rejecting free-form `Quantity * Price` inside the gate. The playbook is the control. A later reject can be added if evals show the model still multiplies.

## GSTACK REVIEW REPORT

| Run | Status | Findings |
|---|---|---|
| plan-eng-review 2026-10-02 | accepted A | Phrase table cut. Playbook paragraph plus metric SQL fix kept. |

VERDICT: proceed with plan A. User chose A in chat.

NO UNRESOLVED DECISIONS
