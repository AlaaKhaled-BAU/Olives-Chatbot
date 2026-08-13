---
type: procedure
database: OSFA_DB
name: OT_UpdateSalesmanKPI
schema: dbo
tags: [#mobile, #sales]
reads_from:
  - [[OT_SalesmanMF]]
  - `dbo`
writes_to:
  - [[OT_SalesmanMF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_UpdateSalesmanKPI


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_SalesmanMF, dbo. Writes OT_SalesmanMF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesmanNo int
- @FromDate smalldatetime
- @ToDate smalldatetime
## Tables Read
- [[OT_SalesmanMF]]
- `dbo`
## Tables Written
- [[OT_SalesmanMF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_SalesmanMF]]
- dbo

**Tables Written**
- [[OT_SalesmanMF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
