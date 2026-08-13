---
type: table
database: OSFA_DB
name: OT_RequestToCancelPayment
schema: dbo
tags: [#maintenance]
foreign_keys: 0
procedures_reading: 2
support_relevance: medium
last_verified: 2026-08-05
---
# OT_RequestToCancelPayment

## Business Purpose

Back-office table in OSFA_DB.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric(30,0) | NO | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
| TrYear | smallint | YES |  |  |  |
| TrType | smallint | YES |  |  |  |
| TrNo | int | YES |  |  |  |
| SalesPersonNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| ReceiptAmount | float | YES |  |  |  |
| ChecksInfo | nvarchar(MAX) | YES |  |  |  |
| InvoiceInfo | nvarchar(MAX) | YES |  |  |  |
| Notes | nvarchar(MAX) | YES |  |  |  |
| DiscountAmount | float | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| IsPosted | bit | YES |  |  |  |
| Latitude | nvarchar(50) | YES |  |  |  |
| Longitude | nvarchar(50) | YES |  |  |  |
| TabletSysID | varchar(50) | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 2 procedure(s): 1 writing, 1 reading.
**Writers (1):**
- [[OT_RequestToCancelPayment_Insert]]
**Readers (1):**
- [[Olives_BO/Procedures/OT_ImportRequestToCancelPayment|OT_ImportRequestToCancelPayment]]

## Estimated Size / Volatility
~0 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-OSFA_DB|OSFA_DB MOC]]
