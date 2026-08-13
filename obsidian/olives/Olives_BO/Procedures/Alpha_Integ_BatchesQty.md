---
type: procedure
database: Olives_BO
name: Alpha_Integ_BatchesQty
schema: dbo
tags: [#integration]
reads_from:
  - Items
writes_to:
  - BatchsItemsInfo
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Alpha_Integ_BatchesQty

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 1 table(s); writes 1. See sections below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Items]]
## Tables Written
- [[BatchsItemsInfo]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
