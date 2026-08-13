---
type: procedure
database: OSFA_DB
name: OT_RequestToVisitCustomerNotInRoute_Insert
schema: dbo
tags: [#customer, #gps, #mobile, #sales, #workflow]
reads_from:
  - [[OT_RequestToVisitCustomerNotInRoute]]
writes_to:
  - [[OT_RequestToVisitCustomerNotInRoute]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToVisitCustomerNotInRoute_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToVisitCustomerNotInRoute. Writes OT_RequestToVisitCustomerNotInRoute. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @CustomerNo bigint
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @ErrNo smallint output
## Tables Read
- [[OT_RequestToVisitCustomerNotInRoute]]
## Tables Written
- [[OT_RequestToVisitCustomerNotInRoute]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToVisitCustomerNotInRoute]]

**Tables Written**
- [[OT_RequestToVisitCustomerNotInRoute]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
