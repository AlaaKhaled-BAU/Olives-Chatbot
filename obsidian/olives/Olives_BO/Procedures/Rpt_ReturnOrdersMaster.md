---
type: procedure
database: Olives_BO
name: Rpt_ReturnOrdersMaster
schema: dbo
tags: [#backoffice, #order, #reporting]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - Fun_GetCompanyBranchesByUser
  - Fun_GetRetOrdersInvoiceNo
  - [[Items]]
  - [[ItemsUnits]]
  - [[RequestToExceedCustomerInvoiceDueDays]]
  - [[ReturnOrdersDetails]]
  - [[ReturnOrdersHeaders]]
  - [[SalesPersons]]
  - [[WF_SubLog]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_ReturnOrdersMaster


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, Fun_GetCompanyBranchesByUser, Fun_GetRetOrdersInvoiceNo, Items, ItemsUnits, RequestToExceedCustomerInvoiceDueDays, ReturnOrdersDetails, ReturnOrdersHeaders, SalesPersons, WF_SubLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromOrdNo bigint
- @ToOrdNo bigint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromSalesman int
- @ToSalesman int
- @UserID nvarchar(50)=null
- @InvType smallint = -1
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- Fun_GetCompanyBranchesByUser
- Fun_GetRetOrdersInvoiceNo
- [[Items]]
- [[ItemsUnits]]
- [[RequestToExceedCustomerInvoiceDueDays]]
- [[ReturnOrdersDetails]]
- [[ReturnOrdersHeaders]]
- [[SalesPersons]]
- [[WF_SubLog]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- Fun_GetCompanyBranchesByUser
- Fun_GetRetOrdersInvoiceNo
- [[Items]]
- [[ItemsUnits]]
- [[RequestToExceedCustomerInvoiceDueDays]]
- [[ReturnOrdersDetails]]
- [[ReturnOrdersHeaders]]
- [[SalesPersons]]
- [[WF_SubLog]]

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
