# TODOs

## Later metrics (transfers, collections $, aging)

- **What:** After the first `run_metric` pack (net sales, returns, orders, van stock, CFD assignment), add grains from `knowledge/reference/tables summary.md`: `TransfersOrdersHeaders/Details`, receipt amounts vs invoiced amounts, CFD aging/credit buckets.
- **Why:** Accountant general use includes تحصيل vs مبيعات and van load/unload, not only invoices. Live H07/H08 already showed receipts-vs-invoices is a real question.
- **Pros:** Completes tables-summary coverage without EXEC of Rpt_*.
- **Cons:** More cards delay the Arabic accuracy gate if built in the same slice.
- **Context:** First pack is locked by eng review (2026-08-14): `run_metric` + tenant pack + Arabic Wave 5. Do not expand until that gate is green on client 105 / CompanyID 2.
- **Depends on:** `core/metrics.py` (or equivalent) shipping and Arabic evals passing.
- **Source:** /plan-eng-review D8 → 7A
