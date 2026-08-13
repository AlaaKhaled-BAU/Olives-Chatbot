---
type: procedure
database: Olives_BO
name: Pro_PromotionsPriorities
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[PromotionsPriorities]]
writes_to:
  - [[PromotionsPriorities]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_PromotionsPriorities


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads PromotionsPriorities. Writes PromotionsPriorities. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint = null
- @ID	int	 = null
- @Name	nvarchar(200) = null
- @IsSuspended bit = null
- @ApplyAllNextPromotion bit = null
- @cmdType varchar(50)=null
## Tables Read
- [[PromotionsPriorities]]
## Tables Written
- [[PromotionsPriorities]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[PromotionsPriorities]]

**Tables Written**
- [[PromotionsPriorities]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
