---
type: table
database: Olives_BO
name: SalesTransHeader
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
referenced_by:
  - [[Pro_SalesTrans]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesTransHeader


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salestransheader records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO |  |  |  |
| TransAutoID | numeric | YES | ✓ |  |  |
| InvoiceNumber | nvarchar | YES |  |  |  |
| SalesmanNo | int | YES |  |  |  |
| TransDate | datetime | YES |  |  |  |
| CACR | smallint | YES |  |  |  |
| CustomerLocationID | nvarchar | YES |  |  |  |
| CustomerID | bigint | YES |  |  |  |
| AssetID | bigint | NO |  |  |  |
| Address | nvarchar | YES |  |  |  |
## Primary Key
TransAutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_SalesTrans]]

**Writes (1):**
- [[Pro_SalesTrans]]

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
