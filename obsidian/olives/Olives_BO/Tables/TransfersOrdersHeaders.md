---
type: table
database: Olives_BO
name: TransfersOrdersHeaders
schema: dbo
tags: [#backoffice, #order]
foreign_keys:
  - [[Companies]]
  - [[SalesPersons]]
referenced_by:
  - [[BaladInsertrtLoadDetailsintoTransactionstyp6]]
  - [[BaladInsertrtLoadHeadersintoTransactionstyp6]]
  - [[DEMOSALESPERSON]]
  - [[DEMOSALESPERSON2]]
  - [[DiagnosticTools_CheckSalespersonunpostedOlivesTransactions]]
  - [[GetTransfersOrdersForOnline]]
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[OT_ImportUploadOrders]]
  - [[OT_SendSalesmanData]]
  - [[Pro_Auto_Unload]]
  - [[Pro_CheckItemsInvoiceBarcode]]
  - [[Pro_ConvertLoadOrderToTransaction]]
  - [[Pro_ConvertUnloadOrderToTransaction]]
  - [[Pro_SalesReport_ItemCode]]
  - [[Pro_SalesmanStockAndReturnLoadOrders]]
  - [[Pro_StockSettlement]]
  - [[Pro_TransfersOrdersDetails]]
  - [[Pro_TransfersOrdersHeaders]]
  - [[Pro_TransfersOrdersQtyValidation]]
  - [[Rpt_LoadOrdersQtySummary]]
  - [[Rpt_LoadTransactionDetails]]
  - [[Rpt_QuantitiesLoadReport]]
  - [[Rpt_ReasonReprint]]
  - [[Rpt_ReprintCount]]
  - [[Rpt_SalesmanCashSales]]
  - [[Rpt_SalesmanDifferences]]
  - [[Rpt_SalesmanSalesByItems]]
  - [[Rpt_SalesmanStock]]
  - [[Rpt_TransactionsNotes]]
  - [[Rpt_TransferOrderWH]]
  - [[Rpt_TransferOrders]]
  - [[Rpt_TransfersOrders]]
  - [[Stock_Transfer_Jebrini_Excel]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-07-05
---
# TransfersOrdersHeaders


## Business Purpose

Core transfer and replenishment document table in Olives_BO for Cash Van vehicle logistics.
- Synced from tablet mobile tables `OSFA_DB.dbo.OT_ConsOrderHF` and `OT_ConsOrderDF` via procedure `dbo.OT_ImportUploadOrders`.
- **Master Discriminator (`VouType`):**
  - **`VouType = 1` (أمر تحميل Load Order):** Restocking the mobile van from the central warehouse (`StoreNo`). Approved via `Pro_ConvertLoadOrderToTransaction`, converting into `TransactionsHeaders` with **`TransactionTypeID = 6`**, and incrementing van stock in `SalesPersonItemsBalance`.
  - **`VouType = 2` (أمر تفريغ/تنزيل Unload Order):** Returning unsold goods from the van back to the central warehouse (`StoreNo`). Approved via `Pro_ConvertUnloadOrderToTransaction`, converting into `TransactionsHeaders` with **`TransactionTypeID = 7`**, and decrementing van stock in `SalesPersonItemsBalance`.
- **Workflow & Approval:** Governed by `WFApproved` and `Approve` flags. Triggers workflow functions (Function 7 for Load, Function 9 for Unload).
- **CRITICAL QUERY RULE:** Approved load/unload orders enter `TransactionsHeaders` as types 6 and 7. The chatbot must never query `TransactionsHeaders` for sales without explicitly filtering `TransactionTypeID = 1`.

## Chatbot semantics
(Query `t.TransfersOrdersHeaders` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule |
|----------------------|-----------|---------------|
| أوامر التحميل للمندوب | `OrderNo`, `OrderYear`, `SalesPersonID`, `OrderDate` | `VouType = 1` |
| أوامر التفريغ / التنزيل للمندوب | `OrderNo`, `OrderYear`, `SalesPersonID`, `OrderDate` | `VouType = 2` |
| حالة اعتماد أمر التحميل/التفريغ | `Approve`, `WFApproved`, `ApproveDate` | `Approve = 1` (معتمد) أو `Approve = 0` (معلق) |
| المستودع الرئيسي | `StoreNo` | مستودع التحميل أو التنزيل |
| تفاصيل الأصناف المحملة/المفرغة | Join `t.TransfersOrdersDetails` | `d.OrderYear = h.OrderYear AND d.OrderNo = h.OrderNo AND d.VouType = h.VouType` |

## Grain & keys
- **Grain**: One row per transfer order header (`OrderYear`, `OrderNo`, `VouType`).
- **Composite PK**: `CompanyID`, `OrderYear`, `OrderNo`, `VouType`.
- **Tenant Key**: `CompanyID`.

## Pipeline
Mobile Tablet (Cash Van) → `OT_ImportUploadOrders` → `TransfersOrdersHeaders` + `TransfersOrdersDetails` → Conversion to Warehouse Transactions (`TransactionTypeID = 6 / 7`).

## Related
- [[TransfersOrdersDetails]]
- [[SalesPersons]]
- [[SalesPersonItemsBalance]]
- [[TransactionsHeaders]]

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| VouType | int | NO | ✓ |  |  |
| SalesPersonID | int | YES |  | ✓ | [[SalesPersons]] |
| OrderDate | smalldatetime | YES |  |  |  |
| DocType | smallint | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| PostedToERP | bit | YES |  |  |  |
| Approve | bit | YES |  |  |  |
| WFApproved | bit | YES |  |  |  |
| StoreNo | int | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| PrintOriginalCount | int | YES |  |  |  |
| PrintCopyCount | int | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| TotalStock | nvarchar | YES |  |  |  |
| ApproveDate | smalldatetime | YES |  |  |  |
| ApprovedBy | nvarchar | YES |  |  |  |
| FirstApproval | bit | YES |  |  |  |
| UnloadBatchNo | bigint | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| PostToInvoice | bit | YES |  |  |  |
| ApprovedToSalesOrder | bit | YES |  |  |  |
| PostToSalesOrder | bit | YES |  |  |  |
## Primary Key
CompanyID
OrderYear
OrderNo
VouType
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (69):**
- [[BaladInsertrtLoadDetailsintoTransactionstyp6]]
- [[BaladInsertrtLoadHeadersintoTransactionstyp6]]
- [[DEMOSALESPERSON]]
- [[DEMOSALESPERSON2]]
- [[DiagnosticTools_CheckSalespersonunpostedOlivesTransactions]]
- [[GetTransfersOrdersForOnline]]
- [[OT_ImportUploadOrders]]
- [[Pro_Auto_Unload]]
- [[Pro_CheckItemsInvoiceBarcode]]
- [[Pro_ConvertUnloadOrderToTransaction]]
- [[Pro_SalesReport_ItemCode]]
- [[Pro_SalesmanStockAndReturnLoadOrders]]
- [[Pro_StockSettlement]]
- [[Pro_TransfersOrdersDetails]]
- [[Pro_TransfersOrdersQtyValidation]]
- [[Rpt_LoadOrdersQtySummary]]
- [[Rpt_LoadTransactionDetails]]
- [[Rpt_QuantitiesLoadReport]]
- [[Rpt_ReasonReprint]]
- [[Rpt_ReprintCount]]
- [[Rpt_SalesmanCashSales]]
- [[Rpt_SalesmanDifferences]]
- [[Rpt_SalesmanSalesByItems]]
- [[Rpt_SalesmanStock]]
- [[Rpt_TransactionsNotes]]
- [[Rpt_TransferOrderWH]]
- [[Rpt_TransferOrders]]
- [[Rpt_TransfersOrders]]
- [[Stock_Transfer_Jebrini_Excel]]

**Writes (59):**
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[OT_ImportUploadOrders]]
- [[OT_SendSalesmanData]]
- [[Pro_Auto_Unload]]
- [[Pro_ConvertLoadOrderToTransaction]]
- [[Pro_ConvertUnloadOrderToTransaction]]
- [[Pro_SalesmanStockAndReturnLoadOrders]]
- [[Pro_StockSettlement]]
- [[Pro_TransfersOrdersHeaders]]
- [[Pro_TransfersOrdersQtyValidation]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **VouType**: separates request vs issue vouchers — values are app-defined; check paired details before summing across types
- **StoreNo type**: StoreNo is int HERE but nvarchar on StoresBalances — cast before comparing/joining the two
## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
