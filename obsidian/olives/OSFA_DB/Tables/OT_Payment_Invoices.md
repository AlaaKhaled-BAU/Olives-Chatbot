---
type: table
database: OSFA_DB
name: OT_Payment_Invoices
schema: dbo
tags: [#billing, #mobile]
foreign_keys:
referenced_by:
  - [[OT_Payment_Invoices_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_Payment_Invoices



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| VouType | smallint | NO | ✓ |  |  |
| VouYear | smallint | NO | ✓ |  |  |
| VouNo | int | NO | ✓ |  |  |
| InvType | smallint | NO | ✓ |  |  |
| InvYear | smallint | NO | ✓ |  |  |
| InvNo | int | NO | ✓ |  |  |
| PaymentAmount | float | YES |  |  |  |
| Ref1 | nvarchar | YES |  |  |  |
| Ref2 | nvarchar | YES |  |  |  |
| Ref3 | nvarchar | YES |  |  |  |
| Ref4 | nvarchar | YES |  |  |  |
| DiscountAmount | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
## Primary Key
CompNo
VouType
VouYear
VouNo
InvType
InvYear
InvNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_Payment_Invoices_Insert]]

**Writes (1):**
- [[OT_Payment_Invoices_Insert]]

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
