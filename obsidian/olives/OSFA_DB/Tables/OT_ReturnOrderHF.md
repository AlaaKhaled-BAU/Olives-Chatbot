---
type: table
database: OSFA_DB
name: OT_ReturnOrderHF
schema: dbo
tags: [#mobile, #order]
foreign_keys:
referenced_by:
  - [[OT_ReturnOrderHF_CheckExist]]
  - [[OT_ReturnOrderHF_Insert]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Return-Reversal-Workflow
---
# OT_ReturnOrderHF



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| VouYear | smallint | NO | ✓ |  |  |
| VouNo | int | NO | ✓ |  |  |
| SalesmanNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| VouDate | smalldatetime | YES |  |  |  |
| StoreNo | int | YES |  |  |  |
| CaCr | bit | YES |  |  |  |
| DiscountAmount | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| GPSX | nvarchar | YES |  |  |  |
| GPSY | nvarchar | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| Currency | int | YES |  |  |  |
| ExRate | float | YES |  |  |  |
| IsPosted | bit | YES |  |  |  |
| PrNo | int | YES |  |  |  |
| RouteID | int | YES |  |  |  |
| IsVoid | int | YES |  |  |  |
| CustomerName | nvarchar | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| CustomerDiscountPerc | float | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| PrintOriginalCount | int | YES |  |  |  |
| PrintCopyCount | int | YES |  |  |  |
| IsWFApproved | int | YES |  |  |  |
| WFApproveDesc | nvarchar | YES |  |  |  |
| ForeignCustomerDiscountPerc | float | YES |  |  |  |
| ForeignCustomerDiscountAmount | float | YES |  |  |  |
| ForeignDiscountAmount | float | YES |  |  |  |
| ForeignDiscountPercent | float | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| Manual_Disc | float | YES |  |  |  |
| DocType | smallint | YES |  |  |  |
| ExtraNotes | varchar | YES |  |  |  |
## Primary Key
CompNo
VouYear
VouNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_ReturnOrderHF_CheckExist]]
- [[OT_ReturnOrderHF_Insert]]

**Writes (1):**
- [[OT_ReturnOrderHF_Insert]]

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
