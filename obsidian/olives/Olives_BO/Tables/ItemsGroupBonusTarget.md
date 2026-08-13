---
type: table
database: Olives_BO
name: ItemsGroupBonusTarget
schema: dbo
tags: [#backoffice, #inventory, #reference, #sales]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[Pro_ItemsGroupBonusTarget]]
  - [[Pro_SalesPersonGroupItemBonusTarget]]
  - [[Pro_SalesPersonItemBonusTargetGroup]]
  - [[Rpt_SalesPersonItemBonusTarget]]
  - [[Rpt_SalesPersonItemBonusTarget_Tablet]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Items-Master-Data-Setup
---
# ItemsGroupBonusTarget


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores itemsgroupbonustarget records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (5):**
- [[Pro_ItemsGroupBonusTarget]]
- [[Pro_SalesPersonGroupItemBonusTarget]]
- [[Pro_SalesPersonItemBonusTargetGroup]]
- [[Rpt_SalesPersonItemBonusTarget]]
- [[Rpt_SalesPersonItemBonusTarget_Tablet]]

**Writes (1):**
- [[Pro_ItemsGroupBonusTarget]]

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
