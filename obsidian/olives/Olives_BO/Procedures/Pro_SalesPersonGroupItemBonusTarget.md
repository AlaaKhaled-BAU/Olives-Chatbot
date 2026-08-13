---
type: procedure
database: Olives_BO
name: Pro_SalesPersonGroupItemBonusTarget
schema: dbo
tags: [#backoffice, #inventory, #reference, #sales]
reads_from:
  - [[Items]]
  - [[ItemsGroupBonusTarget]]
  - [[SalesPersonGroupItemBonusTarget]]
  - [[SalesPersonsGroups]]
writes_to:
  - [[SalesPersonGroupItemBonusTarget]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesPersonGroupItemBonusTarget


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, ItemsGroupBonusTarget, SalesPersonGroupItemBonusTarget, SalesPersonsGroups. Writes SalesPersonGroupItemBonusTarget. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @Source smallint=null,  -- 1 = Items , 2 = Items Groups
- @SalesPersonID int = null
- @TargetYear int = null
- @ItemCode varchar(50)=null
- @UnitID varchar(50)=null
- @M1 int = null,@M2 int = null
- @M3 int = null,@M4 int = null
- @M5 int = null,@M6 int = null
- @M7 int = null,@M8 int = null
- @M9 int = null,@M10 int = null
- @M11 int = null,@M12 int = null
- @cmdType varchar(50)=null
## Tables Read
- [[Items]]
- [[ItemsGroupBonusTarget]]
- [[SalesPersonGroupItemBonusTarget]]
- [[SalesPersonsGroups]]
## Tables Written
- [[SalesPersonGroupItemBonusTarget]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[ItemsGroupBonusTarget]]
- [[SalesPersonGroupItemBonusTarget]]
- [[SalesPersonsGroups]]

**Tables Written**
- [[SalesPersonGroupItemBonusTarget]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
