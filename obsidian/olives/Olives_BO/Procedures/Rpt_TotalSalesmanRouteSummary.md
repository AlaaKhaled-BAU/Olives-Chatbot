---
type: procedure
database: Olives_BO
name: Rpt_TotalSalesmanRouteSummary
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[CustomersFinancialDetails]]
  - LUXintegratopn
  - [[LogActionTransaction]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[Receipts]]
  - [[SalesPersons]]
  - [[SalesPersonsRoutes]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_TotalSalesmanRouteSummary


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersFinancialDetails, LUXintegratopn, LogActionTransaction, OrdersDetails, OrdersHeaders, Receipts, SalesPersons, SalesPersonsRoutes, TransactionsDetails, TransactionsHeaders, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
- @FromDate smalldatetime = '2022-01-17'
- @ToDate smalldatetime = '2022-04-17'
- @FromSalesman int = 3003
- @ToSalesman int = 3003
## Tables Read
- [[CustomersFinancialDetails]]
- LUXintegratopn
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomersFinancialDetails]]
- LUXintegratopn
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- dbo

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
