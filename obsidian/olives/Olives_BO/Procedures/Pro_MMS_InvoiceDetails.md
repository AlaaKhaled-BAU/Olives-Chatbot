---
type: procedure
database: Olives_BO
name: Pro_MMS_InvoiceDetails
schema: dbo
tags: [#backoffice, #billing, #mms]
reads_from:
  - [[MMS_InvoiceDetails]]
  - [[MMS_Items]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_InvoiceDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MMS_InvoiceDetails, MMS_Items. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	= null
- @InvoiceYear	smallint	= null
- @InvoiceNo	bigint	= null
- @LineID	int	= null
- @ItemNo	nvarchar(100)	= null
- @Qty	money	= null
- @UnitPrice	float	= null
- @Price	float	= null
- @TaxPercent	float	= null
- @TaxValue	float	= null
- @ItemDiscountPercent	float	= null
- @ItemDiscountValue	float	= null
- @InvoiceDiscountValue	float	= null
- @IsInWarranty	bit	= null
- @cmdType nvarchar(50) = null
## Tables Read
- [[MMS_InvoiceDetails]]
- [[MMS_Items]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MMS_InvoiceDetails]]
- [[MMS_Items]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
