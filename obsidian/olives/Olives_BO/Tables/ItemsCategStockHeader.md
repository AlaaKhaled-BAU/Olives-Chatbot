---
type: table
database: Olives_BO
name: ItemsCategStockHeader
schema: dbo
tags: [#backoffice]
foreign_keys: 0
procedures_reading: 5
support_relevance: medium
last_verified: 2026-08-05
---
# ItemsCategStockHeader

## Business Purpose

Back-office table in Olives_BO.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| TransactionTypeID | smallint | NO | ✓ |  |  |
| TransactionYear | smallint | NO | ✓ |  |  |
| TransactionNo | int | NO | ✓ |  |  |
| TransactionDate | smalldatetime | YES |  |  |  |
| SalesPersonID | int | YES |  |  |  |
| CustomerID | bigint | YES |  |  |  |
| Latitude | nvarchar(50) | YES |  |  |  |
| Longitude | nvarchar(50) | YES |  |  |  |
| Notes | nvarchar(500) | YES |  |  |  |
| PostedToERP | bit | YES |  |  |  |
| RouteID | int | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
## Primary Key
CompanyID TransactionTypeID TransactionYear TransactionNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 5 procedure(s): 1 writing, 4 reading.
**Writers (1):**
- [[OT_ItemsCategStockHF_Insert]]
**Readers (4):**
- [[OT_ItemsCategStockHF_CheckExist]]
- [[OT_SendSalesmanData]]
- [[OT_SendSalesmanData_Test]]
- [[Pro_ItemsCategStock]]

## Estimated Size / Volatility
~20 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
