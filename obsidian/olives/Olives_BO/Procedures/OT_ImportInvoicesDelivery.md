---
type: procedure
database: Olives_BO
name: OT_ImportInvoicesDelivery
schema: dbo
tags: [#backoffice, #billing, #mobile, #order]
reads_from:
  - [[Customers]]
  - [[InvoiceDeliveryHF]]
  - [[SalespersonsMessages]]
  - `dbo`
writes_to:
  - [[InvoiceDeliveryHF]]
  - [[OT_InvoicesDelivery]]
  - [[SalespersonsMessages]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportInvoicesDelivery


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, InvoiceDeliveryHF, SalespersonsMessages, dbo. Writes InvoiceDeliveryHF, OT_InvoicesDelivery, SalespersonsMessages. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[Customers]]
- [[InvoiceDeliveryHF]]
- [[SalespersonsMessages]]
- `dbo`
## Tables Written
- [[InvoiceDeliveryHF]]
- [[OT_InvoicesDelivery]]
- [[SalespersonsMessages]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[InvoiceDeliveryHF]]
- [[SalespersonsMessages]]
- dbo

**Tables Written**
- [[InvoiceDeliveryHF]]
- [[OT_InvoicesDelivery]]
- [[SalespersonsMessages]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
