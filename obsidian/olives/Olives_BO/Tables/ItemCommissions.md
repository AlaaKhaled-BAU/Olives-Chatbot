---
type: table
database: Olives_BO
name: ItemCommissions
schema: dbo
tags: [#backoffice]
foreign_keys: 0
procedures_reading: 1
support_relevance: low
last_verified: 2026-08-05
---
# ItemCommissions

## Business Purpose

Back-office table in Olives_BO.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyId | int | NO | ✓ |  |  |
| ItemCode | nvarchar(100) | NO | ✓ |  |  |
| CommissionPer | float | YES |  |  |  |
| BonusPer | float | YES |  |  |  |
## Primary Key
CompanyId ItemCode
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 1 procedure(s): 0 writing, 1 reading.
**Readers (1):**
- [[Rpt_ItemSalesCommissionsBySalesman]]

## Estimated Size / Volatility
~1 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
