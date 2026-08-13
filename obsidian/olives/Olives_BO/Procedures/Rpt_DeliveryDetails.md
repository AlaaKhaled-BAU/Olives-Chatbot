---
type: procedure
database: Olives_BO
name: Rpt_DeliveryDetails
schema: dbo
tags: [#backoffice, #order, #reporting]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[InvoiceDeliveryHF]]
  - [[PaymentsTypes]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_DeliveryDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, InvoiceDeliveryHF, PaymentsTypes, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromSalesman int=0
- @ToSalesman int=9999999
- @FromDate smalldatetime='2020-01-01'
- @ToDate smalldatetime ='2025-01-01'
- @FromCust bigint = 0
- @Tocust bigint = 9999999
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[InvoiceDeliveryHF]]
- [[PaymentsTypes]]
- [[SalesPersons]]
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
- [[InvoiceDeliveryHF]]
- [[PaymentsTypes]]
- [[SalesPersons]]

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
