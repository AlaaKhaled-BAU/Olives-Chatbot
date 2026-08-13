---
type: table
database: Olives_BO
name: SalesPersonCustomerCountTargetsDF
schema: dbo
tags: [#backoffice]
foreign_keys: 0
procedures_reading: 1
support_relevance: low
last_verified: 2026-08-05
---
# SalesPersonCustomerCountTargetsDF

## Business Purpose

Back-office table in Olives_BO.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| SalesPersonID | int | NO | ✓ |  |  |
| TargetYear | smallint | NO | ✓ |  |  |
| TargetMonth | int | NO | ✓ |  |  |
| TargetReferenceID | int | NO | ✓ |  |  |
| CustomerCount | nchar(10) | YES |  |  |  |
## Primary Key
CompanyID SalesPersonID TargetYear TargetMonth TargetReferenceID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 1 procedure(s): 1 writing, 0 reading.
**Writers (1):**
- [[Pro_SalesPersonCustomerCountTargets]]

## Estimated Size / Volatility
~36 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
