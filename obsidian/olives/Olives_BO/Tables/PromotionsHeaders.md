---
type: table
database: Olives_BO
name: PromotionsHeaders
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
  - [[Companies]]
  - [[ItemsUnits]]
  - [[PromotionClasses]]
referenced_by:
  - [[Awtar_Integration_GetPromotion]]
  - [[Diag_Check_Linked_Sales_Cust_Promotions]]
  - [[Niroukh_Integration_GetPromotion]]
  - [[OT_SendItemsInfo]]
  - [[Pro_CheckPromotionTarget]]
  - [[Pro_CouponsBooksDetails]]
  - [[Pro_CustomersPromotionsGroupsByDevice]]
  - [[Pro_ImportPromotionData]]
  - [[Pro_NotAppliedPromotion]]
  - [[Pro_PromotionItemsSchema]]
  - [[Pro_PromotionSelectionGroups]]
  - [[Pro_PromotionsApproval]]
  - [[Pro_PromotionsCondUnCodInput]]
  - [[Pro_PromotionsCondUnCodOutput]]
  - [[Pro_PromotionsCustomersGroupsLink]]
  - [[Pro_PromotionsHeaders]]
  - [[Pro_PromotionsPrioritiesLink]]
  - [[Pro_SalesPersonItemBonusTarget_OnlineErrorReporting]]
  - [[RG_Hakkak_CopyPromotions]]
  - [[RG_Rpt_PromotionInformation]]
  - [[RamPharm_SAP_Integ]]
  - [[Rpt_CustomersPromotionsGroupsByType]]
  - [[Rpt_PromotionCheckReport]]
  - [[Rpt_PromotionHeader]]
  - [[Rpt_PromotionInputItem]]
  - [[Rpt_PromotionOutputItem]]
  - [[Rpt_PromotionsDuplicatedItems]]
  - [[Rpt_RangePromotionInput]]
  - [[Rpt_SalesmanGroupsByPromType]]
  - [[SMS_ZumotPromoCodes]]
  - [[SalesmanPromotion_Excel]]
  - [[Spartan_SAP_Integ_draft]]
  - [[WF_AddWorkFlowLevelOne_Promotions]]
  - [[WF_GetPositionWFData]]
  - [[X3_INTEGRATIONPROMOTION_WITHLOG]]
support_relevance: high
last_verified: 2026-07-05
---
# PromotionsHeaders


## Business Purpose

Sales promotion campaign definitions — discount rules, validity periods, and eligibility criteria.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[PromotionClasses]] |
| ID | int | NO | ✓ |  |  |
| PromotionType | int | YES |  |  |  |
| Name | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| StartDate | smalldatetime | YES |  |  |  |
| EndDate | smalldatetime | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
| InputQtyAmount | float | YES |  |  |  |
| OutPutType | int | YES |  |  |  |
| OutQtyAmount | float | YES |  |  |  |
| OutQtyAmount_2 | float | YES |  |  |  |
| UseInReturn | bit | YES |  |  |  |
| UseInSales | bit | YES |  |  |  |
| InputItemUnitID | nvarchar | YES |  | ✓ | [[ItemsUnits]] |
| OutItemUnitID | nvarchar | YES |  |  |  |
| PromotionDetails | nvarchar | YES |  |  |  |
| UseRateToCalcBonus | bit | YES |  |  |  |
| NotDouble | bit | YES |  |  |  |
| ApplyForAllUnit | bit | YES |  |  |  |
| DiscountType | smallint | YES |  |  |  |
| IncludeInTargetBonus | bit | YES |  |  |  |
| RoundType | smallint | YES |  |  |  |
| IsNeedCoupon | bit | YES |  |  |  |
| InvoiceType | smallint | YES |  |  |  |
| RunAfterAllPromos | bit | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| OutPutSameInput | bit | YES |  |  |  |
| SalesmanCanChangeOutPutQty | bit | YES |  |  |  |
| NeedWorkFlowApproval | bit | YES |  |  |  |
| MaxQty | float | YES |  |  |  |
| ApprovedBy | int | YES |  |  |  |
| IsRequiredInTrans | bit | YES |  |  |  |
| IsApproved | bit | YES |  |  |  |
| PromotionClass | int | YES |  | ✓ | [[PromotionClasses]] |
| AccumulatedAmount | float | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, InputItemUnitID -> [[ItemsUnits]](CompanyID, ID)
CompanyID, PromotionClass -> [[PromotionClasses]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (34):**
- [[Awtar_Integration_GetPromotion]]
- [[Diag_Check_Linked_Sales_Cust_Promotions]]
- [[Niroukh_Integration_GetPromotion]]
- [[OT_SendItemsInfo]]
- [[Pro_CheckPromotionTarget]]
- [[Pro_CouponsBooksDetails]]
- [[Pro_CustomersPromotionsGroupsByDevice]]
- [[Pro_ImportPromotionData]]
- [[Pro_NotAppliedPromotion]]
- [[Pro_PromotionItemsSchema]]
- [[Pro_PromotionSelectionGroups]]
- [[Pro_PromotionsApproval]]
- [[Pro_PromotionsCondUnCodInput]]
- [[Pro_PromotionsCondUnCodOutput]]
- [[Pro_PromotionsCustomersGroupsLink]]
- [[Pro_PromotionsHeaders]]
- [[Pro_PromotionsPrioritiesLink]]
- [[Pro_SalesPersonItemBonusTarget_OnlineErrorReporting]]
- [[RG_Hakkak_CopyPromotions]]
- [[RG_Rpt_PromotionInformation]]
- [[Rpt_CustomersPromotionsGroupsByType]]
- [[Rpt_PromotionCheckReport]]
- [[Rpt_PromotionHeader]]
- [[Rpt_PromotionInputItem]]
- [[Rpt_PromotionOutputItem]]
- [[Rpt_PromotionsDuplicatedItems]]
- [[Rpt_RangePromotionInput]]
- [[Rpt_SalesmanGroupsByPromType]]
- [[SMS_ZumotPromoCodes]]
- [[SalesmanPromotion_Excel]]
- [[Spartan_SAP_Integ_draft]]
- [[WF_AddWorkFlowLevelOne_Promotions]]
- [[WF_GetPositionWFData]]
- [[X3_INTEGRATIONPROMOTION_WITHLOG]]

**Writes (7):**
- [[Awtar_Integration_GetPromotion]]
- [[Niroukh_Integration_GetPromotion]]
- [[Pro_CheckPromotionTarget]]
- [[Pro_ImportPromotionData]]
- [[Pro_PromotionsApproval]]
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
