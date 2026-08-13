---
type: table
database: Olives_BO
name: LocationTargetsDetails
schema: dbo
tags: [#backoffice, #gps, #sales]
foreign_keys:
  - [[Companies]]
  - [[Locations]]
  - [[LocationTargets]]
  - [[TargetsReferences]]
referenced_by:
  - [[Pro_LocationTargets]]
  - [[Pro_LocationTargetsDetails]]
  - [[RPT_LOCATIONSMAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
  - [[RPT_LOCATIONS_CUSTOMERTYPE_MAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
  - [[RPT_NIROUKHLOCATIONTARGET]]
  - [[Rpt_Niroukh_LocationTarget]]
support_relevance: high
last_verified: 2026-07-05
---
# LocationTargetsDetails


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores locationtargetsdetails records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[TargetsReferences]] |
| LocationID | int | NO | ✓ | ✓ | [[LocationTargets]] |
| TargetYear | smallint | NO | ✓ | ✓ | [[LocationTargets]] |
| TargetMonth | int | NO | ✓ | ✓ | [[LocationTargets]] |
| TargetReferenceID | int | NO | ✓ | ✓ | [[TargetsReferences]] |
| Quantity | float | YES |  |  |  |
| Amount | float | YES |  |  |  |
## Primary Key
CompanyID
LocationID
TargetYear
TargetMonth
TargetReferenceID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, LocationID -> [[Locations]](CompanyID, ID)
CompanyID, LocationID, TargetYear, TargetMonth -> [[LocationTargets]](CompanyID, LocationID, TargetYear, TargetMonth)
CompanyID, TargetReferenceID -> [[TargetsReferences]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (6):**
- [[Pro_LocationTargets]]
- [[Pro_LocationTargetsDetails]]
- [[RPT_LOCATIONSMAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
- [[RPT_LOCATIONS_CUSTOMERTYPE_MAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
- [[RPT_NIROUKHLOCATIONTARGET]]
- [[Rpt_Niroukh_LocationTarget]]

**Writes (2):**
- [[Pro_LocationTargets]]
- [[Pro_LocationTargetsDetails]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing GPS data**: No coordinates recorded — route planning and distance calc broken
- **Invalid coordinates**: GPSX/GPSY outside expected range — verify device GPS setting
- **Stale locations**: Old coordinates not updated — customer moved but records not refreshed

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
