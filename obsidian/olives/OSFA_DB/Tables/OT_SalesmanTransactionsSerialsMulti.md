---
type: table
database: OSFA_DB
name: OT_SalesmanTransactionsSerialsMulti
schema: dbo
tags: [#mobile, #sales]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_SalesmanTransactionsSerialsMulti



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
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
CompNo
SalesmanNo
SerYear
RefLink
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Orphan lines**: Detail rows without matching header — causes sync failures
- **Posting failure**: IsPosted flag stuck false — check ERP integration log
- **Duplicate vouchers**: Same VouNo generated for different transactions — run dedup check
- **Currency mismatch**: ExRate different from CurrenciesRate table — financial reconciliation off
- **Void inconsistency**: IsVoid flag but original transaction still active — check WF approval

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[OT_LinkedSalesman]]
- [[OT_PromotionsCondUnCodInput]]
- [[OT_PromotionsSalesmanGroupsLink]]

- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]
- [[Glossary]]
