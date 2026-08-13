---
type: table
database: OSFA_DB
name: OT_SalesQuotationHF
schema: dbo
tags: [#mobile, #order, #sales]
foreign_keys:
referenced_by:
  - [[OT_SalesQuotationHF_CheckExist]]
  - [[OT_SalesQuotation_Insert]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Daily-Sales-Cycle
---
# OT_SalesQuotationHF



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| OrderDate | smalldatetime | YES |  |  |  |
| SalesmanNo | smallint | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| Posted | bit | NO |  |  |  |
| VouDisc | float | YES |  |  |  |
| VouDiscPer | float | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
| BusUnitID | int | YES |  |  |  |
| DocType | smallint | YES |  |  |  |
| CustomerName | varchar | YES |  |  |  |
| GPSX | varchar | YES |  |  |  |
| GPSY | varchar | YES |  |  |  |
| PrNo | smallint | YES |  |  |  |
| PaymentType | smallint | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| CustomerDiscountPerc | float | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| IsVoid | int | YES |  |  |  |
| PrintOriginalCount | int | YES |  |  |  |
| PrintCopyCount | int | YES |  |  |  |
| ForeignCustomerDiscountPerc | float | YES |  |  |  |
| ForeignCustomerDiscountAmount | float | YES |  |  |  |
| Currency | int | YES |  |  |  |
| ExRate | float | YES |  |  |  |
| ForeignDiscountAmount | float | YES |  |  |  |
| ForeignDiscountPercent | float | YES |  |  |  |
| CaCr | smallint | YES |  |  |  |
| DeliveryLocation | nvarchar | YES |  |  |  |
| PromisesDate | smalldatetime | YES |  |  |  |
| IsProspectiveCustomer | bit | YES |  |  |  |
| Manual_Disc | float | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| DeliveryDays | int | YES |  |  |  |
## Primary Key
CompNo
OrderYear
OrderNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_SalesQuotationHF_CheckExist]]
- [[OT_SalesQuotation_Insert]]

**Writes (1):**
- [[OT_SalesQuotation_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Sync conflict**: Same record modified on tablet and BO simultaneously — last-write-wins may lose data
- **Orphan tablet records**: Row with no linked BO counterpart — check sync log
- **Duplicate TabletSysID**: Same tablet transaction inserted twice — run dedup check
- **Missing IsPosted flag**: Data not synced to BO — check tablet connectivity

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
