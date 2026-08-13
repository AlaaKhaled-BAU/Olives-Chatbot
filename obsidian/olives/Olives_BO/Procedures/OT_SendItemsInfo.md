---
type: procedure
database: Olives_BO
name: OT_SendItemsInfo
schema: dbo
tags: [#backoffice, #inventory, #mobile]
reads_from:
  - 168
  - [[Companies]]
  - [[CustomersFinancialDetails]]
  - DataBaseAccSqlExport
  - Fun_GetItemsConvertRates
  - GCI
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsPriority]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[PriceListDetails]]
  - [[PromotionsCondUnCodInput]]
  - [[PromotionsHeaders]]
  - [[PromotionsSalesmanGroupsLink]]
writes_to:
  - [[Items]]
  - [[OT_ItemsMF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_SendItemsInfo


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads 168, Companies, CustomersFinancialDetails, DataBaseAccSqlExport, Fun_GetItemsConvertRates, GCI, Items, ItemsCategories, ItemsPriority, ItemsUnits, ItemsUnitsDetails, PriceListDetails, PromotionsCondUnCodInput, PromotionsHeaders, PromotionsSalesmanGroupsLink. Writes Items, OT_ItemsMF. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @ClientActive smallint
- @SalesmanNo int
- @PositionsID int
## Tables Read
- 168
- [[Companies]]
- [[CustomersFinancialDetails]]
- DataBaseAccSqlExport
- Fun_GetItemsConvertRates
- GCI
- [[Items]]
- [[ItemsCategories]]
- [[ItemsPriority]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[PriceListDetails]]
- [[PromotionsCondUnCodInput]]
- [[PromotionsHeaders]]
- [[PromotionsSalesmanGroupsLink]]
## Tables Written
- [[Items]]
- [[OT_ItemsMF]]
## Callers
- [[OT_SendSalesmanData]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- 168
- [[Companies]]
- [[CustomersFinancialDetails]]
- DataBaseAccSqlExport
- Fun_GetItemsConvertRates
- GCI
- [[Items]]
- [[ItemsCategories]]
- [[ItemsPriority]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[PriceListDetails]]
- [[PromotionsCondUnCodInput]]
- [[PromotionsHeaders]]
- [[PromotionsSalesmanGroupsLink]]

**Tables Written**
- [[Items]]
- [[OT_ItemsMF]]

**Callers**
_None_

**Callees**
- [[OT_SendSalesmanData]]


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
