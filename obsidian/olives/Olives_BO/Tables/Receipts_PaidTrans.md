---
type: table
database: Olives_BO
name: Receipts_PaidTrans
schema: dbo
tags: [#backoffice, #billing]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[ABS_Integ_SendPayment_Jebrene]]
  - [[ABS_Integ_SendPayment_Sokhtian]]
  - [[Bajali_SAP_Integ]]
  - [[ECO_Land_SAP_Integ]]
  - [[GArrow_SAP_Integ]]
  - [[OT_ImportReceipts]]
  - [[OT_ImportSalesInvoices]]
  - [[ProTech_Integration_SendPayment]]
  - [[ProTech_Integration_SendSalesInvoice]]
  - [[Pro_Checks]]
  - [[Pro_ReceiptPaid]]
  - [[Pro_RptCashTotalOnline_Android]]
  - [[Pro_TransactionsHeaders]]
  - [[Qetaf_Integ]]
  - [[RamPharm_SAP_Integ]]
  - [[RptOnlineRpt_CustAging]]
  - [[Rpt_Cashier]]
  - [[Rpt_PrintCollectedReceiptByInvoice]]
  - [[Rpt_ReceiptVouchers]]
  - [[Rpt_SalesmanSalesRecStatment]]
  - [[Rpt_Salesman_Collections]]
  - [[Rpt_Salesman_TotalCollections]]
  - [[SAMA_SAP_Integ]]
  - [[SAP_Naouri_SendPayment_Integration]]
  - [[SAP_Tyconz_Integ]]
  - [[SAP_Tyconz_Integ_SendPayments]]
support_relevance: high
last_verified: 2026-07-05
---
# Receipts_PaidTrans


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores receipts paidtrans records.

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
- [[ABS_Integ_SendPayment_Jebrene]]
- [[ABS_Integ_SendPayment_Sokhtian]]
- [[ProTech_Integration_SendPayment]]
- [[ProTech_Integration_SendSalesInvoice]]
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
- [[SAP_Naouri_SendPayment_Integration]]
- [[SAP_Tyconz_Integ_SendPayments]]

**Writes (9):**
- [[Bajali_SAP_Integ]]
- [[ECO_Land_SAP_Integ]]
- [[GArrow_SAP_Integ]]
- [[OT_ImportReceipts]]
- [[OT_ImportSalesInvoices]]
- [[Qetaf_Integ]]
- [[RamPharm_SAP_Integ]]
- [[SAMA_SAP_Integ]]
- [[SAP_Tyconz_Integ]]

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
