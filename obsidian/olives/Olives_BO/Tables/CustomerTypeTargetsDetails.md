---
type: table
database: Olives_BO
name: CustomerTypeTargetsDetails
schema: dbo
tags: [#backoffice, #customer, #reference, #sales]
foreign_keys:
  - [[Companies]]
  - [[CustomersTypes]]
  - [[CustomerTypeTargets]]
  - [[TargetsReferences]]
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# CustomerTypeTargetsDetails


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customertypetargetsdetails records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[TargetsReferences]] |
| CustomertypeID | int | NO | ✓ | ✓ | [[CustomerTypeTargets]] |
| TargetYear | smallint | NO | ✓ | ✓ | [[CustomerTypeTargets]] |
| TargetMonth | int | NO | ✓ | ✓ | [[CustomerTypeTargets]] |
| TargetReferenceID | int | NO | ✓ | ✓ | [[TargetsReferences]] |
| Quantity | float | YES |  |  |  |
| Amount | float | YES |  |  |  |
## Primary Key
CompanyID
CustomertypeID
TargetYear
TargetMonth
TargetReferenceID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomertypeID -> [[CustomersTypes]](CompanyID, ID)
CompanyID, CustomertypeID, TargetYear, TargetMonth -> [[CustomerTypeTargets]](CompanyID, CustomerTypeID, TargetYear, TargetMonth)
CompanyID, TargetReferenceID -> [[TargetsReferences]](CompanyID, ID)
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
