---
type: procedure
database: OSFA_DB
name: OT_RequestToApprovePromotion_Insert
schema: dbo
tags: [#mobile, #sales, #workflow]
reads_from:
  - [[OT_RequestToApprovePromotion]]
  - [[OT_RequestToApprovePromotionDetails]]
writes_to:
  - [[OT_RequestToApprovePromotion]]
  - [[OT_RequestToApprovePromotionDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToApprovePromotion_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToApprovePromotion, OT_RequestToApprovePromotionDetails. Writes OT_RequestToApprovePromotion, OT_RequestToApprovePromotionDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @CustomerNo bigint
- @PromotionInfo nvarchar(max)
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @PromotionID int
- @ErrNo smallint output
- @NewAutoID numeric(30,0) output
- @DtPromotion WFPromotionsDetails ReadOnly
## Tables Read
- [[OT_RequestToApprovePromotion]]
- [[OT_RequestToApprovePromotionDetails]]
## Tables Written
- [[OT_RequestToApprovePromotion]]
- [[OT_RequestToApprovePromotionDetails]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToApprovePromotion]]
- [[OT_RequestToApprovePromotionDetails]]

**Tables Written**
- [[OT_RequestToApprovePromotion]]
- [[OT_RequestToApprovePromotionDetails]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
