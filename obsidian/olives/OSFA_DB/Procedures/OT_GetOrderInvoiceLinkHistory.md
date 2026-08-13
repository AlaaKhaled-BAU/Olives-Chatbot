---
type: procedure
database: OSFA_DB
name: OT_GetOrderInvoiceLinkHistory
schema: dbo
tags: [#billing, #log, #mobile, #order]
reads_from:
  - Olives_BO
  - `dbo`
writes_to:
  - OrderInvoiceLinkHistory
called_by:
  - Alpha_Integration
support_relevance: high
last_verified: 2026-07-05
---
# OT_GetOrderInvoiceLinkHistory


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads Olives_BO, dbo. Writes OrderInvoiceLinkHistory. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesmanNo int
- @FromDate smallDateTime
- @ToDate smallDateTime
## Tables Read
- Olives_BO
- `dbo`
## Tables Written
- OrderInvoiceLinkHistory
## Callers
_None (no known callers)_
## Callees
- Alpha_Integration
## Impact / Dependencies

**Tables Read**
- Olives_BO
- dbo

**Tables Written**
- OrderInvoiceLinkHistory

**Callers**
- Alpha_Integration

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Cross-Database
Also exists in the other database: [[Olives_BO/Procedures/OT_GetOrderInvoiceLinkHistory]] (BO).

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
