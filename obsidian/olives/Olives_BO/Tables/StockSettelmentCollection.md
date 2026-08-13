---
type: table
database: Olives_BO
name: StockSettelmentCollection
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
referenced_by:
  - [[Pro_SalesmanStockAndReturnLoadOrders]]
  - [[Rpt_SalesmanStockAndReturn]]
support_relevance: high
last_verified: 2026-07-05
---
# StockSettelmentCollection


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores stocksettelmentcollection records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| SalesPersonID | int | NO | ✓ |  |  |
| SettlmentDate | smalldatetime | NO | ✓ |  |  |
| LineID | smallint | NO | ✓ |  |  |
| SalesmanCollectedAmout | float | YES |  |  |  |
## Primary Key
CompanyID
SalesPersonID
SettlmentDate
LineID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_SalesmanStockAndReturnLoadOrders]]
- [[Rpt_SalesmanStockAndReturn]]

**Writes (1):**
- [[Pro_SalesmanStockAndReturnLoadOrders]]

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
