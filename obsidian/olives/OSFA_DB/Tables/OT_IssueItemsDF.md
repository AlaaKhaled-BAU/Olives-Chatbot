---
type: table
database: OSFA_DB
name: OT_IssueItemsDF
schema: dbo
tags: [#inventory, #mobile]
foreign_keys:
  - [[OT_IssueItemsHF]]
referenced_by:
  - [[OT_IssueItemsDF_CheckExist]]
  - [[OT_IssueItemsDF_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_IssueItemsDF



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ | ✓ | [[OT_IssueItemsHF]] |
| OrderYear | smallint | NO | ✓ | ✓ | [[OT_IssueItemsHF]] |
| OrderNo | int | NO | ✓ | ✓ | [[OT_IssueItemsHF]] |
| ItemNo | varchar | YES | ✓ |  |  |
| UnitCode | varchar | YES | ✓ |  |  |
| Qty | money | YES |  |  |  |
| Bonus | money | YES |  |  |  |
| SellValue | float | YES |  |  |  |
| DiscPerc | float | YES |  |  |  |
| DiscValue | float | YES |  |  |  |
| TaxPerc | float | YES |  |  |  |
| TaxValue | float | YES |  |  |  |
| QtyOH | money | YES |  |  |  |
| PromisesDate | smalldatetime | YES |  |  |  |
| TaxType | bit | YES |  |  |  |
| ItemDiscValue | float | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| ForeignCustomerDiscountAmount | float | YES |  |  |  |
| ForeignPrice | float | YES |  |  |  |
| ForeignDiscountAmount | float | YES |  |  |  |
| ForeignDiscountPercent | float | YES |  |  |  |
| ForeignVouDiscount | float | YES |  |  |  |
| ForeignTaxPercent | float | YES |  |  |  |
| ForeignTaxAmount | float | YES |  |  |  |
| UPrice | float | YES |  |  |  |
| TaxPerc_1 | float | YES |  |  |  |
| TaxValue_1 | float | YES |  |  |  |
| TaxType_1 | bit | YES |  |  |  |
| TaxPerc_2 | float | YES |  |  |  |
| TaxValue_2 | float | YES |  |  |  |
| TaxType_2 | bit | YES |  |  |  |
| Manual_Bonus | float | YES |  |  |  |
| Manual_Disc | float | YES |  |  |  |
| QtyAsBonus | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| BonusAmount | float | YES |  |  |  |
| BonusTax | float | YES |  |  |  |
## Primary Key
CompNo
OrderYear
OrderNo
ItemNo
UnitCode
## Foreign Keys
CompNo, OrderYear, OrderNo -> [[OT_IssueItemsHF]](CompNo, OrderYear, OrderNo)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_IssueItemsDF_CheckExist]]
- [[OT_IssueItemsDF_Insert]]

**Writes (1):**
- [[OT_IssueItemsDF_Insert]]

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
