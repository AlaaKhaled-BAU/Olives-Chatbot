---
type: procedure
database: Olives_BO
name: AlAmeen_Integ
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Customers]]
  - [[Items]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
  - [[TransactionsTypes]]
  - `dbo`
writes_to:
  - [[Customers]]
  - [[Items]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[TransactionsTypes]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# AlAmeen_Integ


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Items, SalesPersons, TransactionsHeaders, TransactionsTypes, dbo. Writes Customers, Items, SalesPersons, TransactionsDetails, TransactionsHeaders, TransactionsTypes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[Customers]]
- [[Items]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[TransactionsTypes]]
- `dbo`
## Tables Written
- [[Customers]]
- [[Items]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsTypes]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[Items]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[TransactionsTypes]]
- dbo

**Tables Written**
- [[Customers]]
- [[Items]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsTypes]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
