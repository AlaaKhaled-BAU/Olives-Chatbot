---
type: table
database: Olives_BO
name: SalesOrderHistoryDF
schema: dbo
tags: [#backoffice, #log, #order, #sales]
foreign_keys:
referenced_by:
  - [[BO_Online_RptCustomerSalesTargetDetails]]
  - [[GetSalesOrdersForApiReport_GCI]]
  - [[GetSalesOrdersForOnlineReport]]
  - [[GetSalesOrdersForOnlineReport_GCI]]
  - [[Online_RptSalesOrderStatusInERP]]
  - [[Pro_DeliveryAssigning]]
  - [[Rpt_DailyDriver]]
  - [[Rpt_DailyUnit]]
  - [[Rpt_MasterOrders]]
  - [[Rpt_NumericDistribution]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesOrderHistoryDF


## Business Purpose
Historical sales order line-item archive detail table in Olives_BO. Stores archived order line items, ordered quantities (`OrderdQty`), delivered quantities (`DeliveredQty`), open / outstanding quantities (`OutstandingQty`), invoiced quantities (`InvQty`), and line pricing (`UPrice`, `SellValue`).
- **Difference from `OrdersDetails`**:
  - `OrdersDetails` is the **live, operational** pre-sales order line-item table recording current demands taken on tablets for fulfillment.
  - `SalesOrderHistoryDF` is an **historical / archived order line repository** tracking historical order delivery fulfillment, picked quantities (`PickedQty`), and legacy demand history.
- **Header Link**: Pairs with `SalesOrderHistoryHF` on `CompNo`, `OrderYear`, and `OrderNo`.

## Chatbot semantics
(Query `t.SalesOrderHistoryDF` — scoped by session CompNo/CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule |
|----------------------|-----------|---------------|
| تفاصيل أصناف الطلبيات التاريخية | `ItemNo`, `OrderdQty`, `DeliveredQty`, `UPrice` | Join `t.SalesOrderHistoryHF h ON df.OrderYear = h.OrderYear AND df.OrderNo = h.OrderNo` |
| الكمية المطلوبة مقابل المسلمة تاريخياً | `OrderdQty`, `DeliveredQty`, `OutstandingQty` | مقارنة الكمية المطلوبة بالكمية المسلمة فعلياً |
| الكمية المفوترة من الطلبية | `InvQty` | الكمية التي تم تحويلها لفاتورة في النظام القديم |

**CRITICAL RULE FOR CHATBOT:**
For any questions regarding **current order lines, active orders, or live requested quantities**, ALWAYS query `t.OrdersDetails`. Query `t.SalesOrderHistoryDF` only when specifically asked about historical order archives.

## Grain & keys
- **Grain**: One row per item and unit within an archived order header (`OrderYear`, `OrderNo`, `ItemNo`, `UnitCode`).
- **Composite PK**: `CompNo`, `OrderYear`, `OrderNo`, `ItemNo`, `UnitCode`.
- **Tenant Key**: `CompNo`.

## Pipeline
Legacy ERP Migration / Historical Archival → `SalesOrderHistoryDF` → Used in historical order analysis.

## Related
- [[SalesOrderHistoryHF]]
- [[OrdersDetails]]
- [[Items]]

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| ItemNo | varchar | YES | ✓ |  |  |
| UnitCode | varchar | YES | ✓ |  |  |
| OrderdQty | money | YES |  |  |  |
| Bonus | money | YES |  |  |  |
| DeliveredQty | money | YES |  |  |  |
| OutstandingQty | money | YES |  |  |  |
| SellValue | float | YES |  |  |  |
| DiscPerc | money | YES |  |  |  |
| DiscValue | float | YES |  |  |  |
| TaxPerc | money | YES |  |  |  |
| TaxValue | float | YES |  |  |  |
| QtyOH | money | YES |  |  |  |
| ItemDesc | varchar | YES |  |  |  |
| InvQty | money | YES |  |  |  |
| VoucherDiscount | float | YES |  |  |  |
| TaxType | smallint | YES |  |  |  |
| UPrice | float | YES |  |  |  |
| Manual_Bonus | float | YES |  |  |  |
| TotWieght | float | YES |  |  |  |
| PickedQty | float | YES |  |  |  |
## Primary Key
CompNo
OrderYear
OrderNo
ItemNo
UnitCode
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (14):**
- [[BO_Online_RptCustomerSalesTargetDetails]]
- [[GetSalesOrdersForApiReport_GCI]]
- [[GetSalesOrdersForOnlineReport]]
- [[GetSalesOrdersForOnlineReport_GCI]]
- [[Online_RptSalesOrderStatusInERP]]
- [[Pro_DeliveryAssigning]]
- [[Rpt_DailyDriver]]
- [[Rpt_DailyUnit]]
- [[Rpt_MasterOrders]]
- [[Rpt_NumericDistribution]]

**Writes (6):**

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
