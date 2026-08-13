---
type: procedure
database: Olives_BO
name: Rpt_RouteSummaryBySalesman
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - CSales
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
  - [[ReturnOrdersDetails]]
  - [[ReturnOrdersHeaders]]
  - [[RoutesInformation]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Targets-and-Performance
---
# Rpt_RouteSummaryBySalesman


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CSales, ClientsActive, Customers, CustomersClasses, CustomersFinancialDetails, CustomersTypes, LogActionTransaction, NoTransactionsReasons, OrdersDetails, OrdersHeaders, PriceLists, Receipts, ReturnOrdersDetails, ReturnOrdersHeaders, RoutesInformation. Invoked by 7 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate smalldatetime
- @SalesmanNo int
- @WithTax bit = 1
## Tables Read
- CSales
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
- [[ReturnOrdersDetails]]
- [[ReturnOrdersHeaders]]
- [[RoutesInformation]]
## Tables Written
_None_
## Callers
- [[Rpt_RoutePerformanceAnalysis_Spartan]]
- [[Rpt_RouteSummaryBySalesmanCombine]]
- [[Rpt_RouteSummaryBySalesmanCombineforExcel]]
- [[Rpt_RouteSummaryBySalesmanCombineforExcel_Bushnaq]]
- [[RPT_RoutesummarybysalesmancompineExcel2]]
- [[Rpt_RouteVisitsByWeekDayforExcel]]
- [[Rpt_TimeManagement]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- CSales
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
- [[ReturnOrdersDetails]]
- [[ReturnOrdersHeaders]]
- [[RoutesInformation]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
- [[Rpt_RoutePerformanceAnalysis_Spartan]]
- [[Rpt_RouteSummaryBySalesmanCombine]]
- [[Rpt_RouteSummaryBySalesmanCombineforExcel]]
- [[Rpt_RouteSummaryBySalesmanCombineforExcel_Bushnaq]]
- [[RPT_RoutesummarybysalesmancompineExcel2]]
- [[Rpt_RouteVisitsByWeekDayforExcel]]
- [[Rpt_TimeManagement]]


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
