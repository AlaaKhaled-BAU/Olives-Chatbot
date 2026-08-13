---
type: table
database: Olives_BO
name: UserActivity
schema: dbo
tags: [#auth, #backoffice]
foreign_keys:
  - [[Companies]]
  - [[Users]]
referenced_by:
  - [[Pro_UserActivity]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Users-and-Permissions
---
# UserActivity


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores useractivity records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| UserID | nvarchar | YES | ✓ | ✓ | [[Users]] |
| AmendCreditLimit | bit | YES |  |  |  |
| AmendChqsDueDays | bit | YES |  |  |  |
| AmendAllowChqs | bit | YES |  |  |  |
| AmendPaymentType | bit | YES |  |  |  |
| AmendDueDays | bit | YES |  |  |  |
| AmendMaxInvoiceValue | bit | YES |  |  |  |
| AmendInvoiceType | bit | YES |  |  |  |
| AmendPriceList | bit | YES |  |  |  |
| AmendDicount | bit | YES |  |  |  |
| AmendMaxInoiceCount | bit | YES |  |  |  |
| AmendTaxInclude | bit | YES |  |  |  |
| HideBonus | bit | YES |  |  |  |
## Primary Key
CompanyID
UserID
## Foreign Keys
CompanyID -> [[Companies]](ID)
UserID -> [[Users]](UserID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_UserActivity]]

**Writes (1):**
- [[Pro_UserActivity]]

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
