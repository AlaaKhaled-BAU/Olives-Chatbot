---
type: procedure
database: OSFA_DB
name: OT_RequestToCancelPayment_Insert
schema: dbo
tags: [#maintenance]
reads_from:
writes_to:
  - OT_RequestToCancelPayment
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# OT_RequestToCancelPayment_Insert

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in OSFA_DB — writes 1. See sections below for the full dependency map.
## Parameters
- @CompNo smallint
- @TrYear smallint
- @TrType smallint
- @TrNo int
- @SalesPersonNo int
- @CustomerNo bigint
- @ReceiptAmount float
- @DiscountAmount float
- @ChecksInfo nvarchar(MAX)
- @InvoiceInfo nvarchar(MAX)
- @Notes nvarchar(MAX)
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @TabletSysID varchar(50)
- @ErrNo smallint OUTPUT
- @NewAutoID numeric(30,0) OUTPUT
## Tables Read
_None_
## Tables Written
- [[OT_RequestToCancelPayment]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-OSFA_DB|OSFA_DB MOC]]
