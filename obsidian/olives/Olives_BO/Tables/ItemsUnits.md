---
type: table
database: Olives_BO
name: ItemsUnits
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[GetIssueItemsForOnline]]
  - [[GetSalesOrdersForApiReport_GCI]]
  - [[GetSalesOrdersForEdit]]
  - [[GetSalesOrdersForOnlineReport]]
  - [[GetSalesOrdersForOnlineReport_GCI]]
  - [[GetTransfersOrdersForOnline]]
  - [[GetWF_SalesOrderData]]
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[OT_GetOrderInvoiceLinkHistory]]
  - [[OT_SendCompData]]
  - [[OT_SendItemsInfo]]
  - [[Pro_BackOrderItems]]
  - [[Pro_CheckItemsInvoiceBarcode]]
  - [[Pro_Contracts]]
  - [[Pro_CustomerStockTackingDetails]]
  - [[Pro_Dashboard_Almalak]]
  - [[Pro_DeliveryAssigning]]
  - [[Pro_DeliveryCarSummaryReport]]
  - [[Pro_ImportData]]
  - [[Pro_ItemBarcodes]]
  - [[Pro_Items]]
  - [[Pro_ItemsPriceExceptions]]
  - [[Pro_ItemsPriority]]
  - [[Pro_ItemsUnits]]
  - [[Pro_ItemsUnitsDetails]]
  - [[Pro_ItemsUsedInLoadOrderAssignment]]
  - [[Pro_JoTaxApi]]
  - [[Pro_JoTaxApiFromOSFA]]
  - [[Pro_JoTaxApiFromOSFA____]]
  - [[Pro_OrdersDetails]]
  - [[Pro_PriceListDetails]]
  - [[Pro_PromotionInputOutput]]
  - [[Pro_PromotionsCondUnCodInput]]
  - [[Pro_PromotionsCondUnCodOutput]]
  - [[Pro_PromotionsRangeInput]]
  - [[Pro_ReturnOrdersDetails]]
  - [[Pro_ReturnOrdersHeaders]]
  - [[Pro_RptCashTotalOnline_Android_Naqi]]
  - [[Pro_SalesOrdersQtyValidation]]
  - [[Pro_SalesPersonItemsAssignment]]
  - [[Pro_SalesPersonItemsBalance]]
  - [[Pro_SalesPersonItemsSalesUnits]]
  - [[Pro_SalesPersonStockTackingDetails]]
  - [[Pro_SalesPersons]]
  - [[Pro_SalesQuotationDetails]]
  - [[Pro_SalesmanStockAndReturnLoadOrders]]
  - [[Pro_StockSettlement]]
  - [[Pro_TransactionsDetails]]
  - [[Pro_TransfersOrdersDetails]]
  - [[Pro_TransfersOrders_Auto]]
  - [[RptOnlineRpt_DamageReturn]]
  - [[RptOnlineRpt_ReturnDetails]]
  - [[Rpt_ApprovedOrder]]
  - [[Rpt_BackOrder]]
  - [[Rpt_BackOrderItems]]
  - [[Rpt_CustomerSalesByUnit]]
  - [[Rpt_CustomerStockTackingReport]]
  - [[Rpt_DeliveryBatchHeader]]
  - [[Rpt_DeliveryCarSummaryReport]]
  - [[Rpt_InvoiceQty]]
  - [[Rpt_LoadOrderFirstApproval]]
  - [[Rpt_LoadTransactionDetails]]
  - [[Rpt_MasterOrders]]
  - [[Rpt_OrdersSalesReport]]
  - [[Rpt_OrdersSalesReportByCategoty]]
  - [[Rpt_PromotionHeader]]
  - [[Rpt_PromotionInputItem]]
  - [[Rpt_PromotionOutputItem]]
  - [[Rpt_RangePromotionInput]]
  - [[Rpt_ReceivablesSalesInvoice]]
  - [[Rpt_ReturnOrder]]
  - [[Rpt_ReturnOrdersMaster]]
  - [[Rpt_SalesPersonItemBalance]]
  - [[Rpt_SalesPersonStockTackingDetails]]
  - [[Rpt_TransactionByDate]]
  - [[Rpt_TransferOrderWH]]
  - [[Rpt_TransferOrders]]
  - [[Rpt_UnloadOrder]]
  - [[Rpt_WithdrawalVoucher_Report]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Items-Master-Data-Setup
  - PriceList-Management
---
# ItemsUnits


## Business Purpose

Item-unit relationship — conversion rates between buy/sell units (e.g. case → piece).

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | nvarchar | YES | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| IsIntegerQty | bit | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (139):**
- [[GetIssueItemsForOnline]]
- [[GetSalesOrdersForApiReport_GCI]]
- [[GetSalesOrdersForEdit]]
- [[GetSalesOrdersForOnlineReport]]
- [[GetSalesOrdersForOnlineReport_GCI]]
- [[GetTransfersOrdersForOnline]]
- [[GetWF_SalesOrderData]]
- [[OT_GetOrderInvoiceLinkHistory]]
- [[OT_SendCompData]]
- [[OT_SendItemsInfo]]
- [[Pro_BackOrderItems]]
- [[Pro_CheckItemsInvoiceBarcode]]
- [[Pro_Contracts]]
- [[Pro_CustomerStockTackingDetails]]
- [[Pro_Dashboard_Almalak]]
- [[Pro_DeliveryAssigning]]
- [[Pro_DeliveryCarSummaryReport]]
- [[Pro_ImportData]]
- [[Pro_Items]]
- [[Pro_ItemsPriceExceptions]]
- [[Pro_ItemsPriority]]
- [[Pro_ItemsUnits]]
- [[Pro_ItemsUnitsDetails]]
- [[Pro_ItemsUsedInLoadOrderAssignment]]
- [[Pro_JoTaxApi]]
- [[Pro_JoTaxApiFromOSFA]]
- [[Pro_JoTaxApiFromOSFA____]]
- [[Pro_OrdersDetails]]
- [[Pro_PriceListDetails]]
- [[Pro_PromotionInputOutput]]
- [[Pro_PromotionsCondUnCodInput]]
- [[Pro_PromotionsCondUnCodOutput]]
- [[Pro_PromotionsRangeInput]]
- [[Pro_ReturnOrdersDetails]]
- [[Pro_ReturnOrdersHeaders]]
- [[Pro_RptCashTotalOnline_Android_Naqi]]
- [[Pro_SalesOrdersQtyValidation]]
- [[Pro_SalesPersonItemsAssignment]]
- [[Pro_SalesPersonItemsBalance]]
- [[Pro_SalesPersonItemsSalesUnits]]
- [[Pro_SalesPersonStockTackingDetails]]
- [[Pro_SalesPersons]]
- [[Pro_SalesQuotationDetails]]
- [[Pro_SalesmanStockAndReturnLoadOrders]]
- [[Pro_StockSettlement]]
- [[Pro_TransactionsDetails]]
- [[Pro_TransfersOrdersDetails]]
- [[Pro_TransfersOrders_Auto]]
- [[RptOnlineRpt_DamageReturn]]
- [[RptOnlineRpt_ReturnDetails]]
- [[Rpt_ApprovedOrder]]
- [[Rpt_BackOrder]]
- [[Rpt_BackOrderItems]]
- [[Rpt_CustomerSalesByUnit]]
- [[Rpt_CustomerStockTackingReport]]
- [[Rpt_DeliveryBatchHeader]]
- [[Rpt_DeliveryCarSummaryReport]]
- [[Rpt_InvoiceQty]]
- [[Rpt_LoadOrderFirstApproval]]
- [[Rpt_LoadTransactionDetails]]
- [[Rpt_MasterOrders]]
- [[Rpt_OrdersSalesReport]]
- [[Rpt_OrdersSalesReportByCategoty]]
- [[Rpt_PromotionHeader]]
- [[Rpt_PromotionInputItem]]
- [[Rpt_PromotionOutputItem]]
- [[Rpt_RangePromotionInput]]
- [[Rpt_ReceivablesSalesInvoice]]
- [[Rpt_ReturnOrder]]
- [[Rpt_ReturnOrdersMaster]]
- [[Rpt_SalesPersonItemBalance]]
- [[Rpt_SalesPersonStockTackingDetails]]
- [[Rpt_TransactionByDate]]
- [[Rpt_TransferOrderWH]]
- [[Rpt_TransferOrders]]
- [[Rpt_UnloadOrder]]
- [[Rpt_WithdrawalVoucher_Report]]

**Writes (65):**
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[Pro_ImportData]]
- [[Pro_ItemBarcodes]]
- [[Pro_ItemsUnits]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Role**: unit dictionary (Name/ShortName/IsIntegerQty) joined via ID; conversion factors live in [[ItemsUnitsDetails]], not here
- **Key**: ID is NOT NULL identity-style lookup key
## Tenancy

Chatbot queries `t.ItemsUnits` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`. Raw dbo access is blocked for `chatbot_ro`.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Olives_BO/Tables/ItemsUnitsDetails_1]]
