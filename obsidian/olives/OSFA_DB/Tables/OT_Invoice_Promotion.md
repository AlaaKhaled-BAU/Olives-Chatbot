---
type: table
database: OSFA_DB
name: OT_Invoice_Promotion
schema: dbo
tags: [#billing, #mobile, #sales]
foreign_keys:
referenced_by:
  - [[OT_Invoice_Promotion_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_Invoice_Promotion



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
| SerID | int | NO | ✓ |  |  |
| PromotionCode | nvarchar | YES |  |  |  |
| PromotionType | int | YES |  |  |  |
| PromotionName | nvarchar | YES |  |  |  |
| InputItem | nvarchar | YES |  |  |  |
| InputUnit | nvarchar | YES |  |  |  |
| InputQty | money | YES |  |  |  |
| InputAmount | float | YES |  |  |  |
| ItemNo | nvarchar | YES |  |  |  |
| UnitCode | nvarchar | YES |  |  |  |
| Bonus | money | YES |  |  |  |
| ItemDiscountAmount | float | YES |  |  |  |
| ItemDiscountPercent | float | YES |  |  |  |
| VouDiscountAmount | float | YES |  |  |  |
| VouDiscountPercent | float | YES |  |  |  |
| IncludeInTargetBonus | bit | YES |  |  |  |
| IsInInput | bit | YES |  |  |  |
## Primary Key
CompNo
VouType
VouYear
VouNo
SerID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_Invoice_Promotion_Insert]]

**Writes (1):**
- [[OT_Invoice_Promotion_Insert]]

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
