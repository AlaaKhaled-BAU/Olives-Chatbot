---
type: procedure
database: Olives_BO
name: Defaf_Integration
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - AutoTransfer
  - Balance_BeforeAuto
  - [[Banks]]
  - [[Branches]]
  - [[Checks]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - ERP
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[Locations]]
  - [[LogActionTransaction]]
writes_to:
  - Balance_BeforeAuto
  - [[Banks]]
  - [[Branches]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - InvDailyHF
  - InvHistoryHF
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[Locations]]
  - [[OrdersHeaders]]
  - [[PaymentsTypes]]
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[Receipts]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[TransfersOrdersDetails]]
  - [[TransfersOrdersHeaders]]
  - [[TransfersOrder_Auto]]
called_by:
  - calc_balance
  - [[Pro_CalcSalespersonItemBalance]]
support_relevance: high
last_verified: 2026-07-05
---
# Defaf_Integration


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads AutoTransfer, Balance_BeforeAuto, Banks, Branches, Checks, Customers, CustomersFinancialDetails, CustomersTypes, ERP, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, Locations, LogActionTransaction. Writes Balance_BeforeAuto, Banks, Branches, Customers, CustomersFinancialDetails, CustomersTypes, InvDailyHF, InvHistoryHF, Items, ItemsCategories, ItemsUnits, Locations, OrdersHeaders, PaymentsTypes, Positions, PriceListDetails, PriceLists, Receipts, SalesPersons, TransactionsDetails, TransactionsHeaders, TransfersOrdersDetails, TransfersOrdersHeaders, TransfersOrder_Auto. Calls 2 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @CmdType varchar(100)
- @ID int=null
- @Name nvarchar(200)=null
- @Tel nvarchar(50)=null
- @IsSuspended bit=null
- @StoreNo nvarchar(20)=null
- @Type nvarchar(20)=null
- @CategCode nvarchar(20)=null
- @SubCateg nvarchar(20)=null
- @ItemSerial nvarchar(20) = null
- @Unit int=null
- @Barcode nvarchar(20)=null
- @Price float =null
- @Tax float=null
- @CustID nvarchar(50)=null
- @AccountRef nvarchar(50)=null
- @Contact nvarchar(100)=null
- @CustomerType int = null
- @Mobile nvarchar(50) = null
- @Fax nvarchar(50)=null
- @Address nvarchar(200)=null
- @Email nvarchar(100)=null
- @LocationID int=null
- @PaymentTypeID int=null
- @InvoiceDueDay int = null
- @SalesmanID int =null
- @Balance float = null
- @CreditLimit float  = null
- @TransactionTypeID smallint = null
- @TransactionYear smallint = null
- @TransactionNo int = null
- @Qty float = null
- @TransactionDate smalldatetime = null
- @Reference1 nvarchar(50) = null
- @Reference2 nvarchar(50) = null
- @ItemSer int = null
- @FileID bigint = null
- @ItemNo nvarchar(100)=null
- @UnitID nvarchar(50)=null
- @FileName nvarchar(200)=null
- @LastRunDate smalldatetime = null
- @AlphaOrderYear int =null
- @AlphaOrderNo int =null
- @VouType int=null
- @ErrorNo int = null output
## Tables Read
- AutoTransfer
- Balance_BeforeAuto
- [[Banks]]
- [[Branches]]
- [[Checks]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- ERP
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[LogActionTransaction]]
## Tables Written
- Balance_BeforeAuto
- [[Banks]]
- [[Branches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- InvDailyHF
- InvHistoryHF
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Locations]]
- [[OrdersHeaders]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[Receipts]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
- [[TransfersOrder_Auto]]
## Callers
_None (no known callers)_
## Callees
- calc_balance
- [[Pro_CalcSalespersonItemBalance]]
## Impact / Dependencies

**Tables Read**
- AutoTransfer
- Balance_BeforeAuto
- [[Banks]]
- [[Branches]]
- [[Checks]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- ERP
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[LogActionTransaction]]

**Tables Written**
- Balance_BeforeAuto
- [[Banks]]
- [[Branches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- InvDailyHF
- InvHistoryHF
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Locations]]
- [[OrdersHeaders]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[Receipts]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[transactionsheaders]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
- [[TransfersOrder_Auto]]

**Callers**
- calc_balance
- [[Pro_CalcSalespersonItemBalance]]

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
