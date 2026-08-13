---
type: table
database: OSFA_DB
name: OT_InvoiceDF
schema: dbo
tags: [#billing, #mobile]
foreign_keys:
  - [[OT_InvoiceHF]]
referenced_by:
  - [[OT_AddRetInvImages]]
  - [[OT_AutoStoreItemsQty]]
  - [[OT_InvoiceDF_CheckExist]]
  - [[OT_InvoiceDF_Insert]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Daily-Sales-Cycle
---
# OT_InvoiceDF



## Business Purpose


Line-item details for tablet-created invoices, synced to back-office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ | ✓ | [[OT_InvoiceHF]] |
| VouType | smallint | NO | ✓ | ✓ | [[OT_InvoiceHF]] |
| VouYear | smallint | NO | ✓ | ✓ | [[OT_InvoiceHF]] |
| VouNo | int | NO | ✓ | ✓ | [[OT_InvoiceHF]] |
| ItemNo | varchar | YES | ✓ |  |  |
| Unit | varchar | YES | ✓ |  |  |
| Qty | money | YES |  |  |  |
| Bonus | money | YES |  |  |  |
| Price | float | YES |  |  |  |
| DiscountAmount | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| VouDiscount | float | YES |  |  |  |
| TaxType | bit | YES |  |  |  |
| TaxPercent | float | YES |  |  |  |
| TaxAmount | float | YES |  |  |  |
| ItemStatus | smallint | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| ForeignCustomerDiscountAmount | float | YES |  |  |  |
| ForeignPrice | float | YES |  |  |  |
| ForeignDiscountAmount | float | YES |  |  |  |
| ForeignDiscountPercent | float | YES |  |  |  |
| ForeignVouDiscount | float | YES |  |  |  |
| ForeignTaxPercent | float | YES |  |  |  |
| ForeignTaxAmount | float | YES |  |  |  |
| ItemImage | image | YES |  |  |  |
| IsPostedImage | bit | YES |  |  |  |
| UPrice | float | YES |  |  |  |
| TaxPercent_1 | float | YES |  |  |  |
| TaxAmount_1 | float | YES |  |  |  |
| TaxType_1 | bit | YES |  |  |  |
| TaxPercent_2 | float | YES |  |  |  |
| TaxAmount_2 | float | YES |  |  |  |
| TaxType_2 | bit | YES |  |  |  |
| Manual_Bonus | float | YES |  |  |  |
| SP_Qty | float | YES |  |  |  |
| ItemBarcode | varchar | YES |  |  |  |
| Manual_Disc | float | YES |  |  |  |
| QtyAsBonus | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| ReturnReason | int | YES |  |  |  |
| BonusAmount | float | YES |  |  |  |
| BonusTax | float | YES |  |  |  |
| LineSort | smallint | YES |  |  |  |
| CurrentQty | float | YES |  |  |  |
## Primary Key
CompNo
VouType
VouYear
VouNo
ItemNo
Unit
## Foreign Keys
CompNo, VouType, VouYear, VouNo -> [[OT_InvoiceHF]](CompNo, VouType, VouYear, VouNo)
## Impact / Procedures Using This Table

**Reads (4):**
- [[OT_AddRetInvImages]]
- [[OT_AutoStoreItemsQty]]
- [[OT_InvoiceDF_CheckExist]]
- [[OT_InvoiceDF_Insert]]

**Writes (2):**
- [[OT_AddRetInvImages]]
- [[OT_InvoiceDF_Insert]]

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
- [[Shared/Runbooks/Sync-Conflict]]
