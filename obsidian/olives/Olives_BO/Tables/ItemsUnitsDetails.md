---
type: table
database: Olives_BO
name: ItemsUnitsDetails
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[ItemsUnits]]
referenced_by:
  - [[AX_INTEGRATION]]
  - [[AbuOda_BonMarrof_Integ]]
  - [[AbuOda_Comp2_Integ]]
  - [[AbuOda_Integ]]
  - [[AccPack_Integ]]
  - [[AccPack_Integ_LuxuryItems]]
  - [[AccPack_Integyandrug]]
  - [[Alpha_Integ]]
  - [[Alpha_Integ_GoldenArrow]]
  - [[Alpha_updateRoute]]
  - [[Awa2el_Integ]]
  - [[Bajali_SAP_Integ]]
  - [[Bonanza_Integ_Yasmeen]]
  - [[Darwaza_Integration_WithLog]]
  - [[Defaf_Integration]]
  - [[ECO_Land_SAP_Integ]]
  - [[Falcons_Integ]]
  - [[GArrow_SAP_Integ]]
  - [[GP_Integ_Zumot]]
  - [[GP_Integ_Zumot_Aqaba]]
  - [[GTS_Integration_WithLog]]
  - [[Galaxy_Integration]]
  - [[IscoJordan_Integration]]
  - [[Izhiman_SAP_Integ]]
  - [[JV_Integ]]
  - [[Khobara_Integ]]
  - [[MeatLand_Integration]]
  - [[MeatLand_Integrationnew]]
  - [[Motakaml_Integration_WithLog]]
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[OT_SendItemsInfo]]
  - [[Olives_Merch_Integ]]
  - [[Phenix_Sukhtian_Integ_WithLog]]
  - [[Presto_Integ]]
  - [[Pro_Items]]
  - [[Pro_ItemsUnits]]
  - [[Pro_ItemsUnitsDetails]]
  - [[Pro_PriceListDetails]]
  - [[Pro_TransfersOrders_Auto]]
  - [[Qerat_Integ]]
  - [[Qetaf_Integ]]
  - [[RamPharm_SAP_Integ]]
  - [[Retco_Edit_Integ_SalesOrders]]
  - [[Retco_Integ_ItemBal]]
  - [[Rpt_CustomerSalesByUnit]]
  - [[Rpt_LoadOrderFirstApproval]]
  - [[Rpt_ReceivablesSalesInvoice]]
  - [[Rpt_SalesPersonItemBalance]]
  - [[Rpt_SalesmanSalesByCategory2]]
  - [[SAMA_SAP_Integ]]
  - [[SAP_Integ]]
  - [[SAP_Integ_Amazing]]
  - [[SAP_Integ_Hammoudeh]]
  - [[SAP_Integ_Karadsheh]]
  - [[SAP_Integ_Kaylani]]
  - [[SAP_Integ_Lamis]]
  - [[SAP_Integ_MERI]]
  - [[SAP_Integ_Malak]]
  - [[SAP_Tyconz_Integ]]
  - [[SAP_Tyconz_Integ_ItemsUnitAD]]
  - [[SN_Integ_SendOrders]]
  - [[SN_Integ_SendTransactions]]
  - [[SN_Integ_SendTransferOrders]]
  - [[Salbeshian_SAP_Integ]]
  - [[Shamel_Integration]]
  - [[Shini_Integ]]
  - [[Yolande_Integ]]
  - [[Zedan_SAP_Integ]]
