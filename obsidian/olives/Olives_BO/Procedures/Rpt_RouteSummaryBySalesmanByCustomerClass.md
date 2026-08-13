---
type: procedure
database: Olives_BO
name: Rpt_RouteSummaryBySalesmanByCustomerClass
schema: dbo
tags: [#backoffice, #customer, #gps, #reference, #reporting, #sales]
reads_from:
  - CSales
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersClasses]]
  - [[CustomersFinancialDetails]]
  - [[LogActionTransaction]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[Receipts]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[SalesPersonsRoutes]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_RouteSummaryBySalesmanByCustomerClass


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CSales, ClientsActive, Customers, CustomersClasses, CustomersFinancialDetails, LogActionTransaction, OrdersDetails, OrdersHeaders, Receipts, RoutesInformation, SalesPersons, SalesPersonsRoutes, TransactionsDetails, TransactionsHeaders. Invoked by 3 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
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
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
- [[Rpt_RouteSummaryBySalesmanByCustomerClassCombine]]
- [[Rpt_RouteSummaryBySalesmanByCustomerClassCombine2]]
- [[SalesmenRoutesummery_Range_forExcel]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- CSales
- [[ClientsActive]]
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
- [[Rpt_RouteSummaryBySalesmanByCustomerClassCombine]]
- [[Rpt_RouteSummaryBySalesmanByCustomerClassCombine2]]
- [[SalesmenRoutesummery_Range_forExcel]]


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
