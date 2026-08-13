---
type: procedure
database: Olives_BO
name: Pro_ItemsSuggestGroup
schema: dbo
tags: [#backoffice, #inventory, #reference]
reads_from:
  - [[ItemsSuggestGroup]]
  - `dbo`
writes_to:
  - [[ItemsSuggestGroup]]
  - ItemsSuggestGroupImages
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ItemsSuggestGroup


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ItemsSuggestGroup, dbo. Writes ItemsSuggestGroup, ItemsSuggestGroupImages. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID int = null
- @Name nvarchar (200)=null
- @UnitID nvarchar(100) = null
- @Qty float = null
- @ShortName nvarchar (20)= null
- @ItemImage Image = null
- @cmdType varchar(50)=null
## Tables Read
- [[ItemsSuggestGroup]]
- `dbo`
## Tables Written
- [[ItemsSuggestGroup]]
- ItemsSuggestGroupImages
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ItemsSuggestGroup]]
- dbo

**Tables Written**
- [[ItemsSuggestGroup]]
- ItemsSuggestGroupImages

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
