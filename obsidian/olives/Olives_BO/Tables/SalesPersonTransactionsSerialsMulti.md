---
type: table
database: Olives_BO
name: SalesPersonTransactionsSerialsMulti
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
  - [[Companies]]
  - [[SalesPersons]]
referenced_by:
  - [[OT_SendSalesmanData]]
  - [[Pro_SalesPersonTransactionsSerialsMulti]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonTransactionsSerialsMulti


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersontransactionsserialsmulti records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| SalesPersonID | int | NO | ✓ | ✓ | [[SalesPersons]] |
| SerYear | smallint | NO | ✓ |  |  |
| RefLink | varchar | YES | ✓ |  |  |
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
## Primary Key
CompanyID
SalesPersonID
SerYear
RefLink
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_SalesPersonTransactionsSerialsMulti]]

**Writes (2):**
- [[OT_SendSalesmanData]]
- [[Pro_SalesPersonTransactionsSerialsMulti]]

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
