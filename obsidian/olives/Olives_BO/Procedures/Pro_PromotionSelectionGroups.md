---
type: procedure
database: Olives_BO
name: Pro_PromotionSelectionGroups
schema: dbo
tags: [#backoffice, #reference, #sales]
reads_from:
  - [[PromotionSelectionGroups]]
  - [[PromotionSelectionGroupsLink]]
  - [[PromotionsHeaders]]
writes_to:
  - [[PromotionSelectionGroups]]
  - [[PromotionSelectionGroupsLink]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_PromotionSelectionGroups


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads PromotionSelectionGroups, PromotionSelectionGroupsLink, PromotionsHeaders. Writes PromotionSelectionGroups, PromotionSelectionGroupsLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID int = null
- @PromoID int = null
- @Name nvarchar (100)=null
- @Reference1 nvarchar (50)=null
- @Reference2 nvarchar (50)=null
- @IsMaster bit = null
- @cmdType varchar(50)=null
## Tables Read
- [[PromotionSelectionGroups]]
- [[PromotionSelectionGroupsLink]]
- [[PromotionsHeaders]]
## Tables Written
- [[PromotionSelectionGroups]]
- [[PromotionSelectionGroupsLink]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[PromotionSelectionGroups]]
- [[PromotionSelectionGroupsLink]]
- [[PromotionsHeaders]]

**Tables Written**
- [[PromotionSelectionGroups]]
- [[PromotionSelectionGroupsLink]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