support_relevance: high
last_verified: 2026-07-05
---
# ItemsUnitsDetails


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores itemsunitsdetails records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[ItemsUnits]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| UnitID | nvarchar | YES | ✓ | ✓ | [[ItemsUnits]] |
| ConvertRate | float | YES |  |  |  |
| UnitSerial | int | YES |  |  |  |
| Barcode | nvarchar | YES |  |  |  |
| Volume | float | YES |  |  |  |
| Weight | float | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
| UsedInUploadOrder | bit | YES |  |  |  |
## Primary Key
CompanyID
ItemCode
UnitID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, UnitID -> [[ItemsUnits]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (53):**
- [[AX_INTEGRATION]]
- [[AbuOda_BonMarrof_Integ]]
- [[AbuOda_Comp2_Integ]]
- [[AbuOda_Integ]]
- [[AccPack_Integ]]
- [[AccPack_Integ_LuxuryItems]]
- [[AccPack_Integyandrug]]
- [[Alpha_Integ_GoldenArrow]]
- [[Alpha_updateRoute]]
- [[Awa2el_Integ]]
- [[Bonanza_Integ_Yasmeen]]
- [[Defaf_Integration]]
- [[GP_Integ_Zumot]]
- [[GP_Integ_Zumot_Aqaba]]
- [[Galaxy_Integration]]
- [[IscoJordan_Integration]]
- [[Izhiman_SAP_Integ]]
- [[JV_Integ]]
- [[Khobara_Integ]]
- [[MeatLand_Integrationnew]]
- [[OT_SendItemsInfo]]
- [[Olives_Merch_Integ]]
- [[Phenix_Sukhtian_Integ_WithLog]]
- [[Presto_Integ]]
- [[Pro_Items]]
- [[Pro_ItemsUnits]]
- [[Pro_ItemsUnitsDetails]]
- [[Pro_PriceListDetails]]
- [[Pro_TransfersOrders_Auto]]
- [[Qerat_Integ]]
- [[Qetaf_Integ]]
- [[Retco_Edit_Integ_SalesOrders]]
- [[Retco_Integ_ItemBal]]
- [[Rpt_CustomerSalesByUnit]]
- [[Rpt_LoadOrderFirstApproval]]
- [[Rpt_ReceivablesSalesInvoice]]
- [[Rpt_SalesPersonItemBalance]]
- [[Rpt_SalesmanSalesByCategory2]]
- [[SAP_Integ]]
- [[SAP_Integ_Amazing]]
- [[SAP_Integ_Hammoudeh]]
- [[SAP_Integ_Karadsheh]]
- [[SAP_Integ_Kaylani]]
- [[SAP_Integ_Lamis]]
- [[SAP_Integ_MERI]]
- [[SAP_Integ_Malak]]
- [[SN_Integ_SendOrders]]
- [[SN_Integ_SendTransactions]]
- [[SN_Integ_SendTransferOrders]]
- [[Salbeshian_SAP_Integ]]
- [[Shini_Integ]]
- [[Yolande_Integ]]
- [[Zedan_SAP_Integ]]

**Writes (45):**
- [[AbuOda_BonMarrof_Integ]]
- [[AbuOda_Comp2_Integ]]
- [[AbuOda_Integ]]
- [[AccPack_Integ_LuxuryItems]]
- [[Alpha_Integ]]
- [[Alpha_updateRoute]]
- [[Awa2el_Integ]]
- [[Bajali_SAP_Integ]]
- [[Darwaza_Integration_WithLog]]
- [[ECO_Land_SAP_Integ]]
- [[Falcons_Integ]]
- [[GArrow_SAP_Integ]]
- [[GTS_Integration_WithLog]]
- [[Galaxy_Integration]]
- [[Izhiman_SAP_Integ]]
- [[JV_Integ]]
- [[Khobara_Integ]]
- [[MeatLand_Integration]]
- [[MeatLand_Integrationnew]]
- [[Motakaml_Integration_WithLog]]
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[Olives_Merch_Integ]]
- [[Phenix_Sukhtian_Integ_WithLog]]
- [[Presto_Integ]]
- [[Pro_ItemsUnitsDetails]]
- [[Qerat_Integ]]
- [[Qetaf_Integ]]
- [[RamPharm_SAP_Integ]]
- [[SAMA_SAP_Integ]]
- [[SAP_Integ]]
- [[SAP_Integ_Amazing]]
- [[SAP_Integ_Hammoudeh]]
- [[SAP_Integ_Karadsheh]]
- [[SAP_Integ_Kaylani]]
- [[SAP_Integ_Lamis]]
- [[SAP_Integ_MERI]]
- [[SAP_Integ_Malak]]
- [[SAP_Tyconz_Integ]]
- [[SAP_Tyconz_Integ_ItemsUnitAD]]
- [[Salbeshian_SAP_Integ]]
- [[Shamel_Integration]]
- [[Shini_Integ]]
- [[Yolande_Integ]]
- [[Zedan_SAP_Integ]]

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
