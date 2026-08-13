---
type: table
database: Olives_BO
name: CustomerClassTargets
schema: dbo
tags: [#backoffice, #customer, #reference, #sales]
foreign_keys:
  - [[Companies]]
  - [[CustomersClasses]]
  - [[TargetsTypes]]
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# CustomerClassTargets


## Business Purpose

Sales performance targets and goals for sales measurement.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[CustomersClasses]] |
| CustomerClassID | int | NO | ✓ | ✓ | [[CustomersClasses]] |
| TargetYear | smallint | NO | ✓ |  |  |
| TargetMonth | int | NO | ✓ |  |  |
| TargetTypeID | int | YES |  | ✓ | [[TargetsTypes]] |
| Amount | float | YES |  |  |  |
## Primary Key
CompanyID
CustomerClassID
TargetYear
TargetMonth
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerClassID -> [[CustomersClasses]](CompanyID, ID)
TargetTypeID -> [[TargetsTypes]](ID)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing reference values**: Required dropdown items not present — selection fails on tablet
- **Duplicate codes**: Same code used for different descriptions — mapping ambiguity
- **Orphan references**: Referenced by deleted records — FK violation on delete attempt

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
