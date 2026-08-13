---
type: table
database: Olives_BO
name: ReceiptRequestsSchedule
schema: dbo
tags: [#backoffice, #billing]
foreign_keys:
referenced_by:
  - [[Pro_ReceiptRequests]]
  - [[Pro_ReceiptRequestsSchedule]]
support_relevance: high
last_verified: 2026-07-05
---
# ReceiptRequestsSchedule


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores receiptrequestsschedule records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| ScheduleID | int | NO | ✓ |  |  |
| SalesPersonID | int | YES |  |  |  |
| IsVoid | bit | YES |  |  |  |
| ScheduleDateTime | smalldatetime | YES |  |  |  |
| AssigmentDateTime | smalldatetime | YES |  |  |  |
## Primary Key
CompanyID
OrderYear
OrderNo
ScheduleID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_ReceiptRequests]]
- [[Pro_ReceiptRequestsSchedule]]

**Writes (1):**
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
