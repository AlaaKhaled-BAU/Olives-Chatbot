---
type: table
database: OSFA_DB
name: OT_SalesQuotationDF
schema: dbo
tags: [#mobile, #order, #sales]
foreign_keys:
referenced_by:
  - [[OT_SalesQuotationDF_CheckExist]]
  - [[OT_SalesQuotationDF_Insert]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Daily-Sales-Cycle
---
# OT_SalesQuotationDF



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| ItemNo | varchar | YES | ✓ |  |  |
| UnitCode | varchar | YES | ✓ |  |  |
| Qty | money | YES |  |  |  |
| Bonus | money | YES |  |  |  |
| SellValue | float | YES |  |  |  |
| DiscPerc | money | YES |  |  |  |
| DiscValue | float | YES |  |  |  |
| TaxPerc | money | YES |  |  |  |
| TaxValue | float | YES |  |  |  |
| TaxType | bit | YES |  |  |  |
| ItemDiscValue | float | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| ForeignCustomerDiscountAmount | float | YES |  |  |  |
| ForeignPrice | float | YES |  |  |  |
| ForeignDiscountAmount | float | YES |  |  |  |
| ForeignDiscountPercent | float | YES |  |  |  |
| ForeignVouDiscount | float | YES |  |  |  |
| ForeignTaxPercent | float | YES |  |  |  |
| ForeignTaxAmount | float | YES |  |  |  |
| UPrice | float | YES |  |  |  |
| TaxPerc_1 | float | YES |  |  |  |
| TaxValue_1 | float | YES |  |  |  |
| TaxType_1 | bit | YES |  |  |  |
| TaxPerc_2 | float | YES |  |  |  |
| TaxValue_2 | float | YES |  |  |  |
| TaxType_2 | bit | YES |  |  |  |
| Manual_Bonus | float | YES |  |  |  |
| Manual_Disc | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| BonusAmount | float | YES |  |  |  |
| BonusTax | float | YES |  |  |  |
## Primary Key
CompNo
OrderYear
OrderNo
ItemNo
UnitCode
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_SalesQuotationDF_CheckExist]]
- [[OT_SalesQuotationDF_Insert]]

**Writes (1):**
- [[OT_SalesQuotationDF_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Sync conflict**: Same record modified on tablet and BO simultaneously — last-write-wins may lose data
- **Orphan tablet records**: Row with no linked BO counterpart — check sync log
- **Duplicate TabletSysID**: Same tablet transaction inserted twice — run dedup check
- **Missing IsPosted flag**: Data not synced to BO — check tablet connectivity

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
