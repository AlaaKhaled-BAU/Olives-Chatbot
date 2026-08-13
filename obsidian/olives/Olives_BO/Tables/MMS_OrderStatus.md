---
type: table
database: Olives_BO
name: MMS_OrderStatus
schema: dbo
tags: [#backoffice, #mms, #order]
foreign_keys:
referenced_by:
  - [[Pro_MMS_OrderDetailsForVisit]]
  - [[Pro_MMS_OrderStatus]]
  - [[Pro_MMS_ScheduleSupportVisits]]
  - [[Rpt_TechnicianSummary]]
  - [[Rpt_TechnicianVisitDetails]]
support_relevance: high
last_verified: 2026-07-05
---
# MMS_OrderStatus


## Business Purpose

Maintenance management data — technician, order, and visit records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| OrderStatusID | int | NO | ✓ |  |  |
| OrderStatusDesc | varchar | YES |  |  |  |
| OrderStatusForeignDesc | varchar | YES |  |  |  |
| UseInDevice | bit | YES |  |  |  |
| NeedReason | int | YES |  |  |  |
## Primary Key
OrderStatusID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (5):**
- [[Pro_MMS_OrderDetailsForVisit]]
- [[Pro_MMS_OrderStatus]]
- [[Pro_MMS_ScheduleSupportVisits]]
- [[Rpt_TechnicianSummary]]
- [[Rpt_TechnicianVisitDetails]]

**Writes (0):**
_None_

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
