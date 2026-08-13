---
type: procedure
database: Olives_BO
name: Pro_ReturnOrdersDetails
schema: dbo
tags: [#backoffice, #order]
reads_from:
  - [[ClientsActive]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[ReturnOrdersDetails]]
  - [[TransactionsBatchsItemsInfo]]
  - [[TransactionsDetails]]
  - `dbo`
writes_to:
  - [[ReturnOrdersDetails]]
  - ReturnOrdersDetailsLog
called_by:
  - [[Pro_CalcSalespersonItemBalance]]
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ReturnOrdersDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Items, ItemsUnits, ReturnOrdersDetails, TransactionsBatchsItemsInfo, TransactionsDetails, dbo. Writes ReturnOrdersDetails, ReturnOrdersDetailsLog. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @TransactionNo INT = NULL
- @TransactionYear int = null
- @ItemSerial int = null
- @ItemCode nvarchar(100)=null
- @UnitID nvarchar(50)=null
- @Quantity float=null
- @Bonus float=null
- @PromisesDate smalldatetime=null
- @Price float=null
- @DiscountAmount float=null
- @DiscountPercent float=null
- @VoucherDiscount float=null
- @CustomerDiscountAmount float=null
- @TaxType smallint=null
- @TaxPercent float=null
- @TaxAmount float=null
- @TaxType1 smallint=null
- @TaxPercent1 float=null
- @TaxAmount1 float=null
- @ForeignPrice float=null
- @ForeignDiscountAmount float=null
- @ForeignDiscountPercent float=null
- @ForeignVouDiscount float=null
- @ForeignTaxPercent float=null
- @ForeignTaxAmount float=null
- @NewItemCode nvarchar(100)=null
- @NewUnitID nvarchar(50)=null
- @cmdType varchar(50)=null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @UserID_Log nvarchar(100)=null
- @TrNo numeric(30,0) = null
- @UnitPrice float = 0
- @ItemStatus smallint = null
- @ForeignCustomerDiscountAmount int =null
- @UPrice int =null
- @TaxType2 int = null
- @TaxPercent2 float = null
- @TaxAmount2 float = null
- @Manual_Bonus float = null
- @ExchangeRate float = null
- @Notes nvarchar = null
- @Manual_Disc float = null
- @ReturnReason nvarchar = null
- @BonusTax float = null
- @BonusAmount float = null
- @UserID   nvarchar(50)=null
- @FromDate   smalldatetime =null
- @ToDate    smalldatetime =null
## Tables Read
- [[ClientsActive]]
- [[Items]]
- [[ItemsUnits]]
- [[ReturnOrdersDetails]]
- [[TransactionsBatchsItemsInfo]]
- [[TransactionsDetails]]
- `dbo`
## Tables Written
- [[ReturnOrdersDetails]]
- ReturnOrdersDetailsLog
## Callers
_None (no known callers)_
## Callees
- [[Pro_CalcSalespersonItemBalance]]
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Items]]
- [[ItemsUnits]]
- [[ReturnOrdersDetails]]
- [[TransactionsBatchsItemsInfo]]
- [[TransactionsDetails]]
- dbo

**Tables Written**
- [[ReturnOrdersDetails]]
- ReturnOrdersDetailsLog

**Callers**
- [[Pro_CalcSalespersonItemBalance]]

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
