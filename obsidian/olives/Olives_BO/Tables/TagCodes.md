---
type: table
database: Olives_BO
name: TagCodes
schema: dbo
tags: [#backoffice, #reference]
foreign_keys:
referenced_by:
  - [[Rpt_GetGapTrans]]
support_relevance: high
last_verified: 2026-07-05
---
# TagCodes


## Business Purpose

Classification or reference codes for sales data categorization.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| TagTypeID | nvarchar | YES | ✓ |  |  |
| TagID | nvarchar | YES | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
TagTypeID
TagID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Rpt_GetGapTrans]]

**Writes (0):**
_None_

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing reference values**: Required dropdown items not present — selection fails on tablet
- **Duplicate codes**: Same code used for different descriptions — mapping ambiguity
- **Orphan references**: Referenced by deleted records — FK violation on delete attempt

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
