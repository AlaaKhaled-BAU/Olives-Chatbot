---
type: procedure
database: Olives_BO
name: Pro_Items
schema: dbo
tags: [#backoffice, #inventory]
reads_from:
  - [[CatalogMedia]]
  - [[ClientsActive]]
  - [[CompanyParameters]]
  - Fun_ConvArrayToTable
  - Fun_GetCategoryTreeByID
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[OrdersDetails]]
  - [[PriceListDetails]]
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersonItemsBalance]]
  - [[SalespersonCustStockItemsTargetLink]]
  - [[SalespersonTargetReferenceFocusItem]]
writes_to:
  - [[Items]]
  - ItemsImages
  - [[SalespersonCustStockItemsTargetLink]]
  - [[SalespersonTargetReferenceFocusItem]]
called_by:
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Items-Master-Data-Setup
---
# Pro_Items


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CatalogMedia, ClientsActive, CompanyParameters, Fun_ConvArrayToTable, Fun_GetCategoryTreeByID, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, OrdersDetails, PriceListDetails, SalesPersonItemsAssignment, SalesPersonItemsBalance, SalespersonCustStockItemsTargetLink, SalespersonTargetReferenceFocusItem. Writes Items, ItemsImages, SalespersonCustStockItemsTargetLink, SalespersonTargetReferenceFocusItem. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ItemCode nvarchar(20) = null
- @Name nvarchar (200)=null
- @ForeginName nvarchar (200)=null
- @ShortName nvarchar (100)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (100)=null
- @Barcode nvarchar(20) =null
- @CategCode nvarchar(max) =null
- @UnitID nvarchar(50)=null
- @FillSize nvarchar(50)=null
- @MinimumStock float=null
- @IsExpiry bit=null
- @ValidityDays int=null
- @Volume float=null
- @Weight float=null
- @IsSuspended bit=null
- @ItemImage image=null
- @TargetReferenceID int=null
- @SubTargetReferenceID int=null
- @QtyInAllStores money=null
- @cmdType varchar(50)=null
- @pricelist nvarchar(max) =null
- @IsTaxExempt Bit= Null
- @ItemReplacementGroup int = null
- @ItemBonusTargetGroupID int = null
- @SuggestGroupID int =null
- @ItemOrderInList int = null
- @ClassID int = null
- @SalespersonID int = null
- @ToSalesman int = null
- @Year int = null
- @Month int = null
- @UsedInUploadOrder bit = null
- @BasketItemNo nvarchar(100) =null
- @ItemQtyStatus nvarchar(50) =null
- @BasketVolume float =null
- @IsBasketItem bit = null
- @IsBatchItem bit = null
- @PromotionItemGroupID int = null
- @VanCustodyUnitSerial int = null
- @IsCashOnly smallint = null
## Tables Read
- [[CatalogMedia]]
- [[ClientsActive]]
- [[CompanyParameters]]
- Fun_ConvArrayToTable
- Fun_GetCategoryTreeByID
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[OrdersDetails]]
- [[PriceListDetails]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersonItemsBalance]]
- [[SalespersonCustStockItemsTargetLink]]
- [[SalespersonTargetReferenceFocusItem]]
## Tables Written
- [[Items]]
- ItemsImages
- [[SalespersonCustStockItemsTargetLink]]
- [[SalespersonTargetReferenceFocusItem]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CatalogMedia]]
- [[ClientsActive]]
- [[CompanyParameters]]
- Fun_ConvArrayToTable
- Fun_GetCategoryTreeByID
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[OrdersDetails]]
- [[PriceListDetails]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersonItemsBalance]]
- [[SalespersonCustStockItemsTargetLink]]
- [[SalespersonTargetReferenceFocusItem]]

**Tables Written**
- [[Items]]
- ItemsImages
- [[SalespersonCustStockItemsTargetLink]]
- [[SalespersonTargetReferenceFocusItem]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
