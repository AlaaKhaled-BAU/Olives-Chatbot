---
type: procedure
database: Olives_BO
name: Galaxy_Integration_GetItemBalance
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - [[Customers]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[OT_CreditInvoiceList]]
  - [[OT_StoreItemsQty]]
  - [[SalesPersons]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Galaxy_Integration_GetItemBalance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, SalesPersons, dbo. Writes OT_CreditInvoiceList, OT_StoreItemsQty, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
- @SalesmanNo int = 1
- @SendDate smalldatetime = null
- @SendCompanyData bit = 1
## Tables Read
- [[Customers]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[OT_CreditInvoiceList]]
- [[OT_StoreItemsQty]]
- [[SalesPersons]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[OT_CreditInvoiceList]]
- [[OT_StoreItemsQty]]
- [[SalesPersons]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pulling data from an external API/system. Called during sync cycles or on-demand data refresh.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
