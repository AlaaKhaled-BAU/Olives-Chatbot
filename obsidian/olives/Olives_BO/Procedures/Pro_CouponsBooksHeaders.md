---
type: procedure
database: Olives_BO
name: Pro_CouponsBooksHeaders
schema: dbo
tags: [#backoffice]
reads_from:
  - [[CouponsBooksDetails]]
  - [[CouponsBooksHeaders]]
  - [[Customers]]
writes_to:
  - [[CouponsBooksDetails]]
  - [[CouponsBooksHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CouponsBooksHeaders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CouponsBooksDetails, CouponsBooksHeaders, Customers. Writes CouponsBooksDetails, CouponsBooksHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint = null
- @ID	int	= null
- @PrID	int	= null
- @BookNo	nvarchar(100) = null
- @Barcode	nvarchar(100) = null
- @CustomerID	bigint = null
- @ExpiryDate smalldatetime= null
- @IsSuspended bit = null
- @cmdType varchar(50)=null
## Tables Read
- [[CouponsBooksDetails]]
- [[CouponsBooksHeaders]]
- [[Customers]]
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
- [[Customers]]

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
