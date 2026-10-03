---
type: table
database: Olives_BO
name: InvoiceReturnLink
schema: dbo
tags: [#backoffice, #billing, #order]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[ItemsUnits]]
referenced_by:
  - [[OT_ImportInvoiceReturnLink]]
  - [[Pro_JoTaxApi]]
  - [[Pro_JoTaxApiFromOSFA]]
  - [[Pro_JoTaxApiFromOSFA____]]
support_relevance: high
last_verified: 2026-07-05
---
# InvoiceReturnLink


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores invoicereturnlink records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[ItemsUnits]] |
| RetVouType | smallint | NO | ✓ |  |  |
| RetVouYear | smallint | NO | ✓ |  |  |
| RetVouNo | int | NO | ✓ |  |  |
| InvVouType | smallint | NO | ✓ |  |  |
| InvVouYear | smallint | NO | ✓ |  |  |
| InvVouNo | int | NO | ✓ |  |  |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| UnitID | nvarchar | YES | ✓ | ✓ | [[ItemsUnits]] |
| Qty | money | YES |  |  |  |
| Bonus | money | YES |  |  |  |
| UnitPrice | float | YES |  |  |  |
## Primary Key
CompanyID
RetVouType
RetVouYear
RetVouNo
InvVouType
InvVouYear
InvVouNo
ItemCode
UnitID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, UnitID -> [[ItemsUnits]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (8):**
- [[OT_ImportInvoiceReturnLink]]
- [[Pro_JoTaxApi]]
- [[Pro_JoTaxApiFromOSFA]]
- [[Pro_JoTaxApiFromOSFA____]]

**Writes (1):**
- [[OT_ImportInvoiceReturnLink]]

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
