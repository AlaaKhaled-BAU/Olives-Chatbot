---
type: table
database: Olives_BO
name: SalesPersonsAdditionalRoutes
schema: dbo
tags: [#backoffice, #gps, #sales]
foreign_keys:
  - [[Companies]]
  - [[Positions]]
  - [[RoutesInformation]]
referenced_by:
  - [[Pro_SalesPersonsAdditionalRoutes]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonsAdditionalRoutes


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonsadditionalroutes records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[RoutesInformation]] |
| PositionID | int | NO | ✓ | ✓ | [[Positions]] |
| WeekNo | int | NO | ✓ |  |  |
| DayNo | smallint | NO | ✓ |  |  |
| RouteID | int | NO | ✓ | ✓ | [[RoutesInformation]] |
| FromPositionID | int | YES |  | ✓ | [[Positions]] |
| FromWeekNo | int | YES |  |  |  |
| FromDayNo | int | YES |  |  |  |
## Primary Key
CompanyID
PositionID
WeekNo
DayNo
RouteID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, FromPositionID -> [[Positions]](CompanyID, ID)
CompanyID, PositionID -> [[Positions]](CompanyID, ID)
CompanyID, RouteID -> [[RoutesInformation]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_SalesPersonsAdditionalRoutes]]

**Writes (1):**
- [[Pro_SalesPersonsAdditionalRoutes]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
