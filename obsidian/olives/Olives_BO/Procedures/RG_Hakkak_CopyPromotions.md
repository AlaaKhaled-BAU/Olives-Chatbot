---
type: procedure
database: Olives_BO
name: RG_Hakkak_CopyPromotions
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[PromotionsCondUnCodInput]]
  - [[PromotionsCondUnCodOutput]]
  - [[PromotionsCustomersGroupsLink]]
  - [[PromotionsHeaders]]
  - [[PromotionsPriorities]]
  - [[PromotionsPrioritiesLink]]
  - [[PromotionsRangeInput]]
  - [[PromotionsSalesmanGroupsLink]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# RG_Hakkak_CopyPromotions


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads PromotionsCondUnCodInput, PromotionsCondUnCodOutput, PromotionsCustomersGroupsLink, PromotionsHeaders, PromotionsPriorities, PromotionsPrioritiesLink, PromotionsRangeInput, PromotionsSalesmanGroupsLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @FromCompNo int = 1
- @ToCompNo int =2
## Tables Read
- [[PromotionsCondUnCodInput]]
- [[PromotionsCondUnCodOutput]]
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- [[PromotionsPriorities]]
- [[PromotionsPrioritiesLink]]
- [[PromotionsRangeInput]]
- [[PromotionsSalesmanGroupsLink]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[PromotionsCondUnCodInput]]
- [[PromotionsCondUnCodOutput]]
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- [[PromotionsPriorities]]
- [[PromotionsPrioritiesLink]]
- [[PromotionsRangeInput]]
- [[PromotionsSalesmanGroupsLink]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
