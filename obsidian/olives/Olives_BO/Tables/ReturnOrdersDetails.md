---
type: table
database: Olives_BO
name: ReturnOrdersDetails
schema: dbo
tags: [#backoffice, #order]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[ReturnOrdersHeaders]]
referenced_by:
  - [[ConvertReturnOrderToInvoiceDelivery]]
  - [[OT_ImportReturnOrder]]
  - [[Pro_ItemsUnitsDetails]]
  - [[Pro_ReturnOrdersDetails]]
  - [[Pro_ReturnOrdersHeaders]]
  - [[Rpt_CustomerReturnOrdersDetails]]
  - [[Rpt_LoadOrderFirstApproval]]
  - [[Rpt_ReturnOrder]]
  - [[Rpt_ReturnOrdersMaster]]
  - [[Rpt_RouteSummaryBySalesman]]
  - [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
  - [[Rpt_RouteSummaryBySalesman_Sukhtian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Return-Reversal-Workflow
---
# ReturnOrdersDetails


## Business Purpose
Line-item detail for customer return requests (`ReturnOrdersHeaders`). Records items requested to be returned by a customer, including item code (`ItemCode`), unit (`UnitID`), requested return quantity (`Quantity`), unit price (`Price`), and return discount/tax adjustments.
- **Workflow & Conversion**: Return orders are requests submitted from mobile tablets that often require supervisor approval (Workflow Function 22). Once approved, they may be converted into actual return invoices (`TransactionsHeaders` with `TransactionTypeID = 2`).
- **Header Link**: Pairs with `ReturnOrdersHeaders` on `TransactionYear` and `TransactionNo`.

## Chatbot semantics
(Query `t.ReturnOrdersDetails` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule |
|----------------------|-----------|---------------|
| أصناف طلب الإرجاع | `ItemCode`, `Quantity`, `Price` | Join `t.ReturnOrdersHeaders h ON d.TransactionYear = h.TransactionYear AND d.TransactionNo = h.TransactionNo` |
| كمية المرتجع المطلوبة | `Quantity` | `Quantity > 0` |
| سعر وقيمة الإرجاع | `Price`, `DiscountAmount` | قيمة المرتجع المحسوبة للسطر |
| اسم الصنف والوحدة | Join `t.Items`, `t.ItemsUnits` | `d.ItemCode = i.ItemCode`, `d.UnitID = u.UnitID` |

**Do not confuse with:**
- `t.TransactionsDetails` with `TransactionTypeID = 2` (executed return sales invoice lines that affect accounts immediately).
- `t.OrdersDetails` (pre-sales purchase orders).

## Grain & keys
- **Grain**: One row per item and unit within a return order (`TransactionYear`, `TransactionNo`, `ItemCode`, `UnitID`).
- **Composite PK**: `CompanyID`, `TransactionYear`, `TransactionNo`, `ItemCode`, `UnitID`.
- **Tenant Key**: `CompanyID`.

## Pipeline
Mobile Salesman Tablet → `OT_ImportReturnOrder` → `ReturnOrdersHeaders` + `ReturnOrdersDetails` → Supervisor Workflow (Function 22) → Conversion to Return Invoice.

## Related
- [[ReturnOrdersHeaders]]
- [[Items]]
- [[ItemsUnits]]
- [[TransactionsDetails]]

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[ReturnOrdersHeaders]] |
| TransactionYear | smallint | NO | ✓ | ✓ | [[ReturnOrdersHeaders]] |
| TransactionNo | int | NO | ✓ | ✓ | [[ReturnOrdersHeaders]] |
| ItemCode | nvarchar | NO | ✓ | ✓ | [[Items]] |
| UnitID | nvarchar | NO | ✓ | ✓ | [[ItemsUnits]] |
| ItemSerial | int | YES |  |  |  |
| Quantity | float | YES |  |  |  |
| Bonus | float | YES |  |  |  |
| Price | float | YES |  |  |  |
| DiscountAmount | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| VoucherDiscount | float | YES |  |  |  |
| TaxType | smallint | YES |  |  |  |
| TaxPercent | float | YES |  |  |  |
| TaxAmount | float | YES |  |  |  |
| ForeignPrice | float | YES |  |  |  |
| ForeignDiscountAmount | float | YES |  |  |  |
| ForeignDiscountPercent | float | YES |  |  |  |
| ForeignVouDiscount | float | YES |  |  |  |
| ForeignTaxPercent | float | YES |  |  |  |
| ForeignTaxAmount | float | YES |  |  |  |
| ItemStatus | smallint | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| ForeignCustomerDiscountAmount | float | YES |  |  |  |
| UPrice | float | YES |  |  |  |
| TaxType1 | smallint | YES |  |  |  |
| TaxPercent1 | float | YES |  |  |  |
| TaxAmount1 | float | YES |  |  |  |
| TaxType2 | smallint | YES |  |  |  |
| TaxPercent2 | float | YES |  |  |  |
| TaxAmount2 | float | YES |  |  |  |
| Manual_Bonus | float | YES |  |  |  |
| ExchangeRate | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| Manual_Disc | float | YES |  |  |  |
| ReturnReason | int | YES |  |  |  |
| BonusTax | float | YES |  |  |  |
| BonusAmount | float | YES |  |  |  |
| ExpDate | smalldatetime | YES |  |  |  |
## Primary Key
CompanyID
TransactionYear
TransactionNo
ItemCode
UnitID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, UnitID -> [[ItemsUnits]](CompanyID, ID)
CompanyID, TransactionYear, TransactionNo -> [[ReturnOrdersHeaders]](CompanyID, TransactionYear, TransactionNo)
## Impact / Procedures Using This Table

**Reads (16):**
- [[ConvertReturnOrderToInvoiceDelivery]]
- [[Pro_ItemsUnitsDetails]]
- [[Pro_ReturnOrdersDetails]]
- [[Pro_ReturnOrdersHeaders]]
- [[Rpt_CustomerReturnOrdersDetails]]
- [[Rpt_LoadOrderFirstApproval]]
- [[Rpt_ReturnOrder]]
- [[Rpt_ReturnOrdersMaster]]
- [[Rpt_RouteSummaryBySalesman]]
- [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
- [[Rpt_RouteSummaryBySalesman_Sukhtian]]
- [[Rpt_RouteSummaryBySalesman_Suktian]]
- [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]

**Writes (2):**
- [[OT_ImportReturnOrder]]
- [[Pro_ReturnOrdersDetails]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
