---
type: procedure
database: Olives_BO
name: ABS_Integ_GetDataFromAPI_Injaz
schema: dbo
tags: [#integration]
reads_from:
writes_to:
called_by:
  - ABS_Integ_GetAllStoresBalances_Injaz
  - ABS_Integration_Injaz
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# ABS_Integ_GetDataFromAPI_Injaz

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — called by 2 proc(s). See sections below for the full dependency map.
## Parameters
- @ReqDataName nvarchar(1000)
- @JSONResult nvarchar(MAX) OUTPUT
## Tables Read
_None_
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
- [[ABS_Integ_GetAllStoresBalances_Injaz]]
- [[ABS_Integration_Injaz]]
## Callees
_None_
## When to Run

Run during API sync cycles: pulls from or pushes to an external ERP/API when new data is ready or on-demand refresh.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
