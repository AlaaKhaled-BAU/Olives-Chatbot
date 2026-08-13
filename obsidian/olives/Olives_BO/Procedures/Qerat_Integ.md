---
type: procedure
database: Olives_BO
name: Qerat_Integ
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[BusinessUnits]]
  - CalcUnPostedQty
  - [[Checks]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[Locations]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
writes_to:
  - [[BusinessUnits]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[Locations]]
  - [[OrdersHeaders]]
  - [[OT_ErrorLog]]
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[Receipts]]
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
  - [[StoresBalances]]
  - [[TransactionsHeaders]]
  - [[TransfersOrdersHeaders]]
called_by:
  - [[OT_ImportReceipts]]
  - [[OT_ImportSalesInvoices]]
  - [[OT_ImportSalesOrders]]
  - [[OT_ImportUploadOrders]]
  - [[OT_SendSalesmanData]]
support_relevance: high
last_verified: 2026-07-05
---
# Qerat_Integ


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, BusinessUnits, CalcUnPostedQty, Checks, Customers, CustomersFinancialDetails, CustomersTypes, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, Locations, OrdersDetails, OrdersHeaders. Writes BusinessUnits, Customers, CustomersFinancialDetails, CustomersTypes, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, Locations, OrdersHeaders, OT_ErrorLog, Positions, PriceListDetails, PriceLists, Receipts, SalesPersonItemsBalance, SalesPersons, StoresBalances, TransactionsHeaders, TransfersOrdersHeaders. Calls 5 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
- @CmdType varchar(50)
- @UserCode varchar(50)=null
- @UserDesc varchar(50)=null
- @UserID int=null
- @BankCode varchar(50)=null
- @BankName varchar(50)=null
- @ItemBarcode varchar(50)=null
- @ItemDesc varchar(50)=null
- @ItemTax varchar(50)=null
- @ItemCode varchar(50)=null
- @CategoryCode varchar(50)=null
- @DItemCode varchar(50)=null
- @DUnitID varchar(50)=null
- @DUnitCode varchar(50)=null
- @DConvertRate float=null
- @DUnitSerial int = null
- @GroupCode varchar(50)=null
- @GroupDesc varchar(50)=null
- @PLID int=null
- @PLDesc varchar(50)=null
- @PLDID int=null
- @PLItemID varchar(50)=null
- @PLItemPriceValue float=null
- @PLItemUnit varchar(50)=null
- @PLItemTax varchar(50)=null
- @SStoreID int=null
- @SStoreDescA varchar(50)=null
- @SWhsCode varchar(50)=null
- @StoreID varchar(50)=null
- @ItemID varchar(50)=null
- @UnitID varchar(50)=null
- @Qty float=null
- @AddressID varchar(50)=null
- @AddressCode varchar(50)=null
- @AddressDescL varchar(200)=null
- @ClientID varchar(50)=null
- @ClientDesc varchar(200)=null
- @ClientAddress varchar(200)=null
- @ClientContactPerson varchar(50)=null
- @ClientPhone1 varchar(50)=null
- @ClientCreditConsumed float=null
- @ClientCreditLimit float=null
- @ClientPriceListID int=null
- @ClientAddressID int=null
- @ClientGroup  varchar(50)=null
- @SALESPERSONCODE varchar(50)=null
- @TrSalesPersonID int=null
- @TransactionTypeID int=null
- @TransactionYear int=null
- @TransactionNo int=null
- @OrderYear int=null
- @OrderNo int=null
- @CategCode nvarchar(20)=null
- @ItemBrand nvarchar(20)=null
- @TradeChannel nvarchar(20)=null
- @ItemTaxCode nvarchar(50)=null
## Tables Read
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- CalcUnPostedQty
- [[Checks]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
## Tables Written
- [[BusinessUnits]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[OrdersHeaders]]
- [[OT_ErrorLog]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[Receipts]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[StoresBalances]]
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]
## Callers
_None (no known callers)_
## Callees
- [[OT_ImportReceipts]]
- [[OT_ImportSalesInvoices]]
- [[OT_ImportSalesOrders]]
- [[OT_ImportUploadOrders]]
- [[OT_SendSalesmanData]]
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- CalcUnPostedQty
- [[Checks]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[OrdersDetails]]
- [[OrdersHeaders]]

**Tables Written**
- [[BusinessUnits]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[OrdersHeaders]]
- [[OT_ErrorLog]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[Receipts]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[StoresBalances]]
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]

**Callers**
- [[OT_ImportReceipts]]
- [[OT_ImportSalesInvoices]]
- [[OT_ImportSalesOrders]]
- [[OT_ImportUploadOrders]]
- [[OT_SendSalesmanData]]

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
