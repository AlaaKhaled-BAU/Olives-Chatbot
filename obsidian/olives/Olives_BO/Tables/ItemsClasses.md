---
type: table
database: Olives_BO
name: ItemsClasses
schema: dbo
tags: [#backoffice, #inventory, #reference]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[Pro_ItemsClasses]]
  - [[Pro_ItemsUsedInLoadOrderAssignment]]
  - [[Pro_SalesPersonItemsAssignment]]
support_relevance: high
last_verified: 2026-07-05
---
# ItemsClasses


## Business Purpose

Classification or reference codes for sales data categorization.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (3):**
- [[Pro_ItemsClasses]]
- [[Pro_ItemsUsedInLoadOrderAssignment]]
- [[Pro_SalesPersonItemsAssignment]]

**Writes (1):**
- [[Pro_ItemsClasses]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing reference values**: Required dropdown items not present — selection fails on tablet
- **Duplicate codes**: Same code used for different descriptions — mapping ambiguity
- **Orphan references**: Referenced by deleted records — FK violation on delete attempt

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
