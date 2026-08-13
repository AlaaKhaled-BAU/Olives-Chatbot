---
type: procedure
database: OSFA_DB
name: Rpt_AllReturnChecks
schema: dbo
tags: [#mobile, #order, #reporting]
reads_from:
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_AllReturnChecks


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesmanNo int
- @FromDate smallDateTime
- @ToDate smallDateTime
- @WithAllReturnChecks varchar(1)
## Tables Read
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- dbo

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
