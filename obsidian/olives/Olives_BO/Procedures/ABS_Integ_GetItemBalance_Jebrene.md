---
type: procedure
database: Olives_BO
name: ABS_Integ_GetItemBalance_Jebrene
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - OPENJSON
  - [[SalesPersons]]
  - `dbo`
  - [[Items]]
writes_to:
  - [[OT_StoreItemsQty]]
called_by:
  - [[ABS_Integ_GetDataFromAPI]]
support_relevance: high
last_verified: 2026-07-05
---
# ABS_Integ_GetItemBalance_Jebrene


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads OPENJSON, SalesPersons, dbo, Items. Writes OT_StoreItemsQty. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @SalespersonID int
## Tables Read
- OPENJSON
- [[SalesPersons]]
- `dbo`
- [[Items]]
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
- [[items]]

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
