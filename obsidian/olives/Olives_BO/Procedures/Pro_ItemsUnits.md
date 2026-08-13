---
type: procedure
database: Olives_BO
name: Pro_ItemsUnits
schema: dbo
tags: [#backoffice, #inventory]
reads_from:
  - [[Items]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
writes_to:
  - [[ItemsUnits]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ItemsUnits


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, ItemsUnits, ItemsUnitsDetails. Writes ItemsUnits. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID nvarchar(50) = null
- @ItemTargetID int = null
- @Name nvarchar (200)=null
- @ShortName nvarchar (100)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (40)=null
- @ItemCode varchar(50) = null
- @Qty Float = null
- @IsIntegerQty bit=null
- @cmdType varchar(50)=null
## Tables Read
- [[Items]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
## Tables Written
- [[ItemsUnits]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]

**Tables Written**
- [[ItemsUnits]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
