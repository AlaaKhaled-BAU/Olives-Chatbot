---
type: procedure
database: Olives_BO
name: Pro_CopyPricelist
schema: dbo
tags: [#backoffice, #billing]
reads_from:
  - [[PriceListDetails]]
  - Source
  - int
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Items-Master-Data-Setup
  - PriceList-Management
---
# Pro_CopyPricelist


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads PriceListDetails, Source, int. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int =null
- @From int =null
- @To int =null
## Tables Read
- [[PriceListDetails]]
- Source
- int
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[PriceListDetails]]
- Source
- int

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
