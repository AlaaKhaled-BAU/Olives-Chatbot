---
type: procedure
database: OSFA_DB
name: OT_UpdateSalesmanMsgs
schema: dbo
tags: [#mobile, #sales]
reads_from:
  - `dbo`
writes_to:
  - [[SalespersonsMessages]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_UpdateSalesmanMsgs


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads dbo. Writes SalespersonsMessages. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @SalespersonID int
- @MsgID bigint
- @ReadDateTime smalldatetime
## Tables Read
- `dbo`
## Tables Written
- [[SalespersonsMessages]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- dbo

**Tables Written**
- [[SalespersonsMessages]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
