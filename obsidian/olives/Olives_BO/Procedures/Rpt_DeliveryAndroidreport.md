---
type: procedure
database: Olives_BO
name: Rpt_DeliveryAndroidreport
schema: dbo
tags: [#backoffice, #mobile, #order, #reporting]
reads_from:
  - [[Customers]]
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
  - [[LogActionTransaction]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_DeliveryAndroidreport


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, InvoiceDeliveryDF, InvoiceDeliveryHF, LogActionTransaction, SalesPersons, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromDate smalldatetime='2018-01-01'
- @ToDate smalldatetime='2021-09-01'
- @cmdType varchar(500)='GetInvocieDeliveryStatus'
- @DeliveredSalesmanNo int =0
## Tables Read
- [[Customers]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[LogActionTransaction]]
- [[SalesPersons]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[LogActionTransaction]]
- [[SalesPersons]]
- dbo

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
