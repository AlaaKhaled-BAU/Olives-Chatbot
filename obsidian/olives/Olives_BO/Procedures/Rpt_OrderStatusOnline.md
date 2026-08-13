---
type: procedure
database: Olives_BO
name: Rpt_OrderStatusOnline
schema: dbo
tags: [#backoffice, #order, #reporting]
reads_from:
  - DB
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_OrderStatusOnline


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads DB. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromDate smalldatetime='2025-1-1'
- @ToDate smalldatetime='2025-9-9'
- @SalesmaNo int = 101
## Tables Read
- DB
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- DB

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
