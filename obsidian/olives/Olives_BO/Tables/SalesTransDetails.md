---
type: table
database: Olives_BO
name: SalesTransDetails
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
  - [[SalesTransHeader]]
referenced_by:
  - [[Pro_SalesTrans]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesTransDetails


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salestransdetails records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO |  |  |  |
| TransAutoID | numeric | YES |  | ✓ | [[SalesTransHeader]] |
| TaxPerc | float | YES |  |  |  |
| InvAmount | float | YES |  |  |  |
| DiscAmount | float | YES |  |  |  |
| InvTotal | float | YES |  |  |  |
| TaxAmount | float | YES |  |  |  |
| NetAmount | float | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
TransAutoID -> [[SalesTransHeader]](TransAutoID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_SalesTrans]]

**Writes (0):**
_None_

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
