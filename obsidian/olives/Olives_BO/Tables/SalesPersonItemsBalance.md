---
type: table
database: Olives_BO
name: SalesPersonItemsBalance
schema: dbo
tags: [#backoffice, #inventory, #sales]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[SalesPersons]]
referenced_by:
  - [[CalcItemBalance]]
  - [[OT_SendSalesmanData]]
  - [[Pro_Auto_Unload]]
  - [[Pro_CalcSalespersonItemBalance]]
  - [[Pro_CheckSalesmanItemsBalance]]
  - [[Pro_Items]]
  - [[Pro_SalesPersonItemsBalance]]
  - [[Pro_SalesPersonStockTackingDetails]]
  - [[Pro_TransfersOrdersDetails]]
  - [[Pro_TransfersOrdersHeaders]]
  - [[Pro_TransfersOrdersQtyValidation]]
  - [[Rpt_BasketReport]]
  - [[Rpt_LiveQty]]
  - [[Rpt_SalesPersonItemBalance]]
  - [[Rpt_SalesPersonStockTackingDetails]]
  - [[Rpt_StockTakingReport]]
  - [[Rpt_TransfersOrders]]
support_relevance: high
last_verified: 2026-10-03
---
# SalesPersonItemsBalance

## Business Purpose
The van inventory / truck stock balance table — maintains the current on-hand quantity (`ItemQuantity`) of each product (`ItemCode`) and unit (`UnitCode`) in a salesman's mobile vehicle. Essential for van sales operations to determine what goods the salesman can sell immediately without backorders. Queryable via `t.SalesPersonItemsBalance`.

## Chatbot semantics
(Query `t.SalesPersonItemsBalance` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| رصيد سيارة المندوب / بضاعة السيارة | `SalesPersonID`, `ItemCode`, `ItemQuantity` | Filter by salesman | Current inventory on the van |
| اسم المادة ورصيدها في السيارة | Join `t.Items` | `Items.ItemNo = b.ItemCode` | Displays item name alongside quantity |
| وحدة القياس | `UnitCode` | e.g. Box, Piece | Inventory packaging unit |
| مواد نفدت من السيارة | `ItemQuantity` | `ItemQuantity <= 0` | Out of stock items on the van |

**Do not confuse with:**
- `StoresBalances`: Central warehouse stock balances. `SalesPersonItemsBalance` is specifically mobile van stock.
- `TransfersOrdersHeaders`: Load and unload transfer orders moving stock between central warehouse and the van.

## Grain & keys
- **Composite PK**: (`CompanyID`, `SalesPersonID`, `ItemCode`)
- **Tenant key**: `CompanyID`
- **FKs**: `SalesPersonID` → [[SalesPersons]](ID), `ItemCode` → [[Items]](ItemNo)

## Pipeline (how rows get here)
Incremented when load orders (`TransfersOrdersHeaders`, FunctionID 7) are confirmed and synced to BO via `OT_SendSalesmanData`. Decremented upon each invoice sale (`TransactionsHeaders`). Reconciled upon end-of-day van return or stock-taking (`Pro_CalcSalespersonItemBalance`).

## Related
- [[SalesPersons]]
- [[Items]]
- [[TransfersOrdersHeaders]]
- [[TransactionsHeaders]]
- [[StoresBalances]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| SalesPersonID | int | NO | ✓ | ✓ | [[SalesPersons]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| UnitCode | varchar | YES |  |  |  |
| ItemQuantity | float | YES |  |  |  |
## Primary Key
CompanyID
SalesPersonID
ItemCode
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (36):**
- [[CalcItemBalance]]
- [[OT_SendSalesmanData]]
- [[Pro_Auto_Unload]]
- [[Pro_CalcSalespersonItemBalance]]
- [[Pro_CheckSalesmanItemsBalance]]
- [[Pro_Items]]
- [[Pro_SalesPersonItemsBalance]]
- [[Pro_SalesPersonStockTackingDetails]]
- [[Pro_TransfersOrdersDetails]]
- [[Pro_TransfersOrdersHeaders]]
- [[Pro_TransfersOrdersQtyValidation]]
- [[Rpt_BasketReport]]
- [[Rpt_LiveQty]]
- [[Rpt_SalesPersonItemBalance]]
- [[Rpt_SalesPersonStockTackingDetails]]
- [[Rpt_StockTakingReport]]
- [[Rpt_TransfersOrders]]

**Writes (39):**
- [[CalcItemBalance]]
- [[OT_SendSalesmanData]]
- [[Pro_CalcSalespersonItemBalance]]
- [[Pro_SalesPersonItemsBalance]]
- [[Pro_TransfersOrdersHeaders]]
- [[Pro_TransfersOrdersQtyValidation]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Role**: van-custody snapshot per salesman; movement history belongs to Transactions* tables
- **Unit naming**: UnitCode has no declared FK — resolve against ItemsUnits manually
## Tenancy

Chatbot queries `t.SalesPersonItemsBalance` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`. Raw dbo access is blocked for `chatbot_ro`.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
