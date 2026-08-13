---
type: procedure
database: Olives_BO
name: Rpt_RangePromotionInput
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[Items]]
  - [[ItemsUnits]]
  - [[PromotionsHeaders]]
  - [[PromotionsRangeInput]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_RangePromotionInput


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, ItemsUnits, PromotionsHeaders, PromotionsRangeInput. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int
- @PromotionType int
- @ToPromotionType int
- @IsActive smallint
- @FromDate smalldatetime = null
- @ToDate smalldatetime = null
## Tables Read
- [[Items]]
- [[ItemsUnits]]
- [[PromotionsHeaders]]
- [[PromotionsRangeInput]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[ItemsUnits]]
- [[PromotionsHeaders]]
- [[PromotionsRangeInput]]

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
