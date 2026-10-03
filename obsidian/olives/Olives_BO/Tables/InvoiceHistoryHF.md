---
type: table
database: Olives_BO
name: InvoiceHistoryHF
schema: dbo
tags: [#backoffice, #billing, #log]
foreign_keys:
referenced_by:
  - [[BO_Online_RptCustomerSalesTargetDetails]]
  - [[NiroukhMonthlyandQuarter]]
  - [[OT_SendCompData]]
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
# InvoiceHistoryHF


## Business Purpose
Historical invoice and sales archive header table in Olives_BO. Stores imported historical sales invoices, legacy transactions from external ERPs, or archived past-year transactions (`VouYear`, `VouNo`, `VouDate`, `SalesmanNo`, `CustomerNo`).
- **Difference from `TransactionsHeaders`**:
  - `TransactionsHeaders` is the **live, active, operational** transaction header table where all current-year van sales, credit invoices, and return invoices are generated and modified by salesmen and the back-office billing engine.
  - `InvoiceHistoryHF` is an **historical/archival read-only snapshot repository** used primarily to:
    1. Calculate historical sales comparisons and multi-year KPI growth trends (e.g. `Rpt_MonthlyCompareSalesTargetWithSales`, comparing 2026 vs. 2025/2024).
    2. Sync historical purchases down to salesmen tablets via `OT_SendSalesmanData` so salesmen can view past purchase history on the road without bogging down the live transactional engine.
- **Master Discriminator (`VouType`)**: `1` = Historical Sales Invoice, `2` = Historical Return Invoice.

## Chatbot semantics
(Query `t.InvoiceHistoryHF` — scoped by session CompNo/CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule |
|----------------------|-----------|---------------|
| فواتير السنوات السابقة / الأرشيف التاريخي | `VouNo`, `VouYear`, `VouDate`, `CustomerNo`, `SalesmanNo` | `CustomerNo = @CustNo AND VouYear < @CurrentYear` |
| مقارنة مبيعات العام الحالي مع السابق | Aggregate with `TransactionsHeaders` | `InvoiceHistoryHF` للسنوات السابقة و `TransactionsHeaders` للعام الحالي |
| تفاصيل أصناف الفاتورة التاريخية | Join `t.InvoiceHistoryDF` | `df.VouYear = h.VouYear AND df.VouNo = h.VouNo AND df.VouType = h.VouType` |

**CRITICAL RULE FOR CHATBOT:**
For any questions regarding **current transactions, today's sales, this month's invoices, or live returns**, ALWAYS query `t.TransactionsHeaders`. Query `t.InvoiceHistoryHF` only when specifically asked about historical archives, legacy ERP transactions, or multi-year sales history.

## Grain & keys
- **Grain**: One row per historical invoice voucher header (`CompNo`, `VouYear`, `VouNo`, `VouType`).
- **Composite PK**: `CompNo`, `VouYear`, `VouNo`, `VouType`.
- **Tenant Key**: `CompNo`.

## Pipeline
Legacy ERP Migration / Historical Yearly Archival → `InvoiceHistoryHF` + `InvoiceHistoryDF` → Synced to mobile devices for past history lookups.

## Related
- [[InvoiceHistoryDF]]
- [[TransactionsHeaders]]
- [[Customers]]
- [[SalesPersons]]

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| VouYear | smallint | NO | ✓ |  |  |
| VouNo | int | NO | ✓ |  |  |
| VouType | smallint | NO | ✓ |  |  |
| VouDate | smalldatetime | YES |  |  |  |
| StoreNo | int | YES |  |  |  |
| SalesmanNo | smallint | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| InvStatus | varchar | YES |  |  |  |
| Ref1 | varchar | YES |  |  |  |
| Ref2 | varchar | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
| VouDiscPerc | float | YES |  |  |  |
| CustomerDiscPerc | float | YES |  |  |  |
| ERPVouNo | nvarchar | YES |  |  |  |
| PaymentDiscPerc | float | YES |  |  |  |
| PaymentDiscAmt | float | YES |  |  |  |
## Primary Key
CompNo
VouYear
VouNo
VouType
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (45):**
- [[BO_Online_RptCustomerSalesTargetDetails]]
- [[NiroukhMonthlyandQuarter]]
- [[OT_SendCompData]]
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

**Writes (6):**

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Status column**: InvStatus is NULL on essentially all live rows — do not filter on it
- **Doc types**: VouType values observed live: 9 (dominant), 1 — meaning is app-side; never assume 1=invoice
- **Naming**: key is CompNo+VouYear+VouNo+VouType; carrier cols are CustomerNo/SalesmanNo (no underscores)
## Tenancy

Both tables surface as `t.` views scoped via their `CompNo` column (= `SESSION_CONTEXT(N'CompanyID')`; proven live: company 1 sees 2 of InvoiceHistoryDF's InvoiceHistoryHF rows). `CompNo` holds the company id.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
