---
type: procedure
database: OSFA_DB
name: OT_RequestToMakeTransactionToSuspendedCustomer_Insert
schema: dbo
tags: [#customer, #mobile, #workflow]
reads_from:
  - [[OT_RequestToMakeTransactionToSuspendedCustomer]]
writes_to:
  - [[OT_RequestToMakeTransactionToSuspendedCustomer]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToMakeTransactionToSuspendedCustomer_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToMakeTransactionToSuspendedCustomer. Writes OT_RequestToMakeTransactionToSuspendedCustomer. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @TrType smallint
- @SalesPersonNo int
- @CustomerNo bigint
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @ErrNo smallint output
- @NewAutoID numeric(30,0) output
## Tables Read
- [[OT_RequestToMakeTransactionToSuspendedCustomer]]
## Tables Written
- [[OT_RequestToMakeTransactionToSuspendedCustomer]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToMakeTransactionToSuspendedCustomer]]

**Tables Written**
- [[OT_RequestToMakeTransactionToSuspendedCustomer]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
