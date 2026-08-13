---
type: table
database: OSFA_DB
name: OT_StoreItemsQty_Main
schema: dbo
tags: [#inventory, #mobile]
foreign_keys:
referenced_by:
  - [[OT_AutoStoreItemsQty]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_StoreItemsQty_Main



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
| StoreNo | int | NO | ✓ |  |  |
| ItemNo | varchar | YES | ✓ |  |  |
| Qty | money | YES |  |  |  |
## Primary Key
CompNo
SalesmanNo
StoreNo
ItemNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (0):**
_None_

**Writes (1):**
- [[OT_AutoStoreItemsQty]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Duplicate barcodes**: Multiple items sharing same barcode — POS picks wrong item
- **Price mismatch**: Sell price in Items differs from PriceListDetails — customer charged wrong amount
- **Stock discrepancy**: QtyInAllStores differs from sum of StoreBalances — run CALCITEMBALANCE
- **Missing units**: Item has no valid ItemUnits — cannot be sold
- **Tax config wrong**: IsTaxExempt flag incorrect — ZATCA/legal reporting mismatch

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[OT_ItemsQtyAvg]]
- [[OT_StateAccBalance]]
- [[OT_LinkedSalesman]]

- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]
- [[Glossary]]
