---
type: table
database: OSFA_DB
name: OT_InvoiceReturnLinkToTab
schema: dbo
tags: [#billing, #mobile, #order]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_InvoiceReturnLinkToTab



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
| RetVouType | smallint | NO | ✓ |  |  |
| RetVouYear | smallint | NO | ✓ |  |  |
| RetVouNo | int | NO | ✓ |  |  |
| InvVouType | smallint | NO | ✓ |  |  |
| InvVouYear | smallint | NO | ✓ |  |  |
| InvVouNo | int | NO | ✓ |  |  |
| ItemCode | nvarchar | YES | ✓ |  |  |
| UnitID | nvarchar | YES | ✓ |  |  |
| Qty | money | YES |  |  |  |
| Bonus | money | YES |  |  |  |
| UnitPrice | float | YES |  |  |  |
## Primary Key
CompNo
SalesmanNo
RetVouType
RetVouYear
RetVouNo
InvVouType
InvVouYear
InvVouNo
ItemCode
UnitID
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
- [[OT_OrderHF]]
- [[OT_ConsOrderDF]]
- [[OT_OrderHistoryDF]]

- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]
- [[Glossary]]
