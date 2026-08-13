---
type: procedure
database: Olives_BO
name: Pro_CustomerItemQtyLimit
schema: dbo
tags: [#backoffice, #customer, #inventory]
reads_from:
  - [[CustomersItemQtyLimit]]
  - [[Items]]
writes_to:
  - [[CustomersItemQtyLimit]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CustomerItemQtyLimit


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersItemQtyLimit, Items. Writes CustomersItemQtyLimit. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @CustomerID BigInt = null
- @ToCustomer BigInt = null
- @ItemCode nvarchar(100) = null
- @Qty float = null
- @UnitID varchar(50)=null
- @cmdType varchar(50)=null
## Tables Read
- [[CustomersItemQtyLimit]]
- [[Items]]
## Tables Written
- [[CustomersItemQtyLimit]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomersItemQtyLimit]]
- [[Items]]

**Tables Written**
- [[CustomersItemQtyLimit]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
