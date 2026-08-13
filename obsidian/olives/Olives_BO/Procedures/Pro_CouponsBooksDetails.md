---
type: procedure
database: Olives_BO
name: Pro_CouponsBooksDetails
schema: dbo
tags: [#backoffice]
reads_from:
  - [[CouponsBooksDetails]]
  - [[CouponsBooksHeaders]]
  - [[PromotionsHeaders]]
writes_to:
  - [[CouponsBooksDetails]]
  - [[CouponsBooksHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CouponsBooksDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CouponsBooksDetails, CouponsBooksHeaders, PromotionsHeaders. Writes CouponsBooksDetails, CouponsBooksHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	= null
- @BookID	int	= null
- @CuoponNumber	nvarchar(100)	= null
- @CuoponBarcode	nvarchar(100)	= null
- @PromotionID	int	= null
- @CustomerID bigint = null
- @IsUsed	bit	= null
- @UsedInTrType	smallint	= null
- @UsedInTrYear	smallint	= null
- @UsedInTrNo	int	= null
- @cmdType varchar(50)=null
## Tables Read
- [[CouponsBooksDetails]]
- [[CouponsBooksHeaders]]
- [[PromotionsHeaders]]
## Tables Written
- [[CouponsBooksDetails]]
- [[CouponsBooksHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CouponsBooksDetails]]
- [[CouponsBooksHeaders]]
- [[PromotionsHeaders]]

**Tables Written**
- [[CouponsBooksDetails]]
- [[CouponsBooksHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
