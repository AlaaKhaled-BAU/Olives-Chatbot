---
type: procedure
database: Olives_BO
name: Rpt_InvoicesDelivery
schema: dbo
tags: [#backoffice, #billing, #order, #reporting]
reads_from:
  - [[Customers]]
  - [[DeliveryCars]]
  - [[DeliveryManifest]]
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
  - [[SalesPersons]]
  - TransactionsHeaders_Type
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_InvoicesDelivery


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, DeliveryCars, DeliveryManifest, InvoiceDeliveryDF, InvoiceDeliveryHF, SalesPersons, TransactionsHeaders_Type. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @ManifestID INT=NULL
- @HostNamee varchar(100)=HOST_NAME
## Tables Read
- [[Customers]]
- [[DeliveryCars]]
- [[DeliveryManifest]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[SalesPersons]]
- TransactionsHeaders_Type
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[DeliveryCars]]
- [[DeliveryManifest]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[SalesPersons]]
- TransactionsHeaders_Type

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
