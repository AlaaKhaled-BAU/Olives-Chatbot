---
type: table
database: Olives_BO
name: UserPromotionsLink
schema: dbo
tags: [#auth, #backoffice, #integration, #sales]
foreign_keys:
  - [[Companies]]
  - [[PromotionsHeaders]]
  - [[Users]]
referenced_by:
  - [[Pro_PromotionsHeaders]]
support_relevance: high
last_verified: 2026-07-05
---
# UserPromotionsLink


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores userpromotionslink records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[PromotionsHeaders]] |
| UserID | nvarchar | YES | ✓ | ✓ | [[Users]] |
| PromotionCode | int | NO | ✓ | ✓ | [[PromotionsHeaders]] |
## Primary Key
CompanyID
UserID
PromotionCode
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, PromotionCode -> [[PromotionsHeaders]](CompanyID, ID)
UserID -> [[Users]](UserID)
## Impact / Procedures Using This Table

**Reads (0):**
_None_

**Writes (1):**
- [[Pro_PromotionsHeaders]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Integration stuck**: IsPosted flag not clearing — check ERP connection and error log
- **Duplicate sent**: Same transaction sent multiple times — ERP shows duplicates
- **Mapping error**: Field mapping fails — check IntegrationPostedTransactions for error details
- **Timeout**: Large batch exceeds ERP timeout — split into smaller batches

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
