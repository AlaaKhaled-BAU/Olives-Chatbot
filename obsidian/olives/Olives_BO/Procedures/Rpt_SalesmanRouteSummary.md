---
type: procedure
database: Olives_BO
name: Rpt_SalesmanRouteSummary
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[CustomersFinancialDetails]]
  - [[LogActionTransaction]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[SalesPersonsRoutes]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanRouteSummary


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersFinancialDetails, LogActionTransaction, OrdersHeaders, SalesPersons, SalesPersonsGroups, SalesPersonsRoutes, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 2
- @FromDate smalldatetime = '2022-09-01'
- @ToDate smalldatetime = '2022-09-26'
- @FromSalesman int = 0
- @ToSalesman int = 99999
## Tables Read
- [[CustomersFinancialDetails]]
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
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
- [[CustomersFinancialDetails]]
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
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
