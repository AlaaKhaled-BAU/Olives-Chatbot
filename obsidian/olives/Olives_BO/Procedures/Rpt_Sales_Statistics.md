---
type: procedure
database: Olives_BO
name: Rpt_Sales_Statistics
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[ERPStores]]
  - [[Items]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_Sales_Statistics


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ERPStores, Items, OrdersDetails, OrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @Compno int=1
- @FromDate Smalldatetime='2020-04-01'
- @ToDate Smalldatetime='2024-04-07'
## Tables Read
- [[ERPStores]]
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ERPStores]]
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]

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
