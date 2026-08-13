---
type: procedure
database: Olives_BO
name: Rpt_RoutesAvg
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[LogActionTransaction]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
  - [[SalesPersonsRoutes]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_RoutesAvg


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, LogActionTransaction, OrdersHeaders, SalesPersons, SalesPersonsRoutes, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromDate smalldatetime='2023-01-01'
- @ToDate smalldatetime='2023-01-31'
- @FromSalesman int=56
- @ToSalesman int =56
- @FromGroup int=0
- @ToGroup int =999999
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
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
