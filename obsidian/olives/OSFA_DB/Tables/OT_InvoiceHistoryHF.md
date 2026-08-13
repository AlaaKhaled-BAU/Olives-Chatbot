---
type: table
database: OSFA_DB
name: OT_InvoiceHistoryHF
schema: dbo
tags: [#billing, #log, #mobile]
foreign_keys:
referenced_by:
  - [[servics_app_OSFA_Mobile_Ver]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_InvoiceHistoryHF



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| VouYear | smallint | NO | ✓ |  |  |
| VouNo | int | NO | ✓ |  |  |
| VouType | smallint | NO | ✓ |  |  |
| VouDate | smalldatetime | YES |  |  |  |
| StoreNo | int | YES |  |  |  |
| SalesmanNo | smallint | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| VouDiscPerc | float | YES |  |  |  |
| CustomerDiscPerc | float | YES |  |  |  |
| InvStatus | varchar | YES |  |  |  |
| Ref1 | varchar | YES |  |  |  |
| Ref2 | varchar | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
| IsForDelivery | bit | YES |  |  |  |
| SalesmanName | varchar | YES |  |  |  |
| PaymentDiscPerc | float | YES |  |  |  |
| PaymentDiscAmt | float | YES |  |  |  |
## Primary Key
CompNo
VouYear
VouNo
VouType
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[servics_app_OSFA_Mobile_Ver]]

**Writes (0):**
_None_

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
