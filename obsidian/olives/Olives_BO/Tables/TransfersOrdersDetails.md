---
type: table
database: Olives_BO
name: TransfersOrdersDetails
schema: dbo
tags: [#backoffice, #order]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[TransfersOrdersHeaders]]
referenced_by:
  - [[BaladInsertrtLoadDetailsintoTransactionstyp6]]
  - [[GetTransfersOrdersForOnline]]
  - [[OT_ImportUploadOrders]]
  - [[Pro_AutoBasketLoadItems]]
  - [[Pro_Auto_Unload]]
  - [[Pro_CheckItemsInvoiceBarcode]]
  - [[Pro_ItemsUnitsDetails]]
  - [[Pro_SalesReport_ItemCode]]
  - [[Pro_SalesmanStockAndReturnLoadOrders]]
  - [[Pro_StockSettlement]]
  - [[Pro_TransfersOrdersDetails]]
  - [[Pro_TransfersOrdersQtyValidation]]
  - [[Rpt_LoadOrdersQtySummary]]
  - [[Rpt_LoadTransactionDetails]]
  - [[Rpt_QuantitiesLoadReport]]
  - [[Rpt_SalesmanStock]]
  - [[Rpt_TransferOrderWH]]
  - [[Rpt_TransferOrders]]
  - [[Rpt_TransfersOrders]]
  - [[Rpt_WareHouse_Item_Balance]]
  - [[Stock_Transfer_Jebrini_Excel]]
support_relevance: high
last_verified: 2026-07-05
---
# TransfersOrdersDetails


## Business Purpose
Line-item detail for cash van inventory transfer, restocking, and replenishment orders (`TransfersOrdersHeaders`). Records the specific items (`ItemCode`), packaging units (`UnitID`), requested quantities (`Quantity`), and actual warehouse-approved quantities (`QtyAfterApprove`).
- **Load vs Unload**: Determined by `VouType`:
  - `VouType = 1`: Load Order (أمر تحميل بضاعة للمركبة).
  - `VouType = 2`: Unload Order (أمر تنزيل / إعادة بضاعة للمستودع).
- **Header Link**: Pairs with `TransfersOrdersHeaders` on `OrderYear`, `OrderNo`, and `VouType`.
- **Approval Adjustments**: Warehouse supervisors may adjust quantities upon physical loading/unloading; `QtyAfterApprove` stores the final accepted transfer quantity.

## Chatbot semantics
(Query `t.TransfersOrdersDetails` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule |
|----------------------|-----------|---------------|
| أصناف أمر التحميل | `ItemCode`, `Quantity`, `QtyAfterApprove` | `VouType = 1` |
| أصناف أمر التفريغ / التنزيل | `ItemCode`, `Quantity`, `QtyAfterApprove` | `VouType = 2` |
| الكمية المحملة الفعلية / المعتمدة | `QtyAfterApprove` | الكمية المصروفة فعلياً من المستودع بعد الاعتماد |
| اسم الصنف والوحدة | Join `t.Items`, `t.ItemsUnits` | `d.ItemCode = i.ItemCode`, `d.UnitID = u.UnitID` |

**Do not confuse with:**
- `t.SalesPersonItemsBalance` (the resulting aggregated inventory on the vehicle).
- `t.TransactionsDetails` with `TransactionTypeID = 6 / 7` (the posted warehouse movement vouchers).

## Grain & keys
- **Grain**: One row per item and unit within a transfer order (`OrderYear`, `OrderNo`, `VouType`, `ItemCode`, `UnitID`).
- **Composite PK**: `CompanyID`, `OrderYear`, `OrderNo`, `VouType`, `ItemCode`, `UnitID`.
- **Tenant Key**: `CompanyID`.

## Pipeline
Mobile Van Tablet → `OT_ImportUploadOrders` → `TransfersOrdersHeaders` + `TransfersOrdersDetails` → Warehouse Approval (`QtyAfterApprove`).

## Related
- [[TransfersOrdersHeaders]]
- [[Items]]
- [[ItemsUnits]]
- [[SalesPersonItemsBalance]]

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[TransfersOrdersHeaders]] |
| OrderYear | smallint | NO | ✓ | ✓ | [[TransfersOrdersHeaders]] |
| OrderNo | int | NO | ✓ | ✓ | [[TransfersOrdersHeaders]] |
| VouType | int | NO | ✓ | ✓ | [[TransfersOrdersHeaders]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| UnitID | nvarchar | YES | ✓ | ✓ | [[ItemsUnits]] |
| Quantity | float | YES |  |  |  |
| QtyAfterApprove | float | YES |  |  |  |
| DateAfterApprove | smalldatetime | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
OrderYear
OrderNo
VouType
ItemCode
UnitID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, UnitID -> [[ItemsUnits]](CompanyID, ID)
CompanyID, OrderYear, OrderNo, VouType -> [[TransfersOrdersHeaders]](CompanyID, OrderYear, OrderNo, VouType)
## Impact / Procedures Using This Table

**Reads (38):**
- [[BaladInsertrtLoadDetailsintoTransactionstyp6]]
- [[GetTransfersOrdersForOnline]]
- [[Pro_AutoBasketLoadItems]]
- [[Pro_CheckItemsInvoiceBarcode]]
- [[Pro_ItemsUnitsDetails]]
- [[Pro_SalesReport_ItemCode]]
- [[Pro_SalesmanStockAndReturnLoadOrders]]
- [[Pro_StockSettlement]]
- [[Pro_TransfersOrdersDetails]]
- [[Pro_TransfersOrdersQtyValidation]]
- [[Rpt_LoadOrdersQtySummary]]
- [[Rpt_LoadTransactionDetails]]
- [[Rpt_QuantitiesLoadReport]]
- [[Rpt_SalesmanStock]]
- [[Rpt_TransferOrderWH]]
- [[Rpt_TransferOrders]]
- [[Rpt_TransfersOrders]]
- [[Rpt_WareHouse_Item_Balance]]
- [[Stock_Transfer_Jebrini_Excel]]

**Writes (6):**
- [[OT_ImportUploadOrders]]
- [[Pro_AutoBasketLoadItems]]
- [[Pro_Auto_Unload]]
- [[Pro_SalesmanStockAndReturnLoadOrders]]
- [[Pro_TransfersOrdersDetails]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
