---
type: procedure
database: OSFA_DB
name: OT_Online_StateAccBalance
schema: dbo
tags: [#inventory, #mobile]
reads_from:
  - [[OT_StateAccBalance]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Online_StateAccBalance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_StateAccBalance, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1
- @FromDate smalldatetime='2018-02-05'
- @ToDate smalldatetime='2023-10-11'
- @CustomerID Bigint=314
- @SalesmanNo Bigint=3003
## Tables Read
- [[OT_StateAccBalance]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_StateAccBalance]]
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
