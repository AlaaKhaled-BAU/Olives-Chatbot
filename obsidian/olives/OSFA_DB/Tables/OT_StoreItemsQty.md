---
type: table
database: OSFA_DB
name: OT_StoreItemsQty
schema: dbo
tags: [#inventory, #mobile]
foreign_keys:
referenced_by:
  - [[OT_AutoStoreItemsQty]]
  - [[OT_Online_RptAvailableStockByCategory]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_StoreItemsQty



## Business Purpose

Mobile tablet inventory store in OSFA_DB for **Cash Van (فانات البيع المباشر)** salespersons.
- Keyed by `(CompNo, StoreNo, ItemNo)`.
- In Cash Van operations, `@SalesmanNo` is passed as the `@StoreNo` (`StoreNo = SalesmanNo`), representing the salesperson's mobile van custody store.
- Populated and synchronized by the procedure `dbo.OT_SendSalesmanData` directly from Back-Office `dbo.SalesPersonItemsBalance`.
- During field sales on the tablet, the mobile app validates available quantities against this table to prevent negative van stock or out-of-stock invoice issuing.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| StoreNo | int | NO | ✓ |  |  |
| ItemNo | varchar | YES | ✓ |  |  |
| Qty | money | YES |  |  |  |
## Primary Key
CompNo
StoreNo
ItemNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_AutoStoreItemsQty]]
- [[OT_Online_RptAvailableStockByCategory]]

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
