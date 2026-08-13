---
type: procedure
database: Olives_BO
name: Pro_ItemsPriceExceptions
schema: dbo
tags: [#backoffice, #billing, #inventory]
reads_from:
  - [[Customers]]
  - [[Items]]
  - [[ItemsPriceExceptions]]
  - [[ItemsUnits]]
writes_to:
  - [[ItemsPriceExceptions]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ItemsPriceExceptions


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Items, ItemsPriceExceptions, ItemsUnits. Writes ItemsPriceExceptions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	= null
- @CustomerID	bigint	= null
- @ItemCode	nvarchar(100)	= null
- @UnitID	nvarchar(50)	= null
- @StartDate	smalldatetime	= null
- @EndDate	smalldatetime	= null
- @Price	float	= null
- @TaxType	int	= null
- @Tax	float	= null
- @DiscountPercent	float	= null
- @UseInReturn	bit	= null
- @UseInSales	bit	= null
- @Qty	money	= null
- @cmdType varchar(50)=null
## Tables Read
- [[Customers]]
- [[Items]]
- [[ItemsPriceExceptions]]
- [[ItemsUnits]]
## Tables Written
- [[ItemsPriceExceptions]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[Items]]
- [[ItemsPriceExceptions]]
- [[ItemsUnits]]

**Tables Written**
- [[ItemsPriceExceptions]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
