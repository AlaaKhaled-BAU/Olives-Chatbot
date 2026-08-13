---
type: procedure
database: OSFA_DB
name: OT_SalesQuotationDF_Insert
schema: dbo
tags: [#mobile, #order, #sales]
reads_from:
  - [[OT_SalesQuotationDF]]
writes_to:
  - [[OT_SalesQuotationDF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_SalesQuotationDF_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_SalesQuotationDF. Writes OT_SalesQuotationDF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @OrderYear smallint
- @OrderNo int
- @ItemNo varchar (200)
- @UnitCode varchar (100)
- @Qty money
- @Bonus money
- @SellValue float
- @DiscPerc Float
- @DiscValue float
- @TaxPerc Float
- @TaxValue float
- @ErrNo SmallInt Output
- @TaxType bit
- @ItemDiscValue float
- @CustomerDiscountAmount float =0
- @ForeignCustomerDiscountAmount float =0
- @ForeignPrice float =0
- @ForeignDiscountAmount float =0
- @ForeignDiscountPercent float =0
- @ForeignVouDiscount float =0
- @ForeignTaxPercent float =0
- @ForeignTaxAmount float =0
- @UPrice	float=0
- @TaxPerc_1	float	 =0
- @TaxValue_1	float	 =0
- @TaxType_1	bit	 =0
- @TaxPerc_2	float	 =0
- @TaxValue_2	float	 =0
- @TaxType_2	bit	 =0
- @Manual_Bonus float=0
- @Notes nvarchar(300) =''
- @BonusAmount float = 0
- @BonusTax float = 0
## Tables Read
- [[OT_SalesQuotationDF]]
## Tables Written
- [[OT_SalesQuotationDF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_SalesQuotationDF]]

**Tables Written**
- [[OT_SalesQuotationDF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
