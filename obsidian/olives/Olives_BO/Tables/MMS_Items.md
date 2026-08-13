---
type: table
database: Olives_BO
name: MMS_Items
schema: dbo
tags: [#backoffice, #inventory, #mms]
foreign_keys:
referenced_by:
  - [[Pro_MMS_GetDataForAndroid]]
  - [[Pro_MMS_InvoiceDetails]]
  - [[Pro_MMS_Items]]
  - [[Pro_MMS_TechnicianStock]]
  - [[Rpt_PrintInvoices]]
  - [[Rpt_TechnicianVisitDetails]]
support_relevance: high
last_verified: 2026-07-05
---
# MMS_Items


## Business Purpose

Maintenance management data — technician, order, and visit records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| ItemNo | nvarchar | YES | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ForeignName | nvarchar | YES |  |  |  |
| ItemType | int | YES |  |  |  |
| CategoryID | int | YES |  |  |  |
| UnitPrice | float | YES |  |  |  |
| Barcode | nvarchar | YES |  |  |  |
| IsRequiredBarcode | bit | YES |  |  |  |
| IsRequiredSerialNo | bit | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
| IsInWarranty | bit | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
ItemNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (6):**
- [[Pro_MMS_GetDataForAndroid]]
- [[Pro_MMS_InvoiceDetails]]
- [[Pro_MMS_Items]]
- [[Pro_MMS_TechnicianStock]]
- [[Rpt_PrintInvoices]]
- [[Rpt_TechnicianVisitDetails]]

**Writes (1):**
- [[Pro_MMS_Items]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Duplicate barcodes**: Multiple items sharing same barcode — POS picks wrong item
- **Price mismatch**: Sell price in Items differs from PriceListDetails — customer charged wrong amount
- **Stock discrepancy**: QtyInAllStores differs from sum of StoreBalances — run CALCITEMBALANCE
- **Missing units**: Item has no valid ItemUnits — cannot be sold
- **Tax config wrong**: IsTaxExempt flag incorrect — ZATCA/legal reporting mismatch

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
