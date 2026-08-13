---
type: table
database: OSFA_DB
name: OT_ReceiptRequests
schema: dbo
tags: [#billing, #mobile]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ReceiptRequests



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
| OrderDate | smalldatetime | YES |  |  |  |
| CustomerID | bigint | YES |  |  |  |
| Amount | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| OrderStatus | int | YES |  |  |  |
| PaymentType | int | YES |  |  |  |
| IsSettlement | bit | YES |  |  |  |
| Priority | bit | YES |  |  |  |
| DocType | smallint | YES |  |  |  |
## Primary Key
CompanyID
OrderYear
OrderNo
SalesmanNo
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
- [[OT_PaymentsTypes]]
- [[OT_PriceList]]
- [[OT_RequestToChangeInvoicePaymentType]]

- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]
- [[Glossary]]
