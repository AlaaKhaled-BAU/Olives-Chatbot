---
type: table
database: Olives_BO
name: SalesPersonTransactionsSerials
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
  - [[Companies]]
  - [[SalesPersons]]
referenced_by:
  - [[DiagnosticTools_CheckSalespersonConfiguration]]
  - [[OT_SendSalesmanData]]
  - [[Pro_Auto_Unload]]
  - [[Pro_DebitCreditNoteTrans]]
  - [[Pro_ImportData]]
  - [[Pro_SalesPersonTransactionsSerials]]
  - [[Pro_SalesmanStockAndReturnLoadOrders]]
  - [[Pro_TransfersOrdersHeaders]]
  - [[VoidInvoiceAsReturn]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonTransactionsSerials


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersontransactionsserials records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| SalesPersonID | int | NO | ✓ | ✓ | [[SalesPersons]] |
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
| SalesInvoiceNextSerial_Credit | bigint | YES |  |  |  |
| DebitCreditNoteNextSerial | bigint | YES |  |  |  |
| DebitCreditNoteNextSerial_2 | bigint | YES |  |  |  |
| ReceiveItemsNextSerial | bigint | YES |  |  |  |
| PaymentsOrdersNextSerial | bigint | YES |  |  |  |
| ItemsCategStockNextSerial | bigint | YES |  |  |  |
| BankDepositNextSerial | bigint | YES |  |  |  |

## Primary Key
CompanyID
SalesPersonID
SerYear
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (7):**
- [[DiagnosticTools_CheckSalespersonConfiguration]]
- [[Pro_Auto_Unload]]
- [[Pro_DebitCreditNoteTrans]]
- [[Pro_SalesPersonTransactionsSerials]]
- [[Pro_SalesmanStockAndReturnLoadOrders]]
- [[Pro_TransfersOrdersHeaders]]
- [[VoidInvoiceAsReturn]]

**Writes (4):**
- [[OT_SendSalesmanData]]
- [[Pro_DebitCreditNoteTrans]]
- [[Pro_ImportData]]
- [[Pro_SalesPersonTransactionsSerials]]

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
