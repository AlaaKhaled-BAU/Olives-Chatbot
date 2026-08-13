---
type: table
database: Olives_BO
name: TransfersOrdersDetails
schema: dbo
tags: [#backoffice, #order]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[TransfersOrdersHeaders]]
referenced_by:
  - [[ABS_Integ_SendTransferOrders]]
  - [[ABS_Integ_SendTransferOrders_Jebrene]]
  - [[ABS_Integ_SendUnloadOrders_Jebrene]]
  - [[AX_INTEG_SENDTRANSFERS]]
  - [[AX_INTEG_SENDUNLOADTRANSFERS]]
  - [[Acback_Integ_SendTransfer]]
  - [[BaladInsertrtLoadDetailsintoTransactionstyp6]]
  - [[Defaf_Integration]]
  - [[Defaf_Rpt_WareHouse_Item_Balance]]
  - [[Ejabi_Integ_SendTransferOrders]]
  - [[GP_Integ_SendTransfersOrders_Zumot]]
  - [[GP_Integ_SendTransfersOrders_Zumot_Aqaba]]
  - [[GetTransfersOrdersForOnline]]
  - [[IscoJordan_Integ_SendTransferOrder]]
  - [[Motakaml_Integ_SendTransferOrder]]
  - [[OT_ImportUploadOrders]]
  - [[Phenix_Sukhtian_Integ_LoadAndUnLoad]]
  - [[PrestoSoft_Integ_SendTransferOrders]]
  - [[Pro_AutoBasketLoadItems]]
  - [[Pro_Auto_Unload]]
  - [[Pro_CheckItemsInvoiceBarcode]]
  - [[Pro_ItemsUnitsDetails]]
  - [[Pro_Rpt_ItemsUnloadSummaryTablet]]
  - [[Pro_SalesReport_ItemCode]]
  - [[Pro_SalesmanStockAndReturnLoadOrders]]
  - [[Pro_StockSettlement]]
  - [[Pro_TransfersOrdersDetails]]
  - [[Pro_TransfersOrdersQtyValidation]]
  - [[Rpt_LoadOrdersQtySummary]]
  - [[Rpt_LoadTransactionDetails]]
  - [[Rpt_QuantitiesLoadReport]]
  - [[Rpt_SalesmanStock]]
  - [[Rpt_TransferOrderWH]]
  - [[Rpt_TransferOrders]]
  - [[Rpt_TransfersOrders]]
  - [[Rpt_WareHouse_Item_Balance]]
  - [[SN_Integ_SendTransferOrders]]
  - [[Stock_Transfer_Jebrini_Excel]]
  - [[Tahona_Integ_SendLoadOrders]]
  - [[Tahoneh_Integ_CreateInvocieFromUnload]]
  - [[Zoumt_Integ]]
support_relevance: high
last_verified: 2026-07-05
---
# TransfersOrdersDetails


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores transfersordersdetails records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[TransfersOrdersHeaders]] |
| OrderYear | smallint | NO | ✓ | ✓ | [[TransfersOrdersHeaders]] |
| OrderNo | int | NO | ✓ | ✓ | [[TransfersOrdersHeaders]] |
| VouType | int | NO | ✓ | ✓ | [[TransfersOrdersHeaders]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| UnitID | nvarchar | YES | ✓ | ✓ | [[ItemsUnits]] |
| Quantity | float | YES |  |  |  |
| QtyAfterApprove | float | YES |  |  |  |
| DateAfterApprove | smalldatetime | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
OrderYear
OrderNo
VouType
ItemCode
UnitID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, UnitID -> [[ItemsUnits]](CompanyID, ID)
CompanyID, OrderYear, OrderNo, VouType -> [[TransfersOrdersHeaders]](CompanyID, OrderYear, OrderNo, VouType)
## Impact / Procedures Using This Table

**Reads (38):**
- [[ABS_Integ_SendTransferOrders]]
- [[ABS_Integ_SendTransferOrders_Jebrene]]
- [[ABS_Integ_SendUnloadOrders_Jebrene]]
- [[AX_INTEG_SENDTRANSFERS]]
- [[AX_INTEG_SENDUNLOADTRANSFERS]]
- [[Acback_Integ_SendTransfer]]
- [[BaladInsertrtLoadDetailsintoTransactionstyp6]]
- [[Defaf_Rpt_WareHouse_Item_Balance]]
- [[Ejabi_Integ_SendTransferOrders]]
- [[GP_Integ_SendTransfersOrders_Zumot]]
- [[GP_Integ_SendTransfersOrders_Zumot_Aqaba]]
- [[GetTransfersOrdersForOnline]]
- [[IscoJordan_Integ_SendTransferOrder]]
- [[Motakaml_Integ_SendTransferOrder]]
- [[Phenix_Sukhtian_Integ_LoadAndUnLoad]]
- [[PrestoSoft_Integ_SendTransferOrders]]
- [[Pro_AutoBasketLoadItems]]
- [[Pro_CheckItemsInvoiceBarcode]]
- [[Pro_ItemsUnitsDetails]]
- [[Pro_Rpt_ItemsUnloadSummaryTablet]]
- [[Pro_SalesReport_ItemCode]]
- [[Pro_SalesmanStockAndReturnLoadOrders]]
- [[Pro_StockSettlement]]
- [[Pro_TransfersOrdersDetails]]
- [[Pro_TransfersOrdersQtyValidation]]
- [[Rpt_LoadOrdersQtySummary]]
- [[Rpt_LoadTransactionDetails]]
- [[Rpt_QuantitiesLoadReport]]
- [[Rpt_SalesmanStock]]
- [[Rpt_TransferOrderWH]]
- [[Rpt_TransferOrders]]
- [[Rpt_TransfersOrders]]
- [[Rpt_WareHouse_Item_Balance]]
- [[SN_Integ_SendTransferOrders]]
- [[Stock_Transfer_Jebrini_Excel]]
- [[Tahona_Integ_SendLoadOrders]]
- [[Tahoneh_Integ_CreateInvocieFromUnload]]
- [[Zoumt_Integ]]

**Writes (6):**
- [[Defaf_Integration]]
- [[OT_ImportUploadOrders]]
- [[Pro_AutoBasketLoadItems]]
- [[Pro_Auto_Unload]]
- [[Pro_SalesmanStockAndReturnLoadOrders]]
- [[Pro_TransfersOrdersDetails]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
