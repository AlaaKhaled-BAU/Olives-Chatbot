---
type: procedure
database: OSFA_DB
name: OT_InvoiceDF_Insert
schema: dbo
tags: [#billing, #mobile]
reads_from:
  - [[OT_InvoiceDF]]
writes_to:
  - [[OT_InvoiceDF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_InvoiceDF_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_InvoiceDF. Writes OT_InvoiceDF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouType smallint
- @VouYear smallint
- @VouNo int
- @ItemNo varchar (200)
- @Unit varchar (100)
- @Qty money
- @Bonus money
- @Price float
- @DiscountAmount float
- @DiscountPercent Float
- @VouDiscount float
- @TaxType bit
- @TaxPercent Float
- @TaxAmount float
- @ErrNo SmallInt Output
- @ItemStatus	smallint=0
- @CustomerDiscountAmount float=0
- @UPrice	float=0
- @TaxPercent_1	float	=0
- @TaxAmount_1	float	=0
- @TaxType_1	bit	=0
- @TaxPercent_2	float	=0
- @TaxAmount_2	float	=0
- @TaxType_2	bit=0
- @Manual_Bonus float=0
- @SP_Qty	float=0
- @ItemBarcode	varchar(500)=''
- @Manual_Disc float=0
- @QtyAsBonus float=0
- @Notes nvarchar(300) = ''
- @ReturnReason int = 0
- @BonusAmount float = 0
- @BonusTax float = 0
- @LineSort smallint=0
- @CurrentQty float = 0
## Tables Read
- [[OT_InvoiceDF]]
## Tables Written
- [[OT_InvoiceDF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_InvoiceDF]]

**Tables Written**
- [[OT_InvoiceDF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
