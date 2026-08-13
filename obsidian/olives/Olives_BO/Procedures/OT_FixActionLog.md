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
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads LogAction, LogActionTransaction, OrdersHeaders, Receipts, SalesPersons, TransactionsHeaders. Writes LogActionTransaction. Invoked by 6 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
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
