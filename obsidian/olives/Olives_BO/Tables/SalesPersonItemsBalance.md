---
type: table
database: Olives_BO
name: SalesPersonItemsBalance
schema: dbo
tags: [#backoffice, #inventory, #sales]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[SalesPersons]]
referenced_by:
  - [[AbuOda_BonMarrof_Integ]]
  - [[AbuOda_Comp2_Integ]]
  - [[AbuOda_Integ]]
  - [[Alpha_GetItemBalance]]
  - [[Alpha_GetItemBalance_Zoumt]]
  - [[Bajali_SAP_Integ]]
  - [[CalcItemBalance]]
  - [[ECO_Land_SAP_Integ]]
  - [[Falcons_GetItemBalance]]
  - [[GArrow_SAP_Integ]]
  - [[GP_Integ]]
  - [[GP_Integ_GetItemBalance]]
  - [[GP_Integ_GetItemBalanceFromView]]
  - [[IscoJordan_Integ_GetItemsBalance]]
  - [[Izhiman_SAP_Integ]]
  - [[JV_Integ_GetItemBalance]]
  - [[Khobara_Integ]]
  - [[MeatLand_Integration]]
  - [[MeatLand_Integrationnew]]
  - [[OT_SendSalesmanData]]
  - [[Phenix_Sukhtian_Integ_GetItemsBalance]]
  - [[PrestoSoft_Integ_GetItemBalance]]
  - [[Presto_Integ]]
  - [[Pro_Auto_Unload]]
  - [[Pro_CalcSalespersonItemBalance]]
  - [[Pro_CheckSalesmanItemsBalance]]
  - [[Pro_Items]]
  - [[Pro_SalesPersonItemsBalance]]
  - [[Pro_SalesPersonStockTackingDetails]]
  - [[Pro_TransfersOrdersDetails]]
  - [[Pro_TransfersOrdersHeaders]]
  - [[Pro_TransfersOrdersQtyValidation]]
  - [[Qerat_Integ]]
  - [[Qetaf_Integ]]
  - [[RamPharm_SAP_Integ]]
  - [[Retco_Integ_ItemBal]]
  - [[Rpt_BasketReport]]
  - [[Rpt_LiveQty]]
  - [[Rpt_SalesPersonItemBalance]]
  - [[Rpt_SalesPersonStockTackingDetails]]
  - [[Rpt_StockTakingReport]]
  - [[Rpt_TransfersOrders]]
  - [[SAMA_SAP_Integ]]
  - [[SAP_GetItemBalance]]
  - [[SAP_GetItemBalance_Amazing]]
  - [[SAP_GetItemBalance_Karadsheh]]
  - [[SAP_GetItemBalance_Kaylani]]
  - [[SN_Integ_GetItemBalance]]
  - [[Salbeshian_SAP_Integ]]
  - [[Shamel_Integ_GetItemsBalance]]
  - [[Shini_Integ]]
  - [[Wings_Integ_GetItemBalance]]
  - [[X3_Integ_GetItemBalance]]
  - [[Yolande_Integ_GetItemBalance]]
  - [[Zedan_SAP_Integ]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonItemsBalance


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonitemsbalance records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| SalesPersonID | int | NO | ✓ | ✓ | [[SalesPersons]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| UnitCode | varchar | YES |  |  |  |
| ItemQuantity | float | YES |  |  |  |
## Primary Key
CompanyID
SalesPersonID
ItemCode
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (36):**
- [[Alpha_GetItemBalance]]
- [[Alpha_GetItemBalance_Zoumt]]
- [[CalcItemBalance]]
- [[GP_Integ_GetItemBalance]]
- [[GP_Integ_GetItemBalanceFromView]]
- [[IscoJordan_Integ_GetItemsBalance]]
- [[JV_Integ_GetItemBalance]]
- [[OT_SendSalesmanData]]
- [[Phenix_Sukhtian_Integ_GetItemsBalance]]
- [[PrestoSoft_Integ_GetItemBalance]]
- [[Presto_Integ]]
- [[Pro_Auto_Unload]]
- [[Pro_CalcSalespersonItemBalance]]
- [[Pro_CheckSalesmanItemsBalance]]
- [[Pro_Items]]
- [[Pro_SalesPersonItemsBalance]]
- [[Pro_SalesPersonStockTackingDetails]]
- [[Pro_TransfersOrdersDetails]]
- [[Pro_TransfersOrdersHeaders]]
- [[Pro_TransfersOrdersQtyValidation]]
- [[Retco_Integ_ItemBal]]
- [[Rpt_BasketReport]]
- [[Rpt_LiveQty]]
- [[Rpt_SalesPersonItemBalance]]
- [[Rpt_SalesPersonStockTackingDetails]]
- [[Rpt_StockTakingReport]]
- [[Rpt_TransfersOrders]]
- [[SAP_GetItemBalance]]
- [[SAP_GetItemBalance_Amazing]]
- [[SAP_GetItemBalance_Karadsheh]]
- [[SAP_GetItemBalance_Kaylani]]
- [[SN_Integ_GetItemBalance]]
- [[Shamel_Integ_GetItemsBalance]]
- [[Wings_Integ_GetItemBalance]]
- [[X3_Integ_GetItemBalance]]
- [[Yolande_Integ_GetItemBalance]]

**Writes (39):**
- [[AbuOda_BonMarrof_Integ]]
- [[AbuOda_Comp2_Integ]]
- [[AbuOda_Integ]]
- [[Alpha_GetItemBalance]]
- [[Alpha_GetItemBalance_Zoumt]]
- [[Bajali_SAP_Integ]]
- [[CalcItemBalance]]
- [[ECO_Land_SAP_Integ]]
- [[Falcons_GetItemBalance]]
- [[GArrow_SAP_Integ]]
- [[GP_Integ]]
- [[GP_Integ_GetItemBalance]]
- [[IscoJordan_Integ_GetItemsBalance]]
- [[Izhiman_SAP_Integ]]
- [[JV_Integ_GetItemBalance]]
- [[Khobara_Integ]]
- [[MeatLand_Integration]]
- [[MeatLand_Integrationnew]]
- [[OT_SendSalesmanData]]
- [[Phenix_Sukhtian_Integ_GetItemsBalance]]
- [[Presto_Integ]]
- [[Pro_CalcSalespersonItemBalance]]
- [[Pro_SalesPersonItemsBalance]]
- [[Pro_TransfersOrdersHeaders]]
- [[Pro_TransfersOrdersQtyValidation]]
- [[Qerat_Integ]]
- [[Qetaf_Integ]]
- [[RamPharm_SAP_Integ]]
- [[Retco_Integ_ItemBal]]
- [[SAMA_SAP_Integ]]
- [[SAP_GetItemBalance]]
- [[SAP_GetItemBalance_Amazing]]
- [[SAP_GetItemBalance_Karadsheh]]
- [[SAP_GetItemBalance_Kaylani]]
- [[Salbeshian_SAP_Integ]]
- [[Shamel_Integ_GetItemsBalance]]
- [[Shini_Integ]]
- [[Yolande_Integ_GetItemBalance]]
- [[Zedan_SAP_Integ]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Role**: van-custody snapshot per salesman; movement history belongs to Transactions* tables
- **Unit naming**: UnitCode has no declared FK — resolve against ItemsUnits manually
## Tenancy

Chatbot queries `t.SalesPersonItemsBalance` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`. Raw dbo access is blocked for `chatbot_ro`.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Shared/Runbooks/Credit-Limit-Block]]
