---
type: procedure
database: Olives_BO
name: Pro_MMS_PaymentsHeader
schema: dbo
tags: [#backoffice, #billing, #mms]
reads_from:
  - [[Customers]]
  - [[MMS_MaintenanceTechnician]]
  - [[MMS_OrdersHeader]]
  - [[MMS_PaymentsHeader]]
  - [[MMS_ScheduleSupportVisits]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_PaymentsHeader


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, MMS_MaintenanceTechnician, MMS_OrdersHeader, MMS_PaymentsHeader, MMS_ScheduleSupportVisits. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	= null
- @PaymentYear	smallint	= null
- @PaymentNo	bigint	= null
- @PaymentDate	smalldatetime	= null
- @InvoiceYear	smallint	= null
- @InvoiceNo	bigint	= null
- @CashAmount	float	= null
- @CheckAmount	float	= null
- @Notes	nvarchar(500)	= null
- @TabletSysID	varchar(50)	= null
- @OrderAutoID	numeric(30, 0)	= null
- @OrderSubID	int	= null
- @ScheduleID	int	= null
- @cmdType nvarchar(50) = null
- @FromDate smalldatetime = null
- @ToDate smalldatetime = null
## Tables Read
- [[Customers]]
- [[MMS_MaintenanceTechnician]]
- [[MMS_OrdersHeader]]
- [[MMS_PaymentsHeader]]
- [[MMS_ScheduleSupportVisits]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[MMS_MaintenanceTechnician]]
- [[MMS_OrdersHeader]]
- [[MMS_PaymentsHeader]]
- [[MMS_ScheduleSupportVisits]]

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
