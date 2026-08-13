---
type: procedure
database: Olives_BO
name: TransactionsBounsBatch
schema: dbo
tags: [#backoffice]
reads_from:
  - TransactionsBatchsItemsInfo
  - TransactionsDetails
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# TransactionsBounsBatch

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 2 table(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompNo smallint
- @TransactionTypeID int
- @TransactionNo int
- @TransactionYear smallint
## Tables Read
- [[TransactionsBatchsItemsInfo]]
- [[TransactionsDetails]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `GetItemOrgUnitQty`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
