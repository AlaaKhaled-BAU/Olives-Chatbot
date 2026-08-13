---
type: procedure
database: OSFA_DB
name: OT_Online_RptSalesmenVisitSummary
schema: dbo
tags: [#mobile, #sales]
reads_from:
  - Olives_BO
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Online_RptSalesmenVisitSummary


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads Olives_BO, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=1
- @SalesmanNo int=3003
## Tables Read
- Olives_BO
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Olives_BO
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

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
