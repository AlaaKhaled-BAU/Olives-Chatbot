---
type: procedure
database: OSFA_DB
name: OT_Add_Salesman_Survey
schema: dbo
tags: [#mobile, #sales, #survey]
reads_from:
  - [[OT_Salesman_Survey]]
writes_to:
  - [[OT_Salesman_Survey]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Add_Salesman_Survey


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_Salesman_Survey. Writes OT_Salesman_Survey. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @Salesman_Survey_No bigint
- @CompNo smallint
- @Survey_ID int
- @Survey_Date datetime
- @ErrNo SmallInt Output
- @UsedSalesman_Survey_No bigint Output
- @GPSX varchar(50)
- @GPSY varchar(50)
- @SalesmanNo nvarchar(50)
- @ForSalesmanNo nvarchar(50)
## Tables Read
- [[OT_Salesman_Survey]]
## Tables Written
- [[OT_Salesman_Survey]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_Salesman_Survey]]

**Tables Written**
- [[OT_Salesman_Survey]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
