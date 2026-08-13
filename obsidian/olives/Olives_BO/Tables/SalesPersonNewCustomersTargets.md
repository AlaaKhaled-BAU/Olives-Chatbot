---
type: table
database: Olives_BO
name: SalesPersonNewCustomersTargets
schema: dbo
tags: [#backoffice, #customer, #sales]
foreign_keys:
  - [[Companies]]
  - [[SalesPersons]]
referenced_by:
  - [[AppDashBoard]]
  - [[Pro_SalesPersonNewCustomersTargets]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonNewCustomersTargets


## Business Purpose

Sales performance targets and goals for sales measurement.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| SalesPersonID | int | NO | ✓ | ✓ | [[SalesPersons]] |
| TargetYear | smallint | NO | ✓ |  |  |
| TargetMonth | int | NO | ✓ |  |  |
| Value | int | YES |  |  |  |
| DaysNumber | int | YES |  |  |  |
## Primary Key
CompanyID
SalesPersonID
TargetYear
TargetMonth
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (2):**
- [[AppDashBoard]]
- [[Pro_SalesPersonNewCustomersTargets]]

**Writes (1):**
- [[Pro_SalesPersonNewCustomersTargets]]

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
