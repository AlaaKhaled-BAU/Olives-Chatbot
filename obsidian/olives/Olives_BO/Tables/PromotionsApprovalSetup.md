---
type: table
database: Olives_BO
name: PromotionsApprovalSetup
schema: dbo
tags: [#backoffice, #integration, #sales, #workflow]
foreign_keys:
referenced_by:
  - [[Pro_PromotionsApproval]]
  - [[Pro_PromotionsHeaders]]
support_relevance: high
last_verified: 2026-07-05
---
# PromotionsApprovalSetup


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores promotionsapprovalsetup records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| UserID | nvarchar | YES | ✓ |  |  |
| Level | smallint | YES |  |  |  |
## Primary Key
CompanyID
UserID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_PromotionsApproval]]
- [[Pro_PromotionsHeaders]]

**Writes (1):**
- [[Pro_PromotionsApproval]]

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
