---
type: table
database: Olives_BO
name: PromotionsCustomersGroupsLink
schema: dbo
tags: [#backoffice, #customer, #reference, #sales]
foreign_keys:
  - [[Companies]]
  - [[CustomersPromotionsGroups]]
  - [[PromotionsHeaders]]
referenced_by:
  - [[Awtar_Integration_GetPromotion]]
  - [[Diag_Check_Linked_Sales_Cust_Promotions]]
  - [[Niroukh_Integration_GetPromotion]]
  - [[Pro_Customers]]
  - [[Pro_CustomersPromotionsGroups]]
  - [[Pro_CustomersPromotionsGroupsByDevice]]
  - [[Pro_ImportPromotionData]]
  - [[Pro_PromotionsCustomersGroupsLink]]
  - [[Pro_PromotionsHeaders]]
  - [[RG_Hakkak_CopyPromotions]]
  - [[RamPharm_SAP_Integ]]
  - [[Rpt_CustomersPromotionsGroupsByType]]
  - [[X3_INTEGRATIONPROMOTION_WITHLOG]]
support_relevance: high
last_verified: 2026-07-05
---
# PromotionsCustomersGroupsLink


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores promotionscustomersgroupslink records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[PromotionsHeaders]] |
| PromotionID | int | NO | ✓ | ✓ | [[PromotionsHeaders]] |
| CustomersPromotionsGroupsID | int | NO | ✓ | ✓ | [[CustomersPromotionsGroups]] |
## Primary Key
CompanyID
PromotionID
CustomersPromotionsGroupsID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomersPromotionsGroupsID -> [[CustomersPromotionsGroups]](CompanyID, ID)
CompanyID, PromotionID -> [[PromotionsHeaders]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (11):**
- [[Awtar_Integration_GetPromotion]]
- [[Diag_Check_Linked_Sales_Cust_Promotions]]
- [[Niroukh_Integration_GetPromotion]]
- [[Pro_CustomersPromotionsGroups]]
- [[Pro_CustomersPromotionsGroupsByDevice]]
- [[Pro_ImportPromotionData]]
- [[Pro_PromotionsCustomersGroupsLink]]
- [[Pro_PromotionsHeaders]]
- [[RG_Hakkak_CopyPromotions]]
- [[Rpt_CustomersPromotionsGroupsByType]]
- [[X3_INTEGRATIONPROMOTION_WITHLOG]]

**Writes (8):**
- [[Awtar_Integration_GetPromotion]]
- [[Niroukh_Integration_GetPromotion]]
- [[Pro_Customers]]
- [[Pro_CustomersPromotionsGroupsByDevice]]
- [[Pro_ImportPromotionData]]
- [[Pro_PromotionsCustomersGroupsLink]]
- [[Pro_PromotionsHeaders]]
- [[RamPharm_SAP_Integ]]

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
