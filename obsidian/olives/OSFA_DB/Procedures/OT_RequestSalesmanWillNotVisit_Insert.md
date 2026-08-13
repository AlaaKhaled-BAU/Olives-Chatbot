---
type: procedure
database: OSFA_DB
name: OT_RequestSalesmanWillNotVisit_Insert
schema: dbo
tags: [#mobile, #sales]
reads_from:
  - [[OT_RequestSalesmanWillNotVisit]]
writes_to:
  - [[OT_RequestSalesmanWillNotVisit]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestSalesmanWillNotVisit_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestSalesmanWillNotVisit. Writes OT_RequestSalesmanWillNotVisit. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @CustomerNo bigint
- @ReasonID int
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @ErrNo smallint output
- @NewAutoID numeric(30,0) output
## Tables Read
- [[OT_RequestSalesmanWillNotVisit]]
## Tables Written
- [[OT_RequestSalesmanWillNotVisit]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestSalesmanWillNotVisit]]

**Tables Written**
- [[OT_RequestSalesmanWillNotVisit]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
