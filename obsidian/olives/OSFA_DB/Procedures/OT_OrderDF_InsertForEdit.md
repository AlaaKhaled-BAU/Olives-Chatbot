---
type: procedure
database: OSFA_DB
name: OT_OrderDF_InsertForEdit
schema: dbo
tags: [#mobile, #order]
reads_from:
  - [[OT_OrderDF]]
  - Olives_BO
writes_to:
  - [[OrdersDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_OrderDF_InsertForEdit


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_OrderDF, Olives_BO. Writes OrdersDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
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
- @QtyOH money
- @PromisesDate smalldatetime
- @ErrNo SmallInt Output
- @TaxType bit
- @ItemDiscValue float
- @CustomerDiscountAmount float =0
- @UPrice	float=0
- @TaxPerc_1	float	 =0
- @TaxValue_1	float	 =0
- @TaxType_1	bit	 =0
- @TaxPerc_2	float	 =0
- @TaxValue_2	float	 =0
- @TaxType_2	bit	 =0
- @Manual_Bonus float=0
- @Manual_Disc float =0
- @QtyAsBonus float = 0
- @Notes nvarchar(300)= ''
- @BonusAmount float = 0
- @BonusTax float = 0
- @LineSort smallint = 0
- @Ref1	varchar(500)=''
- @Ref2	varchar(500)=''
- @Ref3	varchar(500)=''
## Tables Read
- [[OT_OrderDF]]
- Olives_BO
## Tables Written
- [[OrdersDetails]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_OrderDF]]
- Olives_BO

**Tables Written**
- [[OrdersDetails]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
