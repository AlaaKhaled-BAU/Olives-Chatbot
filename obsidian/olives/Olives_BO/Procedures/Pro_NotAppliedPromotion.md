---
type: procedure
database: Olives_BO
name: Pro_NotAppliedPromotion
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[PromotionsDontApply]]
  - [[PromotionsHeaders]]
writes_to:
  - [[PromotionsDontApply]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_NotAppliedPromotion


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads PromotionsDontApply, PromotionsHeaders. Writes PromotionsDontApply. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @PromotionID int=null
- @DontApplyPromotionID int=null
- @cmdType varchar(50)=null
## Tables Read
- [[PromotionsDontApply]]
- [[PromotionsHeaders]]
## Tables Written
- [[PromotionsDontApply]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[PromotionsDontApply]]
- [[PromotionsHeaders]]

**Tables Written**
- [[PromotionsDontApply]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
