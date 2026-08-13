---
type: procedure
database: Olives_BO
name: Pro_PromotionsRangeInput
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[Items]]
  - [[ItemsUnits]]
  - [[PromotionsRangeInput]]
  - `dbo`
writes_to:
  - [[PromotionsRangeInput]]
  - PromotionsRangeInputLog
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_PromotionsRangeInput


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, ItemsUnits, PromotionsRangeInput, dbo. Writes PromotionsRangeInput, PromotionsRangeInputLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @PromotionID INT = null
- @ItemCode nvarchar(20) = null
- @ItemUnitID nvarchar(50) = null
- @FromQuantity float = null
- @ToQuantity float = null
- @OutputQuantity float = null
- @cmdType varchar(50)=null
- @LogID numeric(30,0)=null
- @OpType smallint = null
## Tables Read
- [[Items]]
- [[ItemsUnits]]
- [[PromotionsRangeInput]]
- `dbo`
## Tables Written
- [[PromotionsRangeInput]]
- PromotionsRangeInputLog
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[ItemsUnits]]
- [[PromotionsRangeInput]]
- dbo

**Tables Written**
- [[PromotionsRangeInput]]
- PromotionsRangeInputLog

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
