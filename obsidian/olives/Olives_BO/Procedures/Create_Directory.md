---
type: procedure
database: Olives_BO
name: Create_Directory
schema: dbo
tags: [#maintenance]
reads_from:
writes_to:
called_by:
  - Write_Files
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# Create_Directory

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — called by 1 proc(s). See sections below for the full dependency map.
## Parameters
- @path varchar(8000)
- @output tinyint OUTPUT
## Tables Read
_None_
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
- [[Write_Files]]
## Callees
_None_
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
