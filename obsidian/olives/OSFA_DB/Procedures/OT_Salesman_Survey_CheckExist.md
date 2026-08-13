---
type: procedure
database: OSFA_DB
name: OT_Salesman_Survey_CheckExist
schema: dbo
tags: [#mobile, #sales, #survey]
reads_from:
  - [[OT_Salesman_Survey]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Salesman_Survey_CheckExist


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_Salesman_Survey. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @Salesman_Survey_No bigint
- @CompNo smallint
- @Survey_ID int
- @Survey_Date datetime
- @ErrNo SmallInt Output
- @GPSX varchar(50)
- @GPSY varchar(50)
- @SalesmanNo nvarchar(50)
- @ForSalesmanNo nvarchar(50)
- @Exist SmallInt Output
## Tables Read
- [[OT_Salesman_Survey]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_Salesman_Survey]]

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
