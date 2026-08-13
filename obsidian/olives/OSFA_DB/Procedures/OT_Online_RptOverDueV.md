---
type: procedure
database: OSFA_DB
name: OT_Online_RptOverDueV
schema: dbo
tags: [#mobile]
reads_from:
  - Olives_BO
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Online_RptOverDueV


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads Olives_BO, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1
- @FromCust nvarchar(100) ='0'
- @ToCust nvarchar(100) ='99999999'
- @Category nvarchar(100) ='-1'
- @Routes nvarchar(100) ='حي الاسرة,'
- @FromSalesman nvarchar(100) ='0'
- @ToSalesman nvarchar(100) ='99999999'
- @SalesmanNo int=0
## Tables Read
- Olives_BO
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Olives_BO
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
