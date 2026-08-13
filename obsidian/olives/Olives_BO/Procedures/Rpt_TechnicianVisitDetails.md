---
type: procedure
database: Olives_BO
name: Rpt_TechnicianVisitDetails
schema: dbo
tags: [#backoffice, #mms, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[MMS_DevicesInfo]]
  - [[MMS_InvoiceDetails]]
  - [[MMS_InvoicesHeaders]]
  - [[MMS_Items]]
  - [[MMS_MaintenanceTechnician]]
  - [[MMS_OrderStatus]]
  - [[MMS_OrderVisits]]
  - [[MMS_OrdersHeader]]
  - [[MMS_ScheduleSupportVisits]]
  - [[SystemCodes]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_TechnicianVisitDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, MMS_DevicesInfo, MMS_InvoiceDetails, MMS_InvoicesHeaders, MMS_Items, MMS_MaintenanceTechnician, MMS_OrderStatus, MMS_OrderVisits, MMS_OrdersHeader, MMS_ScheduleSupportVisits, SystemCodes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = null
- @FromTechnician int = null
- @ToTechnician int = null
- @FromDate smalldatetime = null
- @ToDate smalldatetime = null
## Tables Read
- [[Customers]]
- [[MMS_DevicesInfo]]
- [[MMS_InvoiceDetails]]
- [[MMS_InvoicesHeaders]]
- [[MMS_Items]]
- [[MMS_MaintenanceTechnician]]
- [[MMS_OrderStatus]]
- [[MMS_OrderVisits]]
- [[MMS_OrdersHeader]]
- [[MMS_ScheduleSupportVisits]]
- [[SystemCodes]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[MMS_DevicesInfo]]
- [[MMS_InvoiceDetails]]
- [[MMS_InvoicesHeaders]]
- [[MMS_Items]]
- [[MMS_MaintenanceTechnician]]
- [[MMS_OrderStatus]]
- [[MMS_OrderVisits]]
- [[MMS_OrdersHeader]]
- [[MMS_ScheduleSupportVisits]]
- [[SystemCodes]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
