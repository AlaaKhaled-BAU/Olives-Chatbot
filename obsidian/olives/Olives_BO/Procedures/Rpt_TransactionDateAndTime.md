---
type: procedure
database: Olives_BO
name: Rpt_TransactionDateAndTime
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[OrdersHeaders]]
  - [[ReturnOrdersHeaders]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_TransactionDateAndTime


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads OrdersHeaders, ReturnOrdersHeaders, SalesPersons, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromDate smalldatetime='2015-10-01'
- @ToDate smalldatetime='2025-01-01'
- @FromSalesman int=0
- @ToSalesman int=3003
- @TransType int=2
## Tables Read
- [[OrdersHeaders]]
- [[ReturnOrdersHeaders]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OrdersHeaders]]
- [[ReturnOrdersHeaders]]
- [[SalesPersons]]
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
