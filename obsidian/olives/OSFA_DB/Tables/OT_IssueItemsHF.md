---
type: table
database: OSFA_DB
name: OT_IssueItemsHF
schema: dbo
tags: [#inventory, #mobile]
foreign_keys:
referenced_by:
  - [[OT_IssueItemsHF_CheckExist]]
  - [[OT_IssueItemsHF_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_IssueItemsHF



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
## Primary Key
CompNo
OrderYear
OrderNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_IssueItemsHF_CheckExist]]
- [[OT_IssueItemsHF_Insert]]

**Writes (1):**
- [[OT_IssueItemsHF_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Duplicate barcodes**: Multiple items sharing same barcode — POS picks wrong item
- **Price mismatch**: Sell price in Items differs from PriceListDetails — customer charged wrong amount
- **Stock discrepancy**: QtyInAllStores differs from sum of StoreBalances — run CALCITEMBALANCE
- **Missing units**: Item has no valid ItemUnits — cannot be sold
- **Tax config wrong**: IsTaxExempt flag incorrect — ZATCA/legal reporting mismatch

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
