---
type: table
database: Olives_BO
name: CustomerData_Sample
schema: dbo
tags: [#backoffice, #customer]
foreign_keys:
referenced_by:
support_relevance: low
last_verified: 2026-07-05
---
# CustomerData_Sample


## Business Purpose

Temporary or sample data — not part of core transaction flow.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | int | YES |  |  |  |
| CustID | bigint | YES |  |  |  |
| postion | bigint | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

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
