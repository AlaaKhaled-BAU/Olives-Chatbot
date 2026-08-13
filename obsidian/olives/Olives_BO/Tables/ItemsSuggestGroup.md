---
type: table
database: Olives_BO
name: ItemsSuggestGroup
schema: dbo
tags: [#backoffice, #inventory, #reference]
foreign_keys:
referenced_by:
  - [[Pro_ItemsSuggestGroup]]
support_relevance: high
last_verified: 2026-07-05
---
# ItemsSuggestGroup


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores itemssuggestgroup records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| UnitCode | nvarchar | YES |  |  |  |
| Qty | float | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_ItemsSuggestGroup]]

**Writes (1):**
- [[Pro_ItemsSuggestGroup]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Duplicate barcodes**: Multiple items sharing same barcode — POS picks wrong item
- **Price mismatch**: Sell price in Items differs from PriceListDetails — customer charged wrong amount
- **Stock discrepancy**: QtyInAllStores differs from sum of StoreBalances — run CALCITEMBALANCE
- **Missing units**: Item has no valid ItemUnits — cannot be sold
- **Tax config wrong**: IsTaxExempt flag incorrect — ZATCA/legal reporting mismatch

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
