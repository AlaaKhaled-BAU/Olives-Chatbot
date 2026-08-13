---
type: procedure
database: Olives_BO
name: Pro_PromotionsCondUnCodInput
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[CompanyParameters]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[PromotionItemGroups]]
  - [[PromotionsCondUnCodInput]]
  - [[PromotionsHeaders]]
  - `dbo`
writes_to:
  - [[PromotionsCondUnCodInput]]
  - PromotionsCondUnCodInputLog
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_PromotionsCondUnCodInput


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CompanyParameters, Items, ItemsUnits, PromotionItemGroups, PromotionsCondUnCodInput, PromotionsHeaders, dbo. Writes PromotionsCondUnCodInput, PromotionsCondUnCodInputLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @PromotionID INT = null
- @Quantity float = null
- @ItemCode nvarchar(20) = null
- @ItemUnitID nvarchar(50) = null
- @cmdType varchar(50)=null
- @ItemSerial int = null
- @InputType smallint = null
- @ToQuantity float = null
- @NotDouble bit = null
- @StartDate smalldatetime = null
- @EndDate smalldatetime = null
- @LogID numeric(30,0)=null
- @OpType smallint = null
- @PromotionItemGroupID int = null
## Tables Read
- [[CompanyParameters]]
- [[Items]]
- [[ItemsUnits]]
- [[PromotionItemGroups]]
- [[PromotionsCondUnCodInput]]
- [[PromotionsHeaders]]
- `dbo`
## Tables Written
- [[PromotionsCondUnCodInput]]
- PromotionsCondUnCodInputLog
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CompanyParameters]]
- [[Items]]
- [[ItemsUnits]]
- [[PromotionItemGroups]]
- [[PromotionsCondUnCodInput]]
- [[PromotionsHeaders]]
- dbo

**Tables Written**
- [[PromotionsCondUnCodInput]]
- PromotionsCondUnCodInputLog

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
