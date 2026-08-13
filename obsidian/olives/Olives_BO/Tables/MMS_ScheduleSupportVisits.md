---
type: table
database: Olives_BO
name: MMS_ScheduleSupportVisits
schema: dbo
tags: [#backoffice, #mms, #sales]
foreign_keys:
referenced_by:
  - [[Pro_MMS_InvoicesHeaders]]
  - [[Pro_MMS_OrderAssignLog]]
  - [[Pro_MMS_OrderDetails]]
  - [[Pro_MMS_OrderDetailsForVisit]]
  - [[Pro_MMS_OrderVisits]]
  - [[Pro_MMS_PaymentsHeader]]
  - [[Pro_MMS_ScheduleSupportVisits]]
  - [[Pro_MMS_SetDataForAndroid]]
  - [[Rpt_PrintInvoices]]
  - [[Rpt_TechnicianSatement]]
  - [[Rpt_TechnicianSummary]]
  - [[Rpt_TechnicianVisitDetails]]
support_relevance: high
last_verified: 2026-07-05
---
# MMS_ScheduleSupportVisits


## Business Purpose

Maintenance management data — technician, order, and visit records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| OrderAutoID | numeric | YES | ✓ |  |  |
| OrderSubID | int | NO | ✓ |  |  |
| ScheduleID | int | NO | ✓ |  |  |
| SupervisorID | int | YES |  |  |  |
| TechnicianID | int | YES |  |  |  |
| ScheduleDateTime | smalldatetime | YES |  |  |  |
| AssigmentDateTime | smalldatetime | YES |  |  |  |
| Status | int | YES |  |  |  |
| VisitType | int | YES |  |  |  |
| AssistantsID | int | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
## Primary Key
CompanyID
OrderAutoID
OrderSubID
ScheduleID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (12):**
- [[Pro_MMS_InvoicesHeaders]]
- [[Pro_MMS_OrderAssignLog]]
- [[Pro_MMS_OrderDetails]]
- [[Pro_MMS_OrderDetailsForVisit]]
- [[Pro_MMS_OrderVisits]]
- [[Pro_MMS_PaymentsHeader]]
- [[Pro_MMS_ScheduleSupportVisits]]
- [[Pro_MMS_SetDataForAndroid]]
- [[Rpt_PrintInvoices]]
- [[Rpt_TechnicianSatement]]
- [[Rpt_TechnicianSummary]]
- [[Rpt_TechnicianVisitDetails]]

**Writes (2):**
- [[Pro_MMS_ScheduleSupportVisits]]
- [[Pro_MMS_SetDataForAndroid]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Visit not closed**: Support visit still open — technician forgot to close
- **Missing spare parts**: Maintenance order requires parts not in technician stock
- **Schedule conflict**: Multiple visits assigned same time slot — dispatch needs review

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
