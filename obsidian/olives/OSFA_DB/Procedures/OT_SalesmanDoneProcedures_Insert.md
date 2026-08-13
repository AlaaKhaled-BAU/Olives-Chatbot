---
type: procedure
database: OSFA_DB
name: OT_SalesmanDoneProcedures_Insert
schema: dbo
tags: [#mobile, #sales]
reads_from:
  - [[OT_SalesmanDoneProcedures]]
writes_to:
  - [[OT_SalesmanDoneProcedures]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_SalesmanDoneProcedures_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_SalesmanDoneProcedures. Writes OT_SalesmanDoneProcedures. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesmanNo int
- @CustomerNo bigint
- @ProcedureID int
- @ProcedureDate smalldatetime
- @TrDateTime datetime
- @IsPosted bit
- @ErrNo SmallInt Output
## Tables Read
- [[OT_SalesmanDoneProcedures]]
## Tables Written
- [[OT_SalesmanDoneProcedures]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_SalesmanDoneProcedures]]

**Tables Written**
- [[OT_SalesmanDoneProcedures]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
