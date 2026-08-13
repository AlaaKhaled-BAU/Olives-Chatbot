---
type: procedure
database: Olives_BO
name: ABS_Integ_GetItemBalance
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - OPENJSON
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[OT_StoreItemsQty]]
called_by:
  - [[ABS_Integ_GetDataFromAPI]]
support_relevance: high
last_verified: 2026-07-05
---
# ABS_Integ_GetItemBalance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads OPENJSON, SalesPersons, dbo. Writes OT_StoreItemsQty. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @SalespersonID int=3003
## Tables Read
- OPENJSON
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[OT_StoreItemsQty]]
## Callers
_None (no known callers)_
## Callees
- [[ABS_Integ_GetDataFromAPI]]
## Impact / Dependencies

**Tables Read**
- OPENJSON
- [[SalesPersons]]
- dbo

**Tables Written**
- [[OT_StoreItemsQty]]

**Callers**
- [[ABS_Integ_GetDataFromAPI]]

**Callees**
_None_


## When to Run This

Run when pulling data from an external API/system. Called during sync cycles or on-demand data refresh.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
