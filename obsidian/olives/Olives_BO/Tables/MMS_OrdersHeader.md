---
type: table
database: Olives_BO
name: MMS_OrdersHeader
schema: dbo
tags: [#backoffice, #mms, #order]
foreign_keys:
referenced_by:
  - [[Pro_MMS_InvoicesHeaders]]
  - [[Pro_MMS_OrderAssignLog]]
  - [[Pro_MMS_OrderDetails]]
  - [[Pro_MMS_OrderDetailsForVisit]]
  - [[Pro_MMS_OrdersHeader]]
  - [[Pro_MMS_PaymentsHeader]]
  - [[Pro_MMS_ScheduleSupportVisits]]
  - [[Rpt_PrintInvoices]]
  - [[Rpt_TechnicianSatement]]
  - [[Rpt_TechnicianSummary]]
  - [[Rpt_TechnicianVisitDetails]]
support_relevance: high
last_verified: 2026-07-05
---
# MMS_OrdersHeader


## Business Purpose

Maintenance management data — technician, order, and visit records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO |  |  |  |
| OrderAutoID | numeric | YES | ✓ |  |  |
| OrderYear | smallint | YES |  |  |  |
| OrderNo | bigint | YES |  |  |  |
| OrderDate | smalldatetime | YES |  |  |  |
| CustomerID | numeric | YES |  |  |  |
| OrderTypeID | int | NO |  |  |  |
| TaxTypeID | int | YES |  |  |  |
| ReporterID | int | YES |  |  |  |
| ShowRoom | nvarchar | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| UserID | nvarchar | YES |  |  |  |
| OrderStatus | int | YES |  |  |  |
| CallCenterID | int | YES |  |  |  |
| EnteryDateTime | smalldatetime | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
## Primary Key
OrderAutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (11):**
- [[Pro_MMS_InvoicesHeaders]]
- [[Pro_MMS_OrderAssignLog]]
- [[Pro_MMS_OrderDetails]]
- [[Pro_MMS_OrderDetailsForVisit]]
- [[Pro_MMS_OrdersHeader]]
- [[Pro_MMS_PaymentsHeader]]
- [[Pro_MMS_ScheduleSupportVisits]]
- [[Rpt_PrintInvoices]]
- [[Rpt_TechnicianSatement]]
- [[Rpt_TechnicianSummary]]
- [[Rpt_TechnicianVisitDetails]]

**Writes (1):**
- [[Pro_MMS_OrdersHeader]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Olives_BO/Procedures/Rpt_VoidOrder]]
