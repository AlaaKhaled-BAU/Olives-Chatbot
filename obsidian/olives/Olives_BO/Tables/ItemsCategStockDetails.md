---
type: table
database: Olives_BO
name: ItemsCategStockDetails
schema: dbo
tags: [#backoffice]
foreign_keys: 0
procedures_reading: 3
support_relevance: medium
last_verified: 2026-08-05
---
# ItemsCategStockDetails

## Business Purpose

Back-office table in Olives_BO.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| TransactionTypeID | smallint | NO | ✓ |  |  |
| TransactionYear | smallint | NO | ✓ |  |  |
| TransactionNo | int | NO | ✓ |  |  |
| CategCode | nvarchar(100) | NO | ✓ |  |  |
| UnitID | nvarchar(50) | NO | ✓ |  |  |
| Quantity | float | YES |  |  |  |
| Notes | nvarchar(300) | YES |  |  |  |
## Primary Key
CompanyID TransactionTypeID TransactionYear TransactionNo CategCode UnitID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 3 procedure(s): 1 writing, 2 reading.
**Writers (1):**
- [[OT_ItemsCategStockDF_Insert]]
**Readers (2):**
- [[OT_ItemsCategStocDF_CheckExist]]
- [[Pro_ItemsCategStock]]

## Estimated Size / Volatility
~40 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
