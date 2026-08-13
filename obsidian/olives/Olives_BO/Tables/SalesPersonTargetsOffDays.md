---
type: table
database: Olives_BO
name: SalesPersonTargetsOffDays
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
referenced_by:
  - [[Pro_TargetsOffDays]]
  - [[Rpt_TargetSpartan]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonTargetsOffDays


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersontargetsoffdays records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| SalesPersonID | int | NO | ✓ |  |  |
| TargetYear | smallint | NO | ✓ |  |  |
| TargetMonth | int | NO | ✓ |  |  |
| OffDay | smalldatetime | NO | ✓ |  |  |
## Primary Key
CompanyID
SalesPersonID
TargetYear
TargetMonth
OffDay
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_TargetsOffDays]]
- [[Rpt_TargetSpartan]]

**Writes (1):**
- [[Pro_TargetsOffDays]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
