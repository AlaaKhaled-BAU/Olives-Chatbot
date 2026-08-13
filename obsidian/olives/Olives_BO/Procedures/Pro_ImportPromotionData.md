---
type: procedure
database: Olives_BO
name: Pro_ImportPromotionData
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[PromotionsCondUnCodInput]]
  - [[PromotionsCondUnCodOutput]]
  - [[PromotionsCustomersGroupsLink]]
  - [[PromotionsHeaders]]
  - [[PromotionsRangeInput]]
  - [[PromotionsSalesmanGroupsLink]]
  - cursorName
  - `dbo`
writes_to:
  - ImportPromotionData_Log
  - [[PromotionsCondUnCodInput]]
  - [[PromotionsCondUnCodOutput]]
  - [[PromotionsCustomersGroupsLink]]
  - [[PromotionsHeaders]]
  - [[PromotionsRangeInput]]
  - [[PromotionsSalesmanGroupsLink]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ImportPromotionData


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads PromotionsCondUnCodInput, PromotionsCondUnCodOutput, PromotionsCustomersGroupsLink, PromotionsHeaders, PromotionsRangeInput, PromotionsSalesmanGroupsLink, cursorName, dbo. Writes ImportPromotionData_Log, PromotionsCondUnCodInput, PromotionsCondUnCodOutput, PromotionsCustomersGroupsLink, PromotionsHeaders, PromotionsRangeInput, PromotionsSalesmanGroupsLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
- @ID int = null
- @Name nvarchar(200)= NULL
- @PromotionDeatils nvarchar(200) =NULL
- @StartDate smalldatetime =NULL
- @EndDate smalldatetime =NULL
- @ItemCode bigint =NULL
- @ItemUnitID nvarchar(200)= NULL
- @FromQuantity int= NULL
- @OutputQuantity int= NULL
## Tables Read
- [[PromotionsCondUnCodInput]]
- [[PromotionsCondUnCodOutput]]
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- [[PromotionsRangeInput]]
- [[PromotionsSalesmanGroupsLink]]
- cursorName
- `dbo`
## Tables Written
- ImportPromotionData_Log
- [[PromotionsCondUnCodInput]]
- [[PromotionsCondUnCodOutput]]
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- [[PromotionsRangeInput]]
- [[PromotionsSalesmanGroupsLink]]
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
- [[PromotionsRangeInput]]
- [[PromotionsSalesmanGroupsLink]]
- cursorName
- dbo

**Tables Written**
- ImportPromotionData_Log
- [[PromotionsCondUnCodInput]]
- [[PromotionsCondUnCodOutput]]
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- [[PromotionsRangeInput]]
- [[PromotionsSalesmanGroupsLink]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
