---
type: procedure
database: Olives_BO
name: TechnicalFillUnfilledSalespersonsRoutes
schema: dbo
tags: [#maintenance]
reads_from:
  - Excel
writes_to:
  - SalesPersonsRoutes
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# TechnicalFillUnfilledSalespersonsRoutes

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 1 table(s); writes 1. See sections below for the full dependency map.
## Parameters
- @compno int
## Tables Read
- [[Excel]]
## Tables Written
- [[SalesPersonsRoutes]]
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
