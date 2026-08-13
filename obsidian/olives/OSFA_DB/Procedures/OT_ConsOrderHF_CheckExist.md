---
type: procedure
database: OSFA_DB
name: OT_ConsOrderHF_CheckExist
schema: dbo
tags: [#mobile, #order]
reads_from:
  - [[OT_ConsOrderHF]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ConsOrderHF_CheckExist


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_ConsOrderHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @OrderYear smallint
- @OrderNo int
- @OrderDate smalldatetime
- @SalesmanNo smallint
- @Posted bit
- @Notes varchar (200)
- @GPSX varchar (50)
- @GPSY varchar (50)
- @ErrNo SmallInt Output
- @Exist SmallInt Output
## Tables Read
- [[OT_ConsOrderHF]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_ConsOrderHF]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
