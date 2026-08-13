---
type: procedure
database: Olives_BO
name: CopySystemOption
schema: dbo
tags: [#backoffice]
reads_from:
  - OSFA_DB
writes_to:
  - [[OT_SystemOptions]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# CopySystemOption


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads OSFA_DB. Writes OT_SystemOptions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @companyid int
- @SourceSalesManid int, /* المصدر*/
- @DistinationSalesMan int, /*   المستهدف*/
- @Op_ID int      /* 10,11,16,20,21,41,44,67,96,107,108,113,158,165,210,213 260,287,323,337,364 */
## Tables Read
- OSFA_DB
## Tables Written
- [[OT_SystemOptions]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- OSFA_DB

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

- [[_MOC-Olives_BO|Olives_BO MOC]]
