---
type: table
database: Olives_BO
name: PromotionsPrioritiesLink
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
  - [[Companies]]
  - [[PromotionsHeaders]]
  - [[PromotionsPriorities]]
referenced_by:
  - [[Pro_PromotionsHeaders]]
  - [[Pro_PromotionsPrioritiesLink]]
  - [[RG_Hakkak_CopyPromotions]]
support_relevance: high
last_verified: 2026-07-05
---
# PromotionsPrioritiesLink


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores promotionsprioritieslink records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[PromotionsPriorities]] |
| PriorityID | int | NO | ✓ | ✓ | [[PromotionsPriorities]] |
| PromotionID | int | NO | ✓ | ✓ | [[PromotionsHeaders]] |
| PrioritySerial | int | YES |  |  |  |
## Primary Key
CompanyID
PriorityID
PromotionID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, PromotionID -> [[PromotionsHeaders]](CompanyID, ID)
CompanyID, PriorityID -> [[PromotionsPriorities]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (3):**
- [[Pro_PromotionsHeaders]]
- [[Pro_PromotionsPrioritiesLink]]
- [[RG_Hakkak_CopyPromotions]]

**Writes (1):**
- [[Pro_PromotionsPrioritiesLink]]

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
