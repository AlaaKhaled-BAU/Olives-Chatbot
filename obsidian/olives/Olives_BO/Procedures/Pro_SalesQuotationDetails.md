---
type: procedure
database: Olives_BO
name: Pro_SalesQuotationDetails
schema: dbo
tags: [#backoffice, #order, #sales]
reads_from:
  - [[Items]]
  - [[ItemsUnits]]
  - [[SalesQuotationDetails]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesQuotationDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, ItemsUnits, SalesQuotationDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	 = null
- @OrderYear	int	= null
- @OrderNo	int	= null
- @ItemCode	nvarchar(100)	= null
- @UnitID	nvarchar(50)	= null
- @Quantity	float	= null
- @Bonus	float	= null
- @Price	float	= null
- @DiscountAmount	float	= null
- @DiscountPercent	float	= null
- @VoucherDiscount	float	= null
- @TaxType	smallint	= null
- @TaxPercent	float	= null
- @TaxAmount	float	= null
- @ForeignPrice	float	= null
- @ForeignDiscountAmount	float	= null
- @ForeignDiscountPercent	float	= null
- @ForeignVouDiscount	float	= null
- @ForeignTaxPercent	float	= null
- @ForeignTaxAmount	float	= null
- @CustomerDiscountAmount	float	= null
- @ForeignCustomerDiscountAmount	float	= null
- @FromDate  smalldatetime = null
- @ToDate  smalldatetime = null
- @cmdType varchar(50)=null
## Tables Read
- [[Items]]
- [[ItemsUnits]]
- [[SalesQuotationDetails]]
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
- [[SalesQuotationDetails]]

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
