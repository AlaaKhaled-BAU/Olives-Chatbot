---
type: procedure
database: Olives_BO
name: Awael_Integ_BatchesQty
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - [[BatchsItemsInfo]]
  - [[Items]]
  - `dbo`
writes_to:
  - [[BatchsItemsInfo]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Awael_Integ_BatchesQty


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads BatchsItemsInfo, Items, dbo. Writes BatchsItemsInfo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- [[BatchsItemsInfo]]
- [[Items]]
- `dbo`
## Tables Written
- [[BatchsItemsInfo]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[BatchsItemsInfo]]
- [[Items]]
- dbo

**Tables Written**
- [[BatchsItemsInfo]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
