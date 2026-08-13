---
type: procedure
database: Olives_BO
name: RPT_coverageandfrequency
schema: dbo
tags: [#reporting]
reads_from:
  - Customers
  - CustomersFinancialDetails
  - CustomersGroups
  - CustomersTypes
  - Locations
  - LogActionTransaction
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# RPT_coverageandfrequency

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 6 table(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @Salesman int
- @FromDate smalldatetime
- @ToDate smalldatetime
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGroups]]
- [[CustomersTypes]]
- [[Locations]]
- [[LogActionTransaction]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_GetSalesmanTreeByID`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
