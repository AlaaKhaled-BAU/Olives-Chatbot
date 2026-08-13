---
type: table
database: Olives_BO
name: SalesPersonCollectionsTargets
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
  - [[Companies]]
  - [[SalesPersons]]
referenced_by:
  - [[AccPack_Integ_LuxuryItems]]
  - [[DA_SalesTarget]]
  - [[Pro_SalesPerson_Collection_Targets]]
  - [[Rpt_SalesAndCollectionTargetByLocation]]
  - [[Rpt_SalesCollcetionsTargets]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonCollectionsTargets


## Business Purpose

Sales performance targets and goals for sales measurement.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| SalesPersonID | int | NO | ✓ | ✓ | [[SalesPersons]] |
| TargetYear | smallint | NO | ✓ |  |  |
| TargetMonth | int | NO | ✓ |  |  |
| Amount | float | YES |  |  |  |
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

**Reads (4):**
- [[DA_SalesTarget]]
- [[Pro_SalesPerson_Collection_Targets]]
- [[Rpt_SalesAndCollectionTargetByLocation]]
- [[Rpt_SalesCollcetionsTargets]]

**Writes (2):**
- [[AccPack_Integ_LuxuryItems]]
- [[Pro_SalesPerson_Collection_Targets]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
