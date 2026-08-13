---
type: procedure
database: OSFA_DB
name: OT_Online_RptSalesTargetDetails
schema: dbo
tags: [#mobile, #sales]
reads_from:
  - AS
  - Fun_RetrunQTYTargetByMonth
  - Fun_RetrunSalesTargetByMonth
  - ON
  - PRESTOSOFT
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Online_RptSalesTargetDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads AS, Fun_RetrunQTYTargetByMonth, Fun_RetrunSalesTargetByMonth, ON, PRESTOSOFT, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=1
- @SalesmanNo int=3003
- @TargetYear smallint=2023
- @TargetMonth smallint=7
- @TargetType smallint=2
## Tables Read
- AS
- Fun_RetrunQTYTargetByMonth
- Fun_RetrunSalesTargetByMonth
- ON
- PRESTOSOFT
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- AS
- Fun_RetrunQTYTargetByMonth
- Fun_RetrunSalesTargetByMonth
- ON
- PRESTOSOFT
- dbo

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
