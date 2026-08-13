---
type: table
database: Olives_BO
name: PromotionsDontApply
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
referenced_by:
  - [[Pro_NotAppliedPromotion]]
support_relevance: high
last_verified: 2026-07-05
---
# PromotionsDontApply


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores promotionsdontapply records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| PromotionID | int | NO | ✓ |  |  |
| DontApplyPromotionID | int | NO | ✓ |  |  |
## Primary Key
CompanyID
PromotionID
DontApplyPromotionID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_NotAppliedPromotion]]

**Writes (1):**
- [[Pro_NotAppliedPromotion]]

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
