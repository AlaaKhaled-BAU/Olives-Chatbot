---
type: procedure
database: Olives_BO
name: Pro_PriceListDetails
schema: dbo
tags: [#backoffice, #billing]
reads_from:
  - [[ClientsActive]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[PriceListDetails]]
  - [[PriceLists]]
writes_to:
  - [[PriceListDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - PriceList-Management
---
# Pro_PriceListDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Items, ItemsUnits, ItemsUnitsDetails, PriceListDetails, PriceLists. Writes PriceListDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=null
- @PriceListID smallint = null
- @ItemCode nvarchar (20)=null
- @UnitID nvarchar(50) =null
- @Price float (40)=null
- @TaxType int =null
- @Tax float = null
- @DiscountPercent float =null
- @UseInReturn bit = null
- @UseInSales bit = null
- @SellPrice2 float (40)=null
- @SellPrice3 float (40)=null
- @cmdType varchar(50)=null
## Tables Read
- [[ClientsActive]]
- [[Items]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[PriceListDetails]]
- [[PriceLists]]
## Tables Written
- [[PriceListDetails]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Items]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[PriceListDetails]]
- [[PriceLists]]

**Tables Written**
- [[PriceListDetails]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
