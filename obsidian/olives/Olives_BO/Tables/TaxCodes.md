---
type: table
database: Olives_BO
name: TaxCodes
schema: dbo
tags: [#backoffice, #billing, #legal, #reference]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# TaxCodes


## Business Purpose

Classification or reference codes for sales data categorization.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| TaxID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| Percentage | float | YES |  |  |  |
| isExemptTax | bit | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
TaxID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**

**Writes (1):**

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing reference values**: Required dropdown items not present — selection fails on tablet
- **Duplicate codes**: Same code used for different descriptions — mapping ambiguity
- **Orphan references**: Referenced by deleted records — FK violation on delete attempt

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
