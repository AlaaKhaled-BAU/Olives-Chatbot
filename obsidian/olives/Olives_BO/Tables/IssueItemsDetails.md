---
type: table
database: Olives_BO
name: IssueItemsDetails
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
  - [[Companies]]
  - [[IssueItemsHeaders]]
  - [[Items]]
  - [[ItemsUnits]]
referenced_by:
  - [[GetIssueItemsForOnline]]
  - [[OT_ImportSalesIssueItems]]
support_relevance: high
last_verified: 2026-07-05
---
# IssueItemsDetails


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores issueitemsdetails records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[ItemsUnits]] |
| OrderYear | int | NO | ✓ | ✓ | [[IssueItemsHeaders]] |
| OrderNo | int | NO | ✓ | ✓ | [[IssueItemsHeaders]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| UnitID | nvarchar | YES | ✓ | ✓ | [[ItemsUnits]] |
| Quantity | float | YES |  |  |  |
| Bonus | float | YES |  |  |  |
| PromisesDate | smalldatetime | YES |  |  |  |
| Price | float | YES |  |  |  |
| DiscountAmount | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| VoucherDiscount | float | YES |  |  |  |
| TaxType | smallint | YES |  |  |  |
| TaxPercent | float | YES |  |  |  |
| TaxAmount | float | YES |  |  |  |
| ForeignPrice | float | YES |  |  |  |
| ForeignDiscountAmount | float | YES |  |  |  |
| ForeignDiscountPercent | float | YES |  |  |  |
| ForeignVouDiscount | float | YES |  |  |  |
| ForeignTaxPercent | float | YES |  |  |  |
| ForeignTaxAmount | float | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| ForeignCustomerDiscountAmount | float | YES |  |  |  |
| OrginalQty | float | YES |  |  |  |
| OrginalBonus | float | YES |  |  |  |
| UPrice | float | YES |  |  |  |
| TaxType1 | smallint | YES |  |  |  |
| TaxPercent1 | float | YES |  |  |  |
| TaxAmount1 | float | YES |  |  |  |
| TaxType2 | smallint | YES |  |  |  |
| TaxPercent2 | float | YES |  |  |  |
| TaxAmount2 | float | YES |  |  |  |
| Manual_Bonus | float | YES |  |  |  |
| ExchangeRate | float | YES |  |  |  |
| Manual_Disc | float | YES |  |  |  |
| QtyAsBonus | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| BonusTax | float | YES |  |  |  |
| BonusAmount | float | YES |  |  |  |
## Primary Key
CompanyID
OrderYear
OrderNo
ItemCode
UnitID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, OrderYear, OrderNo -> [[IssueItemsHeaders]](CompanyID, OrderYear, OrderNo)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, UnitID -> [[ItemsUnits]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[GetIssueItemsForOnline]]

**Writes (1):**
- [[OT_ImportSalesIssueItems]]

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
