---
type: table
database: Olives_BO
name: ContractItems
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
  - [[Companies]]
  - [[Contracts]]
  - [[Items]]
  - [[ItemsUnits]]
referenced_by:
  - [[Pro_Contracts]]
support_relevance: high
last_verified: 2026-07-05
---
# ContractItems


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores contractitems records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[ItemsUnits]] |
| ContractID | nvarchar | YES | ✓ | ✓ | [[Contracts]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| UnitID | nvarchar | YES | ✓ | ✓ | [[ItemsUnits]] |
| MaxQty | money | YES |  |  |  |
## Primary Key
CompanyID
ContractID
ItemCode
UnitID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ContractID -> [[Contracts]](CompanyID, ContractID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, UnitID -> [[ItemsUnits]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_Contracts]]

**Writes (1):**
- [[Pro_Contracts]]

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
