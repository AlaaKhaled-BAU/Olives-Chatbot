---
type: table
database: Olives_BO
name: Checks
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Banks]]
  - [[Branches]]
  - [[Companies]]
  - [[Currencies]]
  - [[Customers]]
  - [[Drawers]]
  - [[Receipts]]
  - [[TransactionsTypes]]
referenced_by:
  - [[ABS_Integ_SendPayment_Jebrene]]
  - [[ABS_Integ_SendPayment_Sokhtian]]
  - [[AX_INTEG_SENDRECEIPTS]]
  - [[AX_Integ_SendPayments_AbuTawileh]]
  - [[AbuOda_BonMarrof_Integ]]
  - [[AbuOda_Comp2_Integ]]
  - [[AbuOda_Integ]]
  - [[Acback_Integ_SendPayments]]
  - [[AccPack_Integ_SendReceipts]]
  - [[AccPack_Integ_SendReceipts_LuxuryItems]]
  - [[Awtar_Integ_SendReceipts]]
  - [[Bajali_SAP_Integ]]
  - [[Bonanza_Integ_SendReceipts_SmokingCenter]]
  - [[Bonanza_Integ_SendReceipts_Yasmeen]]
  - [[CL_Integ_SendAllTransactions]]
  - [[Darwaza_Integ_SendReceipts]]
  - [[Defaf_Integration]]
  - [[ECO_Land_SAP_Integ]]
  - [[Ejabi_Integ_SendPayments]]
  - [[Falcons_GetItemBalance]]
  - [[GArrow_SAP_Integ]]
  - [[GP_Integ_SendReceipt_Wadi]]
  - [[IscoJordan_Integ_SendReceipts]]
  - [[Izhiman_SAP_Integ]]
  - [[Khobara_Integ]]
  - [[MeatLand_Integration]]
  - [[MeatLand_Integrationnew]]
  - [[Motakaml_Integ_SendReceipts]]
  - [[NPF_Integ_SendReceipts]]
  - [[Niroukh_Integ_SendReceipts]]
  - [[OT_ImportReceipts]]
  - [[PRO_GETRECEIPTSFOREMAIL]]
  - [[PrestoSoft_Integ_SendReceipts]]
  - [[Presto_Integ]]
  - [[ProTech_Integration_SendPayment]]
  - [[Pro_Checks]]
  - [[Pro_ChecksByStatusDetails]]
  - [[Pro_Dashboard_Almalak]]
  - [[Pro_DeliveryDashboard]]
  - [[Pro_MerchandiseDashboard]]
  - [[Pro_ReceiptPaid]]
  - [[Pro_Receipts]]
  - [[Pro_RptCashTotalOnline_Android]]
  - [[Pro_RptCashTotalOnline_Android_Naqi]]
  - [[Qerat_Integ]]
  - [[Qetaf_Integ]]
  - [[RPT_SUMMARYSALESAND]]
  - [[RamPharm_SAP_Integ]]
  - [[Rpt_ALLReturnChecks]]
  - [[Rpt_CashInvoiceAndReciept]]
  - [[Rpt_CashOnlyReceipts]]
  - [[Rpt_CashReceipts]]
  - [[Rpt_Cashier]]
  - [[Rpt_CheckAging]]
  - [[Rpt_CheckStatusDetails]]
  - [[Rpt_ChecksByStatus]]
  - [[Rpt_ChecksTest]]
  - [[Rpt_ChequeInfrmation]]
  - [[Rpt_ChequeStatusWithSettelment]]
  - [[Rpt_CollectedPaymentByUser]]
  - [[Rpt_CollectedReceipts]]
  - [[Rpt_CollectedReceiptsByCompany]]
  - [[Rpt_DailyReceiptsDetails]]
  - [[Rpt_LoadOrderFirstApproval]]
  - [[Rpt_PrintCollectedReceipt]]
  - [[Rpt_PrintCollectedReceiptByInvoice]]
  - [[Rpt_ReceiptVouchers]]
  - [[Rpt_Receipts]]
  - [[Rpt_ReceiptsByCustomersClass]]
  - [[Rpt_ReceiptsBySalesman]]
  - [[Rpt_ReceiptsDetails]]
  - [[Rpt_ReceivablesSalesInvoice]]
  - [[Rpt_RoutePerformanceAnalysis]]
  - [[Rpt_RoutePerformanceAnalysis_Spartan]]
  - [[Rpt_RouteSummaryBySalesmanCombine_Spartan]]
  - [[Rpt_RouteSummaryBySalesman_Spartan]]
  - [[Rpt_SalesAndOrders]]
  - [[Rpt_SalesmanCashAndChequesSales]]
  - [[Rpt_SalesmanCashPayments]]
  - [[Rpt_SalesmanChequePayments]]
  - [[Rpt_SalesmanDaySummary]]
  - [[Rpt_SalesmanSalesRecStatment]]
  - [[Rpt_SalesmanTransactionDetails]]
  - [[Rpt_UsersKPI]]
  - [[Rpt_WorkFlowAnalysis]]
  - [[Rpt_WorkFlowExceeds]]
  - [[SAMA_SAP_Integ]]
  - [[SAP_Integ_SendPayments]]
  - [[SAP_Integ_SendPayments_Amazing]]
  - [[SAP_Integ_SendPayments_Hammoudeh]]
  - [[SAP_Integ_SendPayments_Karadsheh]]
  - [[SAP_Integ_SendPayments_Kaylani]]
  - [[SAP_Integ_SendPayments_Lamis]]
  - [[SAP_Integ_SendPayments_Malak]]
  - [[SAP_Integ_SendPayments_Meri]]
  - [[SAP_Integ_SendPayments_UniCharm]]
  - [[SAP_Naouri_SendPayment_Integration]]
  - [[SAP_Tyconz_Integ_SendPayments]]
  - [[SN_Integ_SendPayments]]
  - [[Salbeshian_SAP_Integ]]
  - [[SalesmanInfo]]
  - [[Shamel_Integ_SendReciepts]]
  - [[Shini_Integ]]
  - [[Tahona_Integ_SendReceipts]]
  - [[Wings_Integ_SendReceipts]]
  - [[Yolande_Integ_SendReceipts]]
  - [[Zedan_SAP_Integ]]
