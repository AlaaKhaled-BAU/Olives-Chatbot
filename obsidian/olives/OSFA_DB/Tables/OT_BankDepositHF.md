---
type: table
database: OSFA_DB
name: OT_BankDepositHF
schema: dbo
tags: [#maintenance]
foreign_keys: 0
procedures_reading: 5
support_relevance: medium
last_verified: 2026-08-05
---
# OT_BankDepositHF

## Business Purpose

Back-office table in OSFA_DB.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| VouYear | smallint | NO | ✓ |  |  |
| VouNo | int | NO | ✓ |  |  |
| VouDate | smalldatetime | YES |  |  |  |
| SalesmanNo | int | YES |  |  |  |
| BankNo | int | YES |  |  |  |
| BranchNo | int | YES |  |  |  |
| Notes | nvarchar(500) | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| GPSX | nvarchar(50) | YES |  |  |  |
| GPSY | nvarchar(50) | YES |  |  |  |
| IsPosted | bit | YES |  |  |  |
| TabSysID | nvarchar(50) | YES |  |  |  |
## Primary Key
CompNo VouYear VouNo
## Foreign Keys
(none)
**Referenced by (incoming FKs):**
- [[OT_BankDepositDF]].CompNo → OT_BankDepositHF.CompNo
## Impact / Procedures Using This Table

Referenced by 5 procedure(s): 1 writing, 4 reading.
**Writers (1):**
- [[OT_BankDepositHF_Insert]]
**Readers (4):**
- [[OT_BankDepositHF_CheckExist]]
- [[Olives_BO/Procedures/OT_ImportBankDeposit|OT_ImportBankDeposit]]
- [[Olives_BO/Procedures/OT_SendSalesmanData|OT_SendSalesmanData]]
- [[Olives_BO/Procedures/OT_SendSalesmanData_Test|OT_SendSalesmanData_Test]]

## Estimated Size / Volatility
~34 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-OSFA_DB|OSFA_DB MOC]]
