---
type: table
database: Olives_BO
name: LocationTargets
schema: dbo
tags: [#backoffice, #gps, #sales]
foreign_keys:
  - [[Companies]]
  - [[Locations]]
  - [[TargetsTypes]]
referenced_by:
  - [[Pro_LocationTargets]]
support_relevance: high
last_verified: 2026-07-05
---
# LocationTargets


## Business Purpose

Sales performance targets and goals for sales measurement.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Locations]] |
| LocationID | int | NO | ✓ | ✓ | [[Locations]] |
| TargetYear | smallint | NO | ✓ |  |  |
| TargetMonth | int | NO | ✓ |  |  |
| TargetTypeID | int | YES |  | ✓ | [[TargetsTypes]] |
| Amount | float | YES |  |  |  |
## Primary Key
CompanyID
LocationID
TargetYear
TargetMonth
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, LocationID -> [[Locations]](CompanyID, ID)
TargetTypeID -> [[TargetsTypes]](ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_LocationTargets]]

**Writes (1):**
- [[Pro_LocationTargets]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing GPS data**: No coordinates recorded — route planning and distance calc broken
- **Invalid coordinates**: GPSX/GPSY outside expected range — verify device GPS setting
- **Stale locations**: Old coordinates not updated — customer moved but records not refreshed

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
