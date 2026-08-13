---
type: table
database: OSFA_DB
name: OT_InvoicesDelivery
schema: dbo
tags: [#billing, #mobile, #order]
foreign_keys:
referenced_by:
  - [[OT_InvoicesDelivery_CheckExist]]
  - [[OT_InvoicesDelivery_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_InvoicesDelivery



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| TransactionTypeID | smallint | NO | ✓ |  |  |
| TransactionYear | smallint | NO | ✓ |  |  |
| TransactionNo | int | NO | ✓ |  |  |
| InvoiceSalesPersonID | int | YES |  |  |  |
| SalesPersonID | int | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| DeliveredDateTime | smalldatetime | YES |  |  |  |
| IsPosted | bit | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| CancelReasonID | int | YES |  |  |  |
| StoreNo | int | YES |  |  |  |
| PaymentType | int | YES |  |  |  |
## Primary Key
CompanyID
TransactionTypeID
TransactionYear
TransactionNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_InvoicesDelivery_CheckExist]]
- [[OT_InvoicesDelivery_Insert]]

**Writes (1):**
- [[OT_InvoicesDelivery_Insert]]

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
