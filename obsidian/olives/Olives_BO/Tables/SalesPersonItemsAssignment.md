---
type: table
database: Olives_BO
name: SalesPersonItemsAssignment
schema: dbo
tags: [#backoffice, #inventory, #sales]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[Positions]]
referenced_by:
  - [[AcBack_Integ_GetItemBalance]]
  - [[Alpha_GetItemBalance]]
  - [[Bajali_SAP_Integ]]
  - [[Bonanza_Integ_Esmint]]
  - [[DiagnosticTools_CheckSalespersonConfiguration]]
  - [[ECO_Land_SAP_Integ]]
  - [[GArrow_SAP_Integ]]
  - [[IscoJordan_Integ_GetItemsBalance]]
  - [[Izhiman_SAP_Integ]]
  - [[OT_SendSalesmanData]]
  - [[PrestoSoft_Integ_GetItemBalance]]
  - [[Pro_CustomersItemsAssigment]]
  - [[Pro_Items]]
  - [[Pro_ReturnlineManagerApproval]]
  - [[Pro_SalesPersonCustStockItemsAssignment]]
  - [[Pro_SalesPersonItemsAssignment]]
  - [[Pro_SalesPersonStockTackingDetails]]
  - [[Pro_TransfersOrdersDetails]]
  - [[Pro_TransfersOrders_Auto]]
  - [[Retco_Integ_ItemBal]]
  - [[Rpt_DeliveryBatchHeader]]
  - [[Rpt_ItemsCustomersNotSold]]
  - [[Rpt_ItemsCustomersNotSoldBySelection]]
  - [[Rpt_ItemsNotSold]]
  - [[Rpt_ItemsSalesmanNotSold]]
  - [[Rpt_PerformanceMetric]]
  - [[Rpt_PrintOrdersBatches]]
  - [[Rpt_SalesPersonStockTackingDetails]]
  - [[Rpt_StockTakingReport]]
  - [[Rpt_TransfersOrders]]
  - [[SAP_Naouri_Integ]]
  - [[X3_AssignItems]]
  - [[X3_INTEGRATIONPROMOTION_WITHLOG]]
  - [[X3_INTEG_ASSIGNITEMS]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonItemsAssignment


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonitemsassignment records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Positions]] |
| PositionsID | int | NO | ✓ | ✓ | [[Positions]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| DefinitionDate | smalldatetime | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
## Primary Key
CompanyID
PositionsID
ItemCode
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, PositionsID -> [[Positions]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (30):**
- [[AcBack_Integ_GetItemBalance]]
- [[Alpha_GetItemBalance]]
- [[Bonanza_Integ_Esmint]]
- [[DiagnosticTools_CheckSalespersonConfiguration]]
- [[IscoJordan_Integ_GetItemsBalance]]
- [[OT_SendSalesmanData]]
- [[PrestoSoft_Integ_GetItemBalance]]
- [[Pro_CustomersItemsAssigment]]
- [[Pro_Items]]
- [[Pro_ReturnlineManagerApproval]]
- [[Pro_SalesPersonCustStockItemsAssignment]]
- [[Pro_SalesPersonItemsAssignment]]
- [[Pro_SalesPersonStockTackingDetails]]
- [[Pro_TransfersOrdersDetails]]
- [[Pro_TransfersOrders_Auto]]
- [[Retco_Integ_ItemBal]]
- [[Rpt_DeliveryBatchHeader]]
- [[Rpt_ItemsCustomersNotSold]]
- [[Rpt_ItemsCustomersNotSoldBySelection]]
- [[Rpt_ItemsNotSold]]
- [[Rpt_ItemsSalesmanNotSold]]
- [[Rpt_PerformanceMetric]]
- [[Rpt_PrintOrdersBatches]]
- [[Rpt_SalesPersonStockTackingDetails]]
- [[Rpt_StockTakingReport]]
- [[Rpt_TransfersOrders]]
- [[SAP_Naouri_Integ]]
- [[X3_AssignItems]]
- [[X3_INTEGRATIONPROMOTION_WITHLOG]]
- [[X3_INTEG_ASSIGNITEMS]]

**Writes (8):**
- [[Bajali_SAP_Integ]]
- [[Bonanza_Integ_Esmint]]
- [[ECO_Land_SAP_Integ]]
- [[GArrow_SAP_Integ]]
- [[Izhiman_SAP_Integ]]
- [[OT_SendSalesmanData]]
- [[Pro_SalesPersonItemsAssignment]]
- [[SAP_Naouri_Integ]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Duplicate barcodes**: Multiple items sharing same barcode — POS picks wrong item
- **Price mismatch**: Sell price in Items differs from PriceListDetails — customer charged wrong amount
- **Stock discrepancy**: QtyInAllStores differs from sum of StoreBalances — run CALCITEMBALANCE
- **Missing units**: Item has no valid ItemUnits — cannot be sold
- **Tax config wrong**: IsTaxExempt flag incorrect — ZATCA/legal reporting mismatch

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