support_relevance: high
last_verified: 2026-07-05
---
# Checks


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores checks records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Receipts]] |
| BankID | int | NO | ✓ | ✓ | [[Branches]] |
| BranchID | int | NO | ✓ | ✓ | [[Branches]] |
| TransactionYear | smallint | NO | ✓ | ✓ | [[Receipts]] |
| TransactionNo | int | NO | ✓ | ✓ | [[Receipts]] |
| TransactionTypeID | smallint | NO | ✓ | ✓ | [[TransactionsTypes]] |
| CustomerID | bigint | NO | ✓ | ✓ | [[Drawers]] |
| ChequeNo | int | NO | ✓ |  |  |
| DrawerID | int | YES |  | ✓ | [[Drawers]] |
| DueDate | smalldatetime | YES |  |  |  |
| Amount | float | YES |  |  |  |
| ForeignAmount | float | YES |  |  |  |
| CurrencyID | smallint | YES |  | ✓ | [[Currencies]] |
| ExchangeRate | float | YES |  |  |  |
| CheckStatus | smallint | YES |  |  |  |
| ChangeStatusDate | smalldatetime | YES |  |  |  |
| IsGero | bit | YES |  |  |  |
| CustBankAccNo | varchar | YES |  |  |  |
| AC_Payee | bit | YES |  |  |  |
## Primary Key
CompanyID
BankID
BranchID
TransactionYear
TransactionNo
TransactionTypeID
CustomerID
ChequeNo
## Foreign Keys
CompanyID, BankID -> [[Banks]](CompanyID, ID)
CompanyID, BankID, BranchID -> [[Branches]](CompanyID, BankID, ID)
CompanyID -> [[Companies]](ID)
CurrencyID -> [[Currencies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, CustomerID, DrawerID -> [[Drawers]](CompanyID, CustomerID, ID)
CompanyID, TransactionTypeID, TransactionYear, TransactionNo -> [[Receipts]](CompanyID, TransactionTypeID, TransactionYear, TransactionNo)
TransactionTypeID -> [[TransactionsTypes]](ID)
## Known Circular Dependencies
- Part of a circular FK chain: Checks → Receipts → TransactionsTypes → Checks.
## Impact / Procedures Using This Table

**Reads (105):**
- [[ABS_Integ_SendPayment_Jebrene]]
- [[ABS_Integ_SendPayment_Sokhtian]]
- [[AX_INTEG_SENDRECEIPTS]]
- [[AX_Integ_SendPayments_AbuTawileh]]
- [[AbuOda_BonMarrof_Integ]]
- [[AbuOda_Comp2_Integ]]
- [[AbuOda_Integ]]
- [[Acback_Integ_SendPayments]]
- [[AccPack_Integ_SendReceipts]]
- [[AccPack_Integ_SendReceipts_LuxuryItems]]
- [[Awtar_Integ_SendReceipts]]
- [[Bajali_SAP_Integ]]
- [[Bonanza_Integ_SendReceipts_SmokingCenter]]
- [[Bonanza_Integ_SendReceipts_Yasmeen]]
- [[CL_Integ_SendAllTransactions]]
- [[Darwaza_Integ_SendReceipts]]
- [[Defaf_Integration]]
- [[ECO_Land_SAP_Integ]]
- [[Ejabi_Integ_SendPayments]]
- [[Falcons_GetItemBalance]]
- [[GArrow_SAP_Integ]]
- [[GP_Integ_SendReceipt_Wadi]]
- [[IscoJordan_Integ_SendReceipts]]
- [[Izhiman_SAP_Integ]]
- [[Khobara_Integ]]
- [[MeatLand_Integration]]
- [[MeatLand_Integrationnew]]
- [[Motakaml_Integ_SendReceipts]]
- [[NPF_Integ_SendReceipts]]
- [[Niroukh_Integ_SendReceipts]]
- [[PRO_GETRECEIPTSFOREMAIL]]
- [[PrestoSoft_Integ_SendReceipts]]
- [[Presto_Integ]]
- [[ProTech_Integration_SendPayment]]
- [[Pro_Checks]]
- [[Pro_ChecksByStatusDetails]]
- [[Pro_Dashboard_Almalak]]
- [[Pro_DeliveryDashboard]]
- [[Pro_MerchandiseDashboard]]
- [[Pro_ReceiptPaid]]
- [[Pro_Receipts]]
- [[Pro_RptCashTotalOnline_Android]]
- [[Pro_RptCashTotalOnline_Android_Naqi]]
- [[Qerat_Integ]]
- [[Qetaf_Integ]]
- [[RPT_SUMMARYSALESAND]]
- [[RamPharm_SAP_Integ]]
- [[Rpt_ALLReturnChecks]]
- [[Rpt_CashInvoiceAndReciept]]
- [[Rpt_CashOnlyReceipts]]
- [[Rpt_CashReceipts]]
- [[Rpt_Cashier]]
- [[Rpt_CheckAging]]
- [[Rpt_CheckStatusDetails]]
- [[Rpt_ChecksByStatus]]
- [[Rpt_ChecksTest]]
- [[Rpt_ChequeInfrmation]]
- [[Rpt_ChequeStatusWithSettelment]]
- [[Rpt_CollectedPaymentByUser]]
- [[Rpt_CollectedReceipts]]
- [[Rpt_CollectedReceiptsByCompany]]
- [[Rpt_DailyReceiptsDetails]]
- [[Rpt_LoadOrderFirstApproval]]
- [[Rpt_PrintCollectedReceipt]]
- [[Rpt_PrintCollectedReceiptByInvoice]]
- [[Rpt_ReceiptVouchers]]
- [[Rpt_Receipts]]
- [[Rpt_ReceiptsByCustomersClass]]
- [[Rpt_ReceiptsBySalesman]]
- [[Rpt_ReceiptsDetails]]
- [[Rpt_ReceivablesSalesInvoice]]
- [[Rpt_RoutePerformanceAnalysis]]
- [[Rpt_RoutePerformanceAnalysis_Spartan]]
- [[Rpt_RouteSummaryBySalesmanCombine_Spartan]]
- [[Rpt_RouteSummaryBySalesman_Spartan]]
- [[Rpt_SalesAndOrders]]
- [[Rpt_SalesmanCashAndChequesSales]]
- [[Rpt_SalesmanCashPayments]]
- [[Rpt_SalesmanChequePayments]]
- [[Rpt_SalesmanDaySummary]]
- [[Rpt_SalesmanSalesRecStatment]]
- [[Rpt_SalesmanTransactionDetails]]
- [[Rpt_UsersKPI]]
- [[Rpt_WorkFlowAnalysis]]
- [[Rpt_WorkFlowExceeds]]
- [[SAMA_SAP_Integ]]
- [[SAP_Integ_SendPayments]]
- [[SAP_Integ_SendPayments_Amazing]]
- [[SAP_Integ_SendPayments_Hammoudeh]]
- [[SAP_Integ_SendPayments_Karadsheh]]
- [[SAP_Integ_SendPayments_Kaylani]]
- [[SAP_Integ_SendPayments_Lamis]]
- [[SAP_Integ_SendPayments_Malak]]
- [[SAP_Integ_SendPayments_Meri]]
- [[SAP_Integ_SendPayments_UniCharm]]
- [[SAP_Naouri_SendPayment_Integration]]
- [[SAP_Tyconz_Integ_SendPayments]]
- [[SN_Integ_SendPayments]]
- [[Salbeshian_SAP_Integ]]
- [[SalesmanInfo]]
- [[Shamel_Integ_SendReciepts]]
- [[Shini_Integ]]
- [[Tahona_Integ_SendReceipts]]
- [[Wings_Integ_SendReceipts]]
- [[Zedan_SAP_Integ]]

**Writes (13):**
- [[OT_ImportReceipts]]
- [[Pro_Checks]]
- [[Pro_ReceiptPaid]]
- [[SAP_Integ_SendPayments]]
- [[SAP_Integ_SendPayments_Amazing]]
- [[SAP_Integ_SendPayments_Hammoudeh]]
- [[SAP_Integ_SendPayments_Karadsheh]]
- [[SAP_Integ_SendPayments_Kaylani]]
- [[SAP_Integ_SendPayments_Lamis]]
- [[SAP_Integ_SendPayments_Malak]]
- [[SAP_Integ_SendPayments_Meri]]
- [[SAP_Integ_SendPayments_UniCharm]]
- [[Yolande_Integ_SendReceipts]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Partial payment not tracked**: Receipt amount less than invoice total — aging report shows incorrect balance
- **Check bounce**: CheckStatus not updated after bank return — customer credit not restored
- **Currency conversion error**: ExRate differs from daily rate — receipt in wrong amount
- **Duplicate receipts**: Same payment applied twice — customer credit balance wrong

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- See also (OSFA counterpart): [[OSFA_DB/Tables/OT_Checks]]
