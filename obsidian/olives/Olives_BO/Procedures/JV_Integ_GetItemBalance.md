---
type: procedure
database: Olives_BO
name: JV_Integ_GetItemBalance
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - [[Items]]
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# JV_Integ_GetItemBalance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, SalesPersonItemsBalance, SalesPersons, dbo. Writes SalesPersonItemsBalance, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[Items]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pulling data from an external API/system. Called during sync cycles or on-demand data refresh.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
