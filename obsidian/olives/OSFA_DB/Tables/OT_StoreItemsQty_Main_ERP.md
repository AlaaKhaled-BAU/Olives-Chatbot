---
type: table
database: OSFA_DB
name: OT_StoreItemsQty_Main_ERP
schema: dbo
tags: [#maintenance]
foreign_keys: 0
procedures_reading: 2
support_relevance: medium
last_verified: 2026-08-05
---
# OT_StoreItemsQty_Main_ERP

## Business Purpose

Back-office table in OSFA_DB.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| StoreNo | int | NO | ✓ |  |  |
| ItemNo | varchar(100) | NO | ✓ |  |  |
| Qty | money | YES |  |  |  |
## Primary Key
CompNo StoreNo ItemNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 2 procedure(s): 0 writing, 2 reading.
**Readers (2):**
- [[Olives_BO/Procedures/OT_SendSalesmanData|OT_SendSalesmanData]]
- [[Olives_BO/Procedures/OT_SendSalesmanData_Test|OT_SendSalesmanData_Test]]

## Estimated Size / Volatility
~0 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-OSFA_DB|OSFA_DB MOC]]
