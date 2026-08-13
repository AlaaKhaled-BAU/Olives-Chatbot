---
type: procedure
database: Olives_BO
name: Pro_SalespersonsGPSTracking
schema: dbo
tags: [#backoffice, #gps, #sales]
reads_from:
  - [[SalespersonsGPSTracking]]
writes_to:
  - [[SalespersonsGPSTracking]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalespersonsGPSTracking


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalespersonsGPSTracking. Writes SalespersonsGPSTracking. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = null
- @SalesPersonID int = null
- @TrDateTime datetime = null
- @GpsX varchar (50) = null
- @GpsY varchar (50) = null
- @Notes varchar (1000) = null
- @TabletSysID varchar (100) = null
- @cmdType  nvarchar(50) = null
- @Exist SmallInt Output
## Tables Read
- [[SalespersonsGPSTracking]]
## Tables Written
- [[SalespersonsGPSTracking]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalespersonsGPSTracking]]

**Tables Written**
- [[SalespersonsGPSTracking]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
