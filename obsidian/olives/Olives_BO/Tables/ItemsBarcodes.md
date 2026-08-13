---
type: table
database: Olives_BO
name: ItemsBarcodes
schema: dbo
tags: [#backoffice, #inventory, #reference]
foreign_keys:
referenced_by:
  - [[Pro_ItemBarcodes]]
support_relevance: high
last_verified: 2026-07-05
---
# ItemsBarcodes


## Business Purpose

Classification or reference codes for sales data categorization.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| ItemCode | nvarchar | YES | ✓ |  |  |
| UnitID | nvarchar | YES | ✓ |  |  |
| Barcode | nvarchar | YES | ✓ |  |  |
## Primary Key
CompanyID
ItemCode
UnitID
Barcode
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (0):**
_None_

**Writes (1):**
- [[Pro_ItemBarcodes]]

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
- [[Glossary]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[MMS_ItemsCategories]]
- [[IssueItemsDetails]]
- [[SalespersonCustStockItemsAssignment]]
- [[DR_DynamicReportsParameters]]
- [[MMS_TaxType]]
- [[MMS_OrderTypes]]
- [[OSFA_DB/Procedures/OT_ItemsUnitsBarcodes_Insert]]
