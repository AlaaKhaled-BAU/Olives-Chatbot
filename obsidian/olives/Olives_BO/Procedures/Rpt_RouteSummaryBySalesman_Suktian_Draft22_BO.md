---
type: procedure
database: Olives_BO
name: Rpt_RouteSummaryBySalesman_Suktian_Draft22_BO
schema: dbo
tags: [#reporting]
reads_from:
  - ClientsActive
  - Customers
  - CustomersClasses
  - CustomersFinancialDetails
  - CustomersTypes
  - LogActionTransaction
  - NoTransactionsReasons
  - OrdersDetails
  - OrdersHeaders
  - PriceLists
  - Receipts
  - RoutesInformation
  - SalesPersons
  - SalesPersonsGroups
  - SalespersonRouteByDate
  - TransactionsDetails
  - TransactionsHeaders
writes_to:
called_by:
  - Rpt_RouteSummaryBySalesmanCombine_SukhtianForPWPI_22_BO
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Rpt_RouteSummaryBySalesman_Suktian_Draft22_BO

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 17 table(s); called by 1 proc(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate smalldatetime
- @SalesmanNo int
- @WithTax bit
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[LogActionTransaction]]
- [[NoTransactionsReasons]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PriceLists]]
- [[Receipts]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[SalespersonRouteByDate]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
- [[Rpt_RouteSummaryBySalesmanCombine_SukhtianForPWPI_22_BO]]
## Callees
- `Fun_GetWeekNo`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
