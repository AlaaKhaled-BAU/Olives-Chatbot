---
type: table
database: OSFA_DB
name: OT_InvoiceHF
schema: dbo
tags: [#billing, #mobile]
foreign_keys:
referenced_by:
  - [[ADNAN_osfa]]
  - [[A_UnpostedbyTransactionOSFA]]
  - [[OT_AutoStoreItemsQty]]
  - [[OT_InvoiceHF_CheckExist]]
  - [[OT_InvoiceHF_Insert]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Daily-Sales-Cycle
---
# OT_InvoiceHF



## Business Purpose


Header records for invoices created on Android tablets, synced to back-office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| VouType | smallint | NO | ✓ |  |  |
| VouYear | smallint | NO | ✓ |  |  |
| VouNo | int | NO | ✓ |  |  |
| SalesmanNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| StoreNo | int | YES |  |  |  |
| VouDate | smalldatetime | YES |  |  |  |
| CaCr | bit | YES |  |  |  |
| DocType | smallint | YES |  |  |  |
| DiscountAmount | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| GPSX | varchar | YES |  |  |  |
| GPSY | varchar | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
| Currency | smallint | YES |  |  |  |
| ExRate | float | YES |  |  |  |
| IsPosted | bit | NO |  |  |  |
| PrNo | int | YES |  |  |  |
| RouteID | int | YES |  |  |  |
| IsVoid | int | YES |  |  |  |
| CustomerName | varchar | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| BusUnitID | int | YES |  |  |  |
| PaymentType | int | YES |  |  |  |
| CustomerDiscountPerc | float | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| PrintOriginalCount | int | YES |  |  |  |
| PrintCopyCount | int | YES |  |  |  |
| IsWFApproved | bit | YES |  |  |  |
| WFApproveDesc | nvarchar | YES |  |  |  |
| IsCheckInvoice | bit | YES |  |  |  |
| ContractID | nvarchar | YES |  |  |  |
| ForeignCustomerDiscountPerc | float | YES |  |  |  |
| ForeignCustomerDiscountAmount | float | YES |  |  |  |
| ForeignDiscountAmount | float | YES |  |  |  |
| ForeignDiscountPercent | float | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| SalesmanStoreNo | int | YES |  |  |  |
| DetailCount | int | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| PayAmount_Curr1 | float | YES |  |  |  |
| PayAmount_Curr2 | float | YES |  |  |  |
| PatientName | varchar | YES |  |  |  |
| FileNo | varchar | YES |  |  |  |
| LocationLineID | int | YES |  |  |  |
| DeliveryOrderYear | smallint | YES |  |  |  |
| DeliveryOrderNo | int | YES |  |  |  |
| InvDueDays | int | YES |  |  |  |
| IsDirectOnline | bit | YES |  |  |  |
| Manual_Disc | float | YES |  |  |  |
| IsLoan | bit | YES |  |  |  |
| LoanApproveBy | nvarchar | YES |  |  |  |
| SalesmanStockYear | int | YES |  |  |  |
| SalesmanStockNo | int | YES |  |  |  |
| EINV_INV_UUID | uniqueidentifier | YES |  |  |  |
## Primary Key
CompNo
VouType
VouYear
VouNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (5):**
- [[ADNAN_osfa]]
- [[A_UnpostedbyTransactionOSFA]]
- [[OT_AutoStoreItemsQty]]
- [[OT_InvoiceHF_CheckExist]]
- [[OT_InvoiceHF_Insert]]

**Writes (1):**
- [[OT_InvoiceHF_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Orphan lines**: Detail rows without matching header — causes sync failures
- **Posting failure**: IsPosted flag stuck false — check ERP integration log
- **Duplicate vouchers**: Same VouNo generated for different transactions — run dedup check
- **Currency mismatch**: ExRate different from CurrenciesRate table — financial reconciliation off
- **Void inconsistency**: IsVoid flag but original transaction still active — check WF approval


## See also
- [[Olives_BO/Tables/TransactionsHeaders]] (Back Office counterpart table)
- [[Shared/Runbooks/Orphan-Records]]
- [[Shared/Runbooks/Sync-Conflict]]

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
