---
type: procedure
database: Olives_BO
name: Pro_CustomersItemsAssigment
schema: dbo
tags: [#backoffice, #customer, #inventory]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersItemsAssigment]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[SalesPersonItemsAssignment]]
writes_to:
  - [[CustomersItemsAssigment]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CustomersItemsAssigment


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, CustomersItemsAssigment, Items, ItemsCategories, SalesPersonItemsAssignment. Writes CustomersItemsAssigment. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @ItemCode nvarchar(20) = null
- @CompanyID smallint=null
- @PositionsID int = null
- @CustomerID bigint = null
- @CopyTo int = null
- @FilterValue varchar(100) = ''
- @ToGroup int = null
- @cmdType varchar(50) = null
- @CustomersItemsAssigment_Type_DATATABLE CustomersItemsAssigment_Type  readonly
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersItemsAssigment]]
- [[Items]]
- [[ItemsCategories]]
- [[SalesPersonItemsAssignment]]
## Tables Written
- [[CustomersItemsAssigment]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersItemsAssigment]]
- [[Items]]
- [[ItemsCategories]]
- [[SalesPersonItemsAssignment]]

**Tables Written**
- [[CustomersItemsAssigment]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
