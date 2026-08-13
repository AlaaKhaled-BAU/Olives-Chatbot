---
type: table
database: OSFA_DB
name: OT_ItemUnits
schema: dbo
tags: [#inventory, #mobile]
foreign_keys:
referenced_by:
  - [[servics_app_OSFA_Mobile_Ver]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_ItemUnits



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
| UnitID | varchar | YES | ✓ |  |  |
| UnitDesc | varchar | YES |  |  |  |
| IsIntegerQty | bit | YES |  |  |  |
## Primary Key
CompNo
SalesmanNo
UnitID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[servics_app_OSFA_Mobile_Ver]]

**Writes (0):**
_None_

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
