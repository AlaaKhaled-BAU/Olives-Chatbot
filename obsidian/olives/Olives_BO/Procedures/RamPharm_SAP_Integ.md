---
type: procedure
database: Olives_BO
name: RamPharm_SAP_Integ
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - [[BatchsItemsInfo]]
  - [[Branches]]
  - [[BusinessUnits]]
  - CalcUnPostedQty
  - [[Checks]]
  - [[CustomerStatmentOfAccount]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersPaidTransList]]
  - [[CustomersPromotionsGroups]]
  - [[CustomersPromotionsGroupsLink]]
  - [[CustomersTypes]]
  - Fun_GetReceiptsChecksTotal
  - [[InvoiceHistoryDF]]
writes_to:
  - [[Banks]]
  - [[BatchsItemsInfo]]
  - [[Branches]]
  - [[BusinessUnits]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersPromotionsGroups]]
  - [[CustomersPromotionsGroupsLink]]
  - [[CustomerStatmentOfAccount]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[OrdersHeaders]]
  - [[OT_ErrorLog]]
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[PromotionsCondUnCodInput]]
  - [[PromotionsCondUnCodOutput]]
  - [[PromotionsCustomersGroupsLink]]
  - [[PromotionsHeaders]]
  - [[PromotionsRangeInput]]
  - [[PromotionsSalesmanGroupsLink]]
  - [[Receipts]]
  - [[Receipts_PaidTrans]]
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
  - [[TransfersOrdersHeaders]]
called_by:
  - [[OT_ImportActionLog]]
  - [[OT_ImportCustomerGPS]]
  - [[OT_ImportCustStockTacking]]
  - [[OT_ImportReceipts]]
  - [[OT_ImportSalesInvoices]]
  - [[OT_ImportSalesOrders]]
  - [[OT_ImportUploadOrders]]
  - [[OT_SendCompData]]
  - [[OT_SendSalesmanData]]
