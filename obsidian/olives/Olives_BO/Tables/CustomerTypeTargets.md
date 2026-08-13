---
type: table
database: Olives_BO
name: CustomerTypeTargets
schema: dbo
tags: [#backoffice, #customer, #reference, #sales]
foreign_keys:
  - [[Companies]]
  - [[CustomersTypes]]
  - [[TargetsTypes]]
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# CustomerTypeTargets


## Business Purpose

Sales performance targets and goals for sales measurement.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[CustomersTypes]] |
| CustomerTypeID | int | NO | ✓ | ✓ | [[CustomersTypes]] |
| TargetYear | smallint | NO | ✓ |  |  |
| TargetMonth | int | NO | ✓ |  |  |
| TargetTypeID | int | YES |  | ✓ | [[TargetsTypes]] |
| Amount | float | YES |  |  |  |
## Primary Key
CompanyID
CustomerTypeID
TargetYear
TargetMonth
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerTypeID -> [[CustomersTypes]](CompanyID, ID)
TargetTypeID -> [[TargetsTypes]](ID)
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
- [[Olives_BO/Tables/CustomerTypeTargetsDetails]]
