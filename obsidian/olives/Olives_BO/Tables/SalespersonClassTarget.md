---
type: table
database: Olives_BO
name: SalespersonClassTarget
schema: dbo
tags: [#backoffice, #reference, #sales]
foreign_keys:
referenced_by:
  - [[Pro_SalesmanClassTarget]]
  - [[Rpt_Coverage]]
support_relevance: high
last_verified: 2026-07-05
---
# SalespersonClassTarget


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonclasstarget records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | int | NO | ✓ |  |  |
| SalesmanID | int | NO | ✓ |  |  |
| ClassID | int | NO | ✓ |  |  |
| TargetFrequency | int | YES |  |  |  |
## Primary Key
CompanyID
SalesmanID
ClassID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_SalesmanClassTarget]]
- [[Rpt_Coverage]]

**Writes (1):**
- [[Pro_SalesmanClassTarget]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