support_relevance: high
last_verified: 2026-07-05
---
# RamPharm_SAP_Integ


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, BatchsItemsInfo, Branches, BusinessUnits, CalcUnPostedQty, Checks, CustomerStatmentOfAccount, Customers, CustomersFinancialDetails, CustomersPaidTransList, CustomersPromotionsGroups, CustomersPromotionsGroupsLink, CustomersTypes, Fun_GetReceiptsChecksTotal, InvoiceHistoryDF. Writes Banks, BatchsItemsInfo, Branches, BusinessUnits, Customers, CustomersFinancialDetails, CustomersPromotionsGroups, CustomersPromotionsGroupsLink, CustomerStatmentOfAccount, CustomersTypes, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, OrdersHeaders, OT_ErrorLog, Positions, PriceListDetails, PriceLists, PromotionsCondUnCodInput, PromotionsCondUnCodOutput, PromotionsCustomersGroupsLink, PromotionsHeaders, PromotionsRangeInput, PromotionsSalesmanGroupsLink, Receipts, Receipts_PaidTrans, SalesPersonItemsBalance, SalesPersons, TransactionsHeaders, TransfersOrdersHeaders. Calls 9 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
- @CmdType varchar(50)
- @UserCode varchar(50)=null
- @UserDesc varchar(50)=null
- @UserID int=null
- @BankCode varchar(50)=null
- @BankName varchar(50)=null
- @ItemBarcode varchar(50)=null
- @ItemDesc varchar(1000)=null
- @ItemDescF varchar(1000)=null
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
- @ClientDescF varchar(200)=null
- @ClientAddress varchar(200)=null
- @ClientContactPerson varchar(50)=null
- @ClientPhone1 varchar(50)=null
- @ClientCreditConsumed float=null
- @ClientCreditLimit float=null
- @ClientPriceListID int=null
- @ClientAddressID int=null
- @ClientGroup  varchar(50)=null
- @SALESPERSONCODE varchar(50)=null
- @TaxNumber varchar(50)=null
- @RegistrationNumber varchar(100)=null
- @TrSalesPersonID int=null
- @TransactionTypeID int=null
- @TransactionYear int=null
- @TransactionNo int=null
- @OrderYear int=null
- @OrderNo int=null
- @CategCode nvarchar(20)=null
- @UserCashAccount nvarchar(20)=null
- @SAPCustomer nvarchar(100)=null
- @SAPInvoiceID nvarchar(100)=null
- @SAPInvoiceNumber nvarchar(100)=null
- @InvoiceFinalAmount float=null
- @InvoiceRemainingAmount float=null
- @CostCenter nvarchar(100)=null
- @Deprtment nvarchar(100)=null
- @VouType int = 1
- @CreditCash int = null
- @PRM_RAM_DT_HH_GET_AccountStatement dbo.RAM_DT_HH_GET_AccountStatement READONLY
- @PRM_RAM_DT_HH_Get_Batch_Inventory RAM_DT_HH_Get_Batch_Inventory READONLY
- @PRM_RAM_DT_HH_Get_InvoiceList RAM_DT_HH_Get_InvoiceList READONLY
- @PRM_RAM_DT_HH_Get_Bonus RAM_DT_HH_Get_Bonus READONLY
## Tables Read
- [[Banks]]
- [[BatchsItemsInfo]]
- [[Branches]]
- [[BusinessUnits]]
- CalcUnPostedQty
- [[Checks]]
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- [[CustomersPromotionsGroups]]
- [[CustomersPromotionsGroupsLink]]
- [[CustomersTypes]]
- Fun_GetReceiptsChecksTotal
- [[InvoiceHistoryDF]]
## Tables Written
- [[Banks]]
- [[BatchsItemsInfo]]
- [[Branches]]
- [[BusinessUnits]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPromotionsGroups]]
- [[CustomersPromotionsGroupsLink]]
- [[CustomerStatmentOfAccount]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[OrdersHeaders]]
- [[OT_ErrorLog]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[PromotionsCondUnCodInput]]
- [[PromotionsCondUnCodOutput]]
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- [[PromotionsRangeInput]]
- [[PromotionsSalesmanGroupsLink]]
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]
## Callers
_None (no known callers)_
## Callees
- [[OT_ImportActionLog]]
- [[OT_ImportCustomerGPS]]
- [[OT_ImportCustStockTacking]]
- [[OT_ImportReceipts]]
- [[OT_ImportSalesInvoices]]
- [[OT_ImportSalesOrders]]
- [[OT_ImportUploadOrders]]
- [[OT_SendCompData]]
- [[OT_SendSalesmanData]]
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[BatchsItemsInfo]]
- [[Branches]]
- [[BusinessUnits]]
- CalcUnPostedQty
- [[Checks]]
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- [[CustomersPromotionsGroups]]
- [[CustomersPromotionsGroupsLink]]
- [[CustomersTypes]]
- Fun_GetReceiptsChecksTotal
- [[InvoiceHistoryDF]]

**Tables Written**
- [[Banks]]
- [[BatchsItemsInfo]]
- [[Branches]]
- [[BusinessUnits]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPromotionsGroups]]
- [[CustomersPromotionsGroupsLink]]
- [[CustomerStatmentOfAccount]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[OrdersHeaders]]
- [[OT_ErrorLog]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[PromotionsCondUnCodInput]]
- [[PromotionsCondUnCodOutput]]
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- [[PromotionsRangeInput]]
- [[PromotionsSalesmanGroupsLink]]
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]

**Callers**
- [[OT_ImportActionLog]]
- [[OT_ImportCustomerGPS]]
- [[OT_ImportCustStockTacking]]
- [[OT_ImportReceipts]]
- [[OT_ImportSalesInvoices]]
- [[OT_ImportSalesOrders]]
- [[OT_ImportUploadOrders]]
- [[OT_SendCompData]]
- [[OT_SendSalesmanData]]

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
