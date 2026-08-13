---
type: procedure
database: Olives_BO
name: BaladInsertrtLoadHeadersintoTransactionstyp6
schema: dbo
tags: [#backoffice, #order]
reads_from:
  - [[TransactionsHeaders]]
  - [[TransfersOrdersHeaders]]
writes_to:
  - [[TransactionsHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# BaladInsertrtLoadHeadersintoTransactionstyp6


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads TransactionsHeaders, TransfersOrdersHeaders. Writes TransactionsHeaders. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int
- @VouType int
- @OrderYear int
- @SalesPersonID int
- @OrderNo int
## Tables Read
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]
## Tables Written
- [[TransactionsHeaders]]
## Callers
- [[Pro_TransfersOrdersHeaders]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]

**Tables Written**
- [[TransactionsHeaders]]

**Callers**
_None_

**Callees**
- [[Pro_TransfersOrdersHeaders]]


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
