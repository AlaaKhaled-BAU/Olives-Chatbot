---
type: procedure
database: OSFA_DB
name: OT_LockStock
schema: dbo
tags: [#inventory, #mobile]
reads_from:
  - `dbo`
writes_to:
  - [[SalesPersons]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_LockStock


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads dbo. Writes SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesmanNo smallint
## Tables Read
- `dbo`
## Tables Written
- [[SalesPersons]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- dbo

**Tables Written**
- [[SalesPersons]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
