---
type: table
database: Olives_BO
name: SalespersonRouteByDate
schema: dbo
tags: [#backoffice, #gps, #sales]
foreign_keys:
referenced_by:
  - [[Pro_SalespersonRouteByDate]]
support_relevance: high
last_verified: 2026-07-05
---
# SalespersonRouteByDate


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonroutebydate records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| PositionID | int | NO | ✓ |  |  |
| RouteID | int | NO | ✓ |  |  |
| Date | date | NO | ✓ |  |  |
| Notes | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
PositionID
RouteID
Date
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_SalespersonRouteByDate]]

**Writes (1):**
- [[Pro_SalespersonRouteByDate]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
