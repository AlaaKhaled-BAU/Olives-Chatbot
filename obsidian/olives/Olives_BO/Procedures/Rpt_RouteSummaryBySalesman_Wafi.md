---
type: procedure
database: Olives_BO
name: Rpt_RouteSummaryBySalesman_Wafi
schema: dbo
tags: [#reporting]
reads_from:
  - ClientsActive
  - Customers
  - CustomersClasses
  - CustomersFinancialDetails
  - CustomersTypes
  - Items
  - Locations
  - LogActionTransaction
  - NoTransactionsReasons
  - OrdersDetails
  - OrdersHeaders
  - PriceLists
  - Receipts
  - ReturnOrdersDetails
  - ReturnOrdersHeaders
  - RoutesInformation
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
# Rpt_RouteSummaryBySalesman_Wafi

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 20 table(s); calls 2 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID_ smallint
- @FromDate_ smalldatetime
- @SalesmanNo_ int
- @WithTax_ bit
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[Locations]]
- [[LogActionTransaction]]
- [[NoTransactionsReasons]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PriceLists]]
- [[Receipts]]
- [[ReturnOrdersDetails]]
- [[ReturnOrdersHeaders]]
- [[RoutesInformation]]
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
- `GetOrderNote`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
