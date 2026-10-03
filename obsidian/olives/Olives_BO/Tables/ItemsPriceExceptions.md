---
type: table
database: Olives_BO
name: ItemsPriceExceptions
schema: dbo
tags: [#backoffice, #billing, #inventory]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
  - [[Items]]
  - [[ItemsUnits]]
referenced_by:
  - [[Pro_ItemsPriceExceptions]]
support_relevance: high
last_verified: 2026-07-05
---
# ItemsPriceExceptions


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores itemspriceexceptions records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | NO | ✓ | ✓ | [[ItemsUnits]] |
| CustomerID | bigint | NO | ✓ | ✓ | [[Customers]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| UnitID | nvarchar | YES | ✓ | ✓ | [[ItemsUnits]] |
| StartDate | smalldatetime | YES |  |  |  |
| EndDate | smalldatetime | YES |  |  |  |
| Price | float | YES |  |  |  |
| TaxType | int | YES |  |  |  |
| Tax | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| UseInReturn | bit | YES |  |  |  |
| UseInSales | bit | YES |  |  |  |
| SellPrice2 | float | YES |  |  |  |
| SellPrice3 | float | YES |  |  |  |
| Qty | money | YES |  |  |  |
| TaxType1 | int | YES |  |  |  |
| Tax1 | float | YES |  |  |  |
| TaxType2 | int | YES |  |  |  |
| Tax2 | float | YES |  |  |  |
| CreateDate | datetime | YES |  |  |  |
| Reference1 | varchar | YES |  |  |  |
| Reference2 | varchar | YES |  |  |  |
## Primary Key
AutoID
CompanyID
CustomerID
ItemCode
UnitID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, UnitID -> [[ItemsUnits]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (4):**
- [[Pro_ItemsPriceExceptions]]

**Writes (7):**
- [[Pro_ItemsPriceExceptions]]

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
