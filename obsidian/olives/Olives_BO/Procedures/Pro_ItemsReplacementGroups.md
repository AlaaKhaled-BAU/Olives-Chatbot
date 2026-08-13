---
type: procedure
database: Olives_BO
name: Pro_ItemsReplacementGroups
schema: dbo
tags: [#backoffice, #inventory, #reference]
reads_from:
  - [[ItemsReplacementGroups]]
writes_to:
  - [[ItemsReplacementGroups]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ItemsReplacementGroups


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ItemsReplacementGroups. Writes ItemsReplacementGroups. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	=null
- @ID	int	=null
- @Name	nvarchar(100)	=null
- @ShortName	nvarchar(50)	=null
- @Reference1	nvarchar(20)	=null
- @Reference2	nvarchar(20)	=null
- @cmdType nvarchar(50) = null
## Tables Read
- [[ItemsReplacementGroups]]
## Tables Written
- [[ItemsReplacementGroups]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ItemsReplacementGroups]]

**Tables Written**
- [[ItemsReplacementGroups]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
