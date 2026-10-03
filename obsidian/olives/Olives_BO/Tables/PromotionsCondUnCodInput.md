---
type: table
database: Olives_BO
name: PromotionsCondUnCodInput
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
referenced_by:
  - [[OT_SendItemsInfo]]
  - [[Pro_ImportPromotionData]]
  - [[Pro_PromotionInputOutput]]
  - [[Pro_PromotionItemsSchema]]
  - [[Pro_PromotionsCondUnCodInput]]
  - [[Pro_PromotionsCondUnCodOutput]]
  - [[Pro_PromotionsHeaders]]
  - [[Pro_SalesPersonItemBonusTarget_OnlineErrorReporting]]
  - [[RG_Hakkak_CopyPromotions]]
  - [[RG_Rpt_PromotionInformation]]
  - [[Rpt_PromotionInputItem]]
  - [[Rpt_PromotionsDuplicatedItems]]
  - [[SalesmanPromotion_Excel]]
support_relevance: high
last_verified: 2026-07-05
---
# PromotionsCondUnCodInput


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores promotionsconduncodinput records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| PromotionID | int | NO | ✓ |  |  |
| ItemCode | nvarchar | YES | ✓ |  |  |
| ItemSerial | smallint | NO | ✓ |  |  |
| ItemUnitID | nvarchar | YES |  |  |  |
| Quantity | float | YES |  |  |  |
| InputType | smallint | YES |  |  |  |
| ToQuantity | float | YES |  |  |  |
| NotDouble | bit | YES |  |  |  |
| StartDate | smalldatetime | YES |  |  |  |
| EndDate | smalldatetime | YES |  |  |  |
| PromotionItemGroupID | int | YES |  |  |  |
## Primary Key
CompanyID
PromotionID
ItemCode
ItemSerial
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (16):**
- [[OT_SendItemsInfo]]
- [[Pro_ImportPromotionData]]
- [[Pro_PromotionInputOutput]]
- [[Pro_PromotionItemsSchema]]
- [[Pro_PromotionsCondUnCodInput]]
- [[Pro_PromotionsCondUnCodOutput]]
- [[Pro_PromotionsHeaders]]
- [[Pro_SalesPersonItemBonusTarget_OnlineErrorReporting]]
- [[RG_Hakkak_CopyPromotions]]
- [[RG_Rpt_PromotionInformation]]
- [[Rpt_PromotionInputItem]]
- [[Rpt_PromotionsDuplicatedItems]]
- [[SalesmanPromotion_Excel]]

**Writes (6):**
- [[Pro_ImportPromotionData]]
- [[Pro_PromotionsCondUnCodInput]]
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
