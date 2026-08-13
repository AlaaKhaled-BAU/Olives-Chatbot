---
type: table
database: Olives_BO
name: SurveySalesPersonsAssignment
schema: dbo
tags: [#backoffice, #sales, #survey]
foreign_keys:
  - [[SalesPersons]]
  - [[Surveys]]
referenced_by:
  - [[Pro_Surveys]]
support_relevance: high
last_verified: 2026-07-05
---
# SurveySalesPersonsAssignment


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores surveysalespersonsassignment records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Surveys]] |
| Survey_ID | int | NO | ✓ | ✓ | [[Surveys]] |
| SalesPersonsID | int | NO | ✓ | ✓ | [[SalesPersons]] |
## Primary Key
CompanyID
Survey_ID
SalesPersonsID
## Foreign Keys
CompanyID, SalesPersonsID -> [[SalesPersons]](CompanyID, ID)
CompanyID, Survey_ID -> [[Surveys]](CompanyID, Survey_ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_Surveys]]

**Writes (1):**
- [[Pro_Surveys]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
