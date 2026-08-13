---
type: procedure
database: Olives_BO
name: Pro_CustomersVisitActivity
schema: dbo
tags: [#backoffice, #customer, #sales]
reads_from:
  - [[CustomersVisitActivity]]
writes_to:
  - [[CustomersVisitActivity]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CustomersVisitActivity


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersVisitActivity. Writes CustomersVisitActivity. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @PositionID int = null
- @CustomerID bigint = null
- @ToCustomerID bigint = null
- @ActivityInOrder nvarchar (4000)=null
- @cmdType nvarchar (50)=null
## Tables Read
- [[CustomersVisitActivity]]
## Tables Written
- [[CustomersVisitActivity]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomersVisitActivity]]

**Tables Written**
- [[CustomersVisitActivity]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
