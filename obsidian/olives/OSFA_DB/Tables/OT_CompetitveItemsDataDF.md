---
type: table
database: OSFA_DB
name: OT_CompetitveItemsDataDF
schema: dbo
tags: [#inventory, #mobile]
foreign_keys:
  - [[OT_CompetitveItemsDataHF]]
referenced_by:
  - [[OT_AddCompetitveItemsDataImages]]
  - [[OT_CompetitveItemsDataDF_CheckExist]]
  - [[OT_CompetitveItemsDataDF_Insert]]
  - [[OT_CompetitveItemsDataDF_UpdateImage]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_CompetitveItemsDataDF



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[OT_CompetitveItemsDataHF]] |
| TrYear | smallint | NO | ✓ | ✓ | [[OT_CompetitveItemsDataHF]] |
| TrNo | int | NO | ✓ | ✓ | [[OT_CompetitveItemsDataHF]] |
| CompetitiveItem | nvarchar | YES | ✓ |  |  |
| Qty | money | YES |  |  |  |
| Price | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| ItemImage | image | YES |  |  |  |
| ShelfPrice | float | YES |  |  |  |
| RetailPrice | float | YES |  |  |  |
| WholeSalePrice | float | YES |  |  |  |
## Primary Key
CompanyID
TrYear
TrNo
CompetitiveItem
## Foreign Keys
CompanyID, TrYear, TrNo -> [[OT_CompetitveItemsDataHF]](CompanyID, TrYear, TrNo)
## Impact / Procedures Using This Table

**Reads (4):**
- [[OT_AddCompetitveItemsDataImages]]
- [[OT_CompetitveItemsDataDF_CheckExist]]
- [[OT_CompetitveItemsDataDF_Insert]]
- [[OT_CompetitveItemsDataDF_UpdateImage]]

**Writes (3):**
- [[OT_AddCompetitveItemsDataImages]]
- [[OT_CompetitveItemsDataDF_Insert]]
- [[OT_CompetitveItemsDataDF_UpdateImage]]

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
