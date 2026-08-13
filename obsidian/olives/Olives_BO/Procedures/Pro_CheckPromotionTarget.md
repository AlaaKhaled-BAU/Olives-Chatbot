---
type: procedure
database: Olives_BO
name: Pro_CheckPromotionTarget
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[CompanyParameters]]
  - Cur_Promotions
  - [[PromotionsHeaders]]
  - [[TransactionsPromotions]]
writes_to:
  - [[PromotionsHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CheckPromotionTarget


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CompanyParameters, Cur_Promotions, PromotionsHeaders, TransactionsPromotions. Writes PromotionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
## Tables Read
- [[CompanyParameters]]
- Cur_Promotions
- [[PromotionsHeaders]]
- [[TransactionsPromotions]]
## Tables Written
- [[PromotionsHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CompanyParameters]]
- Cur_Promotions
- [[PromotionsHeaders]]
- [[TransactionsPromotions]]

**Tables Written**
- [[PromotionsHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
