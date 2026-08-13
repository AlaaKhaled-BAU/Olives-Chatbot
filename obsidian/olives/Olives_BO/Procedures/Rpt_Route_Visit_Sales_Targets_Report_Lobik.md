---
type: procedure
database: Olives_BO
name: Rpt_Route_Visit_Sales_Targets_Report_Lobik
schema: dbo
tags: [#reporting]
reads_from:
  - ClientsActive
  - CustomersFinancialDetails
  - LogActionTransaction
  - RoutesInformation
  - SalesPersonTargets
  - SalesPersons
  - SalesPersonsRoutes
  - TransactionsDetails
  - TransactionsHeaders
writes_to:
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Rpt_Route_Visit_Sales_Targets_Report_Lobik

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 9 table(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @FromSalesmanNo int
- @ToSalesmanNo int
- @FromDate smalldatetime
- @ToDate smalldatetime
## Tables Read
- [[ClientsActive]]
- [[CustomersFinancialDetails]]
- [[LogActionTransaction]]
- [[RoutesInformation]]
- [[SalesPersonTargets]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_GetWeekNo`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
