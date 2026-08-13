---
type: procedure
database: OSFA_DB
name: OT_AutoRefreshCustomerInfo
schema: dbo
tags: [#customer, #mobile]
reads_from:
  - DBO
  - [[OT_ActionLog]]
  - [[OT_CustomerMF]]
writes_to:
  - [[OT_ActionLog]]
  - [[OT_CustomerMF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_AutoRefreshCustomerInfo


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads DBO, OT_ActionLog, OT_CustomerMF. Writes OT_ActionLog, OT_CustomerMF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesmanNo int
- @CustomerNo bigint
## Tables Read
- DBO
- [[OT_ActionLog]]
- [[OT_CustomerMF]]
## Tables Written
- [[OT_ActionLog]]
- [[OT_CustomerMF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- DBO
- [[OT_ActionLog]]
- [[OT_CustomerMF]]

**Tables Written**
- [[OT_ActionLog]]
- [[OT_CustomerMF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
