---
type: procedure
database: Olives_BO
name: Rpt_PrintInvoices
schema: dbo
tags: [#backoffice, #billing, #reporting]
reads_from:
  - [[Companies]]
  - [[Customers]]
  - [[MMS_InvoiceDetails]]
  - [[MMS_InvoicesHeaders]]
  - [[MMS_Items]]
  - [[MMS_MaintenanceTechnician]]
  - [[MMS_OrdersHeader]]
  - [[MMS_ScheduleSupportVisits]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_PrintInvoices


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, Customers, MMS_InvoiceDetails, MMS_InvoicesHeaders, MMS_Items, MMS_MaintenanceTechnician, MMS_OrdersHeader, MMS_ScheduleSupportVisits. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = null
- @FromDate smalldatetime = null
- @ToDate smalldatetime = null
- @FromCustomerID numeric(20 ,0) = null
- @ToCustomerID numeric(20 ,0) = null
- @FromInvNo numeric(20 ,0) = null
- @ToInvNo numeric(20 ,0) = null
- @InvType int = null
## Tables Read
- [[Companies]]
- [[Customers]]
- [[MMS_InvoiceDetails]]
- [[MMS_InvoicesHeaders]]
- [[MMS_Items]]
- [[MMS_MaintenanceTechnician]]
- [[MMS_OrdersHeader]]
- [[MMS_ScheduleSupportVisits]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Companies]]
- [[Customers]]
- [[MMS_InvoiceDetails]]
- [[MMS_InvoicesHeaders]]
- [[MMS_Items]]
- [[MMS_MaintenanceTechnician]]
- [[MMS_OrdersHeader]]
- [[MMS_ScheduleSupportVisits]]

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
