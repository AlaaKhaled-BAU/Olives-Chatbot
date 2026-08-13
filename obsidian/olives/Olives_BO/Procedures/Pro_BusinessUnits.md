---
type: procedure
database: Olives_BO
name: Pro_BusinessUnits
schema: dbo
tags: [#backoffice, #inventory]
reads_from:
  - [[BusinessUnits]]
  - Level
writes_to:
  - [[BusinessUnits]]
  - Level
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_BusinessUnits


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads BusinessUnits, Level. Writes BusinessUnits, Level. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID smallint = null
- @Parent smallint = null
- @Name nvarchar (200)=null
- @ShortName nvarchar (100)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (40)=null
- @Level int = null
- @PositionsID int = null
- @RouteID int = null
- @CompanyBrancheID int =null
- @cmdType varchar(50)=null
## Tables Read
- [[BusinessUnits]]
- Level
## Tables Written
- [[BusinessUnits]]
- Level
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[BusinessUnits]]
- Level

**Tables Written**
- [[BusinessUnits]]
- Level

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
