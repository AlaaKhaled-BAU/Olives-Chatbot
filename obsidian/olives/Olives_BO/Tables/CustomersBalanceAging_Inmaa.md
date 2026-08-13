---
type: table
database: Olives_BO
name: CustomersBalanceAging_Inmaa
schema: dbo
tags: [#backoffice]
foreign_keys: 0
procedures_reading: 1
support_relevance: low
last_verified: 2026-08-05
---
# CustomersBalanceAging_Inmaa

## Business Purpose

Back-office table in Olives_BO.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| CustomerID | bigint | NO | ✓ |  |  |
| BalanceAge1 | float | YES |  |  |  |
| BalanceAge2 | float | YES |  |  |  |
| BalanceAge3 | float | YES |  |  |  |
| BalanceAge4 | float | YES |  |  |  |
| BalanceAge5 | float | YES |  |  |  |
| BalanceAge6 | float | YES |  |  |  |
| BalanceAge7 | float | YES |  |  |  |
| BalanceAge8 | float | YES |  |  |  |
| BalanceAge9 | float | YES |  |  |  |
| BalanceAge10 | float | YES |  |  |  |
## Primary Key
CompanyID CustomerID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 1 procedure(s): 0 writing, 1 reading.
**Readers (1):**
- [[Rpt_SalesOrdersApprovalEnmaa]]

## Estimated Size / Volatility
~0 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
