---
type: table
database: Olives_BO
name: RequestToChangeItemSellPrice
schema: dbo
tags: [#backoffice, #billing, #inventory, #workflow]
foreign_keys:
referenced_by:
  - [[OT_ImportRequestToChangeItemSellPrice]]
  - [[Rpt_WorkFlowFunctions]]
  - [[Rpt_Workflow_ChangePrice]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-10-03
---
# RequestToChangeItemSellPrice

## Business Purpose
Stores approval requests submitted when a salesman attempts to change an item's selling price on a mobile device below the minimum price list threshold. Corresponds to workflow `FunctionID = 18` (Change Price In Invoice) or `19` (Change Price In Order). Captures item, customer, salesman, requested price, original price, timestamp, and `IsAproved`. Queryable via `t.RequestToChangeItemSellPrice`.

## Chatbot semantics
(Query `t.RequestToChangeItemSellPrice` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| طلبات تعديل سعر المادة | `SalesPersonNo`, `CustomerNo`, `TrDate` | Direct filter | Price modification requests |
| حالة الموافقة | `IsAproved` | `IsAproved = 1` (approved), `0` or `NULL` (pending) | Direct approval status |
| نوع الحركة (فاتورة أو طلبية) | `TrType` | 1 = Invoice, 2 = Order | Context of price override |
| الربط مع سجل الموافقات العام | Join `t.WF_MasterLog` | `m.FunctionID IN (18, 19) AND TRY_CAST(m.Ref1 AS numeric) = req.AutoID AND m.CompanyID = req.CompanyID` | View supervisor decision levels & notes |

## Grain & keys
- **PK**: `AutoID` (numeric identity, 1 row = 1 price change request)
- **Tenant key**: `CompanyID`
- **Conventions**: `CustomerNo` → [[Customers]](ID), `SalesPersonNo` → [[SalesPersons]](ID), Item codes → [[Items]](ItemNo)

## Pipeline (how rows get here)
Salesman alters price on tablet → `OT_ImportRequestToChangeItemSellPrice` inserts into this table (`IsAproved = 0`) → calls `WF_AddWorkFlowLevelOne @CompNo, @FunctionID, @NewAutoID` → inserts `WF_MasterLog` (`Ref1 = AutoID`). When supervisor approves, `WF_AddWorkFlowLevels` sets `IsAproved = 1`.

## Related
- [[WF_MasterLog]]
- [[WF_SubLog]]
- [[WF_Functions]]
- [[Items]]
- [[PriceLists]]
- [[_RequestTo-Join-Conventions]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| TrType | int | YES |  |  |  |
| CompanyID | smallint | YES |  |  |  |
| SalesPersonNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| InvoiceAmount | float | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| IsAproved | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| OSFA_AutoID | numeric | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OT_ImportRequestToChangeItemSellPrice]]
- [[Rpt_WorkFlowFunctions]]
- [[Rpt_Workflow_ChangePrice]]

**Writes (3):**
- [[OT_ImportRequestToChangeItemSellPrice]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]

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
