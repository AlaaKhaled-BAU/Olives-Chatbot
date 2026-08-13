---
type: procedure
database: Olives_BO
name: RPT_CoverageandFrequencybysalesmanByCompany
schema: dbo
tags: [#reporting]
reads_from:
  - Customers
  - CustomersFinancialDetails
  - CustomersGroups
  - CustomersTypes
  - Locations
  - LogActionTransaction
  - SalesPersons
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# RPT_CoverageandFrequencybysalesmanByCompany

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 7 table(s); calls 2 proc(s). See sections below for the full dependency map.
## Parameters
- @FromDate smalldatetime
- @ToDate smalldatetime
- @CompanyIdVal int
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGroups]]
- [[CustomersTypes]]
- [[Locations]]
- [[LogActionTransaction]]
- [[SalesPersons]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_CalcSalesmanCoverage`
- `Fun_GetSalesmanTreeByID`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
