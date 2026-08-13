---
type: procedure
database: Olives_BO
name: Hesabate_Integ_CreateToken
schema: dbo
tags: [#integration]
reads_from:
writes_to:
called_by:
  - Hesabate_Integ_PostToAPI
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# Hesabate_Integ_CreateToken

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — called by 1 proc(s). See sections below for the full dependency map.
## Parameters
- @Token nvarchar(MAX) OUTPUT
## Tables Read
_None_
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
- [[Hesabate_Integ_PostToAPI]]
## Callees
_None_
## When to Run

Run during API sync cycles: pulls from or pushes to an external ERP/API when new data is ready or on-demand refresh.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
