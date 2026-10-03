---
type: table
database: Olives_BO
name: TransactionsTypes
schema: dbo
tags: [#backoffice, #reference]
foreign_keys:
referenced_by:
  - [[Pro_Checks]]
  - [[Pro_ConvertLoadOrderToTransaction]]
  - [[Pro_ConvertUnloadOrderToTransaction]]
  - [[Pro_DocumentsTypes]]
  - [[Pro_SalesPersonNotbookTransactionsSerials]]
  - [[Pro_TransactionType]]
  - [[Pro_TransactionsTypes]]
  - [[Rpt_CategTransaction]]
  - [[Rpt_CustomersSalesDetails]]
  - [[Rpt_InvoiceQty]]
  - [[Rpt_ItemTransaction]]
  - [[Rpt_ReasonReprint]]
  - [[Rpt_ReprintCount]]
  - [[Rpt_SalesmanCashPayments]]
  - [[Rpt_SalesmanCashSales]]
  - [[Rpt_SalesmanChequePayments]]
  - [[Rpt_SalesmanCreditSales]]
  - [[Rpt_SalesmanSalesDetails]]
  - [[Rpt_TransactionByDate]]
  - [[Rpt_WareHouse_Item_Balance]]
support_relevance: high
last_verified: 2026-07-05
---
# TransactionsTypes


## Business Purpose

Reference/lookup table defining transactionstypes categories.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| ID | smallint | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
## Primary Key
ID
## Foreign Keys
(none)
## Known Circular Dependencies
- Part of a circular FK chain: Checks → Receipts → TransactionsTypes → Checks.
- Part of a circular FK chain: DocumentsTypes → TransactionsTypes → TransactionsDetails → TransactionsHeaders → DocumentsTypes.
- Part of a circular FK chain: DocumentsTypes → TransactionsTypes → TransactionsHeaders → DocumentsTypes.
## Impact / Procedures Using This Table

**Reads (22):**
- [[Pro_Checks]]
- [[Pro_ConvertLoadOrderToTransaction]]
- [[Pro_ConvertUnloadOrderToTransaction]]
- [[Pro_DocumentsTypes]]
- [[Pro_SalesPersonNotbookTransactionsSerials]]
- [[Pro_TransactionType]]
- [[Pro_TransactionsTypes]]
- [[Rpt_CategTransaction]]
- [[Rpt_CustomersSalesDetails]]
- [[Rpt_InvoiceQty]]
- [[Rpt_ItemTransaction]]
- [[Rpt_ReasonReprint]]
- [[Rpt_ReprintCount]]
- [[Rpt_SalesmanCashPayments]]
- [[Rpt_SalesmanCashSales]]
- [[Rpt_SalesmanChequePayments]]
- [[Rpt_SalesmanCreditSales]]
- [[Rpt_SalesmanSalesDetails]]
- [[Rpt_TransactionByDate]]
- [[Rpt_WareHouse_Item_Balance]]

**Writes (3):**
- [[Pro_ConvertLoadOrderToTransaction]]
- [[Pro_ConvertUnloadOrderToTransaction]]

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
