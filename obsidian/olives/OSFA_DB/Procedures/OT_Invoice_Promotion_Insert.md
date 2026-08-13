---
type: procedure
database: OSFA_DB
name: OT_Invoice_Promotion_Insert
schema: dbo
tags: [#billing, #mobile, #sales]
reads_from:
  - [[OT_Invoice_Promotion]]
writes_to:
  - [[OT_Invoice_Promotion]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Invoice_Promotion_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_Invoice_Promotion. Writes OT_Invoice_Promotion. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouType smallint
- @VouYear smallint
- @VouNo int
- @SerID int
- @PromotionCode nvarchar(100)
- @PromotionType int
- @PromotionName nvarchar(200)
- @InputItem nvarchar(100)=NULL
- @InputUnit nvarchar(100)=NULL
- @InputQty money
- @InputAmount float
- @ItemNo nvarchar(100)=NULL
- @UnitCode nvarchar(100)=NULL
- @Bonus money
- @ItemDiscountAmount float
- @ItemDiscountPercent float
- @VouDiscountAmount float
- @VouDiscountPercent float
- @IncludeInTargetBonus bit = 0
- @ErrNo SmallInt Output
- @IsInInput bit=0
## Tables Read
- [[OT_Invoice_Promotion]]
## Tables Written
- [[OT_Invoice_Promotion]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_Invoice_Promotion]]

**Tables Written**
- [[OT_Invoice_Promotion]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
