---
type: table
database: Olives_BO
name: ItemsUnitsDetails_1
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[ItemsUnits]]
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# ItemsUnitsDetails_1


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores itemsunitsdetails 1 records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[ItemsUnits]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| UnitID | nvarchar | YES | ✓ | ✓ | [[ItemsUnits]] |
| ConvertRate | float | YES |  |  |  |
| UnitSerial | int | YES |  |  |  |
| Barcode | nvarchar | YES |  |  |  |
| Volume | float | YES |  |  |  |
| Weight | float | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
| UsedInUploadOrder | bit | YES |  |  |  |
## Primary Key
CompanyID
ItemCode
UnitID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, UnitID -> [[ItemsUnits]](CompanyID, ID)
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

- [[_MOC-Olives_BO|Olives_BO MOC]]
