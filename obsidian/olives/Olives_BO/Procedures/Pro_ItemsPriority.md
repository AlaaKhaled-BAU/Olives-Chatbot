---
type: procedure
database: Olives_BO
name: Pro_ItemsPriority
schema: dbo
tags: [#backoffice, #inventory]
reads_from:
  - [[Items]]
  - [[ItemsPriority]]
  - [[ItemsUnits]]
writes_to:
  - [[ItemsPriority]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ItemsPriority


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, ItemsPriority, ItemsUnits. Writes ItemsPriority. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @AutoID	bigint	= null
- @CompanyID	smallint = null
- @ItemCode	nvarchar(100) = null
- @UseInSuggestedOrder bit = null
- @UnitID	nvarchar(50)	= null
- @Qty	nchar(10)	= null
- @CustTypeID	int	= null
- @cmdType  nvarchar(50) = null
## Tables Read
- [[Items]]
- [[ItemsPriority]]
- [[ItemsUnits]]
## Tables Written
- [[ItemsPriority]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[ItemsPriority]]
- [[ItemsUnits]]

**Tables Written**
- [[ItemsPriority]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
