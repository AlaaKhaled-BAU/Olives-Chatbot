---
type: table
database: Olives_BO
name: BatchsItemsInfo
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
  - [[Companies]]
  - [[Items]]
referenced_by:
  - [[Awael_Integ_BatchesQty]]
  - [[Awael_Integ_HisInvoices]]
  - [[Awtar_Integration_WithLog]]
  - [[Niroukh_Integration_WithLog]]
  - [[Pro_OrdersHeaders]]
  - [[Pro_ReturnOrdersHeaders]]
  - [[RamPharm_SAP_Integ]]
  - [[X3_Integ_SOA_Batches]]
support_relevance: high
last_verified: 2026-07-05
---
# BatchsItemsInfo


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores batchsitemsinfo records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Items]] |
| ItemNo | nvarchar | YES | ✓ | ✓ | [[Items]] |
| BatchNo | varchar | YES | ✓ |  |  |
| ExpireDate | smalldatetime | YES |  |  |  |
| Qty | money | YES |  |  |  |
| Ref1 | varchar | YES |  |  |  |
| Ref2 | varchar | YES |  |  |  |
| BatchBarcode | varchar | YES |  |  |  |
## Primary Key
CompanyID
ItemNo
BatchNo
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemNo -> [[Items]](CompanyID, ItemCode)
## Impact / Procedures Using This Table

**Reads (8):**
- [[Awael_Integ_BatchesQty]]
- [[Awael_Integ_HisInvoices]]
- [[Awtar_Integration_WithLog]]
- [[Niroukh_Integration_WithLog]]
- [[Pro_OrdersHeaders]]
- [[Pro_ReturnOrdersHeaders]]
- [[RamPharm_SAP_Integ]]
- [[X3_Integ_SOA_Batches]]

**Writes (6):**
- [[Awael_Integ_BatchesQty]]
- [[Awael_Integ_HisInvoices]]
- [[Awtar_Integration_WithLog]]
- [[Niroukh_Integration_WithLog]]
- [[RamPharm_SAP_Integ]]
- [[X3_Integ_SOA_Batches]]

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
