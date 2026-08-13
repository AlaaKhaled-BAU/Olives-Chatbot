---
type: table
database: Olives_BO
name: ItemsReplacementDetails
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[ItemsReplacementHeaders]]
  - [[ItemsUnits]]
referenced_by:
  - [[OT_ImportReplacement]]
  - [[Pro_ItemsReplacementDetails]]
support_relevance: high
last_verified: 2026-07-05
---
# ItemsReplacementDetails


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores itemsreplacementdetails records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[ItemsUnits]] |
| TransactionTypeID | smallint | NO | ✓ | ✓ | [[ItemsReplacementHeaders]] |
| TransactionYear | smallint | NO | ✓ | ✓ | [[ItemsReplacementHeaders]] |
| TransactionNo | int | NO | ✓ | ✓ | [[ItemsReplacementHeaders]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| UnitID | nvarchar | YES | ✓ | ✓ | [[ItemsUnits]] |
| ItemSerial | int | NO | ✓ |  |  |
| InOutType | int | NO | ✓ |  |  |
| Quantity | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
TransactionTypeID
TransactionYear
TransactionNo
ItemCode
UnitID
ItemSerial
InOutType
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, TransactionTypeID, TransactionYear, TransactionNo -> [[ItemsReplacementHeaders]](CompanyID, TransactionTypeID, TransactionYear, TransactionNo)
CompanyID, UnitID -> [[ItemsUnits]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_ItemsReplacementDetails]]

**Writes (1):**
- [[OT_ImportReplacement]]

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
