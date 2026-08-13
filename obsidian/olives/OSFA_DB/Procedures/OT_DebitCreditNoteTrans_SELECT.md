---
type: procedure
database: OSFA_DB
name: OT_DebitCreditNoteTrans_SELECT
schema: dbo
tags: [#billing, #mobile]
reads_from:
  - [[OT_DebitCreditNoteTrans]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_DebitCreditNoteTrans_SELECT


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_DebitCreditNoteTrans. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @SalesmanNo  int=3003
- @CompNo smallint =1
## Tables Read
- [[OT_DebitCreditNoteTrans]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_DebitCreditNoteTrans]]

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
