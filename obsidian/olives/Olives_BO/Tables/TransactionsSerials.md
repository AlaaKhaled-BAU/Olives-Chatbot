---
type: table
database: Olives_BO
name: TransactionsSerials
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[Pro_OrdersHeaders]]
  - [[Pro_Receipts]]
  - [[Pro_ReturnOrdersHeaders]]
  - [[Pro_TransactionsHeaders]]
  - [[Pro_TransfersOrdersHeaders]]
support_relevance: high
last_verified: 2026-07-05
---
# TransactionsSerials


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores transactionsserials records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| SerYear | smallint | NO | ✓ |  |  |
| OrderTakingNextSerial | bigint | YES |  |  |  |
| TransferOrderNextSerial | bigint | YES |  |  |  |
| SalesInvoiceNextSerial | bigint | YES |  |  |  |
| ReturnSalesNextSerial | bigint | YES |  |  |  |
| ReceiptNextSerial | bigint | YES |  |  |  |
| ConsNextSerial | bigint | YES |  |  |  |
| CustStockNextSerial | bigint | YES |  |  |  |
| CompetitiveItemsInfoNextSerial | bigint | YES |  |  |  |
| UnLoadOrdersNextSerials | bigint | YES |  |  |  |
| SalesmanStockNextSerial | bigint | YES |  |  |  |
| ReturnOrderNextSerial | bigint | YES |  |  |  |
| VanTransferNextSerial | bigint | YES |  |  |  |
| SalesQuotationNextSerial | bigint | YES |  |  |  |
| ItemsReplacementNextSerial | bigint | YES |  |  |  |
| IssueItemsNextSerial | bigint | YES |  |  |  |
## Primary Key
CompanyID
SerYear
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_Receipts]]
- [[Pro_TransfersOrdersHeaders]]

**Writes (5):**
- [[Pro_OrdersHeaders]]
- [[Pro_Receipts]]
- [[Pro_ReturnOrdersHeaders]]
- [[Pro_TransactionsHeaders]]
- [[Pro_TransfersOrdersHeaders]]

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
