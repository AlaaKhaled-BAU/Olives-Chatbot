---
type: table
database: Olives_BO
name: PromotionsCondUnCodOutput
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[PromotionsHeaders]]
referenced_by:
  - [[Pro_ImportPromotionData]]
  - [[Pro_PromotionInputOutput]]
  - [[Pro_PromotionItemsSchema]]
  - [[Pro_PromotionsCondUnCodOutput]]
  - [[Pro_PromotionsHeaders]]
  - [[Pro_SalesPersonItemBonusTarget_OnlineErrorReporting]]
  - [[RG_Hakkak_CopyPromotions]]
  - [[RG_Rpt_PromotionInformation]]
  - [[Rpt_PromotionOutputItem]]
  - [[Rpt_PromotionsDuplicatedItems]]
  - [[SalesmanPromotion_Excel]]
support_relevance: high
last_verified: 2026-07-05
---
# PromotionsCondUnCodOutput


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores promotionsconduncodoutput records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[PromotionsHeaders]] |
| PromotionID | int | NO | ✓ | ✓ | [[PromotionsHeaders]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| ItemSerial | smallint | NO | ✓ |  |  |
| ItemUnitID | nvarchar | YES |  |  |  |
| Quantity | float | YES |  |  |  |
| OutPutType | int | YES |  |  |  |
| DiscountType | smallint | YES |  |  |  |
| IsConditional | bit | YES |  |  |  |
| DiscountValue | float | YES |  |  |  |
| StartDate | smalldatetime | YES |  |  |  |
| EndDate | smalldatetime | YES |  |  |  |
## Primary Key
CompanyID
PromotionID
ItemCode
ItemSerial
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, PromotionID -> [[PromotionsHeaders]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (14):**
- [[Pro_ImportPromotionData]]
- [[Pro_PromotionInputOutput]]
- [[Pro_PromotionItemsSchema]]
- [[Pro_PromotionsCondUnCodOutput]]
- [[Pro_PromotionsHeaders]]
- [[Pro_SalesPersonItemBonusTarget_OnlineErrorReporting]]
- [[RG_Hakkak_CopyPromotions]]
- [[RG_Rpt_PromotionInformation]]
- [[Rpt_PromotionOutputItem]]
- [[Rpt_PromotionsDuplicatedItems]]
- [[SalesmanPromotion_Excel]]

**Writes (6):**
- [[Pro_ImportPromotionData]]
- [[Pro_PromotionsCondUnCodOutput]]
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
