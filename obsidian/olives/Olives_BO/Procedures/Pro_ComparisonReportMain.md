---
type: procedure
database: Olives_BO
name: Pro_ComparisonReportMain
schema: dbo
tags: [#reporting]
reads_from:
  - Customers
  - Items
  - ItemsCategories
  - LogActionTransaction
  - SalesPersons
  - TransactionsDetails
  - TransactionsHeaders
writes_to:
called_by:
  - Pro_ComparisonReport
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Pro_ComparisonReportMain

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 7 table(s); called by 1 proc(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @Supervisor nvarchar(MAX)
- @Salesperson nvarchar(MAX)
- @Customer nvarchar(MAX)
- @CustomersGroup nvarchar(MAX)
- @FromDate datetime
- @ToDate datetime
- @TaxInclude int
- @AmountQty int
- @GroupBy int
- @WithDetails bit
## Tables Read
- [[Customers]]
- [[Items]]
- [[ItemsCategories]]
- [[LogActionTransaction]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
- [[Pro_ComparisonReport]]
## Callees
- `SplitString`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
