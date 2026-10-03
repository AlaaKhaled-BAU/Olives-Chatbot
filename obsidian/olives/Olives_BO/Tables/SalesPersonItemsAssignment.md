---
type: table
database: Olives_BO
name: SalesPersonItemsAssignment
schema: dbo
tags: [#backoffice, #inventory, #sales]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[Positions]]
referenced_by:
  - [[DiagnosticTools_CheckSalespersonConfiguration]]
  - [[OT_SendSalesmanData]]
  - [[Pro_CustomersItemsAssigment]]
  - [[Pro_Items]]
  - [[Pro_ReturnlineManagerApproval]]
  - [[Pro_SalesPersonCustStockItemsAssignment]]
  - [[Pro_SalesPersonItemsAssignment]]
  - [[Pro_SalesPersonStockTackingDetails]]
  - [[Pro_TransfersOrdersDetails]]
  - [[Pro_TransfersOrders_Auto]]
  - [[Rpt_DeliveryBatchHeader]]
  - [[Rpt_ItemsCustomersNotSold]]
  - [[Rpt_ItemsCustomersNotSoldBySelection]]
  - [[Rpt_ItemsNotSold]]
  - [[Rpt_ItemsSalesmanNotSold]]
  - [[Rpt_PerformanceMetric]]
  - [[Rpt_PrintOrdersBatches]]
  - [[Rpt_SalesPersonStockTackingDetails]]
  - [[Rpt_StockTakingReport]]
  - [[Rpt_TransfersOrders]]
  - [[X3_AssignItems]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonItemsAssignment


## Business Purpose
Salesman item portfolio / catalog assignment table in Olives_BO. Restricts or designates which specific products (`ItemCode`) a sales position or representative (`PositionsID`) is authorized to sell, load, or distribute on their mobile device.
- **Selective Distribution**: Used in multi-division companies where distinct sales forces (e.g. Food vs. Non-Food, Pharma vs. Personal Care, Van vs. Pre-sales) only handle a specific subset of the overall 18,000+ item catalog.
- **Mobile Filter**: Handheld devices sync and display only items assigned to the salesman's active position, preventing salesmen from selling unauthorized categories.
- **Suspension Flag**: `IsSuspended = 1` temporarily revokes a salesman's permission to sell that specific item.

## Chatbot semantics
(Query `t.SalesPersonItemsAssignment` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule |
|----------------------|-----------|---------------|
| الأصناف المصرح بها للمندوب / بورتفوليو المندوب | `PositionsID`, `ItemCode`, `IsSuspended` | `PositionsID = @PositionID AND IsSuspended = 0` |
| هل المندوب مخول ببيع هذا الصنف | `PositionsID`, `ItemCode` | `PositionsID = @PositionID AND ItemCode = @ItemCode AND IsSuspended = 0` |
| أصناف موقوفة عن مندوب معين | `IsSuspended` | `PositionsID = @PositionID AND IsSuspended = 1` |
| اسم الصنف وتفاصيله المخصصة | Join `t.Items` | `a.ItemCode = i.ItemCode` |

**Do not confuse with:**
- `t.CustomersItemsAssigment` (restriction of items permitted for sale to a specific customer).
- `t.SalesPersonItemsBalance` (actual physical quantity currently on the van).
- `t.Items` (master catalog of all products).

## Grain & keys
- **Grain**: One row per position and assigned item (`PositionsID`, `ItemCode`).
- **Composite PK**: `CompanyID`, `PositionsID`, `ItemCode`.
- **Tenant Key**: `CompanyID`.

## Pipeline
Back Office Product Assignment Screen (`Pro_SalesPersonItemsAssignment`) → `SalesPersonItemsAssignment` → Synced to mobile handheld devices via `OT_SendSalesmanData`.

## Related
- [[Positions]]
- [[SalesPersons]]
- [[Items]]
- [[CustomersItemsAssigment]]
- [[SalesPersonItemsBalance]]

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Positions]] |
| PositionsID | int | NO | ✓ | ✓ | [[Positions]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| DefinitionDate | smalldatetime | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
## Primary Key
CompanyID
PositionsID
ItemCode
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, PositionsID -> [[Positions]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (30):**
- [[DiagnosticTools_CheckSalespersonConfiguration]]
- [[OT_SendSalesmanData]]
- [[Pro_CustomersItemsAssigment]]
- [[Pro_Items]]
- [[Pro_ReturnlineManagerApproval]]
- [[Pro_SalesPersonCustStockItemsAssignment]]
- [[Pro_SalesPersonItemsAssignment]]
- [[Pro_SalesPersonStockTackingDetails]]
- [[Pro_TransfersOrdersDetails]]
- [[Pro_TransfersOrders_Auto]]
- [[Rpt_DeliveryBatchHeader]]
- [[Rpt_ItemsCustomersNotSold]]
- [[Rpt_ItemsCustomersNotSoldBySelection]]
- [[Rpt_ItemsNotSold]]
- [[Rpt_ItemsSalesmanNotSold]]
- [[Rpt_PerformanceMetric]]
- [[Rpt_PrintOrdersBatches]]
- [[Rpt_SalesPersonStockTackingDetails]]
- [[Rpt_StockTakingReport]]
- [[Rpt_TransfersOrders]]
- [[X3_AssignItems]]

**Writes (8):**
- [[OT_SendSalesmanData]]
- [[Pro_SalesPersonItemsAssignment]]

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
