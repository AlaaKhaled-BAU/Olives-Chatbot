---
type: table
database: OSFA_DB
name: OT_OrderDF
schema: dbo
tags: [#mobile, #order]
foreign_keys:
  - [[OT_OrderHF]]
referenced_by:
  - [[OT_AutoStoreItemsQty]]
  - [[OT_OrderDF_CheckExist]]
  - [[OT_OrderDF_Insert]]
  - [[OT_OrderDF_InsertForEdit]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Daily-Sales-Cycle
---
# OT_OrderDF



## Business Purpose


Line-item details for tablet-created sales orders.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ | ✓ | [[OT_OrderHF]] |
| OrderYear | smallint | NO | ✓ | ✓ | [[OT_OrderHF]] |
| OrderNo | int | NO | ✓ | ✓ | [[OT_OrderHF]] |
| ItemNo | varchar | YES | ✓ |  |  |
| UnitCode | varchar | YES | ✓ |  |  |
| Qty | money | YES |  |  |  |
| Bonus | money | YES |  |  |  |
| SellValue | float | YES |  |  |  |
| DiscPerc | float | YES |  |  |  |
| DiscValue | float | YES |  |  |  |
| TaxPerc | float | YES |  |  |  |
| TaxValue | float | YES |  |  |  |
| QtyOH | money | YES |  |  |  |
| PromisesDate | smalldatetime | YES |  |  |  |
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
| QtyAsBonus | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| BonusAmount | float | YES |  |  |  |
| BonusTax | float | YES |  |  |  |
| LineSort | smallint | YES |  |  |  |
| Ref1 | varchar | YES |  |  |  |
| Ref2 | varchar | YES |  |  |  |
| Ref3 | varchar | YES |  |  |  |
## Primary Key
CompNo
OrderYear
OrderNo
ItemNo
UnitCode
## Foreign Keys
CompNo, OrderYear, OrderNo -> [[OT_OrderHF]](CompNo, OrderYear, OrderNo)
## Impact / Procedures Using This Table

**Reads (4):**
- [[OT_AutoStoreItemsQty]]
- [[OT_OrderDF_CheckExist]]
- [[OT_OrderDF_Insert]]
- [[OT_OrderDF_InsertForEdit]]

**Writes (1):**
- [[OT_OrderDF_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
