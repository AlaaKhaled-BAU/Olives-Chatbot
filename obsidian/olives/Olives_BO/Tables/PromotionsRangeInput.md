---
type: table
database: Olives_BO
name: PromotionsRangeInput
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[PromotionsHeaders]]
referenced_by:
  - [[Pro_ImportPromotionData]]
  - [[Pro_PromotionItemsSchema]]
  - [[Pro_PromotionsHeaders]]
  - [[Pro_PromotionsRangeInput]]
  - [[RG_Hakkak_CopyPromotions]]
  - [[Rpt_PromotionsDuplicatedItems]]
  - [[Rpt_RangePromotionInput]]
support_relevance: high
last_verified: 2026-07-05
---
# PromotionsRangeInput


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores promotionsrangeinput records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[PromotionsHeaders]] |
| PromotionID | int | NO | ✓ | ✓ | [[PromotionsHeaders]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| ItemUnitID | nvarchar | YES | ✓ | ✓ | [[ItemsUnits]] |
| FromQuantity | float | NO | ✓ |  |  |
| ToQuantity | float | YES |  |  |  |
| OutputQuantity | float | YES |  |  |  |
## Primary Key
CompanyID
PromotionID
ItemCode
ItemUnitID
FromQuantity
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, ItemUnitID -> [[ItemsUnits]](CompanyID, ID)
CompanyID, PromotionID -> [[PromotionsHeaders]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (10):**
- [[Pro_ImportPromotionData]]
- [[Pro_PromotionItemsSchema]]
- [[Pro_PromotionsHeaders]]
- [[Pro_PromotionsRangeInput]]
- [[RG_Hakkak_CopyPromotions]]
- [[Rpt_PromotionsDuplicatedItems]]
- [[Rpt_RangePromotionInput]]

**Writes (5):**
- [[Pro_ImportPromotionData]]
- [[Pro_PromotionsRangeInput]]

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
