---
type: procedure
database: Olives_BO
name: Hesabate_Integ_PostToAPI
schema: dbo
tags: [#integration]
reads_from:
  - Items
writes_to:
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# Hesabate_Integ_PostToAPI

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 1 table(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @Cmd nvarchar(100)
- @JSONResult nvarchar(MAX) OUTPUT
## Tables Read
- [[Items]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- [[Hesabate_Integ_CreateToken]]
## When to Run

Run during API sync cycles: pulls from or pushes to an external ERP/API when new data is ready or on-demand refresh.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
