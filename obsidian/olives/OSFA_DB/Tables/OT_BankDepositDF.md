---
type: table
database: OSFA_DB
name: OT_BankDepositDF
schema: dbo
tags: [#maintenance]
foreign_keys: 3
procedures_reading: 3
support_relevance: medium
last_verified: 2026-08-05
---
# OT_BankDepositDF

## Business Purpose

Back-office table in OSFA_DB.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ | ✓ | [[OT_BankDepositHF]] |
| VouYear | smallint | NO | ✓ | ✓ | [[OT_BankDepositHF]] |
| VouNo | int | NO | ✓ | ✓ | [[OT_BankDepositHF]] |
| RecYear | smallint | NO | ✓ |  |  |
| RecType | smallint | NO | ✓ |  |  |
| RecNo | int | NO | ✓ |  |  |
| RecAmount | float | YES |  |  |  |
## Primary Key
CompNo VouYear VouNo RecYear RecType RecNo
## Foreign Keys
- OT_BankDepositDF.CompNo → [[OT_BankDepositHF]].CompNo
## Impact / Procedures Using This Table

Referenced by 3 procedure(s): 1 writing, 2 reading.
**Writers (1):**
- [[OT_BankDepositDF_Insert]]
**Readers (2):**
- [[OT_BankDepositDF_CheckExist]]
- [[Olives_BO/Procedures/OT_ImportBankDeposit|OT_ImportBankDeposit]]

## Estimated Size / Volatility
~50 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-OSFA_DB|OSFA_DB MOC]]
