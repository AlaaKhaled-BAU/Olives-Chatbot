---
type: table
database: Olives_BO
name: BankDepositDF
schema: dbo
tags: [#backoffice]
foreign_keys: 4
procedures_reading: 3
support_relevance: medium
last_verified: 2026-08-05
---
# BankDepositDF

## Business Purpose

Back-office table in Olives_BO.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[BankDepositHF]] |
| VouYear | smallint | NO | ✓ | ✓ | [[BankDepositHF]] |
| VouNo | int | NO | ✓ | ✓ | [[BankDepositHF]] |
| RecYear | smallint | NO | ✓ |  |  |
| RecType | smallint | NO | ✓ |  |  |
| RecNo | int | NO | ✓ |  |  |
| RecAmount | float | YES |  |  |  |
## Primary Key
CompanyID VouYear VouNo RecYear RecType RecNo
## Foreign Keys
- BankDepositDF.CompanyID → [[BankDepositHF]].CompanyID
- BankDepositDF.CompanyID → [[Companies]].ID
## Impact / Procedures Using This Table

Referenced by 3 procedure(s): 1 writing, 2 reading.
**Writers (1):**
- [[OT_ImportBankDeposit]]
**Readers (2):**
- [[Pro_BankDeposit]]
- [[Pro_Receipts]]

## Estimated Size / Volatility
~49 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
