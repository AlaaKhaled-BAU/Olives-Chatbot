---
type: table
database: Olives_BO
name: MIMETypes
schema: dbo
tags: [#backoffice, #reference]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# MIMETypes


## Business Purpose

Reference/lookup table defining mimetypes categories.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AppType | nvarchar | YES | ✓ |  |  |
| AppExt | nvarchar | YES | ✓ |  |  |
## Primary Key
AppType
AppExt
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing reference values**: Required dropdown items not present — selection fails on tablet
- **Duplicate codes**: Same code used for different descriptions — mapping ambiguity
- **Orphan references**: Referenced by deleted records — FK violation on delete attempt

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
