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
  - [[OT_ImportReceipts]]
  - [[PRO_GETRECEIPTSFOREMAIL]]
  - [[Pro_Checks]]
  - [[Pro_ChecksByStatusDetails]]
  - [[Pro_Dashboard_Almalak]]
  - [[Pro_DeliveryDashboard]]
  - [[Pro_MerchandiseDashboard]]
  - [[Pro_ReceiptPaid]]
  - [[Pro_Receipts]]
  - [[Pro_RptCashTotalOnline_Android]]
  - [[Pro_RptCashTotalOnline_Android_Naqi]]
  - [[RPT_SUMMARYSALESAND]]
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
  - [[SalesmanInfo]]
support_relevance: high
last_verified: 2026-07-05
---
# Checks


## Business Purpose
Stores bank checks received from customers as payment instruments attached to collection receipts (`Receipts`). Records issuing bank (`BankID`), branch (`BranchID`), check number (`ChequeNo`), maturity / due date (`DueDate`), face amount (`Amount`), and check collection status (`CheckStatus`).
- **Header Link**: Pairs with collection receipts (`Receipts`) via `TransactionYear` and `TransactionNo` (with `TransactionTypeID`).
- **Check Status**: `CheckStatus` tracks check maturity and lifecycle in Olives (e.g. In Portfolio / في الصندوق, Deposited / برسم التحصيل, Collected / محصل, Bounced / راجع).
- **Due Date Aging**: `DueDate` determines whether a check is current or post-dated (شيكات مؤجلة / برسم التحصيل).

## Chatbot semantics
(Query `t.Checks` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule |
|----------------------|-----------|---------------|
| الشيكات المستلمة من العميل | `ChequeNo`, `Amount`, `DueDate`, `BankID` | Join `t.Customers c ON ch.CustomerID = c.ID` |
| شيكات سند القبض | `TransactionYear`, `TransactionNo`, `Amount` | Join `t.Receipts r ON ch.TransactionYear = r.TransactionYear AND ch.TransactionNo = r.TransactionNo` |
| تاريخ استحقاق الشيك | `DueDate` | `DueDate <= GETDATE()` (مستحق) أو `DueDate > GETDATE()` (مؤجل) |
| حالة الشيك | `CheckStatus` | حالة الشيك (محصل، راجع، برسم التحصيل) |
| البنك والفرع | `BankID`, `BranchID` | Join `t.Banks`, `t.Branches` |
| قيمة الشيك بالعملة | `Amount`, `ForeignAmount`, `CurrencyID` | قيمة الشيك المودع |

**Do not confuse with:**
- `t.Receipts` (the overall collection receipt header, which includes total cash and total check amounts).
- `t.Receipts_PaidTrans` (reconciliation / allocation of receipt amounts against specific sales invoices).

## Grain & keys
- **Grain**: One row per physical check attached to a receipt (`BankID`, `BranchID`, `TransactionYear`, `TransactionNo`, `CustomerID`, `ChequeNo`).
- **Composite PK**: `CompanyID`, `BankID`, `BranchID`, `TransactionYear`, `TransactionNo`, `TransactionTypeID`, `CustomerID`, `ChequeNo`.
- **Tenant Key**: `CompanyID`.

## Pipeline
Mobile Salesman / Cashier Tablet → `OT_ImportReceipts` → `Receipts` + `Checks`.

## Related
- [[Receipts]]
- [[Customers]]
- [[Banks]]
- [[Receipts_PaidTrans]]

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
- [[PRO_GETRECEIPTSFOREMAIL]]
- [[Pro_Checks]]
- [[Pro_ChecksByStatusDetails]]
- [[Pro_Dashboard_Almalak]]
- [[Pro_DeliveryDashboard]]
- [[Pro_MerchandiseDashboard]]
- [[Pro_ReceiptPaid]]
- [[Pro_Receipts]]
- [[Pro_RptCashTotalOnline_Android]]
- [[Pro_RptCashTotalOnline_Android_Naqi]]
- [[RPT_SUMMARYSALESAND]]
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
- [[SalesmanInfo]]

**Writes (13):**
- [[OT_ImportReceipts]]
- [[Pro_Checks]]
- [[Pro_ReceiptPaid]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Check lifecycle**: CheckStatus is tri-state in live data: NULL = pending, then 1/2 after transition; ChangeStatusDate records the flip
- **Exchange rate**: ExchangeRate here can drift from CurrenciesRate — reconcile before FX reporting
- **Dual FK targets**: BankID references Banks.ID AND Branches.BankID; CustomerID references Customers.ID AND Drawers.CustomerID — pick the target that matches your question
## Tenancy

Chatbot queries `t.Checks` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`. Raw dbo access is blocked for `chatbot_ro`.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- See also (OSFA counterpart): [[OSFA_DB/Tables/OT_Checks]]
