---
type: procedure
database: Olives_BO
name: Rpt_SalesmanSummaryRoute_Dandana
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[LogActionTransaction]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[Receipts]]
  - [[SalesPersons]]
  - [[SalesPersonsRoutes]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanSummaryRoute_Dandana


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, CustomersFinancialDetails, LogActionTransaction, OrdersDetails, OrdersHeaders, Receipts, SalesPersons, SalesPersonsRoutes, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=1
- @FromDate smalldatetime='2024-10-2'
- @ToDate smalldatetime = '2024-10-2'
- @FromSalesman int=159
- @ToSalesman int=159
- @GPSVisit BIT =1
- @FromSuperVisor int=1
- @ToSuperVisor	int=9999
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
