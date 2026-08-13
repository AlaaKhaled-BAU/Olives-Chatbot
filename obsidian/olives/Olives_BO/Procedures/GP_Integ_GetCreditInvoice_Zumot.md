---
type: procedure
database: Olives_BO
name: GP_Integ_GetCreditInvoice_Zumot
schema: dbo
tags: [#backoffice, #billing, #integration]
reads_from:
  - 168
  - [[CustomerPaidTrans_FormERP]]
  - [[Customers]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# GP_Integ_GetCreditInvoice_Zumot


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads 168, CustomerPaidTrans_FormERP, Customers, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
- @SalesmanNo int
## Tables Read
- 168
- [[CustomerPaidTrans_FormERP]]
- [[Customers]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- 168
- [[CustomerPaidTrans_FormERP]]
- [[Customers]]
- dbo

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pulling data from an external API/system. Called during sync cycles or on-demand data refresh.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
