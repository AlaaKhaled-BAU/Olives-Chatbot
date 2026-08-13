---
type: procedure
database: Olives_BO
name: GArrow_SAP_Integ
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[BusinessUnits]]
  - CalcUnPostedQty
  - [[Checks]]
  - [[CustomerStatmentOfAccount]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersItemsAssigment]]
  - [[CustomersPaidTransList]]
  - [[CustomersTypes]]
  - Fun_GetReceiptsChecksTotal
  - [[InvoiceHistoryDF]]
  - InvoiceHistoryDF_TT
  - [[InvoiceHistoryHF]]
writes_to:
  - [[Banks]]
  - [[Branches]]
  - [[BusinessUnits]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersItemsAssigment]]
  - [[CustomersPaidTransList]]
  - [[CustomerStatmentOfAccount]]
  - [[CustomersTypes]]
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsPriceExceptions]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[Locations]]
  - [[OrdersHeaders]]
  - [[OT_ErrorLog]]
  - [[OT_NewCustomers]]
  - [[PaymentsTypes]]
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - PRM_RAM_DT_HH_Get_InvoiceList
  - [[Receipts]]
  - [[Receipts_PaidTrans]]
  - [[ReturnOrdersHeaders]]
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
  - [[StoresBalances]]
  - [[TransactionsHeaders]]
  - [[TransfersOrdersHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# GArrow_SAP_Integ


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, BusinessUnits, CalcUnPostedQty, Checks, CustomerStatmentOfAccount, Customers, CustomersFinancialDetails, CustomersItemsAssigment, CustomersPaidTransList, CustomersTypes, Fun_GetReceiptsChecksTotal, InvoiceHistoryDF, InvoiceHistoryDF_TT, InvoiceHistoryHF. Writes Banks, Branches, BusinessUnits, Customers, CustomersFinancialDetails, CustomersItemsAssigment, CustomersPaidTransList, CustomerStatmentOfAccount, CustomersTypes, InvoiceHistoryDF, InvoiceHistoryHF, Items, ItemsCategories, ItemsPriceExceptions, ItemsUnits, ItemsUnitsDetails, Locations, OrdersHeaders, OT_ErrorLog, OT_NewCustomers, PaymentsTypes, Positions, PriceListDetails, PriceLists, PRM_RAM_DT_HH_Get_InvoiceList, Receipts, Receipts_PaidTrans, ReturnOrdersHeaders, SalesPersonItemsAssignment, SalesPersonItemsBalance, SalesPersons, StoresBalances, TransactionsHeaders, TransfersOrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int=2
- @CmdType varchar(50)='HH_Add_GoodsReciept'
- @UserCode varchar(50)=null
- @UserDesc varchar(50)=null
- @UserID int=null
- @BankCode varchar(50)=null
- @BankName varchar(50)=null
- @ItemBarcode varchar(50)=null
- @ItemDesc varchar(500)=null
- @ItemDesc_F varchar(500)=null
- @ItemTax varchar(50)=null
- @ItemCode varchar(50)=null
- @CategoryCode varchar(50)=null
- @DItemCode varchar(50)=null
- @DUnitID varchar(50)=null
- @DUnitCode varchar(50)=null
- @DConvertRate float=null
- @DUnitSerial int = null
- @InvUnitID varchar(50)=null
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
- @GroupName  varchar(50)=null
- @SALESPERSONCODE varchar(50)=null
- @ClientDisc float=null
- @Division  varchar(100)=null
- @VAT_Liable  varchar(100)=null
- @TrSalesPersonID int=246
- @TransactionTypeID int=null
- @TransactionYear int=null
- @TransactionNo int=null
- @OrderYear int=null
- @OrderNo int=null
- @VouType int=null
- @CategCode nvarchar(20)=null
- @ItemBrand nvarchar(20)=null
- @TradeChannel nvarchar(20)=null
- @Deprtment nvarchar(20)=null
- @ERP_CustNo varchar(50)=null
- @NewCustID varchar(50)=null
- @StoreNo varchar(100)=''
- @PayID int=null
- @PayDesc  varchar(100)=''
- @PRM_RAM_DT_HH_GET_AccountStatement dbo.RAM_DT_HH_GET_AccountStatement READONLY
- @PRM_RAM_DT_HH_Get_InvoiceList RAM_DT_HH_Get_InvoiceList READONLY
- @WarehouseCode nvarchar(100)=null
- @CashAccount nvarchar(100)=null
- @ChequeAccount nvarchar(100)=null
- @ValidFrom varchar(50) = null
- @ValidTo varchar(50) = null
- @Class varchar(50) = null
- @SAP_ItemsPriceExceptions SAP_ItemsPriceExceptions READONLY
- @SAP_ItemsClassification SAP_ItemsClassification READONLY
- @GPSX nvarchar(100)=null
- @GPSY nvarchar(100)=null
- @CardCode  nvarchar(100)=null
- @Discount  float=null
- @MainWarehouse varchar(500)=''
- @MAINWHS varchar(500)=''
- @Erp_Reference varchar(500)=''
- @ACTIVE varchar(50)=''
- @FIRSTLAYERCLASS varchar(50)=''
- @SECONDLAYERCLASS varchar(50)=''
- @VatGroup  varchar(50)=''
- @XWHS  varchar(50)=''
- @FatherSAPCustomer nvarchar(100)=null
- @SAPCustomer nvarchar(100)=null
- @SAPInvoiceID nvarchar(100)=null
- @SAPInvoiceNumber nvarchar(100)=null
- @InvoiceFinalAmount float=null
- @InvoiceRemainingAmount float=null
- @DocDueDate smalldatetime=null
- @DocDate smalldatetime=null
- @AmountWhithoutTax varchar(100)=0
- @InvoiceNumber varchar(100)=NULL
## Tables Read
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- CalcUnPostedQty
- [[Checks]]
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersItemsAssigment]]
- [[CustomersPaidTransList]]
- [[CustomersTypes]]
- Fun_GetReceiptsChecksTotal
- [[InvoiceHistoryDF]]
- InvoiceHistoryDF_TT
- [[InvoiceHistoryHF]]
## Tables Written
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersItemsAssigment]]
- [[CustomersPaidTransList]]
- [[CustomerStatmentOfAccount]]
- [[CustomersTypes]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsPriceExceptions]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[OrdersHeaders]]
- [[OT_ErrorLog]]
- [[OT_NewCustomers]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- PRM_RAM_DT_HH_Get_InvoiceList
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[ReturnOrdersHeaders]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[StoresBalances]]
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- CalcUnPostedQty
- [[Checks]]
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersItemsAssigment]]
- [[CustomersPaidTransList]]
- [[CustomersTypes]]
- Fun_GetReceiptsChecksTotal
- [[InvoiceHistoryDF]]
- InvoiceHistoryDF_TT
- [[InvoiceHistoryHF]]

**Tables Written**
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersItemsAssigment]]
- [[CustomersPaidTransList]]
- [[CustomerStatmentOfAccount]]
- [[CustomersTypes]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsPriceExceptions]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[OrdersHeaders]]
- [[OT_ErrorLog]]
- [[OT_NewCustomers]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- PRM_RAM_DT_HH_Get_InvoiceList
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[ReturnOrdersHeaders]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[StoresBalances]]
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
