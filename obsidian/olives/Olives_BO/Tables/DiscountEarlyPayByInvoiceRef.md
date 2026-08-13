---
type: table
database: Olives_BO
name: DiscountEarlyPayByInvoiceRef
schema: dbo
tags: [#backoffice]
foreign_keys: 0
procedures_reading: 2
support_relevance: medium
last_verified: 2026-08-05
---
# DiscountEarlyPayByInvoiceRef

## Business Purpose

Back-office table in Olives_BO.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| InvoiceRef | varchar(500) | NO | ✓ |  |  |
| CustomerID | bigint | NO | ✓ |  |  |
| SalespersonID | int | YES |  |  |  |
| DiscountPerc | float | YES |  |  |  |
| Ref1 | varchar(50) | YES |  |  |  |
| Ref2 | varchar(50) | YES |  |  |  |
## Primary Key
CompanyID InvoiceRef CustomerID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 2 procedure(s): 1 writing, 1 reading.
**Writers (1):**
- [[Pro_DiscountEarlyPayByInvoiceRef]]
**Readers (1):**
- [[OSFA_DB/Procedures/OT_AppService|OT_AppService]]

## Estimated Size / Volatility
~2 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
