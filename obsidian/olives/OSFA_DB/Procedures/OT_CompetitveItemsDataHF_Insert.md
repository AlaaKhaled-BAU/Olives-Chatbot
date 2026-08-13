---
type: procedure
database: OSFA_DB
name: OT_CompetitveItemsDataHF_Insert
schema: dbo
tags: [#inventory, #mobile]
reads_from:
  - [[OT_CompetitveItemsDataHF]]
writes_to:
  - [[OT_CompetitveItemsDataHF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_CompetitveItemsDataHF_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_CompetitveItemsDataHF. Writes OT_CompetitveItemsDataHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @TrYear smallint
- @TrNo int
- @SalesPersons int
- @CustomerID bigint
- @TrDate smalldatetime
- @Notes nvarchar (600)
- @GPSX varchar (50)
- @GPSY varchar (50)
- @TrDateTime smalldatetime = null
- @IsProspectiveCustomer bit = null
- @ErrNo SmallInt Output
## Tables Read
- [[OT_CompetitveItemsDataHF]]
## Tables Written
- [[OT_CompetitveItemsDataHF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_CompetitveItemsDataHF]]

**Tables Written**
- [[OT_CompetitveItemsDataHF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
