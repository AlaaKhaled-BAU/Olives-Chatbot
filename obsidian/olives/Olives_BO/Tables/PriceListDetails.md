---
type: table
database: Olives_BO
name: PriceListDetails
schema: dbo
tags: [#backoffice, #billing]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[PriceLists]]
referenced_by:
  - [[ABS_Integration_Jebrene]]
  - [[ABS_Integration_Sokhtian]]
  - [[AX_INTEGRATION]]
  - [[AbuOda_BonMarrof_Integ]]
  - [[AbuOda_Comp2_Integ]]
  - [[AbuOda_Integ]]
  - [[Acback_Integration]]
  - [[AccPack_Integ]]
  - [[AccPack_Integ_LuxuryItems]]
  - [[AccPack_Integyandrug]]
  - [[Alpha_Integ]]
  - [[Alpha_updateRoute]]
  - [[Awa2el_Integ]]
  - [[Awael_Integration_WithLog]]
  - [[Awtar_Integration_WithLog]]
  - [[Bajali_SAP_Integ]]
  - [[Bonanza_Integ_Yasmeen]]
  - [[CustPricelistD_TMP]]
  - [[Darwaza_Integration_WithLog]]
  - [[Defaf_Integration]]
  - [[ECO_Land_SAP_Integ]]
  - [[Ejabi_Integration]]
  - [[Falcons_Integ]]
  - [[GArrow_SAP_Integ]]
  - [[GP_Integ]]
  - [[GP_Integ_Wadi]]
  - [[GP_Integ_Zumot]]
  - [[GP_Integ_Zumot_Aqaba]]
  - [[GTS_Integration_WithLog]]
  - [[Galaxy_Integration]]
  - [[Isco_Integration_WithLog]]
  - [[Izhiman_SAP_Integ]]
  - [[JV_Integ]]
  - [[Khobara_Integ]]
  - [[MeatLand_Integration]]
  - [[MeatLand_Integrationnew]]
  - [[Motakaml_Integration_WithLog]]
  - [[NPF_Integration]]
  - [[Niroukh_Integration_WithLog]]
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[OT_SendItemsInfo]]
  - [[PRESTOSOFT_INTEGRATION_COMP2]]
  - [[Phenix_Sukhtian_Integ_WithLog]]
  - [[PrestoSoft_Integration]]
  - [[Presto_Integ]]
  - [[ProTech_Integration]]
  - [[Pro_CopyPricelist]]
  - [[Pro_ImportData]]
  - [[Pro_ImportPriceListData]]
  - [[Pro_Items]]
  - [[Pro_ItemsImageReport]]
  - [[Pro_PriceListDetails]]
  - [[Pro_PromotionsCondUnCodOutput]]
  - [[Pro_SalesTrans]]
  - [[Pro_TransfersOrdersDetails]]
  - [[Pro_TransfersOrdersQtyAmtValidation]]
  - [[Pro_TransfersOrdersQtyValidation]]
  - [[Qerat_Integ]]
  - [[Qetaf_Integ]]
  - [[RamPharm_SAP_Integ]]
  - [[Rpt_ItemsStockStatement]]
  - [[Rpt_LoadTransactionDetails]]
  - [[Rpt_QuantitiesLoadReport]]
  - [[Rpt_SalesmanItemsSales]]
  - [[Rpt_SalesmanStock]]
  - [[Rpt_StockTakingReport]]
  - [[Rpt_StockTakingReportWithPrices]]
  - [[Rpt_UPriceReport]]
  - [[SAMA_SAP_Integ]]
  - [[SAP_Integ]]
  - [[SAP_Integ_Amazing]]
  - [[SAP_Integ_Hammoudeh]]
  - [[SAP_Integ_Karadsheh]]
  - [[SAP_Integ_Kaylani]]
  - [[SAP_Integ_Lamis]]
  - [[SAP_Integ_MERI]]
  - [[SAP_Integ_Malak]]
  - [[SAP_Integration_WithLog]]
  - [[SAP_Naouri_Integ]]
  - [[SAP_Tyconz_Integ]]
  - [[Salbeshian_SAP_Integ]]
  - [[Shamel_Integration]]
  - [[Shini_Integ]]
  - [[Spartan_SAP_Integ_draft]]
  - [[Wings_Integration]]
  - [[Yolande_Integ]]
  - [[Zedan_SAP_Integ]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Items-Master-Data-Setup
  - PriceList-Management
---
# PriceListDetails


## Business Purpose

Item-level pricing within each price list — per-unit prices and discount rules.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[PriceLists]] |
| PriceListID | int | NO | ✓ | ✓ | [[PriceLists]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| UnitID | nvarchar | YES | ✓ | ✓ | [[ItemsUnits]] |
| Price | float | YES |  |  |  |
| TaxType | int | YES |  |  |  |
| Tax | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| UseInReturn | bit | YES |  |  |  |
| UseInSales | bit | YES |  |  |  |
| SellPrice2 | float | YES |  |  |  |
| SellPrice3 | float | YES |  |  |  |
| Qty | money | YES |  |  |  |
| TaxType1 | int | YES |  |  |  |
| Tax1 | float | YES |  |  |  |
| TaxType2 | int | YES |  |  |  |
| Tax2 | float | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
PriceListID
ItemCode
UnitID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, UnitID -> [[ItemsUnits]](CompanyID, ID)
CompanyID, PriceListID -> [[PriceLists]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (42):**
- [[ABS_Integration_Jebrene]]
- [[AX_INTEGRATION]]
- [[Acback_Integration]]
- [[AccPack_Integ]]
- [[AccPack_Integ_LuxuryItems]]
- [[AccPack_Integyandrug]]
- [[Awa2el_Integ]]
- [[Bonanza_Integ_Yasmeen]]
- [[CustPricelistD_TMP]]
- [[Ejabi_Integration]]
- [[GP_Integ]]
- [[GP_Integ_Zumot]]
- [[GP_Integ_Zumot_Aqaba]]
- [[JV_Integ]]
- [[OT_SendItemsInfo]]
- [[PRESTOSOFT_INTEGRATION_COMP2]]
- [[PrestoSoft_Integration]]
- [[Presto_Integ]]
- [[ProTech_Integration]]
- [[Pro_CopyPricelist]]
- [[Pro_ImportData]]
- [[Pro_ImportPriceListData]]
- [[Pro_Items]]
- [[Pro_ItemsImageReport]]
- [[Pro_PriceListDetails]]
- [[Pro_PromotionsCondUnCodOutput]]
- [[Pro_SalesTrans]]
- [[Pro_TransfersOrdersDetails]]
- [[Pro_TransfersOrdersQtyAmtValidation]]
- [[Pro_TransfersOrdersQtyValidation]]
- [[Rpt_ItemsStockStatement]]
- [[Rpt_LoadTransactionDetails]]
- [[Rpt_QuantitiesLoadReport]]
- [[Rpt_SalesmanItemsSales]]
- [[Rpt_SalesmanStock]]
- [[Rpt_StockTakingReport]]
- [[Rpt_StockTakingReportWithPrices]]
- [[Rpt_UPriceReport]]
- [[SAP_Naouri_Integ]]
- [[Spartan_SAP_Integ_draft]]
- [[Wings_Integration]]
- [[Yolande_Integ]]

**Writes (62):**
- [[ABS_Integration_Jebrene]]
- [[ABS_Integration_Sokhtian]]
- [[AbuOda_BonMarrof_Integ]]
- [[AbuOda_Comp2_Integ]]
- [[AbuOda_Integ]]
- [[Acback_Integration]]
- [[AccPack_Integ]]
- [[AccPack_Integ_LuxuryItems]]
- [[AccPack_Integyandrug]]
- [[Alpha_Integ]]
- [[Alpha_updateRoute]]
- [[Awa2el_Integ]]
- [[Awael_Integration_WithLog]]
- [[Awtar_Integration_WithLog]]
- [[Bajali_SAP_Integ]]
- [[Darwaza_Integration_WithLog]]
- [[Defaf_Integration]]
- [[ECO_Land_SAP_Integ]]
- [[Ejabi_Integration]]
- [[Falcons_Integ]]
- [[GArrow_SAP_Integ]]
- [[GP_Integ]]
- [[GP_Integ_Wadi]]
- [[GTS_Integration_WithLog]]
- [[Galaxy_Integration]]
- [[Isco_Integration_WithLog]]
- [[Izhiman_SAP_Integ]]
- [[JV_Integ]]
- [[Khobara_Integ]]
- [[MeatLand_Integration]]
- [[MeatLand_Integrationnew]]
- [[Motakaml_Integration_WithLog]]
- [[NPF_Integration]]
- [[Niroukh_Integration_WithLog]]
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[Phenix_Sukhtian_Integ_WithLog]]
- [[ProTech_Integration]]
- [[Pro_ImportData]]
- [[Pro_ImportPriceListData]]
- [[Pro_PriceListDetails]]
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
- [[SAP_Integration_WithLog]]
- [[SAP_Naouri_Integ]]
- [[SAP_Tyconz_Integ]]
- [[Salbeshian_SAP_Integ]]
- [[Shamel_Integration]]
- [[Shini_Integ]]
- [[Wings_Integration]]
- [[Yolande_Integ]]
- [[Zedan_SAP_Integ]]

## Estimated Size / Volatility
Typical business table
## Common Issues
> [!warning] AUTO-GENERATED — verify before trusting

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
