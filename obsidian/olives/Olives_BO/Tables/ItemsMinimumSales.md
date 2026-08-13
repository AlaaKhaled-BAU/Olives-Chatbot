---
type: table
database: Olives_BO
name: ItemsMinimumSales
schema: dbo
tags: [#backoffice]
foreign_keys: 0
procedures_reading: 1
support_relevance: low
last_verified: 2026-08-05
---
# ItemsMinimumSales

## Business Purpose

Back-office table in Olives_BO.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| ItemCateg | varchar(50) | NO | ✓ |  |  |
| CustomerGroup | int | NO | ✓ |  |  |
| MinimumSales | float | YES |  |  |  |
| Reference1 | nvarchar(20) | YES |  |  |  |
| Reference2 | nvarchar(20) | YES |  |  |  |
## Primary Key
CompanyID ItemCateg CustomerGroup
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 1 procedure(s): 0 writing, 1 reading.
**Readers (1):**
- [[Pro_ItemsMinimumSales]]

## Estimated Size / Volatility
~1 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
