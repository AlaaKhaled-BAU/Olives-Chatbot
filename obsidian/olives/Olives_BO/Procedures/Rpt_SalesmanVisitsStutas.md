---
type: procedure
database: Olives_BO
name: Rpt_SalesmanVisitsStutas
schema: dbo
tags: [#reporting]
reads_from:
  - Customers
  - CustomersFinancialDetails
  - CustomersTypes
  - LogActionTransaction
  - RoutesInformation
  - SalesPersons
  - SalesPersonsRoutes
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Rpt_SalesmanVisitsStutas

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 7 table(s); calls 3 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @SalesmanNo int
- @WorkDay smalldatetime
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[LogActionTransaction]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_GetSalesmanTotalAmountByCustomer`
- `Fun_GetSalesmanTreeByID`
- `Fun_GetWeekNo`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
