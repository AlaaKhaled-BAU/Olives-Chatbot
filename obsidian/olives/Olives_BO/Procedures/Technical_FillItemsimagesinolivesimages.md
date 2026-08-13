---
type: procedure
database: Olives_BO
name: Technical_FillItemsimagesinolivesimages
schema: dbo
tags: [#maintenance]
reads_from:
  - Items
writes_to:
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# Technical_FillItemsimagesinolivesimages

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 1 table(s). See sections below for the full dependency map.
## Parameters
- @compno int
## Tables Read
- [[Items]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Maintenance/one-off fix: run under DBA supervision; verify row counts before and after.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
