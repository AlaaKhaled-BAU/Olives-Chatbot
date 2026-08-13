---
type: procedure
database: Olives_BO
name: Pro_TransactionsDetails
schema: dbo
tags: [#backoffice]
reads_from:
  - [[Items]]
  - [[ItemsUnits]]
  - [[TransactionsDetails]]
  - `dbo`
writes_to:
  - [[TransactionsDetails]]
  - TransactionsDetailsLog
called_by:
  - [[Pro_CalcSalespersonItemBalance]]
support_relevance: high
last_verified: 2026-07-05
---
# Pro_TransactionsDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, ItemsUnits, TransactionsDetails, dbo. Writes TransactionsDetails, TransactionsDetailsLog. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @TransactionNo INT = NULL
- @TransactionTypeID INT = null
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
## Tables Read
- [[Items]]
- [[ItemsUnits]]
- [[TransactionsDetails]]
- `dbo`
## Tables Written
- [[TransactionsDetails]]
- TransactionsDetailsLog
## Callers
_None (no known callers)_
## Callees
- [[Pro_CalcSalespersonItemBalance]]
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[ItemsUnits]]
- [[TransactionsDetails]]
- dbo

**Tables Written**
- [[TransactionsDetails]]
- TransactionsDetailsLog

**Callers**
- [[Pro_CalcSalespersonItemBalance]]

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
