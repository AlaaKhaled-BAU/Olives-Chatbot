---
type: table
database: OSFA_DB
name: OT_ItemsReplacmentDF
schema: dbo
tags: [#inventory, #mobile]
foreign_keys:
referenced_by:
  - [[OT_ItemsReplacmentDF_CheckExist]]
  - [[OT_ItemsReplacmentDF_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_ItemsReplacmentDF



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| VouType | smallint | NO | ✓ |  |  |
| VouYear | smallint | NO | ✓ |  |  |
| VouNo | int | NO | ✓ |  |  |
| ItemNo | varchar | YES | ✓ |  |  |
| Unit | varchar | YES | ✓ |  |  |
| LineSerial | int | NO | ✓ |  |  |
| InOutType | int | NO | ✓ |  |  |
| Qty | money | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
## Primary Key
CompNo
VouType
VouYear
VouNo
ItemNo
Unit
LineSerial
InOutType
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_ItemsReplacmentDF_CheckExist]]
- [[OT_ItemsReplacmentDF_Insert]]

**Writes (1):**
- [[OT_ItemsReplacmentDF_Insert]]

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
