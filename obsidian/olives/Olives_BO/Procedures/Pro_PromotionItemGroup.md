---
type: procedure
database: Olives_BO
name: Pro_PromotionItemGroup
schema: dbo
tags: [#backoffice, #inventory, #reference, #sales]
reads_from:
  - [[Items]]
  - [[PromotionItemGroups]]
writes_to:
  - [[PromotionItemGroups]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_PromotionItemGroup


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, PromotionItemGroups. Writes PromotionItemGroups. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID int = null
- @Name nvarchar(50) = null
- @ShortName nvarchar(50) = null
- @Reference1 nvarchar(100)=null
- @Reference2 nvarchar(100)=null
- @cmdType varchar(50)=null
## Tables Read
- [[Items]]
- [[PromotionItemGroups]]
## Tables Written
- [[PromotionItemGroups]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[PromotionItemGroups]]

**Tables Written**
- [[PromotionItemGroups]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
