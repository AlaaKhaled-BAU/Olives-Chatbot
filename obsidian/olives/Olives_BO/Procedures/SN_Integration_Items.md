---
type: procedure
database: Olives_BO
name: SN_Integration_Items
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - Cur_Items
  - [[ItemsCategories]]
  - SN
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SN_Integration_Items


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Cur_Items, ItemsCategories, SN. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID nvarchar(50) = 1
## Tables Read
- Cur_Items
- [[ItemsCategories]]
- SN
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Cur_Items
- [[ItemsCategories]]
- SN

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
