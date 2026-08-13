---
type: procedure
database: Olives_BO
name: GetSalesOrdersForEdit
schema: dbo
tags: [#backoffice, #order, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# GetSalesOrdersForEdit


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, Items, ItemsUnits, OrdersDetails, OrdersHeaders, SalesPersons, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int= 2
- @SalesmanNo int=1
- @CustID bigint=-1
- @ForUploadOrder bit=0
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Items]]
- [[ItemsUnits]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Items]]
- [[ItemsUnits]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- dbo

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
