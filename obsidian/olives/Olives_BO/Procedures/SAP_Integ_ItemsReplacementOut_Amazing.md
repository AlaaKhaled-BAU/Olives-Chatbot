---
type: procedure
database: Olives_BO
name: SAP_Integ_ItemsReplacementOut_Amazing
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - [[ItemsReplacementHeaders]]
  - `dbo`
writes_to:
  - GoodsIssue
  - GoodsIssueItems
  - [[ItemsReplacementHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SAP_Integ_ItemsReplacementOut_Amazing


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ItemsReplacementHeaders, dbo. Writes GoodsIssue, GoodsIssueItems, ItemsReplacementHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
## Tables Read
- [[ItemsReplacementHeaders]]
- `dbo`
## Tables Written
- GoodsIssue
- GoodsIssueItems
- [[ItemsReplacementHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ItemsReplacementHeaders]]
- dbo

**Tables Written**
- GoodsIssue
- GoodsIssueItems
- [[ItemsReplacementHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
