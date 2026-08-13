---
type: table
database: Olives_BO
name: PriceListQtyRanges
schema: dbo
tags: [#backoffice, #billing]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# PriceListQtyRanges


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores pricelistqtyranges records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| PriceListID | int | NO | ✓ |  |  |
| ItemCode | nvarchar | YES | ✓ |  |  |
| UnitID | nvarchar | YES | ✓ |  |  |
| FromQty | float | NO | ✓ |  |  |
| ToQty | float | NO | ✓ |  |  |
| Price | float | YES |  |  |  |
## Primary Key
CompanyID
PriceListID
ItemCode
UnitID
FromQty
ToQty
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
- [[Glossary]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[ReceiptRequestsInvoicesLink]]
- [[MMS_PaymentsChecksDetails]]
- [[MMS_TaxType]]
