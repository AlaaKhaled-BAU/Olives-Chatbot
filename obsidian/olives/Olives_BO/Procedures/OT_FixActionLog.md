---
type: procedure
database: Olives_BO
name: OT_FixActionLog
schema: dbo
tags: [#backoffice, #log, #mobile]
reads_from:
  - LogAction
  - [[LogActionTransaction]]
  - [[OrdersHeaders]]
  - [[Receipts]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
writes_to:
  - [[LogActionTransaction]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_FixActionLog


## Purpose
Maintenance and reconciliation procedure in Olives_BO that repairs and links missing action log entries with back-office transactional documents.
- **Trigger**: Automatically executed prior to running combined supervisor route and performance reports (such as `Rpt_SalesmanDaySummaryCombine` and `Rpt_RouteSummaryBySalesman*`).
- **Outcome**: Reconciles orphan or unlinked document actions in `LogActionTransaction` against actual posted headers in `OrdersHeaders`, `TransactionsHeaders`, and `Receipts` for a given salesman and date range, ensuring visit durations and document counts are aligned before reporting.
## Parameters
- @CompanyID int
- @SalesmanNo int
- @FromDate smalldatetime
## Tables Read
- LogAction
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
## Tables Written
- [[LogActionTransaction]]
## Callers
- [[Rpt_RouteSummaryBySalesmanByCustomerClassCombine]]
- [[Rpt_RouteSummaryBySalesmanByCustomerClassCombine2]]
- [[Rpt_RouteSummaryBySalesmanCombine_Merchandisers]]
- [[Rpt_SalesmanDaySummaryCombine]]
- [[Rpt_SalesmanTimeSpentPerCustomer4Combine]]
- [[SalesmenRoutesummery_Range_forExcel]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- LogAction
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[SalesPersons]]
- [[TransactionsHeaders]]

**Tables Written**
- [[LogActionTransaction]]

**Callers**
_None_

**Callees**
- [[Rpt_RouteSummaryBySalesmanByCustomerClassCombine]]
- [[Rpt_RouteSummaryBySalesmanByCustomerClassCombine2]]
- [[Rpt_RouteSummaryBySalesmanCombine_Merchandisers]]
- [[Rpt_SalesmanDaySummaryCombine]]
- [[Rpt_SalesmanTimeSpentPerCustomer4Combine]]
- [[SalesmenRoutesummery_Range_forExcel]]


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
