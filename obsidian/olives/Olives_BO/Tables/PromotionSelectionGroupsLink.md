---
type: table
database: Olives_BO
name: PromotionSelectionGroupsLink
schema: dbo
tags: [#backoffice, #reference, #sales]
foreign_keys:
referenced_by:
  - [[Pro_PromotionSelectionGroups]]
support_relevance: high
last_verified: 2026-07-05
---
# PromotionSelectionGroupsLink


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores promotionselectiongroupslink records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| SelectionGroupID | int | NO | ✓ |  |  |
| PromotionID | int | NO | ✓ |  |  |
| IsMaster | bit | YES |  |  |  |
## Primary Key
CompanyID
SelectionGroupID
PromotionID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_PromotionSelectionGroups]]

**Writes (1):**
- [[Pro_PromotionSelectionGroups]]

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
