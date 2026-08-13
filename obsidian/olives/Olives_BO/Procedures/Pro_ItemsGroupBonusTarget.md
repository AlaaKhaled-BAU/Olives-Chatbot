---
type: procedure
database: Olives_BO
name: Pro_ItemsGroupBonusTarget
schema: dbo
tags: [#backoffice, #inventory, #reference, #sales]
reads_from:
  - [[ItemsGroupBonusTarget]]
writes_to:
  - [[ItemsGroupBonusTarget]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ItemsGroupBonusTarget


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ItemsGroupBonusTarget. Writes ItemsGroupBonusTarget. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID int = null
- @Name nvarchar (100)=null
- @ShortName nvarchar (10)=null
- @Reference1 nvarchar (20)=null
- @Reference2 nvarchar (20)=null
- @cmdType varchar(50)=null
## Tables Read
- [[ItemsGroupBonusTarget]]
## Tables Written
- [[ItemsGroupBonusTarget]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ItemsGroupBonusTarget]]

**Tables Written**
- [[ItemsGroupBonusTarget]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
