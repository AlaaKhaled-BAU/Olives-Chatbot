---
type: procedure
database: Olives_BO
name: Pro_OrdersPayment
schema: dbo
tags: [#backoffice, #billing, #order]
reads_from:
  - [[Customers]]
  - [[PaymentsOrders]]
  - [[SalesPersons]]
writes_to:
  - [[PaymentsOrders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_OrdersPayment


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, PaymentsOrders, SalesPersons. Writes PaymentsOrders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @OrderYear smallint = null
- @OrderNo   int = null
- @OrderDate smalldatetime = null
- @CustomerID bigint = null
- @SalesmanID int = null
- @Amount     float = null
- @IssuedAmount float = null
- @IsIssued bit = null
- @IssuedDate smalldatetime = null
- @IsSuspended  bit= null
- @RefNo nvarchar(50) = null
- @cmdType nvarchar(50) = null
## Tables Read
- [[Customers]]
- [[PaymentsOrders]]
- [[SalesPersons]]
## Tables Written
- [[PaymentsOrders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[PaymentsOrders]]
- [[SalesPersons]]

**Tables Written**
- [[PaymentsOrders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
