---
type: table
database: OSFA_DB
name: OT_OrderHF
schema: dbo
tags: [#mobile, #order]
foreign_keys:
referenced_by:
  - [[ADNAN_osfa]]
  - [[A_UnpostedbyTransactionOSFA]]
  - [[OT_AutoStoreItemsQty]]
  - [[OT_OrderHF_CheckExist]]
  - [[OT_OrderHF_Insert]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Daily-Sales-Cycle
---
# OT_OrderHF



## Business Purpose


Header records for sales orders created on Android tablets.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| OrderDate | smalldatetime | YES |  |  |  |
| SalesmanNo | smallint | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| CheckInTime | smalldatetime | YES |  |  |  |
| PromisesDate | smalldatetime | YES |  |  |  |
| Posted | bit | NO |  |  |  |
| VouDisc | float | YES |  |  |  |
| VouDiscPer | float | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
| BusUnitID | int | YES |  |  |  |
| StoreNo | int | YES |  |  |  |
| DocType | smallint | YES |  |  |  |
| CustomerName | varchar | YES |  |  |  |
| GPSX | varchar | YES |  |  |  |
| GPSY | varchar | YES |  |  |  |
| PrNo | smallint | YES |  |  |  |
| RouteID | int | YES |  |  |  |
| PaymentType | smallint | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| CustomerDiscountPerc | float | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| IsVoid | int | YES |  |  |  |
| PrintOriginalCount | int | YES |  |  |  |
| PrintCopyCount | int | YES |  |  |  |
| ContractID | nvarchar | YES |  |  |  |
| ForeignCustomerDiscountPerc | float | YES |  |  |  |
| ForeignCustomerDiscountAmount | float | YES |  |  |  |
| Currency | int | YES |  |  |  |
| ExRate | float | YES |  |  |  |
| ForeignDiscountAmount | float | YES |  |  |  |
| ForeignDiscountPercent | float | YES |  |  |  |
| CaCr | smallint | YES |  |  |  |
| DetailCount | int | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| ExtraNote | nvarchar | YES |  |  |  |
| Manual_Disc | float | YES |  |  |  |
| BackOrderYear | smallint | YES |  |  |  |
| BackOrderNo | bigint | YES |  |  |  |
| MakeCashDiscount | bit | YES |  |  |  |
| QuotationYear | smallint | YES |  |  |  |
| QuotationNo | int | YES |  |  |  |
| NeedApproval | bit | YES |  |  |  |
| TransFees | float | YES |  |  |  |
## Primary Key
CompNo
OrderYear
OrderNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (5):**
- [[ADNAN_osfa]]
- [[A_UnpostedbyTransactionOSFA]]
- [[OT_AutoStoreItemsQty]]
- [[OT_OrderHF_CheckExist]]
- [[OT_OrderHF_Insert]]

**Writes (1):**
- [[OT_OrderHF_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
