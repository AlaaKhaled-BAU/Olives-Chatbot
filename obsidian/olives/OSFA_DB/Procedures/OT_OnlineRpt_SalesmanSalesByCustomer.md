---
type: procedure
database: OSFA_DB
name: OT_OnlineRpt_SalesmanSalesByCustomer
schema: dbo
tags: [#customer, #integration, #mobile, #reporting, #sales]
reads_from:
  - `dbo`
  - olives_BO
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_OnlineRpt_SalesmanSalesByCustomer


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads dbo, olives_BO. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesmanNo int
- @FromDate smallDateTime
- @ToDate smallDateTime
## Tables Read
- `dbo`
- olives_BO
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- dbo
- olives_BO

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

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
