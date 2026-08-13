---
type: procedure
database: Olives_BO
name: Alpha_InvoiceDeliveryHF_BD
schema: dbo
tags: [#backoffice, #billing, #order]
reads_from:
  - [[Customers]]
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
  - [[Items]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Alpha_InvoiceDeliveryHF_BD


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, InvoiceDeliveryDF, InvoiceDeliveryHF, Items, SalesPersons, dbo. Writes InvoiceDeliveryDF, InvoiceDeliveryHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Customers]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Items]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Items]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
