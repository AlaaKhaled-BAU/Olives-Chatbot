---
type: table
database: Olives_BO
name: SalesPersonBonusLimit
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
  - [[Companies]]
  - [[SalesPersons]]
referenced_by:
  - [[Pro_SalesPersonBonusLimit]]
  - [[Pro_SalesPersonCollectionTargets]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonBonusLimit


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonbonuslimit records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| SalesPersonID | int | NO | ✓ | ✓ | [[SalesPersons]] |
| BonusYear | smallint | NO | ✓ |  |  |
| BonusMonth | smallint | NO | ✓ |  |  |
| BonusType | int | NO | ✓ |  |  |
| BonusLimit | float | YES |  |  |  |
## Primary Key
CompanyID
SalesPersonID
BonusYear
BonusMonth
BonusType
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_SalesPersonBonusLimit]]
- [[Pro_SalesPersonCollectionTargets]]

**Writes (2):**
- [[Pro_SalesPersonBonusLimit]]
- [[Pro_SalesPersonCollectionTargets]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
