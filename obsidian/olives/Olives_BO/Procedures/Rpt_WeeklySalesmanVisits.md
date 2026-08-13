---
type: procedure
database: Olives_BO
name: Rpt_WeeklySalesmanVisits
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[LogActionTransaction]]
  - [[SalesPersons]]
  - [[SalesPersonsRoutes]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - x
writes_to:
  - x
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_WeeklySalesmanVisits


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, CustomersFinancialDetails, LogActionTransaction, SalesPersons, SalesPersonsRoutes, TransactionsDetails, TransactionsHeaders, x. Writes x. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int=1
- @SalesmanNo int=4010
- @FromDate datetime  = '2021-08-1'
- @ToDate smalldatetime = '2021-08-30'
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[LogActionTransaction]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- x
## Tables Written
- x
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
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- x

**Tables Written**
- x

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
