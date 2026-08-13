---
type: procedure
database: OSFA_DB
name: OT_InvoicesDelivery_Insert
schema: dbo
tags: [#billing, #mobile, #order]
reads_from:
  - [[OT_ErrorLog]]
  - [[OT_InvoicesDelivery]]
  - Olives_BO
  - `dbo`
writes_to:
  - [[OT_ErrorLog]]
  - [[OT_InvoicesDelivery]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_InvoicesDelivery_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_ErrorLog, OT_InvoicesDelivery, Olives_BO, dbo. Writes OT_ErrorLog, OT_InvoicesDelivery. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @TransactionTypeID smallint
- @TransactionYear smallint
- @TransactionNo int
- @InvoiceSalesPersonID int
- @SalesPersonID int
- @Latitude nvarchar (100)
- @Longitude nvarchar (100)
- @Notes nvarchar (4000)
- @DeliveredDateTime smalldatetime
- @IsPosted bit
- @TabletSysID varchar (50)
- @ErrNo SmallInt Output
- @CancelReasonID	int=0
- @StoreNo	int	=0
- @PaymentType	varchar (50)=0
## Tables Read
- [[OT_ErrorLog]]
- [[OT_InvoicesDelivery]]
- Olives_BO
- `dbo`
## Tables Written
- [[OT_ErrorLog]]
- [[OT_InvoicesDelivery]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_ErrorLog]]
- [[OT_InvoicesDelivery]]
- Olives_BO
- dbo

**Tables Written**
- [[OT_ErrorLog]]
- [[OT_InvoicesDelivery]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
