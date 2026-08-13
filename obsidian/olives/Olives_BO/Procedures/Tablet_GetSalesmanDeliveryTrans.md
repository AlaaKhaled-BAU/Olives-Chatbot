---
type: procedure
database: Olives_BO
name: Tablet_GetSalesmanDeliveryTrans
schema: dbo
tags: [#backoffice, #mobile, #order, #sales]
reads_from:
  - [[ClientsActive]]
  - [[DeliveryManifest]]
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
  - Olives_BO
  - [[SalesPersons]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Tablet_GetSalesmanDeliveryTrans


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, DeliveryManifest, InvoiceDeliveryDF, InvoiceDeliveryHF, Olives_BO, SalesPersons, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1
- @SalesmanNo int =3003
- @CustomerNo bigint=314
- @Header bit=1
## Tables Read
- [[ClientsActive]]
- [[DeliveryManifest]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- Olives_BO
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
- [[ClientsActive]]
- [[DeliveryManifest]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- Olives_BO
- [[SalesPersons]]
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
