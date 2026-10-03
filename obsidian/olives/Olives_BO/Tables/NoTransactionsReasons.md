---
type: table
database: Olives_BO
name: NoTransactionsReasons
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[Online_RptInvoiceDeliveryByDriver]]
  - [[Pro_ApproveImagesApp]]
  - [[Pro_DeliveryCar]]
  - [[Pro_DriverDetailsDashboard]]
  - [[Pro_MapTransactionLog]]
  - [[Pro_NoTransactionsReasons]]
  - [[Pro_SalesmanDetailsDashboard]]
  - [[Pro_UnCloseOrder]]
  - [[Rpt_DeliveryInvoiceTransaction]]
  - [[Rpt_DriverNotDeliveryCounts]]
  - [[Rpt_DriversDeliverySummary]]
  - [[Rpt_NoSalesReasons]]
  - [[Rpt_RouteSummaryByDelivery]]
  - [[Rpt_RouteSummaryBySalesman]]
  - [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
  - [[Rpt_RouteSummaryBySalesman_Delivery]]
  - [[Rpt_RouteSummaryBySalesman_Merchandisers]]
  - [[Rpt_RouteSummaryBySalesman_Sukhtian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
  - [[Rpt_SalesmanTimeSpentPerCustomer]]
  - [[Rpt_SalesmanTimeSpentPerCustomer2]]
  - [[Rpt_SalesmanTimeSpentPerCustomer3]]
  - [[Rpt_SalesmanTimeSpentPerCustomer4]]
  - [[Rpt_SalesmanTimeSpentPerCustomer6_QimaH]]
  - [[Rpt_TimeManagement]]
support_relevance: high
last_verified: 2026-10-03
---
# NoTransactionsReasons

## Business Purpose
Master table defining reasons for non-transaction and non-visit field events (e.g., customer closed, no cash available, sufficient stock, postponed visit). Grouped by `ReasonType`, which maps to `SystemCodes.SysCodeTypeID = 'ReasonType'`. Used when salesmen log a no-sale exit, skip a scheduled visit, or record delivery exceptions. Queryable as `t.NoTransactionsReasons`.

## Chatbot semantics
(Query `t.NoTransactionsReasons` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| أسباب عدم الزيارة | `ReasonType`, `Name` | `ReasonType = 2` | SysCode `2` in `SystemCodes` ("No Visit Reason") |
| أسباب عدم البيع / خروج بدون بيع | `ReasonType`, `Name` | `ReasonType = 1` | SysCode `1` ("No Sales Reason") |
| أسباب الإرجاع | `ReasonType`, `Name` | `ReasonType = 3` | SysCode `3` ("Return Reason") |
| أسباب إلغاء التوصيل | `ReasonType`, `Name` | `ReasonType = 4` | SysCode `4` ("Cancel Invoice Delivery Reason") |
| التحقق من سبب العملية | `ID`, `Name` | Join on `ReasonID = r.ID AND r.ReasonType = ...` | Matches `NoTransactionsLog.ReasonID` or `RequestSalesmanWillNotVisit.ReasonID` |

**Do not confuse with:**
- `LogActionTransaction.ActionID`: Action 8 is `NoSaleExit` (Data1=Customer), Action 21 is `RequestSalesmanWillNotVisit`. The text explanation comes from joining `NoTransactionsReasons`.
- `SystemCodes`: SystemCodes gives the broad category names (`ReasonType` 1..6), while `NoTransactionsReasons` stores the actual customer-facing reason choices shown in tablet dropdowns.

## ReasonType Catalog (Olives_BO Verified)
- **ReasonType = 1**: No Sales Reason (e.g. 'Cash Unavailability', 'مغلق', 'وجود كميات', 'المحل مغلق')
- **ReasonType = 2**: No Visit Reason (e.g. 'NO1', skipped store)
- **ReasonType = 3**: Return Reason (customer return goods)
- **ReasonType = 4**: Cancel Invoice Delivery Reason (delivery failure)
- **ReasonType = 5**: Cancel Return Delivery Reason
- **ReasonType = 6**: Customer Gallery Image Reject Reason

## Grain & keys
- **Composite PK**: (`CompanyID`, `ID`, `ReasonType`)
- **Tenant key**: `CompanyID`

## Pipeline
Configured in Back Office UI (`Pro_NoTransactionsReasons`). Synced to mobile devices so salesmen select from approved reason lists. Stamped onto `NoTransactionsLog`, `RequestSalesmanWillNotVisit`, and `LogActionTransaction` exit notes.

## Related
- [[SystemCodes]]
- [[NoTransactionsLog]]
- [[RequestSalesmanWillNotVisit]]
- [[LogActionTransaction]]
- [[LogActions]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | int | NO | ✓ |  |  |
| ReasonType | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| IsNeedNote | bit | YES |  |  |  |
## Primary Key
CompanyID
ID
ReasonType
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (31):**
- [[Online_RptInvoiceDeliveryByDriver]]
- [[Pro_ApproveImagesApp]]
- [[Pro_DeliveryCar]]
- [[Pro_DriverDetailsDashboard]]
- [[Pro_MapTransactionLog]]
- [[Pro_NoTransactionsReasons]]
- [[Pro_SalesmanDetailsDashboard]]
- [[Pro_UnCloseOrder]]
- [[Rpt_DeliveryInvoiceTransaction]]
- [[Rpt_DriverNotDeliveryCounts]]
- [[Rpt_DriversDeliverySummary]]
- [[Rpt_NoSalesReasons]]
- [[Rpt_RouteSummaryByDelivery]]
- [[Rpt_RouteSummaryBySalesman]]
- [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
- [[Rpt_RouteSummaryBySalesman_Delivery]]
- [[Rpt_RouteSummaryBySalesman_Merchandisers]]
- [[Rpt_RouteSummaryBySalesman_Sukhtian]]
- [[Rpt_RouteSummaryBySalesman_Suktian]]
- [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
- [[Rpt_SalesmanTimeSpentPerCustomer]]
- [[Rpt_SalesmanTimeSpentPerCustomer2]]
- [[Rpt_SalesmanTimeSpentPerCustomer3]]
- [[Rpt_SalesmanTimeSpentPerCustomer4]]
- [[Rpt_SalesmanTimeSpentPerCustomer6_QimaH]]
- [[Rpt_TimeManagement]]

**Writes (2):**
- [[Pro_NoTransactionsReasons]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Orphan lines**: Detail rows without matching header — causes sync failures
- **Posting failure**: IsPosted flag stuck false — check ERP integration log
- **Duplicate vouchers**: Same VouNo generated for different transactions — run dedup check
- **Currency mismatch**: ExRate different from CurrenciesRate table — financial reconciliation off
- **Void inconsistency**: IsVoid flag but original transaction still active — check WF approval

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
