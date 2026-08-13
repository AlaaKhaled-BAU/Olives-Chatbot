---
type: table
database: Olives_BO
name: TargetsTypes
schema: dbo
tags: [#backoffice, #reference, #sales]
foreign_keys:
referenced_by:
  - [[Pro_CustomerTargets]]
  - [[Pro_LocationTargets]]
  - [[Pro_SalesPersonTargets]]
  - [[Pro_TargetsTypes]]
support_relevance: high
last_verified: 2026-07-05
---
# TargetsTypes


## Business Purpose

Reference/lookup table defining targetstypes categories.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
## Primary Key
ID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (4):**
- [[Pro_CustomerTargets]]
- [[Pro_LocationTargets]]
- [[Pro_SalesPersonTargets]]
- [[Pro_TargetsTypes]]

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
