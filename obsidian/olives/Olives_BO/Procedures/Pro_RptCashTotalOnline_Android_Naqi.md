---
type: procedure
database: Olives_BO
name: Pro_RptCashTotalOnline_Android_Naqi
schema: dbo
tags: [#backoffice, #mobile]
reads_from:
  - [[Checks]]
  - [[Customers]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[Receipts]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_RptCashTotalOnline_Android_Naqi


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, Customers, Items, ItemsUnits, Receipts, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @SalesPersonID smallint=3003
- @FromDate smalldatetime = '2010-02-13'
- @ToDate smalldatetime = '2019-02-13'
## Tables Read
- [[Checks]]
- [[Customers]]
- [[Items]]
- [[ItemsUnits]]
- [[Receipts]]
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
- [[Checks]]
- [[Customers]]
- [[Items]]
- [[ItemsUnits]]
- [[Receipts]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
