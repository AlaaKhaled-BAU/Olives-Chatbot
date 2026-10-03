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
  - [[Diag_Check_Linked_Sales_Cust_Promotions]]
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
  - [[SalesmanPromotion_Excel]]
  - [[WF_AddWorkFlowLevelOne_Promotions]]
  - [[WF_GetPositionWFData]]
support_relevance: high
last_verified: 2026-07-05
---
# PromotionsHeaders


## Business Purpose
Sales promotion and bonus campaign master table in Olives_BO. Defines promotional incentive rules for mobile presales and van sales, including campaign name (`Name`), validity period (`StartDate` to `EndDate`), active status (`IsSuspended = 0`), output reward types (`OutPutType`, e.g. Free goods / Bonus items or Extra discounts), and qualification criteria (`InputQtyAmount`).
- **Applicability & Conditions**: Controls whether promotions apply to sales (`UseInSales = 1`) or returns (`UseInReturn`), whether approval is needed (`NeedWorkFlowApproval`, `IsApproved`), and coupon requirements (`IsNeedCoupon`).
- **Promotions Engine**: Tablet sales apps evaluate active promotions during order or invoice entry; qualifying orders automatically calculate bonus items (`Bonus`) in `OrdersDetails` or `TransactionsDetails`.

## Chatbot semantics
(Query `t.PromotionsHeaders` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule |
|----------------------|-----------|---------------|
| العروض الترويجية النشطة / الحالية | `Name`, `StartDate`, `EndDate`, `PromotionType` | `IsSuspended = 0 AND GETDATE() BETWEEN StartDate AND EndDate` |
| نوع البونص أو المكافأة | `OutPutType`, `OutQtyAmount` | صنف مجاني (بونص) أو خصم إضافي |
| شروط استحقاق العرض | `InputQtyAmount`, `InputItemUnitID` | الحد الأدنى للكمية أو القيمة المؤهلة للعرض |
| هل العرض معتمد | `IsApproved`, `NeedWorkFlowApproval` | حالة اعتماد العرض الترويجي |
| عروض الفواتير مقابل الطلبيات | `UseInSales`, `InvoiceType` | يحدد قنوات سريان العرض الترويجي |

**Do not confuse with:**
- `t.TransactionsPromotions` (log of promotions that were actually applied to a specific sales transaction).
- `t.PriceLists` (base price list definitions for items).

## Grain & keys
- **Grain**: One row per promotion campaign header (`ID`).
- **Composite PK**: `CompanyID`, `ID`.
- **Tenant Key**: `CompanyID`.

## Pipeline
Back Office Marketing / Sales Ops Setup → `PromotionsHeaders` (linked to `PromotionsCondUnCodInput` / `Output` or `PromotionsRangeInput`) → Synced to Handheld Devices via `OT_SendItemsInfo`.

## Related
- [[TransactionsHeaders]]
- [[OrdersHeaders]]
- [[TransactionsPromotions]]
- [[PriceLists]]

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
| IsAmountWithoutTax | bit | YES |  |  |  |
| NeedWorkFlowApproval | bit | YES |  |  |  |
| MaxQty | float | YES |  |  |  |
| ApprovedBy | int | YES |  |  |  |
| BonusWithPrice | bit | YES |  |  |  |
| IsRequiredInTrans | bit | YES |  |  |  |
| IsApproved | bit | YES |  |  |  |
| PromotionClass | int | YES |  | ✓ | [[PromotionClasses]] |
| AccumulatedAmount | float | YES |  |  |  |
| IONumber | nvarchar | YES |  |  |  |

## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, InputItemUnitID -> [[ItemsUnits]](CompanyID, ID)
CompanyID, PromotionClass -> [[PromotionClasses]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (34):**
- [[Diag_Check_Linked_Sales_Cust_Promotions]]
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
- [[SalesmanPromotion_Excel]]
- [[WF_AddWorkFlowLevelOne_Promotions]]
- [[WF_GetPositionWFData]]

**Writes (7):**
- [[Pro_CheckPromotionTarget]]
- [[Pro_ImportPromotionData]]
- [[Pro_PromotionsApproval]]
- [[Pro_PromotionsHeaders]]

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
