---
type: procedure
database: Olives_BO
name: PerformanceRreportsForAlthuray
schema: dbo
tags: [#reporting]
reads_from:
  - Customers
  - CustomersClasses
  - CustomersFinancialDetails
  - Locations
  - LogActionTransaction
  - POADetails
  - POAHeader
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# PerformanceRreportsForAlthuray

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 7 table(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @TrYear int
- @TrMonth int
- @SalesmanNo int
## Tables Read
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[Locations]]
- [[LogActionTransaction]]
- [[POADetails]]
- [[POAHeader]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_GetSalesmanTreeByID`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
