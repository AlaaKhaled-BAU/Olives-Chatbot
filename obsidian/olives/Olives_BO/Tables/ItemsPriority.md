---
type: table
database: Olives_BO
name: ItemsPriority
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
  - [[Companies]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsUnits]]
referenced_by:
  - [[GetWF_SalesOrderData]]
  - [[OT_SendItemsInfo]]
  - [[Pro_ItemsPriority]]
  - [[Rpt_SalesTargetByCustCount_Telegraph]]
support_relevance: high
last_verified: 2026-07-05
---
# ItemsPriority


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores itemspriority records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | bigint | YES | ✓ |  |  |
| CompanyID | smallint | YES |  | ✓ | [[ItemsUnits]] |
| ItemCode | nvarchar | YES |  | ✓ | [[Items]] |
| UseInSuggestedOrder | bit | YES |  |  |  |
| UnitID | nvarchar | YES |  | ✓ | [[ItemsUnits]] |
| Qty | float | YES |  |  |  |
| CustTypeID | int | YES |  | ✓ | [[CustomersTypes]] |
## Primary Key
AutoID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustTypeID -> [[CustomersTypes]](CompanyID, ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, UnitID -> [[ItemsUnits]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (4):**
- [[GetWF_SalesOrderData]]
- [[OT_SendItemsInfo]]
- [[Pro_ItemsPriority]]
- [[Rpt_SalesTargetByCustCount_Telegraph]]

**Writes (1):**
- [[Pro_ItemsPriority]]

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
