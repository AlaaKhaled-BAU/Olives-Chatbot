---
type: table
database: Olives_BO
name: PromptEmbeddings
schema: dbo
tags: [#backoffice]
foreign_keys: 0
procedures_reading: 0
support_relevance: low
last_verified: 2026-08-05
---
# PromptEmbeddings

## Business Purpose

Back-office table in Olives_BO.
No procedures or foreign keys reference it in the dependency graph — likely a temp/utility table.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| Id | int | NO | ✓ |  |  |
| PromptText | nvarchar(MAX) | YES |  |  |  |
| Response | nvarchar(MAX) | YES |  |  |  |
| Embedding | nvarchar(MAX) | YES |  |  |  |
## Primary Key
Id
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 0 procedure(s): 0 writing, 0 reading.
_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
~5 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
