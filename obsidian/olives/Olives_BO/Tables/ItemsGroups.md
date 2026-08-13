---
type: table
database: Olives_BO
name: ItemsGroups
schema: dbo
tags: [#backoffice]
foreign_keys: 1
procedures_reading: 3
support_relevance: medium
last_verified: 2026-08-05
---
# ItemsGroups

## Business Purpose

Back-office table in Olives_BO.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar(100) | NO |  |  |  |
| ShortName | nvarchar(10) | YES |  |  |  |
| Reference1 | nvarchar(20) | YES |  |  |  |
| Reference2 | nvarchar(20) | YES |  |  |  |
## Primary Key
CompanyID ID
## Foreign Keys
- ItemsGroups.CompanyID → [[Companies]].ID
**Referenced by (incoming FKs):**
- [[Items]].CompanyID → ItemsGroups.CompanyID
## Impact / Procedures Using This Table

Referenced by 3 procedure(s): 0 writing, 3 reading.
**Readers (3):**
- [[Bisan_Integration]]
- [[MeatLand_Integration]]
- [[MeatLand_Integrationnew]]

## Estimated Size / Volatility
~3 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
