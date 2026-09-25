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
  - [[ABS_Integ_SendInvoices]]
  - [[ABS_Integ_SendTransferOrders]]
  - [[ABS_Integ_SendTransferOrders_Jebrene]]
  - [[ABS_Integ_SendUnloadOrders_Jebrene]]
  - [[AX_INTEG_SENDTRANSFERS]]
  - [[AX_INTEG_SENDUNLOADTRANSFERS]]
  - [[AbuOda_BonMarrof_Integ]]
  - [[AbuOda_Comp2_Integ]]
  - [[AbuOda_Integ]]
  - [[Acback_Integ_SendTransfer]]
  - [[AccPack_Integ_SendTransfersOrders]]
  - [[AccPack_Integ_SendTransfersOrders_LuxuryItems]]
  - [[AccPack_Integ_SendTransfersOrdersunload]]
  - [[Alpha_Integ_SendTransfersOrders]]
  - [[Bajali_SAP_Integ]]
  - [[BaladInsertrtLoadDetailsintoTransactionstyp6]]
  - [[BaladInsertrtLoadHeadersintoTransactionstyp6]]
  - [[Bonanza_Integ_SendTransfer_Yasmeen]]
  - [[DEMOSALESPERSON]]
  - [[DEMOSALESPERSON2]]
  - [[Darwaza_Integ_SendTransfersOrders]]
  - [[Defaf_Integration]]
  - [[DiagnosticTools_CheckSalespersonunpostedOlivesTransactions]]
  - [[ECO_Land_SAP_Integ]]
  - [[Ejabi_Integ_SendTransferOrders]]
  - [[Falcon_Integ_SendUploadOrders]]
  - [[GArrow_SAP_Integ]]
  - [[GP_Integ_SendTransfersOrders]]
  - [[GP_Integ_SendTransfersOrders_Zumot]]
  - [[GP_Integ_SendTransfersOrders_Zumot_Aqaba]]
  - [[Galaxy_Integ_SendLoadOrder]]
  - [[GetTransfersOrdersForOnline]]
  - [[IscoJordan_Integ_SendTransferOrder]]
  - [[Isco_Integ_SendTransferOrders]]
  - [[Izhiman_SAP_Integ]]
  - [[JV_Integ_SendTransfersOrders]]
  - [[Khobara_Integ]]
  - [[Motakaml_Integ_SendTransferOrder]]
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[OT_ImportUploadOrders]]
  - [[OT_SendSalesmanData]]
  - [[Phenix_Sukhtian_Integ_LoadAndUnLoad]]
  - [[PrestoSoft_Integ_SendTransferOrders]]
  - [[Presto_Integ]]
  - [[Pro_Auto_Unload]]
  - [[Pro_CheckItemsInvoiceBarcode]]
  - [[Pro_ConvertLoadOrderToTransaction]]
  - [[Pro_ConvertUnloadOrderToTransaction]]
  - [[Pro_Rpt_ItemsUnloadSummaryTablet]]
  - [[Pro_SalesReport_ItemCode]]
  - [[Pro_SalesmanStockAndReturnLoadOrders]]
  - [[Pro_StockSettlement]]
  - [[Pro_TransfersOrdersDetails]]
  - [[Pro_TransfersOrdersHeaders]]
  - [[Pro_TransfersOrdersQtyValidation]]
  - [[Qerat_Integ]]
  - [[Qetaf_Integ]]
  - [[RamPharm_SAP_Integ]]
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
  - [[SAMA_SAP_Integ]]
  - [[SAP_Integ_SendTransferOrders]]
  - [[SAP_Integ_SendTransferOrders_Amazing]]
  - [[SAP_Integ_SendTransferOrders_Karadsheh]]
  - [[SAP_Integ_SendTransferOrders_Kaylani]]
  - [[SAP_Integ_SendTransferOrders_Lamis]]
  - [[SAP_Integ_SendTransferOrders_Malak]]
  - [[SAP_Integ_SendTransferOrders_Meri]]
  - [[SAP_Tyconz_Integ_SendTransfersOrders]]
  - [[SN_Integ_SendPayments]]
  - [[SN_Integ_SendTransferOrders]]
  - [[Salbeshian_SAP_Integ]]
  - [[Shini_Integ]]
  - [[Stock_Transfer_Jebrini_Excel]]
  - [[Tahona_Integ_SendLoadOrders]]
  - [[Tahoneh_Integ_CreateInvocieFromUnload]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
  - [[X3_Integ_SendTransfersOrders]]
  - [[Yolande_Integ_SendLoadOrders]]
  - [[Zedan_SAP_Integ]]
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
- [[ABS_Integ_SendInvoices]]
- [[ABS_Integ_SendTransferOrders]]
- [[ABS_Integ_SendTransferOrders_Jebrene]]
- [[ABS_Integ_SendUnloadOrders_Jebrene]]
- [[AX_INTEG_SENDTRANSFERS]]
- [[AX_INTEG_SENDUNLOADTRANSFERS]]
- [[Acback_Integ_SendTransfer]]
- [[AccPack_Integ_SendTransfersOrders]]
- [[AccPack_Integ_SendTransfersOrders_LuxuryItems]]
- [[AccPack_Integ_SendTransfersOrdersunload]]
- [[Alpha_Integ_SendTransfersOrders]]
- [[BaladInsertrtLoadDetailsintoTransactionstyp6]]
- [[BaladInsertrtLoadHeadersintoTransactionstyp6]]
- [[Bonanza_Integ_SendTransfer_Yasmeen]]
- [[DEMOSALESPERSON]]
- [[DEMOSALESPERSON2]]
- [[Darwaza_Integ_SendTransfersOrders]]
- [[DiagnosticTools_CheckSalespersonunpostedOlivesTransactions]]
- [[Ejabi_Integ_SendTransferOrders]]
- [[Falcon_Integ_SendUploadOrders]]
- [[GP_Integ_SendTransfersOrders]]
- [[GP_Integ_SendTransfersOrders_Zumot]]
- [[GP_Integ_SendTransfersOrders_Zumot_Aqaba]]
- [[Galaxy_Integ_SendLoadOrder]]
- [[GetTransfersOrdersForOnline]]
- [[IscoJordan_Integ_SendTransferOrder]]
- [[Isco_Integ_SendTransferOrders]]
- [[JV_Integ_SendTransfersOrders]]
- [[Motakaml_Integ_SendTransferOrder]]
- [[OT_ImportUploadOrders]]
- [[Phenix_Sukhtian_Integ_LoadAndUnLoad]]
- [[PrestoSoft_Integ_SendTransferOrders]]
- [[Pro_Auto_Unload]]
- [[Pro_CheckItemsInvoiceBarcode]]
- [[Pro_ConvertUnloadOrderToTransaction]]
- [[Pro_Rpt_ItemsUnloadSummaryTablet]]
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
- [[SAP_Integ_SendTransferOrders]]
- [[SAP_Integ_SendTransferOrders_Amazing]]
- [[SAP_Integ_SendTransferOrders_Karadsheh]]
- [[SAP_Integ_SendTransferOrders_Kaylani]]
- [[SAP_Integ_SendTransferOrders_Lamis]]
- [[SAP_Integ_SendTransferOrders_Malak]]
- [[SAP_Integ_SendTransferOrders_Meri]]
- [[SAP_Tyconz_Integ_SendTransfersOrders]]
- [[SN_Integ_SendPayments]]
- [[SN_Integ_SendTransferOrders]]
- [[Stock_Transfer_Jebrini_Excel]]
- [[Tahona_Integ_SendLoadOrders]]
- [[Tahoneh_Integ_CreateInvocieFromUnload]]
- [[X3_Integ_SendTransfersOrders]]
- [[Yolande_Integ_SendLoadOrders]]

**Writes (59):**
- [[ABS_Integ_SendTransferOrders]]
- [[ABS_Integ_SendTransferOrders_Jebrene]]
- [[ABS_Integ_SendUnloadOrders_Jebrene]]
- [[AbuOda_BonMarrof_Integ]]
- [[AbuOda_Comp2_Integ]]
- [[AbuOda_Integ]]
- [[Acback_Integ_SendTransfer]]
- [[AccPack_Integ_SendTransfersOrders]]
- [[AccPack_Integ_SendTransfersOrders_LuxuryItems]]
- [[AccPack_Integ_SendTransfersOrdersunload]]
- [[Alpha_Integ_SendTransfersOrders]]
- [[Bajali_SAP_Integ]]
- [[Bonanza_Integ_SendTransfer_Yasmeen]]
- [[Darwaza_Integ_SendTransfersOrders]]
- [[Defaf_Integration]]
- [[ECO_Land_SAP_Integ]]
- [[Ejabi_Integ_SendTransferOrders]]
- [[Falcon_Integ_SendUploadOrders]]
- [[GArrow_SAP_Integ]]
- [[GP_Integ_SendTransfersOrders]]
- [[Galaxy_Integ_SendLoadOrder]]
- [[IscoJordan_Integ_SendTransferOrder]]
- [[Isco_Integ_SendTransferOrders]]
- [[Izhiman_SAP_Integ]]
- [[JV_Integ_SendTransfersOrders]]
- [[Khobara_Integ]]
- [[Motakaml_Integ_SendTransferOrder]]
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[OT_ImportUploadOrders]]
- [[OT_SendSalesmanData]]
- [[Phenix_Sukhtian_Integ_LoadAndUnLoad]]
- [[Presto_Integ]]
- [[Pro_Auto_Unload]]
- [[Pro_ConvertLoadOrderToTransaction]]
- [[Pro_ConvertUnloadOrderToTransaction]]
- [[Pro_SalesmanStockAndReturnLoadOrders]]
- [[Pro_StockSettlement]]
- [[Pro_TransfersOrdersHeaders]]
- [[Pro_TransfersOrdersQtyValidation]]
- [[Qerat_Integ]]
- [[Qetaf_Integ]]
- [[RamPharm_SAP_Integ]]
- [[SAMA_SAP_Integ]]
- [[SAP_Integ_SendTransferOrders]]
- [[SAP_Integ_SendTransferOrders_Amazing]]
- [[SAP_Integ_SendTransferOrders_Karadsheh]]
- [[SAP_Integ_SendTransferOrders_Kaylani]]
- [[SAP_Integ_SendTransferOrders_Lamis]]
- [[SAP_Integ_SendTransferOrders_Malak]]
- [[SAP_Integ_SendTransferOrders_Meri]]
- [[SAP_Tyconz_Integ_SendTransfersOrders]]
- [[Salbeshian_SAP_Integ]]
- [[Shini_Integ]]
- [[Tahoneh_Integ_CreateInvocieFromUnload]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]
- [[Yolande_Integ_SendLoadOrders]]
- [[Zedan_SAP_Integ]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **VouType**: separates request vs issue vouchers — values are app-defined; check paired details before summing across types
- **StoreNo type**: StoreNo is int HERE but nvarchar on StoresBalances — cast before comparing/joining the two
## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Shared/Runbooks/Van-Stock-Mismatch]]
