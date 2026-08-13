---
type: procedure
database: Olives_BO
name: Shamel_Integ_GetItemsBalance
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - OPENJSON
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
  - [[Items]]
writes_to:
  - [[SalesPersonItemsBalance]]
called_by:
  - [[Shamel_Integ_GetDataFromAPI]]
  - sp_OACreate
  - sp_OADestroy
  - sp_OAGetProperty
  - sp_OAMethod
support_relevance: high
last_verified: 2026-07-05
---
# Shamel_Integ_GetItemsBalance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads OPENJSON, SalesPersonItemsBalance, SalesPersons, Items. Writes SalesPersonItemsBalance. Calls 5 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
- @SalesmanNo int = 6
## Tables Read
- OPENJSON
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[Items]]
## Tables Written
- [[SalesPersonItemsBalance]]
## Callers
_None (no known callers)_
## Callees
- [[Shamel_Integ_GetDataFromAPI]]
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod
## Impact / Dependencies

**Tables Read**
- OPENJSON
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[items]]

**Tables Written**
- [[SalesPersonItemsBalance]]

**Callers**
- [[Shamel_Integ_GetDataFromAPI]]
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod

**Callees**
_None_


## When to Run This

Run when pulling data from an external API/system. Called during sync cycles or on-demand data refresh.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
