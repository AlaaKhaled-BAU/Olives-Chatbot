---
type: procedure
database: Olives_BO
name: Pro_PromotionsCondUnCodOutput
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[ClientsActive]]
  - [[CompanyParameters]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[PriceListDetails]]
  - [[PromotionsCondUnCodInput]]
  - [[PromotionsCondUnCodOutput]]
  - [[PromotionsHeaders]]
  - `dbo`
writes_to:
  - [[PromotionsCondUnCodOutput]]
  - PromotionsCondUnCodOutputLog
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_PromotionsCondUnCodOutput


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CompanyParameters, Items, ItemsUnits, PriceListDetails, PromotionsCondUnCodInput, PromotionsCondUnCodOutput, PromotionsHeaders, dbo. Writes PromotionsCondUnCodOutput, PromotionsCondUnCodOutputLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @PromotionID INT = null
- @ItemCode nvarchar(20) = null
- @ItemUnitID nvarchar(50) = null
- @Quantity float = 0
- @cmdType varchar(50)=null
- @ItemSerial int = null
- @OutPutType int = null
- @DiscountType smallint = null
- @LogID numeric(30,0)=null
- @OpType smallint = null
- @StartDate smalldatetime = null
- @EndDate smalldatetime = null
- @IsConditional bit = false
## Tables Read
- [[ClientsActive]]
- [[CompanyParameters]]
- [[Items]]
- [[ItemsUnits]]
- [[PriceListDetails]]
- [[PromotionsCondUnCodInput]]
- [[PromotionsCondUnCodOutput]]
- [[PromotionsHeaders]]
- `dbo`
## Tables Written
- [[PromotionsCondUnCodOutput]]
- PromotionsCondUnCodOutputLog
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[CompanyParameters]]
- [[Items]]
- [[ItemsUnits]]
- [[PriceListDetails]]
- [[PromotionsCondUnCodInput]]
- [[PromotionsCondUnCodOutput]]
- [[PromotionsHeaders]]
- dbo

**Tables Written**
- [[PromotionsCondUnCodOutput]]
- PromotionsCondUnCodOutputLog

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
