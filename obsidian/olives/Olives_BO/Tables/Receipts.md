---
type: table
database: Olives_BO
name: Receipts
schema: dbo
tags: [#backoffice, #billing]
foreign_keys:
  - [[Companies]]
  - [[Currencies]]
  - [[Customers]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[TransactionsTypes]]
referenced_by:
  - [[DA_SalesTarget]]
  - [[DEMOSALESPERSON]]
  - [[DEMOSALESPERSON2]]
  - [[DiagnosticTools_CheckSalespersonunpostedOlivesTransactions]]
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[OT_FixActionLog]]
  - [[OT_ImportActionLog]]
  - [[OT_ImportReceipts]]
  - [[OT_SendMultiSalesmanData]]
  - [[OT_SendSalesmanData]]
  - [[PRO_AUTOSENDEMAIL]]
  - [[PRO_GETRECEIPTSFOREMAIL]]
  - [[PRO_GETVOIDEDRECEIPTSFOREMAIL]]
  - [[Pro_Checks]]
  - [[Pro_ChecksByStatusDetails]]
  - [[Pro_CompanyParameters]]
  - [[Pro_Dashboard_Almalak]]
  - [[Pro_DeliveryDashboard]]
  - [[Pro_DriverDetailsDashboard]]
  - [[Pro_GetCashCloseTotals]]
  - [[Pro_MapTransactionLog]]
  - [[Pro_ReceiptPaid]]
  - [[Pro_ReceiptRequestsSchedule]]
  - [[Pro_Receipts]]
  - [[Pro_RptCashTotalOnline_Android]]
  - [[Pro_RptCashTotalOnline_Android_Naqi]]
  - [[Pro_SalesmanCashSettlement]]
  - [[Pro_SalesmanDetailsDashboard]]
  - [[Pro_SalesmanStockAndReturnLoadOrders]]
  - [[Pro_TransactionsHeaders]]
  - [[RPT_SUMMARYSALESAND]]
  - [[RptOnlineRpt_CustAging]]
  - [[RptOnlineRpt_SalesmanJournySummary]]
  - [[Rpt_ALLReturnChecks]]
  - [[Rpt_CashInvoiceAndReciept]]
  - [[Rpt_CashOnlyReceipts]]
  - [[Rpt_CashReceipts]]
  - [[Rpt_CashSummary]]
  - [[Rpt_Cashier]]
  - [[Rpt_CheckAging]]
  - [[Rpt_CheckStatusDetails]]
  - [[Rpt_ChecksByStatus]]
  - [[Rpt_ChequeInfrmation]]
  - [[Rpt_ChequeStatusWithSettelment]]
  - [[Rpt_CollectedPaymentByUser]]
  - [[Rpt_CollectedReceipts]]
  - [[Rpt_CollectedReceiptsByCompany]]
  - [[Rpt_CustomersSalesReturnCollectionMatching]]
  - [[Rpt_CustomersVisitsCount]]
  - [[Rpt_DailyReceiptsDetails]]
  - [[Rpt_LoadOrderFirstApproval]]
  - [[Rpt_LuxuryItemsCustTarget]]
  - [[Rpt_NetVisitsTime]]
  - [[Rpt_PaymentsMappingNew]]
  - [[Rpt_PrintCollectedReceipt]]
  - [[Rpt_PrintCollectedReceiptByInvoice]]
  - [[Rpt_PrintReceiptDetailsInfo]]
  - [[Rpt_ReasonReprint]]
  - [[Rpt_ReceiptVouchers]]
  - [[Rpt_Receipts]]
  - [[Rpt_ReceiptsApproveDate]]
  - [[Rpt_ReceiptsByCustomersClass]]
  - [[Rpt_ReceiptsBySalesman]]
  - [[Rpt_ReceiptsDetails]]
  - [[Rpt_ReprintCount]]
  - [[Rpt_RoutePerformanceAnalysis]]
  - [[Rpt_RouteScoreBySalesman]]
  - [[Rpt_RouteSummaryBySalesman]]
  - [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
  - [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
  - [[Rpt_RouteSummaryBySalesman_Merchandisers]]
  - [[Rpt_RouteSummaryBySalesman_Sukhtian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
  - [[Rpt_RouteSummaryDeatils]]
  - [[Rpt_SalesAndCollectionTargetByLocation]]
  - [[Rpt_SalesAndOrders]]
  - [[Rpt_SalesCollcetionsTargets]]
  - [[Rpt_SalesmanCashAndChequesSales]]
  - [[Rpt_SalesmanCashPayments]]
  - [[Rpt_SalesmanChequePayments]]
  - [[Rpt_SalesmanDailyActivities]]
  - [[Rpt_SalesmanDaySummary]]
  - [[Rpt_SalesmanReceiptsCurrency]]
  - [[Rpt_SalesmanRouteEfficiency]]
  - [[Rpt_SalesmanRouteEfficiency_SV_LV_TV2]]
  - [[Rpt_SalesmanSalesRecStatment]]
  - [[Rpt_SalesmanSalesSummary]]
  - [[Rpt_SalesmanSalesSummaryByCustomer]]
  - [[Rpt_SalesmanStockAndReturn]]
  - [[Rpt_SalesmanSummaryRoute]]
  - [[Rpt_SalesmanSummaryRoute_60]]
  - [[Rpt_SalesmanSummaryRoute_Atieh]]
  - [[Rpt_SalesmanSummaryRoute_Dandana]]
  - [[Rpt_SalesmanSummaryRoute_zz]]
  - [[Rpt_SalesmanTimeSpentPerCustomer]]
  - [[Rpt_SalesmanTimeSpentPerCustomer3]]
  - [[Rpt_SalesmanTimeSpentPerCustomer6_QimaH]]
  - [[Rpt_SalesmanTimeSpentPerCustomerQima7]]
  - [[Rpt_SalesmanTimeSpentPerCustomerQima8]]
  - [[Rpt_SalesmanTotalCashAndCheck]]
  - [[Rpt_SalesmanTransactionDetails]]
  - [[Rpt_SalesmanVisitsRoute]]
  - [[Rpt_Salesman_Collections]]
  - [[Rpt_Salesman_TotalCollections]]
  - [[Rpt_TargetSpartan]]
  - [[Rpt_TotalSalesmanRouteSummary]]
  - [[Rpt_TransactionsNotes]]
  - [[Rpt_UsersKPI]]
  - [[Rpt_WorkFlowAnalysis]]
  - [[Rpt_WorkFlowExceeds]]
  - [[TECHNICAL_CHECKMISSINGSERIAL_OLIVES_BO_ORDER_RECEIPT_INV_RETINV]]
support_relevance: high
last_verified: 2026-10-03
---
# Receipts

## Business Purpose
The customer collections header table — stores payment receipts collected from customers by salesmen in the field or recorded in the back office. Captures composite PK (`TransactionTypeID`, `TransactionYear`, `TransactionNo`), customer (`CustomerID`), collecting salesman (`SalesPersonID`), date (`TransactionDate`), total collected amount (`NetTotal`, `Total`), and void flags (`IsVoid`). Queryable via `t.Receipts`.

## Chatbot semantics
(Query `t.Receipts` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| سندات القبض / تحصيلات المندوب | `CustomerID`, `SalesPersonID`, `TransactionDate` | Direct filters | Cash and check collection vouchers |
| إجمالي مبالغ التحصيل | `NetTotal` | `SUM(NetTotal) WHERE (IsVoid = 0 OR IsVoid IS NULL)` | Total money collected |
| سندات غير ملغاة | `IsVoid` | `IsVoid = 0 OR IsVoid IS NULL` | Active collection receipts |
| تفاصيل الشيكات المحصلة | Join `t.Checks` | Join on receipt key / `Receipts_PaidTransChecks` | Bank, check number, due date |
| تسوية الفواتير المقبوضة | Join `t.Receipts_PaidTrans` | Links receipt to paid invoice | Shows which invoices were cleared |

**Do not confuse with:**
- `TransactionsHeaders`: Invoices/sales issued (`TransactionTypeID = 1`). Receipts represent cash/checks incoming to settle invoices or customer accounts.
- `LogActionTransaction`: ActionID `12` ("PaymentIssue") logs the receipt generation *event*, while `Receipts` holds the accounting voucher.

## Grain & keys
- **Composite PK**: (`CompanyID`, `TransactionTypeID`, `TransactionYear`, `TransactionNo`)
- **Tenant key**: `CompanyID`
- **FKs**: `CustomerID` → [[Customers]](ID), `SalesPersonID` → [[SalesPersons]](ID), `CurrencyID` → [[Currencies]](ID)

## Pipeline (how rows get here)
Collected on mobile devices → imported via `OT_ImportReceipts` or ERP integration procs.

## Related
- [[TransactionsHeaders]]
- [[Customers]]
- [[SalesPersons]]
- [[Checks]]
- [[LogActionTransaction]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| TransactionTypeID | smallint | NO | ✓ | ✓ | [[TransactionsTypes]] |
| TransactionYear | smallint | NO | ✓ |  |  |
| TransactionNo | int | NO | ✓ |  |  |
| TransactionDate | smalldatetime | YES |  |  |  |
| DocumentTypeID | int | YES |  |  |  |
| CustomerID | bigint | YES |  | ✓ | [[Customers]] |
| SalesPersonID | int | YES |  | ✓ | [[SalesPersons]] |
| Amount | float | YES |  |  |  |
| ForeignAmount | float | YES |  |  |  |
| CurrencyID | smallint | YES |  | ✓ | [[Currencies]] |
| ExchangeRate | float | YES |  |  |  |
| IsPrinted | bit | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| RouteID | int | YES |  | ✓ | [[RoutesInformation]] |
| PostedToERP | bit | YES |  |  |  |
| Collected | bit | YES |  |  |  |
| Discount | float | YES |  |  |  |
| RefNo | nvarchar | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| PrintOriginalCount | int | YES |  |  |  |
| PrintCopyCount | int | YES |  |  |  |
| IsWFApproved | bit | YES |  |  |  |
| WFApproveDesc | nvarchar | YES |  |  |  |
| IsVoid | bit | YES |  |  |  |
| AcceptDate | smalldatetime | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| DetailCount | int | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| AcceptedBy | nvarchar | YES |  |  |  |
| ReceiptRequestYear | smallint | YES |  |  |  |
| ReceiptRequestNo | int | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| PostedToEmail | bit | YES |  |  |  |
| Bank_TransferNo | nvarchar | YES |  |  |  |
| Bank_Transfer_Date | smalldatetime | YES |  |  |  |
| Bank_Transfer_Amount | float | YES |  |  |  |
| Bank_Transfer_BankID | int | YES |  |  |  |
| Bank_Transfer_BankAccount | int | YES |  |  |  |
| FirstVoid | bit | YES |  |  |  |
| VoidPostedToERP | bit | YES |  |  |  |
| VoidPostedToEmail | bit | YES |  |  |  |
| VoidedByUser | nvarchar | YES |  |  |  |
| SecondCollected | bit | YES |  |  |  |
| PostedToERPDateTime | smalldatetime | YES |  |  |  |
| LocationLineID | int | YES |  |  |  |
| ForeignDiscount | float | YES |  |  |  |
| IsDepositInBank | bit | YES |  |  |  |
| PostDate | smalldatetime | YES |  |  |  |
## Primary Key
CompanyID
TransactionTypeID
TransactionYear
TransactionNo
## Foreign Keys
CompanyID -> [[Companies]](ID)
CurrencyID -> [[Currencies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, RouteID -> [[RoutesInformation]](CompanyID, ID)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
TransactionTypeID -> [[TransactionsTypes]](ID)
## Known Circular Dependencies
- Part of a circular FK chain: Checks → Receipts → TransactionsTypes → Checks.
## Impact / Procedures Using This Table

**Reads (177):**
- [[DA_SalesTarget]]
- [[DEMOSALESPERSON]]
- [[DEMOSALESPERSON2]]
- [[DiagnosticTools_CheckSalespersonunpostedOlivesTransactions]]
- [[OT_FixActionLog]]
- [[OT_SendMultiSalesmanData]]
- [[OT_SendSalesmanData]]
- [[PRO_AUTOSENDEMAIL]]
- [[PRO_GETRECEIPTSFOREMAIL]]
- [[PRO_GETVOIDEDRECEIPTSFOREMAIL]]
- [[Pro_Checks]]
- [[Pro_ChecksByStatusDetails]]
- [[Pro_CompanyParameters]]
- [[Pro_Dashboard_Almalak]]
- [[Pro_DeliveryDashboard]]
- [[Pro_DriverDetailsDashboard]]
- [[Pro_GetCashCloseTotals]]
- [[Pro_MapTransactionLog]]
- [[Pro_ReceiptPaid]]
- [[Pro_ReceiptRequestsSchedule]]
- [[Pro_Receipts]]
- [[Pro_RptCashTotalOnline_Android]]
- [[Pro_RptCashTotalOnline_Android_Naqi]]
- [[Pro_SalesmanCashSettlement]]
- [[Pro_SalesmanDetailsDashboard]]
- [[Pro_SalesmanStockAndReturnLoadOrders]]
- [[Pro_TransactionsHeaders]]
- [[RPT_SUMMARYSALESAND]]
- [[RptOnlineRpt_CustAging]]
- [[RptOnlineRpt_SalesmanJournySummary]]
- [[Rpt_ALLReturnChecks]]
- [[Rpt_CashInvoiceAndReciept]]
- [[Rpt_CashOnlyReceipts]]
- [[Rpt_CashReceipts]]
- [[Rpt_CashSummary]]
- [[Rpt_Cashier]]
- [[Rpt_CheckAging]]
- [[Rpt_CheckStatusDetails]]
- [[Rpt_ChecksByStatus]]
- [[Rpt_ChequeInfrmation]]
- [[Rpt_ChequeStatusWithSettelment]]
- [[Rpt_CollectedPaymentByUser]]
- [[Rpt_CollectedReceipts]]
- [[Rpt_CollectedReceiptsByCompany]]
- [[Rpt_CustomersSalesReturnCollectionMatching]]
- [[Rpt_CustomersVisitsCount]]
- [[Rpt_DailyReceiptsDetails]]
- [[Rpt_LoadOrderFirstApproval]]
- [[Rpt_LuxuryItemsCustTarget]]
- [[Rpt_NetVisitsTime]]
- [[Rpt_PaymentsMappingNew]]
- [[Rpt_PrintCollectedReceipt]]
- [[Rpt_PrintCollectedReceiptByInvoice]]
- [[Rpt_PrintReceiptDetailsInfo]]
- [[Rpt_ReasonReprint]]
- [[Rpt_ReceiptVouchers]]
- [[Rpt_Receipts]]
- [[Rpt_ReceiptsApproveDate]]
- [[Rpt_ReceiptsByCustomersClass]]
- [[Rpt_ReceiptsBySalesman]]
- [[Rpt_ReceiptsDetails]]
- [[Rpt_ReprintCount]]
- [[Rpt_RoutePerformanceAnalysis]]
- [[Rpt_RouteScoreBySalesman]]
- [[Rpt_RouteSummaryBySalesman]]
- [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
- [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
- [[Rpt_RouteSummaryBySalesman_Merchandisers]]
- [[Rpt_RouteSummaryBySalesman_Sukhtian]]
- [[Rpt_RouteSummaryBySalesman_Suktian]]
- [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
- [[Rpt_RouteSummaryDeatils]]
- [[Rpt_SalesAndCollectionTargetByLocation]]
- [[Rpt_SalesAndOrders]]
- [[Rpt_SalesCollcetionsTargets]]
- [[Rpt_SalesmanCashAndChequesSales]]
- [[Rpt_SalesmanCashPayments]]
- [[Rpt_SalesmanChequePayments]]
- [[Rpt_SalesmanDailyActivities]]
- [[Rpt_SalesmanDaySummary]]
- [[Rpt_SalesmanReceiptsCurrency]]
- [[Rpt_SalesmanRouteEfficiency]]
- [[Rpt_SalesmanRouteEfficiency_SV_LV_TV2]]
- [[Rpt_SalesmanSalesRecStatment]]
- [[Rpt_SalesmanSalesSummary]]
- [[Rpt_SalesmanSalesSummaryByCustomer]]
- [[Rpt_SalesmanStockAndReturn]]
- [[Rpt_SalesmanSummaryRoute]]
- [[Rpt_SalesmanSummaryRoute_60]]
- [[Rpt_SalesmanSummaryRoute_Atieh]]
- [[Rpt_SalesmanSummaryRoute_Dandana]]
- [[Rpt_SalesmanSummaryRoute_zz]]
- [[Rpt_SalesmanTimeSpentPerCustomer]]
- [[Rpt_SalesmanTimeSpentPerCustomer3]]
- [[Rpt_SalesmanTimeSpentPerCustomer6_QimaH]]
- [[Rpt_SalesmanTimeSpentPerCustomerQima7]]
- [[Rpt_SalesmanTimeSpentPerCustomerQima8]]
- [[Rpt_SalesmanTotalCashAndCheck]]
- [[Rpt_SalesmanTransactionDetails]]
- [[Rpt_SalesmanVisitsRoute]]
- [[Rpt_Salesman_Collections]]
- [[Rpt_Salesman_TotalCollections]]
- [[Rpt_TargetSpartan]]
- [[Rpt_TotalSalesmanRouteSummary]]
- [[Rpt_TransactionsNotes]]
- [[Rpt_UsersKPI]]
- [[Rpt_WorkFlowAnalysis]]
- [[Rpt_WorkFlowExceeds]]
- [[TECHNICAL_CHECKMISSINGSERIAL_OLIVES_BO_ORDER_RECEIPT_INV_RETINV]]

**Writes (65):**
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[OT_ImportActionLog]]
- [[OT_ImportReceipts]]
- [[OT_SendSalesmanData]]
- [[Pro_ReceiptPaid]]
- [[Pro_Receipts]]
- [[Pro_SalesmanCashSettlement]]
- [[Pro_TransactionsHeaders]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Posting**: PostedToERP marks ERP export; PostDate timestamps it
- **Voiding**: IsVoid exists here (unlike detail tables); check paired ReturnOrdersHeaders before treating voids as revenue reversals
- **Naming**: receipt voucher number columns are TransactionYear/TransactionNo — there is no VouNo column
## Tenancy

Chatbot queries `t.Receipts` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`. Raw dbo access is blocked for `chatbot_ro`.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- See also (OSFA counterpart): [[OSFA_DB/Tables/OT_Payments]]
