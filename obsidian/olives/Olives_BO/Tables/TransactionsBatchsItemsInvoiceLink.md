---
type: table
database: Olives_BO
name: TransactionsBatchsItemsInvoiceLink
schema: dbo
tags: [#backoffice, #billing, #inventory]
foreign_keys:
referenced_by:
  - [[Pro_ReturnOrdersHeaders]]
support_relevance: high
last_verified: 2026-07-05
---
# TransactionsBatchsItemsInvoiceLink


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores transactionsbatchsitemsinvoicelink records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| VouType | smallint | NO | ✓ |  |  |
| VouYear | smallint | NO | ✓ |  |  |
| VouNo | int | NO | ✓ |  |  |
| ItemNo | nvarchar | YES | ✓ |  |  |
| Unit | nvarchar | YES | ✓ |  |  |
| BatchNo | varchar | YES | ✓ |  |  |
| InvYear | nvarchar | YES | ✓ |  |  |
| InvNo | nvarchar | YES | ✓ |  |  |
| Qty | money | YES |  |  |  |
## Primary Key
CompanyID
VouType
VouYear
VouNo
ItemNo
Unit
BatchNo
InvYear
InvNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (0):**
_None_

**Writes (1):**
- [[Pro_ReturnOrdersHeaders]]

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
- [[ReceiptRequestsInvoicesLink]]
- [[MMS_PaymentsChecksDetails]]
- [[MMS_TaxType]]
- [[MMS_ItemsCategories]]
- [[IssueItemsDetails]]
- [[SalespersonCustStockItemsAssignment]]
