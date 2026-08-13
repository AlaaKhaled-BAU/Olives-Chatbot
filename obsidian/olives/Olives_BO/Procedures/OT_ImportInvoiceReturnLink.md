---
type: procedure
database: Olives_BO
name: OT_ImportInvoiceReturnLink
schema: dbo
tags: [#backoffice, #billing, #mobile, #order]
reads_from:
  - [[InvoiceReturnLink]]
  - `dbo`
writes_to:
  - [[InvoiceReturnLink]]
  - [[OT_InvoiceReturnLink]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportInvoiceReturnLink


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads InvoiceReturnLink, dbo. Writes InvoiceReturnLink, OT_InvoiceReturnLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[InvoiceReturnLink]]
- `dbo`
## Tables Written
- [[InvoiceReturnLink]]
- [[OT_InvoiceReturnLink]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[InvoiceReturnLink]]
- dbo

**Tables Written**
- [[InvoiceReturnLink]]
- [[OT_InvoiceReturnLink]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
