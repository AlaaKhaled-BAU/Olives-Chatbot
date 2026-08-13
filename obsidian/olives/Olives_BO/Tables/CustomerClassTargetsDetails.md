---
type: table
database: Olives_BO
name: CustomerClassTargetsDetails
schema: dbo
tags: [#backoffice, #customer, #reference, #sales]
foreign_keys:
  - [[Companies]]
  - [[CustomerClassTargets]]
  - [[CustomersClasses]]
  - [[TargetsReferences]]
referenced_by:
  - [[RPT_NIROUKHCUSTOMERCLASSTARGET]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomerClassTargetsDetails


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customerclasstargetsdetails records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[TargetsReferences]] |
| CustomerClassID | int | NO | ✓ | ✓ | [[CustomersClasses]] |
| TargetYear | smallint | NO | ✓ | ✓ | [[CustomerClassTargets]] |
| TargetMonth | int | NO | ✓ | ✓ | [[CustomerClassTargets]] |
| TargetReferenceID | int | NO | ✓ | ✓ | [[TargetsReferences]] |
| Quantity | float | YES |  |  |  |
| Amount | float | YES |  |  |  |
## Primary Key
CompanyID
CustomerClassID
TargetYear
TargetMonth
TargetReferenceID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerClassID, TargetYear, TargetMonth -> [[CustomerClassTargets]](CompanyID, CustomerClassID, TargetYear, TargetMonth)
CompanyID, CustomerClassID -> [[CustomersClasses]](CompanyID, ID)
CompanyID, TargetReferenceID -> [[TargetsReferences]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[RPT_NIROUKHCUSTOMERCLASSTARGET]]

**Writes (0):**
_None_

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing reference values**: Required dropdown items not present — selection fails on tablet
- **Duplicate codes**: Same code used for different descriptions — mapping ambiguity
- **Orphan references**: Referenced by deleted records — FK violation on delete attempt

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
