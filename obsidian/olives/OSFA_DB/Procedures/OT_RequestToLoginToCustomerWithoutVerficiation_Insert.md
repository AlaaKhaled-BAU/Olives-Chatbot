---
type: procedure
database: OSFA_DB
name: OT_RequestToLoginToCustomerWithoutVerficiation_Insert
schema: dbo
tags: [#auth, #customer, #log, #mobile, #workflow]
reads_from:
  - [[OT_RequestToLoginToCustomerWithoutVerficiation]]
writes_to:
  - [[OT_RequestToLoginToCustomerWithoutVerficiation]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToLoginToCustomerWithoutVerficiation_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToLoginToCustomerWithoutVerficiation. Writes OT_RequestToLoginToCustomerWithoutVerficiation. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @CustomerNo bigint
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @ErrNo smallint output
- @NewAutoID numeric(30,0) output
- @LoggedIn	bit	=0
## Tables Read
- [[OT_RequestToLoginToCustomerWithoutVerficiation]]
## Tables Written
- [[OT_RequestToLoginToCustomerWithoutVerficiation]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToLoginToCustomerWithoutVerficiation]]

**Tables Written**
- [[OT_RequestToLoginToCustomerWithoutVerficiation]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
