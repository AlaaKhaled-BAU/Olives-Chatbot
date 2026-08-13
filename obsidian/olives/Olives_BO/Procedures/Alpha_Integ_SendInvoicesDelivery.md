---
type: procedure
database: Olives_BO
name: Alpha_Integ_SendInvoicesDelivery
schema: dbo
tags: [#backoffice, #billing, #integration, #order]
reads_from:
  - [[ClientsActive]]
  - [[InvoiceDeliveryHF]]
  - `dbo`
writes_to:
  - [[InvoiceDeliveryHF]]
  - [[OT_InvoicesDelivery]]
  - Sales_InvoicesDelivery
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Alpha_Integ_SendInvoicesDelivery


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, InvoiceDeliveryHF, dbo. Writes InvoiceDeliveryHF, OT_InvoicesDelivery, Sales_InvoicesDelivery. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[ClientsActive]]
- [[InvoiceDeliveryHF]]
- `dbo`
## Tables Written
- [[InvoiceDeliveryHF]]
- [[OT_InvoicesDelivery]]
- Sales_InvoicesDelivery
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[InvoiceDeliveryHF]]
- dbo

**Tables Written**
- [[InvoiceDeliveryHF]]
- [[OT_InvoicesDelivery]]
- Sales_InvoicesDelivery

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
