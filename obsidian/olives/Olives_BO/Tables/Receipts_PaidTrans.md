---
type: table
database: Olives_BO
name: Receipts_PaidTrans
schema: dbo
tags: [#backoffice, #billing]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_ImportReceipts]]
  - [[OT_ImportSalesInvoices]]
  - [[Pro_Checks]]
  - [[Pro_ReceiptPaid]]
  - [[Pro_RptCashTotalOnline_Android]]
  - [[Pro_TransactionsHeaders]]
  - [[RptOnlineRpt_CustAging]]
  - [[Rpt_Cashier]]
  - [[Rpt_PrintCollectedReceiptByInvoice]]
  - [[Rpt_ReceiptVouchers]]
  - [[Rpt_SalesmanSalesRecStatment]]
  - [[Rpt_Salesman_Collections]]
  - [[Rpt_Salesman_TotalCollections]]
support_relevance: high
last_verified: 2026-07-05
---
# Receipts_PaidTrans


## Business Purpose
Invoice settlement and payment allocation bridge table — connects collection receipts (`Receipts`) to specific sales invoices or credit transactions (`TransactionsHeaders`) that are settled by the payment.
- **Join Mechanics**:
  - `TransactionYear`, `TransactionNo`, `TransactionTypeID`: Identifies the collection receipt (`Receipts`).
  - `PaidTransYear`, `PaidTransNo`, `PaidTransTypeID`: Identifies the settled invoice (`TransactionsHeaders` where `TransactionTypeID = PaidTransTypeID`, typically `1` for sales invoice).
- **Payment Distribution**: Records the allocated payment portion (`PaidAmount`) applied against each specific invoice, along with cash settlement discounts (`DiscountAmount`, `DiscountPercent`).
- **Reconciliation**: `IsManualReconciliation` indicates whether the payment was matched to invoices manually by an accountant or automatically at receipt capture.

## Chatbot semantics
(Query `t.Receipts_PaidTrans` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule |
|----------------------|-----------|---------------|
| الفواتير المسددة بالسند | `PaidTransNo`, `PaidTransYear`, `PaidAmount` | `TransactionYear = @ReceiptYear AND TransactionNo = @ReceiptNo` |
| المبالغ المسددة من الفاتورة | `PaidAmount`, `DiscountAmount` | Join `t.TransactionsHeaders inv ON pt.PaidTransYear = inv.TransactionYear AND pt.PaidTransNo = inv.TransactionNo AND pt.PaidTransTypeID = inv.TransactionTypeID` |
| سندات قبض الفاتورة | `TransactionNo`, `TransactionYear` | `PaidTransYear = @InvYear AND PaidTransNo = @InvNo` |
| خصم تعجيل الدفع / تسوية | `DiscountAmount` | الخصم الممنوح للعميل عند سداد الفاتورة |

**Do not confuse with:**
- `t.Receipts` (header summary of collections).
- `t.Checks` (individual check instruments collected).

## Grain & keys
- **Grain**: One row per receipt-to-invoice payment allocation (`TransactionYear`, `TransactionNo`, `PaidTransYear`, `PaidTransNo`, `PaidTransTypeID`).
- **Composite PK**: `CompanyID`, `TransactionYear`, `TransactionNo`, `TransactionTypeID`, `PaidTransYear`, `PaidTransNo`, `PaidTransTypeID`.
- **Tenant Key**: `CompanyID`.

## Pipeline
Mobile Salesman Tablet (Invoice Allocation) / BO Cashier → `OT_ImportReceipts` → `Receipts_PaidTrans`.

## Related
- [[Receipts]]
- [[TransactionsHeaders]]
- [[Checks]]

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| TransactionYear | smallint | NO | ✓ |  |  |
| TransactionNo | int | NO | ✓ |  |  |
| TransactionTypeID | smallint | NO | ✓ |  |  |
| PaidTransYear | smallint | NO | ✓ |  |  |
| PaidTransNo | int | NO | ✓ |  |  |
| PaidTransTypeID | smallint | NO | ✓ |  |  |
| PaidAmount | float | YES |  |  |  |
| PostedToERP | bit | YES |  |  |  |
| Ref1 | nvarchar | YES |  |  |  |
| Ref2 | nvarchar | YES |  |  |  |
| Ref3 | nvarchar | YES |  |  |  |
| Ref4 | nvarchar | YES |  |  |  |
| DiscountAmount | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| IsManualReconciliation | bit | YES |  |  |  |
## Primary Key
CompanyID
TransactionYear
TransactionNo
TransactionTypeID
PaidTransYear
PaidTransNo
PaidTransTypeID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (17):**
- [[Pro_Checks]]
- [[Pro_ReceiptPaid]]
- [[Pro_RptCashTotalOnline_Android]]
- [[Pro_TransactionsHeaders]]
- [[RptOnlineRpt_CustAging]]
- [[Rpt_Cashier]]
- [[Rpt_PrintCollectedReceiptByInvoice]]
- [[Rpt_ReceiptVouchers]]
- [[Rpt_SalesmanSalesRecStatment]]
- [[Rpt_Salesman_Collections]]
- [[Rpt_Salesman_TotalCollections]]

**Writes (9):**
- [[OT_ImportReceipts]]
- [[OT_ImportSalesInvoices]]

## Estimated Size / Volatility
Typical business table
## Common Issues

> [!warning] AUTO-GENERATED — verify before trusting

- **Settlement key**: joins Receipts via CompanyID+TransactionTypeID+TransactionYear+TransactionNo (convention — no ReceiptID column exists)
- **Discount fields**: DiscountAmount/DiscountPercent apply at settlement time, distinct from receipt-level discount
## Tenancy

Chatbot queries `t.Receipts_PaidTrans` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`. Raw dbo access is blocked for `chatbot_ro`.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
