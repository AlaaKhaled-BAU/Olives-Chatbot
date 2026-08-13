---
type: procedure
database: Olives_BO
name: Rpt_DriversDeliverySummary
schema: dbo
tags: [#backoffice, #order, #reporting]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[DeliveryManifest]]
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
  - [[Locations]]
  - [[NoTransactionsReasons]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_DriversDeliverySummary


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, DeliveryManifest, InvoiceDeliveryDF, InvoiceDeliveryHF, Locations, NoTransactionsReasons, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @IsDelivered smallint
- @FromManifest int
- @ToManifest int
- @FromDriver int
- @ToDriver int
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromAssistantID int= null
- @ToAssistantID int = null
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[DeliveryManifest]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Locations]]
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
- [[DeliveryManifest]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Locations]]
- [[NoTransactionsReasons]]
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
