---
type: procedure
database: Olives_BO
name: Rpt_RoutePerformanceAnalysis
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[Checks]]
  - [[ClientsActive]]
  - [[Companies]]
  - [[LogActionTransaction]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[Receipts]]
  - [[RequestToVisitCustomerNotInRoute]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[CustomersFinancialDetails]]
  - [[SalesPersons]]
writes_to:
called_by:
  - Rpt_RouteSummaryBySalesman_New
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_RoutePerformanceAnalysis


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, ClientsActive, Companies, LogActionTransaction, OrdersDetails, OrdersHeaders, Receipts, RequestToVisitCustomerNotInRoute, TransactionsDetails, TransactionsHeaders, CustomersFinancialDetails, SalesPersons. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @Date smalldatetime
## Tables Read
- [[Checks]]
- [[ClientsActive]]
- [[Companies]]
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[RequestToVisitCustomerNotInRoute]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[CustomersFinancialDetails]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- Rpt_RouteSummaryBySalesman_New
## Impact / Dependencies

**Tables Read**
- [[Checks]]
- [[ClientsActive]]
- [[Companies]]
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[RequestToVisitCustomerNotInRoute]]
- [[TransactionsDetails]]
- [[Transactionsheaders]]
- [[customersfinancialdetails]]
- [[salespersons]]

**Tables Written**
_None_

**Callers**
- Rpt_RouteSummaryBySalesman_New

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
