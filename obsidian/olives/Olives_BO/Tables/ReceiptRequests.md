---
type: table
database: Olives_BO
name: ReceiptRequests
schema: dbo
tags: [#backoffice, #billing]
foreign_keys:
referenced_by:
  - [[OT_ImportReceipts]]
  - [[PRO_GETRECEIPTSFOREMAIL]]
  - [[Pro_ReceiptRequests]]
  - [[Pro_ReceiptRequestsSchedule]]
  - [[Rpt_UsersKPI]]
support_relevance: high
last_verified: 2026-07-05
---
# ReceiptRequests


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores receiptrequests records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| OrderDate | smalldatetime | YES |  |  |  |
| CustomerID | bigint | YES |  |  |  |
| Amount | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| OrderStatus | int | YES |  |  |  |
| PaymentType | int | YES |  |  |  |
| IsSettlement | bit | YES |  |  |  |
| Priority | bit | YES |  |  |  |
| CreatedBy | nvarchar | YES |  |  |  |
| CreatedDate | smalldatetime | YES |  |  |  |
| DocumentTypeID | int | YES |  |  |  |
## Primary Key
CompanyID
OrderYear
OrderNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (4):**
- [[PRO_GETRECEIPTSFOREMAIL]]
- [[Pro_ReceiptRequests]]
- [[Pro_ReceiptRequestsSchedule]]
- [[Rpt_UsersKPI]]

**Writes (3):**
- [[OT_ImportReceipts]]
- [[Pro_ReceiptRequests]]
- [[Pro_ReceiptRequestsSchedule]]

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
