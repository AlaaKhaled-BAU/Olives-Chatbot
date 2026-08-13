---
type: procedure
database: OSFA_DB
name: OT_CompetitveItemsDataDF_Insert
schema: dbo
tags: [#inventory, #mobile]
reads_from:
  - [[OT_CompetitveItemsDataDF]]
  - [[OT_NewCompetitiveItems]]
writes_to:
  - [[OT_CompetitveItemsDataDF]]
  - [[OT_NewCompetitiveItems]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_CompetitveItemsDataDF_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_CompetitveItemsDataDF, OT_NewCompetitiveItems. Writes OT_CompetitveItemsDataDF, OT_NewCompetitiveItems. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @TrYear smallint
- @TrNo int
- @CompetitiveItem nvarchar (200)
- @Qty money
- @Price float
- @Notes nvarchar (600)
- @ErrNo SmallInt Output
- @Name	nvarchar(100)
- @CompetitiveCompany	nvarchar(100)
- @SalesPersons int
- @ShelfPrice float=0
- @RetailPrice float=0
- @WholeSalePrice float=0
## Tables Read
- [[OT_CompetitveItemsDataDF]]
- [[OT_NewCompetitiveItems]]
## Tables Written
- [[OT_CompetitveItemsDataDF]]
- [[OT_NewCompetitiveItems]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_CompetitveItemsDataDF]]
- [[OT_NewCompetitiveItems]]

**Tables Written**
- [[OT_CompetitveItemsDataDF]]
- [[OT_NewCompetitiveItems]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
