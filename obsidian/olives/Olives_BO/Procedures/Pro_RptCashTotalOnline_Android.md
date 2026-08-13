---
type: procedure
database: Olives_BO
name: Pro_RptCashTotalOnline_Android
schema: dbo
tags: [#backoffice, #mobile]
reads_from:
  - [[Checks]]
  - [[ClientsActive]]
  - [[Customers]]
  - [[Receipts]]
  - [[Receipts_PaidTrans]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_RptCashTotalOnline_Android


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, ClientsActive, Customers, Receipts, Receipts_PaidTrans, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=2
- @SalesPersonID smallint=4
- @FromDate smalldatetime = '2019-02-13'
- @ToDate smalldatetime = '2019-02-13'
## Tables Read
- [[Checks]]
- [[ClientsActive]]
- [[Customers]]
- [[Receipts]]
- [[Receipts_PaidTrans]]
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
- [[ClientsActive]]
- [[Customers]]
- [[Receipts]]
- [[Receipts_PaidTrans]]
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
