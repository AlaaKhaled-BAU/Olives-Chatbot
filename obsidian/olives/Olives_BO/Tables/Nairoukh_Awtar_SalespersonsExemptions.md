---
type: table
database: Olives_BO
name: Nairoukh_Awtar_SalespersonsExemptions
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
referenced_by:
  - [[Pro_SalesPersons]]
support_relevance: high
last_verified: 2026-07-05
---
# Nairoukh_Awtar_SalespersonsExemptions


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores nairoukh awtar salespersonsexemptions records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | YES |  |  |  |
| SalespersonID | int | YES |  |  |  |
| PositionID | int | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_SalesPersons]]

**Writes (0):**
_None_

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
