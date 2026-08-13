---
type: procedure
database: Olives_BO
name: Pro_ComparisonReport
schema: dbo
tags: [#reporting]
reads_from:
writes_to:
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# Pro_ComparisonReport

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — standalone procedure. See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @Supervisor nvarchar(MAX)
- @Salesperson nvarchar(MAX)
- @Customer nvarchar(MAX)
- @CustomersGroup nvarchar(MAX)
- @FromDate1 datetime
- @ToDate1 datetime
- @FromDate2 datetime
- @ToDate2 datetime
- @TaxInclude int
- @AmountQty int
- @GroupBy int
- @WithDetails bit
## Tables Read
_None_
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
