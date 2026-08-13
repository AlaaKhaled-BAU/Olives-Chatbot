---
type: table
database: OSFA_DB
name: OT_ReturnChecks
schema: dbo
tags: [#mobile, #order]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ReturnChecks



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
| CustomerNo | bigint | NO | ✓ |  |  |
| TransType | smallint | NO | ✓ |  |  |
| TransYear | smallint | NO | ✓ |  |  |
| TransNo | int | NO | ✓ |  |  |
| BankNo | int | NO | ✓ |  |  |
| BranchNo | int | NO | ✓ |  |  |
| CheckNo | int | NO | ✓ |  |  |
| Amount | float | YES |  |  |  |
| RemainingAmount | float | YES |  |  |  |
| DueDate | smalldatetime | YES |  |  |  |
| TransDate | smalldatetime | YES |  |  |  |
| Ref1 | nvarchar | YES |  |  |  |
| Ref2 | nvarchar | YES |  |  |  |
| Ref3 | nvarchar | YES |  |  |  |
| Ref4 | nvarchar | YES |  |  |  |
## Primary Key
CompNo
SalesmanNo
CustomerNo
TransType
TransYear
TransNo
BankNo
BranchNo
CheckNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Partial payment not tracked**: Receipt amount less than invoice total — aging report shows incorrect balance
- **Check bounce**: CheckStatus not updated after bank return — customer credit not restored
- **Currency conversion error**: ExRate differs from daily rate — receipt in wrong amount
- **Duplicate receipts**: Same payment applied twice — customer credit balance wrong

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[OT_OrderHF]]
- [[OT_ConsOrderDF]]
- [[OT_OrderHistoryDF]]

- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]
- [[Glossary]]
