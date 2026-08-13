---
type: table
database: Olives_BO
name: RequestToCancelPayment
schema: dbo
tags: [#backoffice]
foreign_keys: 0
procedures_reading: 4
support_relevance: medium
last_verified: 2026-08-05
---
# RequestToCancelPayment

## Business Purpose

Back-office table in Olives_BO.

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
| Latitude | nvarchar(50) | YES |  |  |  |
| Longitude | nvarchar(50) | YES |  |  |  |
| TabletSysID | varchar(50) | YES |  |  |  |
| IsAproved | bit | YES |  |  |  |
| OSFA_AutoID | numeric(30,0) | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 4 procedure(s): 3 writing, 1 reading.
**Writers (3):**
- [[OT_ImportRequestToCancelPayment]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]
**Readers (1):**
- [[OSFA_DB/Procedures/OT_AppService|OT_AppService]]

## Estimated Size / Volatility
~0 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
