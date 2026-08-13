---
type: table
database: Olives_BO
name: BankDepositHF
schema: dbo
tags: [#backoffice]
foreign_keys: 8
procedures_reading: 3
support_relevance: high
last_verified: 2026-08-05
---
# BankDepositHF

## Business Purpose

Back-office table in Olives_BO.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Banks]] |
| VouYear | smallint | NO | ✓ |  |  |
| VouNo | int | NO | ✓ |  |  |
| VouDate | smalldatetime | YES |  |  |  |
| SalespersonID | int | YES |  | ✓ | [[SalesPersons]] |
| BankNo | int | YES |  | ✓ | [[Banks]] |
| BranchNo | int | YES |  | ✓ | [[Branches]] |
| Notes | nvarchar(500) | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| Latitude | nvarchar(50) | YES |  |  |  |
| Longitude | nvarchar(50) | YES |  |  |  |
| IsPostedToERP | bit | YES |  |  |  |
| TabSysID | nvarchar(50) | YES |  |  |  |
| Approve | bit | YES |  |  |  |
## Primary Key
CompanyID VouYear VouNo
## Foreign Keys
- BankDepositHF.CompanyID → [[Banks]].CompanyID
- BankDepositHF.CompanyID → [[Branches]].CompanyID
- BankDepositHF.CompanyID → [[Companies]].ID
- BankDepositHF.CompanyID → [[SalesPersons]].CompanyID
**Referenced by (incoming FKs):**
- [[BankDepositDF]].CompanyID → BankDepositHF.CompanyID
## Impact / Procedures Using This Table

Referenced by 3 procedure(s): 2 writing, 1 reading.
**Writers (2):**
- [[OT_ImportBankDeposit]]
- [[Pro_Receipts]]
**Readers (1):**
- [[Pro_BankDeposit]]

## Estimated Size / Volatility
~33 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
