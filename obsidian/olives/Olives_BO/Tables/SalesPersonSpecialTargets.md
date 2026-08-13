---
type: table
database: Olives_BO
name: SalesPersonSpecialTargets
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
referenced_by:
  - [[Rpt_SalesPersonSpecialTargets]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonSpecialTargets


## Business Purpose

Sales performance targets and goals for sales measurement.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| SalesPersonID | int | NO | ✓ |  |  |
| TargetYear | smallint | NO | ✓ |  |  |
| TargetMonth | int | NO | ✓ |  |  |
| SalesAmount | float | YES |  |  |  |
| InvoiceAvgCount | int | YES |  |  |  |
| ItemAvgCount | int | YES |  |  |  |
## Primary Key
CompanyID
SalesPersonID
TargetYear
TargetMonth
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Rpt_SalesPersonSpecialTargets]]

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
