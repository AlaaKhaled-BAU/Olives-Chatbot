---
type: procedure
database: Olives_BO
name: ABS_Integ_GetAllStoresBalances_Injaz
schema: dbo
tags: [#integration]
reads_from:
writes_to:
  - StoresBalances
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# ABS_Integ_GetAllStoresBalances_Injaz

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — writes 1. See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
## Tables Read
_None_
## Tables Written
- [[StoresBalances]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Run during API sync cycles: pulls from or pushes to an external ERP/API when new data is ready or on-demand refresh.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
