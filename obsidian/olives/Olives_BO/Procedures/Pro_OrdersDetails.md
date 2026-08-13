---
type: procedure
database: Olives_BO
name: Pro_OrdersDetails
schema: dbo
tags: [#backoffice, #order]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - DefQuantity
  - [[Items]]
  - [[ItemsUnits]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - Price
  - [[SalespersonsMessages]]
  - `dbo`
writes_to:
  - DefQuantity
  - [[OrdersDetails]]
  - OrdersDetailsLog
  - Price
  - [[SalespersonsMessages]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_OrdersDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, DefQuantity, Items, ItemsUnits, OrdersDetails, OrdersHeaders, Price, SalespersonsMessages, dbo. Writes DefQuantity, OrdersDetails, OrdersDetailsLog, Price, SalespersonsMessages. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @OrderYear smallint=null
- @OrderNo INT = NULL
- @ItemCode nvarchar(100)=null
- @UnitID nvarchar(50)=null
- @Quantity float=null
- @Bonus float=null
- @PromisesDate smalldatetime=null
- @Price float=null
- @DiscountAmount float=null
- @DiscountPercent float=null
- @VoucherDiscount float=null
- @TaxType smallint=null
- @TaxPercent float=null
- @TaxAmount float=null
- @TaxType1 smallint=null
- @TaxPercent1 float=null
- @TaxAmount1 float=null
- @CustomerDiscountAmount float=null
- @ForeignPrice float=null
- @ForeignDiscountAmount float=null
- @ForeignDiscountPercent float=null
- @ForeignVouDiscount float=null
- @ForeignTaxPercent float=null
- @ForeignTaxAmount float=null
- @cmdType varchar(50)=null
- @NewItemCode nvarchar(100)=null
- @NewUnitID nvarchar(50)=null
- @FromDate  smalldatetime = null
- @ToDate  smalldatetime = null
- @SalesPersonID int = null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @UserID_Log nvarchar(100)=null
- @TrNo numeric(30,0) = null
- @UnitPrice float = 0
- @UserID nvarchar(50) = null
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- DefQuantity
- [[Items]]
- [[ItemsUnits]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- Price
- [[SalespersonsMessages]]
- `dbo`
## Tables Written
- DefQuantity
- [[OrdersDetails]]
- OrdersDetailsLog
- Price
- [[SalespersonsMessages]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- DefQuantity
- [[Items]]
- [[ItemsUnits]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- Price
- [[SalespersonsMessages]]
- dbo

**Tables Written**
- DefQuantity
- [[OrdersDetails]]
- OrdersDetailsLog
- Price
- [[SalespersonsMessages]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
