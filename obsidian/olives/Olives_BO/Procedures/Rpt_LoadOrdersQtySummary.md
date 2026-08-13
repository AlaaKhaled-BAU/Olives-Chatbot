---
type: procedure
database: Olives_BO
name: Rpt_LoadOrdersQtySummary
schema: dbo
tags: [#backoffice, #order, #reporting]
reads_from:
  - [[Items]]
  - [[TransfersOrdersDetails]]
  - [[TransfersOrdersHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_LoadOrdersQtySummary


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, TransfersOrdersDetails, TransfersOrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromDate SmallDateTime = '2021-12-01'
- @ToDate SmallDateTime = '2022-12-01'
- @FromItem Nvarchar(100) = '0'
- @ToItem Nvarchar(100) = 'zzzz'
- @Type smallint = -1
## Tables Read
- [[Items]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]

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
