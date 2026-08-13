---
type: procedure
database: Olives_BO
name: Online_RptInvoiceDeliveryByDriver
schema: dbo
tags: [#backoffice, #billing, #order]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
  - [[NoTransactionsReasons]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Online_RptInvoiceDeliveryByDriver


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, InvoiceDeliveryDF, InvoiceDeliveryHF, NoTransactionsReasons, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int=1
- @FromDate smalldatetime='2000-1-1'
- @ToDate smalldatetime='2025-1-1'
- @SalesmanNo int=3003
- @FromDriverNo int=0
- @ToDriverNo int=999999
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[NoTransactionsReasons]]
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
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[NoTransactionsReasons]]
- [[SalesPersons]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
