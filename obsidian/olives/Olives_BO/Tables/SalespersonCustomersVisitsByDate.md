---
type: table
database: Olives_BO
name: SalespersonCustomersVisitsByDate
schema: dbo
tags: [#backoffice]
foreign_keys: 0
procedures_reading: 2
support_relevance: medium
last_verified: 2026-08-05
---
# SalespersonCustomersVisitsByDate

## Business Purpose

Back-office table in Olives_BO.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| PositionID | int | NO | ✓ |  |  |
| CustomerID | bigint | NO | ✓ |  |  |
| Date | date | NO | ✓ |  |  |
| Notes | nvarchar(MAX) | YES |  |  |  |
| IsApproved | bit | YES |  |  |  |
## Primary Key
CompanyID PositionID CustomerID Date
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 2 procedure(s): 1 writing, 1 reading.
**Writers (1):**
- [[SRV_SalespersonRouteByDate]]
**Readers (1):**
- [[Rpt_SummaryRouteVisitOnline]]

## Estimated Size / Volatility
~13 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
