---
type: procedure
database: Olives_BO
name: RptOnlineRpt_DeliveryInvoiceStoresQty
schema: dbo
tags: [#backoffice, #billing, #integration, #order, #reporting]
reads_from:
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
  - [[Items]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# RptOnlineRpt_DeliveryInvoiceStoresQty


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads InvoiceDeliveryDF, InvoiceDeliveryHF, Items, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
- @SalesmanNo int
## Tables Read
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Items]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Items]]
- dbo

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
