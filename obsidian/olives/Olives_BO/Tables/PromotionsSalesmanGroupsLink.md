---
type: table
database: Olives_BO
name: PromotionsSalesmanGroupsLink
schema: dbo
tags: [#backoffice, #reference, #sales]
foreign_keys:
  - [[Companies]]
  - [[PromotionsHeaders]]
  - [[SalesPersonsGroups]]
referenced_by:
  - [[Awtar_Integration_GetPromotion]]
  - [[Diag_Check_Linked_Sales_Cust_Promotions]]
  - [[Niroukh_Integration_GetPromotion]]
  - [[OT_SendItemsInfo]]
  - [[Pro_CustomersPromotionsGroupsByDevice]]
  - [[Pro_ImportPromotionData]]
  - [[Pro_PromotionsHeaders]]
  - [[Pro_PromotionsSalesmanGroupsLink]]
  - [[Pro_SalesPersons]]
  - [[RG_Hakkak_CopyPromotions]]
  - [[RG_Rpt_PromotionInformation]]
  - [[RamPharm_SAP_Integ]]
  - [[Rpt_SalesmanGroupsByPromType]]
  - [[SalesmanPromotion_Excel]]
  - [[X3_INTEGRATIONPROMOTION_WITHLOG]]
support_relevance: high
last_verified: 2026-07-05
---
# PromotionsSalesmanGroupsLink


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores promotionssalesmangroupslink records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersonsGroups]] |
| PromotionID | int | NO | ✓ | ✓ | [[PromotionsHeaders]] |
| SalesPersonsGroupID | int | NO | ✓ | ✓ | [[SalesPersonsGroups]] |
## Primary Key
CompanyID
PromotionID
SalesPersonsGroupID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, PromotionID -> [[PromotionsHeaders]](CompanyID, ID)
CompanyID, SalesPersonsGroupID -> [[SalesPersonsGroups]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (13):**
- [[Awtar_Integration_GetPromotion]]
- [[Diag_Check_Linked_Sales_Cust_Promotions]]
- [[Niroukh_Integration_GetPromotion]]
- [[OT_SendItemsInfo]]
- [[Pro_CustomersPromotionsGroupsByDevice]]
- [[Pro_ImportPromotionData]]
- [[Pro_PromotionsHeaders]]
- [[Pro_PromotionsSalesmanGroupsLink]]
- [[RG_Hakkak_CopyPromotions]]
- [[RG_Rpt_PromotionInformation]]
- [[Rpt_SalesmanGroupsByPromType]]
- [[SalesmanPromotion_Excel]]
- [[X3_INTEGRATIONPROMOTION_WITHLOG]]

**Writes (7):**
- [[Awtar_Integration_GetPromotion]]
- [[Niroukh_Integration_GetPromotion]]
- [[Pro_ImportPromotionData]]
- [[Pro_PromotionsHeaders]]
- [[Pro_PromotionsSalesmanGroupsLink]]
- [[Pro_SalesPersons]]
- [[RamPharm_SAP_Integ]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
