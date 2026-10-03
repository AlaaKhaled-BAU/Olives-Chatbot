---
type: table
database: Olives_BO
name: SalesOrderHistoryHF
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
# SalesOrderHistoryHF


## Business Purpose
Historical sales order archive header table in Olives_BO. Stores archived pre-sales orders, historical customer purchase orders, or orders imported from legacy ERP systems (`OrderYear`, `OrderNo`, `OrderDate`, `SalesmanNo`, `CustomerNo`, `OrderState`, `PO_No`).
- **Difference from `OrdersHeaders`**:
  - `OrdersHeaders` is the **live, active, operational** sales order table where new pre-sales customer orders are submitted from mobile devices, modified, approved via workflow, and dispatched for fulfillment.
  - `SalesOrderHistoryHF` is an **archived / external order repository** used for historical demand tracking, customer ordering patterns, and delivery fulfillment status tracking in ERP (`OrderState`, `OrderStateDesc`).
- **Header Link**: Pairs with detail lines in `SalesOrderHistoryDF` on `CompNo`, `OrderYear`, and `OrderNo`.

## Chatbot semantics
(Query `t.SalesOrderHistoryHF` — scoped by session CompNo/CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule |
|----------------------|-----------|---------------|
| طلبيات سابقة في الأرشيف / تاريخ الطلبيات | `OrderNo`, `OrderYear`, `OrderDate`, `CustomerNo` | `CustomerNo = @CustNo` |
| حالة الطلبية في الأرشيف | `OrderState`, `OrderStateDesc`, `ReasonDesc` | حالة تسليم أو إغلاق الطلبية في النظام القديم |
| رقم أمر الشراء التاريخي للعميل | `PO_No` | رقم أمر الشراء الوارد من العميل |

**CRITICAL RULE FOR CHATBOT:**
For any questions regarding **current open orders, today's customer orders, or pending approvals**, ALWAYS query `t.OrdersHeaders`. Query `t.SalesOrderHistoryHF` only when specifically asked about historical order archives or legacy ERP orders.

## Grain & keys
- **Grain**: One row per historical order header (`CompNo`, `OrderYear`, `OrderNo`).
- **Composite PK**: `CompNo`, `OrderYear`, `OrderNo`.
- **Tenant Key**: `CompNo`.

## Pipeline
Legacy ERP Migration / Historical Yearly Archival → `SalesOrderHistoryHF` + `SalesOrderHistoryDF` → Used in delivery and historical fulfillment tracking.

## Related
- [[SalesOrderHistoryDF]]
- [[OrdersHeaders]]
- [[Customers]]
- [[SalesPersons]]

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| OrderDate | smalldatetime | YES |  |  |  |
| SalesmanNo | smallint | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| OrderState | smallint | YES |  |  |  |
| Reason | smallint | YES |  |  |  |
| OrderStateDesc | varchar | YES |  |  |  |
| ReasonDesc | varchar | YES |  |  |  |
| PO_No | varchar | YES |  |  |  |
| DiscountAmount | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| CustomerDiscountPerc | float | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| OrderDeliveryDate | smalldatetime | YES |  |  |  |
## Primary Key
CompNo
OrderYear
OrderNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (15):**
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

- **Role**: archived twin of SalesOrderDeliveryHF (identical shape); query here for closed periods
## Tenancy

Both tables surface as `t.` views scoped via their `CompNo` column (= `SESSION_CONTEXT(N'CompanyID')`; proven live: company 1 sees 2 of SalesOrderHistoryDF's SalesOrderHistoryHF rows). `CompNo` holds the company id.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
