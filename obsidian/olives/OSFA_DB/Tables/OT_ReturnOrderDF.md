---
type: table
database: OSFA_DB
name: OT_ReturnOrderDF
schema: dbo
tags: [#mobile, #order]
foreign_keys:
  - [[OT_ReturnOrderHF]]
referenced_by:
  - [[OT_ReturnOrderDF_CheckExist]]
  - [[OT_ReturnOrderDF_Insert]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Return-Reversal-Workflow
---
# OT_ReturnOrderDF



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ | ✓ | [[OT_ReturnOrderHF]] |
| VouYear | smallint | NO | ✓ | ✓ | [[OT_ReturnOrderHF]] |
| VouNo | int | NO | ✓ | ✓ | [[OT_ReturnOrderHF]] |
| ItemNo | nvarchar | YES | ✓ |  |  |
| Unit | nvarchar | YES | ✓ |  |  |
| Qty | money | YES |  |  |  |
| Bonus | money | YES |  |  |  |
| Price | float | YES |  |  |  |
| DiscountAmount | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| VouDiscount | float | YES |  |  |  |
| TaxType | int | YES |  |  |  |
| TaxPercent | float | YES |  |  |  |
| TaxAmount | float | YES |  |  |  |
| ItemStatus | int | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| ForeignCustomerDiscountAmount | float | YES |  |  |  |
| ForeignPrice | float | YES |  |  |  |
| ForeignDiscountAmount | float | YES |  |  |  |
| ForeignDiscountPercent | float | YES |  |  |  |
| ForeignVouDiscount | float | YES |  |  |  |
| ForeignTaxPercent | float | YES |  |  |  |
| ForeignTaxAmount | float | YES |  |  |  |
| UPrice | float | YES |  |  |  |
| TaxPercent_1 | float | YES |  |  |  |
| TaxAmount_1 | float | YES |  |  |  |
| TaxType_1 | bit | YES |  |  |  |
| TaxPercent_2 | float | YES |  |  |  |
| TaxAmount_2 | float | YES |  |  |  |
| TaxType_2 | bit | YES |  |  |  |
| Manual_Bonus | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| Manual_Disc | float | YES |  |  |  |
| ReturnReason | int | YES |  |  |  |
| BonusAmount | float | YES |  |  |  |
| BonusTax | float | YES |  |  |  |
| ExpDate | smalldatetime | YES |  |  |  |
## Primary Key
CompNo
VouYear
VouNo
ItemNo
Unit
## Foreign Keys
CompNo, VouYear, VouNo -> [[OT_ReturnOrderHF]](CompNo, VouYear, VouNo)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_ReturnOrderDF_CheckExist]]
- [[OT_ReturnOrderDF_Insert]]

**Writes (1):**
- [[OT_ReturnOrderDF_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[Olives_BO/Procedures/OT_ImportReturnOrderMerch]]
