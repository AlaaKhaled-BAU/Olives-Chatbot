---
type: procedure
database: OSFA_DB
name: OT_CopySystemOption
schema: dbo
tags: [#mobile]
reads_from:
  - [[CopySystemOptions]]
  - Cur_Op_ID
  - [[OT_SystemOptions]]
  - cur_Salesman
writes_to:
  - [[OT_SystemOptions]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_CopySystemOption


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads CopySystemOptions, Cur_Op_ID, OT_SystemOptions, cur_Salesman. Writes OT_SystemOptions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromSalesman int
- @ToSalesman int
- @AllSysOp bit = 0
## Tables Read
- [[CopySystemOptions]]
- Cur_Op_ID
- [[OT_SystemOptions]]
- cur_Salesman
## Tables Written
- [[OT_SystemOptions]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CopySystemOptions]]
- Cur_Op_ID
- [[OT_SystemOptions]]
- cur_Salesman

**Tables Written**
- [[OT_SystemOptions]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
