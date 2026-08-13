---
type: table
database: Olives_BO
name: PromotionsApprovalLog
schema: dbo
tags: [#backoffice, #integration, #log, #sales, #workflow]
foreign_keys:
referenced_by:
  - [[Pro_PromotionsApproval]]
  - [[Pro_PromotionsHeaders]]
support_relevance: low
last_verified: 2026-07-05
---
# PromotionsApprovalLog


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores promotionsapprovallog records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | decimal | YES | ✓ |  |  |
| CompanyID | smallint | NO |  |  |  |
| UserID | nvarchar | YES |  |  |  |
| PromoID | int | NO |  |  |  |
| ApprovedBy | nvarchar | YES |  |  |  |
| ApproveDate | smalldatetime | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| Approved | bit | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_PromotionsApproval]]
- [[Pro_PromotionsHeaders]]

**Writes (2):**
- [[Pro_PromotionsApproval]]
- [[Pro_PromotionsHeaders]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Rapid growth**: Table size growing fast — archive old records periodically
- **Orphan log entries**: No corresponding source transaction — investigate data source
- **No cleanup**: No purge job configured — disk space may fill up

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Olives_BO/Tables/CustomerSalesByCategory]]
- [[Olives_BO/Tables/SpecialCustomerTarget]]
