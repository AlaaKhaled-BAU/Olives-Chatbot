---
type: procedure
database: Olives_BO
name: Technical_CheckRouteCount
schema: dbo
tags: [#maintenance]
reads_from:
  - CustomersFinancialDetails
  - Excel
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Technical_CheckRouteCount

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 2 table(s). See sections below for the full dependency map.
## Parameters
- @compno int
## Tables Read
- [[CustomersFinancialDetails]]
- [[Excel]]
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
