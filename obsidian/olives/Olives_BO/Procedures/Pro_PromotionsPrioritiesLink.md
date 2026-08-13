---
type: procedure
database: Olives_BO
name: Pro_PromotionsPrioritiesLink
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[PromotionsHeaders]]
  - [[PromotionsPrioritiesLink]]
  - Serial
  - `dbo`
writes_to:
  - [[PromotionsPrioritiesLink]]
  - PromotionsPrioritiesLinkLog
  - Serial
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_PromotionsPrioritiesLink


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads PromotionsHeaders, PromotionsPrioritiesLink, Serial, dbo. Writes PromotionsPrioritiesLink, PromotionsPrioritiesLinkLog, Serial. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	 = null
- @PriorityID	int	= null
- @PromotionID	int	= null
- @PrioritySerial	int	= null
- @cmdType varchar(50)=null
- @LogID numeric(30,0) = null
## Tables Read
- [[PromotionsHeaders]]
- [[PromotionsPrioritiesLink]]
- Serial
- `dbo`
## Tables Written
- [[PromotionsPrioritiesLink]]
- PromotionsPrioritiesLinkLog
- Serial
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[PromotionsHeaders]]
- [[PromotionsPrioritiesLink]]
- Serial
- dbo

**Tables Written**
- [[PromotionsPrioritiesLink]]
- PromotionsPrioritiesLinkLog
- Serial

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
