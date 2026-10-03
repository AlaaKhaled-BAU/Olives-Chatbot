---
type: table
database: Olives_BO
name: ZatcaMode
schema: dbo
tags: [#backoffice, #legal]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# ZatcaMode


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores zatcamode records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| ModeID | int | NO | ✓ |  |  |
| ModeDesc | nvarchar | YES |  |  |  |
## Primary Key
ModeID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues
> [!warning] AUTO-GENERATED — verify before trusting

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[JOTaxSettings]]

- [[ZatcaResultGenerateXml]]
- [[ZatcaCustomer]]
- [[ZatcaCompany]]
