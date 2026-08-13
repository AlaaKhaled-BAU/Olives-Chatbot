---
type: procedure
database: Olives_BO
name: Rpt_RoutePerformanceAnalysis_Spartan
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[Checks]]
  - [[ClientsActive]]
  - [[LogActionTransaction]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[Receipts]]
  - [[SalesPersonsGroups]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[CustomersFinancialDetails]]
  - [[SalesPersons]]
writes_to:
called_by:
  - [[Rpt_RouteSummaryBySalesman]]
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_RoutePerformanceAnalysis_Spartan


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, ClientsActive, LogActionTransaction, OrdersDetails, OrdersHeaders, Receipts, SalesPersonsGroups, TransactionsDetails, TransactionsHeaders, CustomersFinancialDetails, SalesPersons. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @Date smalldatetime='2022-04-25'
- @fromSalespersonID int =1
- @ToSalespersonID int =9999
- @FromGroupID int=5
- @ToGroupID int=5
- @UserID nvarchar(50) = 'admin'
- @WithTax bit = 1
## Tables Read
- [[Checks]]
- [[ClientsActive]]
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[SalesPersonsGroups]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[CustomersFinancialDetails]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[Rpt_RouteSummaryBySalesman]]
## Impact / Dependencies

**Tables Read**
- [[Checks]]
- [[ClientsActive]]
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[SalesPersonsGroups]]
- [[TransactionsDetails]]
- [[Transactionsheaders]]
- [[customersfinancialdetails]]
- [[salespersons]]

**Tables Written**
_None_

**Callers**
- [[Rpt_RouteSummaryBySalesman]]

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
