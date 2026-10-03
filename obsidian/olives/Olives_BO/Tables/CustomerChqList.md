---
type: table
database: Olives_BO
name: CustomerChqList
schema: dbo
tags: [#backoffice, #customer]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# CustomerChqList


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customerchqlist records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| CustomerID | nvarchar | YES | ✓ |  |  |
| ChqNo | int | NO | ✓ |  |  |
| BankNo | int | NO | ✓ |  |  |
| BankDesc | varchar | YES |  |  |  |
| DeptNo | int | YES |  |  |  |
| DeptName | varchar | YES |  |  |  |
| DueDate | smalldatetime | YES |  |  |  |
| VouNo | int | YES |  |  |  |
| VouDate | smalldatetime | YES |  |  |  |
| ChqStatus | varchar | YES |  |  |  |
| Amount | float | YES |  |  |  |
| PaidAmount | float | YES |  |  |  |
| RemAmount | float | YES |  |  |  |
## Primary Key
CompNo
CustomerID
ChqNo
BankNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (5):**

**Writes (4):**

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Duplicate customers**: Multiple records with same name/phone created during sync — support agent sees duplicate entries in dropdowns
- **Orphan references**: Customer records referenced by transactions that were soft-deleted — causes FK violation on cleanup
- **Balance mismatch**: CustomerBalance field diverges from actual calculated balance — run reconciliation proc
- **Suspend stuck**: IsSuspended flag not clearing after payment — check WF approval chain
- **GPS not collected**: IsCollectedGPS flag false — affects route optimization

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
