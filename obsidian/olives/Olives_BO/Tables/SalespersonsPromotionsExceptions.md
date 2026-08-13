---
type: table
database: Olives_BO
name: SalespersonsPromotionsExceptions
schema: dbo
tags: [#backoffice]
foreign_keys: 0
procedures_reading: 2
support_relevance: medium
last_verified: 2026-08-05
---
# SalespersonsPromotionsExceptions

## Business Purpose

Back-office table in Olives_BO.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| SalespersonID | int | NO | ✓ |  |  |
| PromotionID | int | NO | ✓ |  |  |
## Primary Key
CompanyID SalespersonID PromotionID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 2 procedure(s): 1 writing, 1 reading.
**Writers (1):**
- [[Pro_PromotionsSalesmanGroupsLink]]
**Readers (1):**
- [[Pro_SalesPersonsGroups]]

## Estimated Size / Volatility
~2 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
