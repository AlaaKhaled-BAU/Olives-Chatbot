---
type: procedure
database: OSFA_DB
name: OT_RequestToAddExtraBonus_Insert
schema: dbo
tags: [#mobile, #workflow]
reads_from:
  - [[OT_RequestToAddExtraBonus]]
  - Olives_BO
writes_to:
  - [[OT_RequestToAddExtraBonus]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToAddExtraBonus_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToAddExtraBonus, Olives_BO. Writes OT_RequestToAddExtraBonus. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @TrType int
- @CustomerNo bigint
- @InvoiceAmount float
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @Notes nvarchar(Max)
- @TabletSysID varchar(50)=null
- @BonusAmount varchar(50)=null
- @ErrNo smallint output
- @NewAutoID numeric(30,0) output
## Tables Read
- [[OT_RequestToAddExtraBonus]]
- Olives_BO
## Tables Written
- [[OT_RequestToAddExtraBonus]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToAddExtraBonus]]
- Olives_BO

**Tables Written**
- [[OT_RequestToAddExtraBonus]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
