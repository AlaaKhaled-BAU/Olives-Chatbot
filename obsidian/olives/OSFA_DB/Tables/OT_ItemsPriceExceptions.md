---
type: table
database: OSFA_DB
name: OT_ItemsPriceExceptions
schema: dbo
tags: [#billing, #inventory, #mobile]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ItemsPriceExceptions



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| SalesmanNo | smallint | NO | ✓ |  |  |
| CustomerNo | bigint | NO | ✓ |  |  |
| ItemNo | varchar | YES | ✓ |  |  |
| UnitCode | varchar | YES | ✓ |  |  |
| StartDate | smalldatetime | YES |  |  |  |
| EndDate | smalldatetime | YES |  |  |  |
| SellPrice | money | YES |  |  |  |
| TaxPerc | money | YES |  |  |  |
| SellPrice2 | money | YES |  |  |  |
| SellPrice3 | money | YES |  |  |  |
| TaxType | bit | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| UseInReturn | bit | YES |  |  |  |
| UseInSales | bit | YES |  |  |  |
| Qty | money | YES |  |  |  |
| Tax_1_Type | bit | YES |  |  |  |
| Tax_1_Perc | float | YES |  |  |  |
| Tax_2_Type | bit | YES |  |  |  |
| Tax_2_Perc | float | YES |  |  |  |
## Primary Key
CompNo
SalesmanNo
CustomerNo
ItemNo
UnitCode
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

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
- [[OT_PaymentsTypes]]
- [[OT_PriceList]]
- [[OT_RequestToChangeInvoicePaymentType]]
- [[OT_ItemsQtyAvg]]
- [[OT_StateAccBalance]]
- [[OT_LinkedSalesman]]

- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]
- [[Glossary]]
