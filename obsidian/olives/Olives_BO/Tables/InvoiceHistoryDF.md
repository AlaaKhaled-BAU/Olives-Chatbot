---
type: table
database: Olives_BO
name: InvoiceHistoryDF
schema: dbo
tags: [#backoffice, #billing, #log]
foreign_keys:
referenced_by:
  - [[BO_Online_RptCustomerSalesTargetDetails]]
  - [[NiroukhMonthlyandQuarter]]
  - [[OT_SendSalesmanData]]
  - [[Pro_ReturnOrdersHeaders]]
  - [[RPT_CUSTOMERSMAIN_SUBTARGETREPORT_COLLECTIONS]]
  - [[RPT_CUSTOMERSMAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
  - [[RPT_LOCATIONSMAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
  - [[RPT_LOCATIONS_CUSTOMERTYPE_MAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
  - [[RPT_NEWNIROUKH_MONTHTARGET]]
  - [[RPT_NIROUKHCUSTOMERCLASSTARGET]]
  - [[RPT_NIROUKHCUSTOMERSMAIN_SUBTARGETREPORT]]
  - [[RPT_NIROUKHLOCATIONTARGET]]
  - [[Rpt_CompareCustSalesByCategAndTargetRef]]
  - [[Rpt_CustomerMonthlySalesByArea]]
  - [[Rpt_CustomerSalesByItems]]
  - [[Rpt_MonthlyCompareSalesTargetWithSales]]
  - [[Rpt_NiroukhMonths_Q_Target]]
  - [[Rpt_SalesmanSalesByItems]]
  - [[Rpt_SalesmanSalesTotal]]
  - [[Rpt_SalesmanSalesTotal_BO]]
  - [[Rpt_SalesmanSoldAndNoSoldCustomers]]
  - [[Rpt_SalesmanSoldAndNoSoldCustomers_BO]]
  - [[Rpt_TargetSpartan]]
  - [[Rpt_TowerTargets]]
  - [[Rpt_newNiroukh_monthTarget_comm]]
  - [[SalesmanInfo]]
support_relevance: high
last_verified: 2026-07-05
---
# InvoiceHistoryDF


## Business Purpose
Historical and archived invoice line-item detail table in Olives_BO. Stores archived invoice line items, products, quantities, prices, and discounts (`ItemNo`, `UnitCode`, `Qty`, `Bonus`, `UnitPrice`, `SellValue`).
- **Difference from `TransactionsDetails`**:
  - `TransactionsDetails` is the **live, active, operational** transaction details table recording current sales and returns created by salesmen and back-office billing.
  - `InvoiceHistoryDF` is the **archived / historical line-item repository** used for multi-year sales reporting, historical category trends, and offline purchase history lookups on mobile tablets.
- **Header Link**: Pairs with `InvoiceHistoryHF` on `CompNo`, `VouYear`, `VouNo`, and `VouType`.

## Chatbot semantics
(Query `t.InvoiceHistoryDF` — scoped by session CompNo/CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule |
|----------------------|-----------|---------------|
| تفاصيل أصناف الفواتير التاريخية | `ItemNo`, `Qty`, `SellValue`, `UnitPrice` | Join `t.InvoiceHistoryHF h ON df.VouYear = h.VouYear AND df.VouNo = h.VouNo AND df.VouType = h.VouType` |
| الكمية التاريخية المباعة | `Qty` | `Qty > 0` |
| قيمة المبيعات التاريخية للصنف | `SellValue` | إجمالي قيمة مبيعات الصنف في الفاتورة التاريخية |

**CRITICAL RULE FOR CHATBOT:**
For any questions regarding **current transaction lines or today's sales details**, ALWAYS query `t.TransactionsDetails`. Query `t.InvoiceHistoryDF` only when specifically asked about historical archives or legacy multi-year sales.

## Grain & keys
- **Grain**: One row per item, batch, and unit within an archived invoice header (`VouYear`, `VouNo`, `VouType`, `ItemNo`, `BatchNo`, `UnitCode`).
- **Composite PK**: `CompNo`, `VouYear`, `VouNo`, `VouType`, `ItemNo`, `BatchNo`, `UnitCode`.
- **Tenant Key**: `CompNo`.

## Pipeline
Legacy ERP Migration / Historical Archival → `InvoiceHistoryDF` → Used by historical sales comparative reporting.

## Related
- [[InvoiceHistoryHF]]
- [[TransactionsDetails]]
- [[Items]]

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| VouYear | smallint | NO | ✓ |  |  |
| VouNo | int | NO | ✓ |  |  |
| VouType | smallint | NO | ✓ |  |  |
| ItemNo | varchar | NO | ✓ |  |  |
| BatchNo | varchar | NO | ✓ |  |  |
| UnitCode | varchar | NO | ✓ |  |  |
| Qty | money | YES |  |  |  |
| Bonus | money | YES |  |  |  |
| SellValue | float | YES |  |  |  |
| DiscPerc | money | YES |  |  |  |
| DiscValue | float | YES |  |  |  |
| TaxPerc | money | YES |  |  |  |
| TaxValue | float | YES |  |  |  |
| ItemDesc | varchar | YES |  |  |  |
| UnitPrice | float | YES |  |  |  |
| VouDiscValue | float | YES |  |  |  |
## Primary Key
CompNo
VouYear
VouNo
VouType
ItemNo
BatchNo
UnitCode
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (48):**
- [[BO_Online_RptCustomerSalesTargetDetails]]
- [[NiroukhMonthlyandQuarter]]
- [[OT_SendSalesmanData]]
- [[Pro_ReturnOrdersHeaders]]
- [[RPT_CUSTOMERSMAIN_SUBTARGETREPORT_COLLECTIONS]]
- [[RPT_CUSTOMERSMAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
- [[RPT_LOCATIONSMAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
- [[RPT_LOCATIONS_CUSTOMERTYPE_MAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
- [[RPT_NEWNIROUKH_MONTHTARGET]]
- [[RPT_NIROUKHCUSTOMERCLASSTARGET]]
- [[RPT_NIROUKHCUSTOMERSMAIN_SUBTARGETREPORT]]
- [[RPT_NIROUKHLOCATIONTARGET]]
- [[Rpt_CompareCustSalesByCategAndTargetRef]]
- [[Rpt_CustomerMonthlySalesByArea]]
- [[Rpt_CustomerSalesByItems]]
- [[Rpt_MonthlyCompareSalesTargetWithSales]]
- [[Rpt_NiroukhMonths_Q_Target]]
- [[Rpt_SalesmanSalesByItems]]
- [[Rpt_SalesmanSalesTotal]]
- [[Rpt_SalesmanSalesTotal_BO]]
- [[Rpt_SalesmanSoldAndNoSoldCustomers]]
- [[Rpt_SalesmanSoldAndNoSoldCustomers_BO]]
- [[Rpt_TargetSpartan]]
- [[Rpt_TowerTargets]]
- [[Rpt_newNiroukh_monthTarget_comm]]
- [[SalesmanInfo]]

**Writes (7):**

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Line key**: ItemNo+BatchNo+UnitCode identify the sold batch/unit; Qty and Bonus are separate columns — bonus units ship free but are still stock movement
## Tenancy

Both tables surface as `t.` views scoped via their `CompNo` column (= `SESSION_CONTEXT(N'CompanyID')`; proven live: company 1 sees 2 of InvoiceHistoryHF's InvoiceHistoryDF rows). `CompNo` holds the company id.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
