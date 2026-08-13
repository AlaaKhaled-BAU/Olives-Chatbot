---
type: table
database: Olives_BO
name: PromotionBudget
schema: dbo
tags: [#backoffice]
foreign_keys: 0
procedures_reading: 4
support_relevance: medium
last_verified: 2026-08-05
---
# PromotionBudget

## Business Purpose

Back-office table in Olives_BO.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | int | NO | ✓ |  |  |
| IONumber | nvarchar(200) | NO | ✓ |  |  |
| IODescription | nvarchar(200) | YES |  |  |  |
| IODate | datetime | YES |  |  |  |
| IOLimitValue | float | YES |  |  |  |
| IOValue | float | YES |  |  |  |
## Primary Key
CompanyID IONumber
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 4 procedure(s): 3 writing, 1 reading.
**Writers (3):**
- [[Pro_ImportPromotionBudgetData]]
- [[Pro_PromotionBudget]]
- [[Pro_UpdatePromotionBudgetFromSAP]]
**Readers (1):**
- [[Pro_CheckPromotionBudgetValue]]

## Estimated Size / Volatility
~3 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
