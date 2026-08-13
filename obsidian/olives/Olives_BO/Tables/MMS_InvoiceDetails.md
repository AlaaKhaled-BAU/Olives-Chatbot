---
type: table
database: Olives_BO
name: MMS_InvoiceDetails
schema: dbo
tags: [#backoffice, #billing, #mms]
foreign_keys:
referenced_by:
  - [[Pro_MMS_InvoiceDetails]]
  - [[Pro_MMS_SetDataForAndroid]]
  - [[Rpt_PrintInvoices]]
  - [[Rpt_TechnicianVisitDetails]]
support_relevance: high
last_verified: 2026-07-05
---
# MMS_InvoiceDetails


## Business Purpose

Maintenance management data — technician, order, and visit records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| InvoiceYear | smallint | NO | ✓ |  |  |
| InvoiceNo | bigint | NO | ✓ |  |  |
| LineID | int | NO | ✓ |  |  |
| ItemNo | nvarchar | YES | ✓ |  |  |
| Qty | money | YES |  |  |  |
| UnitPrice | float | YES |  |  |  |
| Price | float | YES |  |  |  |
| TaxPercent | float | YES |  |  |  |
| TaxValue | float | YES |  |  |  |
| ItemDiscountPercent | float | YES |  |  |  |
| ItemDiscountValue | float | YES |  |  |  |
| InvoiceDiscountValue | float | YES |  |  |  |
| IsInWarranty | bit | YES |  |  |  |
## Primary Key
CompanyID
InvoiceYear
InvoiceNo
LineID
ItemNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (4):**
- [[Pro_MMS_InvoiceDetails]]
- [[Pro_MMS_SetDataForAndroid]]
- [[Rpt_PrintInvoices]]
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
