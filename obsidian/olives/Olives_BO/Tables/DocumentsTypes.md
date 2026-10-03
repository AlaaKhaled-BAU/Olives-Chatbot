---
type: table
database: Olives_BO
name: DocumentsTypes
schema: dbo
tags: [#backoffice, #reference]
foreign_keys:
  - [[Companies]]
  - [[TransactionsTypes]]
referenced_by:
  - [[OT_SendCompData]]
  - [[Pro_ConvertLoadOrderToTransaction]]
  - [[Pro_ConvertUnloadOrderToTransaction]]
  - [[Pro_DocumentsTypes]]
  - [[Pro_GetCashCloseTotals]]
  - [[Pro_Receipts]]
  - [[Pro_TransactionsHeaders]]
  - [[Rpt_AcceptedSalesInvoices]]
  - [[Rpt_CashSummary]]
  - [[Rpt_InvoiceByDocTypes]]
  - [[Rpt_ReceivablesSalesInvoice]]
  - [[Rpt_SalesTransactionByDocumentsTypes]]
  - [[Rpt_SalesmanCashSales]]
  - [[Rpt_SalesmanSalesRecStatment]]
  - [[Rpt_TotalInvoiceByDocTypes]]
support_relevance: high
last_verified: 2026-07-05
---
# DocumentsTypes


## Business Purpose

Reference/lookup table defining documentstypes categories.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| TransactionTypeID | smallint | NO | ✓ | ✓ | [[TransactionsTypes]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
## Primary Key
CompanyID
TransactionTypeID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
TransactionTypeID -> [[TransactionsTypes]](ID)
## Known Circular Dependencies
- Part of a circular FK chain: DocumentsTypes → TransactionsTypes → TransactionsDetails → TransactionsHeaders → DocumentsTypes.
- Part of a circular FK chain: DocumentsTypes → TransactionsTypes → TransactionsHeaders → DocumentsTypes.
## Impact / Procedures Using This Table

**Reads (19):**
- [[OT_SendCompData]]
- [[Pro_DocumentsTypes]]
- [[Pro_GetCashCloseTotals]]
- [[Pro_Receipts]]
- [[Pro_TransactionsHeaders]]
- [[Rpt_AcceptedSalesInvoices]]
- [[Rpt_CashSummary]]
- [[Rpt_InvoiceByDocTypes]]
- [[Rpt_ReceivablesSalesInvoice]]
- [[Rpt_SalesTransactionByDocumentsTypes]]
- [[Rpt_SalesmanCashSales]]
- [[Rpt_SalesmanSalesRecStatment]]
- [[Rpt_TotalInvoiceByDocTypes]]

**Writes (4):**
- [[Pro_ConvertLoadOrderToTransaction]]
- [[Pro_ConvertUnloadOrderToTransaction]]
- [[Pro_DocumentsTypes]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing reference values**: Required dropdown items not present — selection fails on tablet
- **Duplicate codes**: Same code used for different descriptions — mapping ambiguity
- **Orphan references**: Referenced by deleted records — FK violation on delete attempt

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
