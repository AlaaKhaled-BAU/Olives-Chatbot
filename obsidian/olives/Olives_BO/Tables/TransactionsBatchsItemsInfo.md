---
type: table
database: Olives_BO
name: TransactionsBatchsItemsInfo
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[ItemsUnits]]
referenced_by:
  - [[OT_ImportCustStockTacking]]
  - [[OT_ImportReplacement]]
  - [[OT_ImportReturnOrder]]
  - [[OT_ImportSalesInvoices]]
  - [[OT_ImportSalesOrders]]
  - [[OT_ImportUploadOrders]]
  - [[Pro_OrdersHeaders]]
  - [[Pro_ReturnOrdersDetails]]
  - [[Rpt_ApprovedOrder]]
  - [[Rpt_CustomerStockByExpire]]
  - [[Rpt_PrintOrdersBatches]]
support_relevance: high
last_verified: 2026-07-05
---
# TransactionsBatchsItemsInfo


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores transactionsbatchsitemsinfo records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[ItemsUnits]] |
| VouType | smallint | NO | ✓ |  |  |
| VouYear | smallint | NO | ✓ |  |  |
| VouNo | int | NO | ✓ |  |  |
| ItemNo | nvarchar | YES | ✓ | ✓ | [[Items]] |
| Unit | nvarchar | YES | ✓ | ✓ | [[ItemsUnits]] |
| BatchNo | varchar | YES | ✓ |  |  |
| Qty | money | NO | ✓ |  |  |
| ExpireDate | smalldatetime | YES |  |  |  |
| Bonus | money | YES |  |  |  |
## Primary Key
CompanyID
VouType
VouYear
VouNo
ItemNo
Unit
BatchNo
Qty
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemNo -> [[Items]](CompanyID, ItemCode)
CompanyID, Unit -> [[ItemsUnits]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (6):**
- [[Pro_ReturnOrdersDetails]]
- [[Rpt_ApprovedOrder]]
- [[Rpt_CustomerStockByExpire]]
- [[Rpt_PrintOrdersBatches]]

**Writes (7):**
- [[OT_ImportCustStockTacking]]
- [[OT_ImportReplacement]]
- [[OT_ImportReturnOrder]]
- [[OT_ImportSalesInvoices]]
- [[OT_ImportSalesOrders]]
- [[OT_ImportUploadOrders]]
- [[Pro_OrdersHeaders]]

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
