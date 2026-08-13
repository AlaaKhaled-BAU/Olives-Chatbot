---
type: procedure
database: Olives_BO
name: Technical_CopyRoutesCustomersFromPositiontoposition
schema: dbo
tags: [#maintenance]
reads_from:
writes_to:
  - CustomersFinancialDetails
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# Technical_CopyRoutesCustomersFromPositiontoposition

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — writes 1; calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @compno int
- @from_p int
- @To_p int
## Tables Read
_None_
## Tables Written
- [[CustomersFinancialDetails]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_Get_Salesmen_AssignedRoutesperWeek`
## When to Run

Maintenance/one-off fix: run under DBA supervision; verify row counts before and after.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
