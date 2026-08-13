---
type: procedure
database: Olives_BO
name: Rpt_TransactionsNotes
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[Customers]]
  - [[OrdersHeaders]]
  - [[Receipts]]
  - [[ReturnOrdersHeaders]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
  - [[TransfersOrdersHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_TransactionsNotes


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, OrdersHeaders, Receipts, ReturnOrdersHeaders, SalesPersons, TransactionsHeaders, TransfersOrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int
- @FromSalesman int
- @ToSalesman int
- @FromDate smalldatetime
- @ToDate smalldatetime
- @TransactionType int
## Tables Read
- [[Customers]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[ReturnOrdersHeaders]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[ReturnOrdersHeaders]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]

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
