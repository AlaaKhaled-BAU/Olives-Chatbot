---
type: table
database: Olives_BO
name: ERPStoresItemsLink
schema: dbo
tags: [#backoffice, #integration, #inventory]
foreign_keys:
  - [[Companies]]
  - [[Items]]
referenced_by:
  - [[Pro_ERPStoresLinkWithItems]]
support_relevance: high
last_verified: 2026-07-05
---
# ERPStoresItemsLink


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores erpstoresitemslink records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Items]] |
| StoreNo | int | NO | ✓ |  |  |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
## Primary Key
CompanyID
StoreNo
ItemCode
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_ERPStoresLinkWithItems]]

**Writes (2):**
- [[Pro_ERPStoresLinkWithItems]]

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
