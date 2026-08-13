---
type: table
database: Olives_BO
name: MMS_InvoicesHeaders
schema: dbo
tags: [#backoffice, #billing, #mms]
foreign_keys:
referenced_by:
  - [[Pro_MMS_GetDataForAndroid]]
  - [[Pro_MMS_InvoicesHeaders]]
  - [[Pro_MMS_SetDataForAndroid]]
  - [[Rpt_PrintInvoices]]
  - [[Rpt_TechnicianSatement]]
  - [[Rpt_TechnicianVisitDetails]]
support_relevance: high
last_verified: 2026-07-05
---
# MMS_InvoicesHeaders


## Business Purpose

Maintenance management data — technician, order, and visit records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| InvoiceYear | smallint | NO | ✓ |  |  |
| InvoiceNo | bigint | NO | ✓ |  |  |
| InvoiceDate | smalldatetime | YES |  |  |  |
| InvoiceDiscountPercent | float | YES |  |  |  |
| TotalInvoiceDiscountValue | float | YES |  |  |  |
| TotalItemDiscountValue | float | YES |  |  |  |
| TotalTaxValue | float | YES |  |  |  |
| TotalPrice | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| OrderAutoID | numeric | YES |  |  |  |
| OrderSubID | int | YES |  |  |  |
| ScheduleID | int | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| InvType | int | YES |  |  |  |
| DetailCount | int | YES |  |  |  |
| IsNewSerial | bit | YES |  |  |  |
## Primary Key
CompanyID
InvoiceYear
InvoiceNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (6):**
- [[Pro_MMS_GetDataForAndroid]]
- [[Pro_MMS_InvoicesHeaders]]
- [[Pro_MMS_SetDataForAndroid]]
- [[Rpt_PrintInvoices]]
- [[Rpt_TechnicianSatement]]
- [[Rpt_TechnicianVisitDetails]]

**Writes (1):**
- [[Pro_MMS_SetDataForAndroid]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Orphan lines**: Detail rows without matching header — causes sync failures
- **Posting failure**: IsPosted flag stuck false — check ERP integration log
- **Duplicate vouchers**: Same VouNo generated for different transactions — run dedup check
- **Currency mismatch**: ExRate different from CurrenciesRate table — financial reconciliation off
- **Void inconsistency**: IsVoid flag but original transaction still active — check WF approval

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
