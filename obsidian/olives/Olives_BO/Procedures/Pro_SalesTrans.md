---
type: procedure
database: Olives_BO
name: Pro_SalesTrans
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[Assets]]
  - [[Customers]]
  - [[Locations]]
  - [[PaymentsTypes]]
  - [[PriceListDetails]]
  - [[SalesPersons]]
  - [[SalesTransDetails]]
  - [[SalesTransHeader]]
writes_to:
  - [[SalesTransHeader]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesTrans


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Assets, Customers, Locations, PaymentsTypes, PriceListDetails, SalesPersons, SalesTransDetails, SalesTransHeader. Writes SalesTransHeader. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @AssetID smallint = null
- @SalesmanNo int =null
- @StoreNo int =null
- @TransAutoID numeric = null
- @CACR int=null
- @TransDate smallDateTime = null
- @CustomerID bigint=null
- @ContractDate smalldatetime = null
- @InvoiceNumber nvarchar(100)= null
- @UserID nvarchar(50) = null
- @Notes nvarchar(500) = null
- @Address nvarchar(50) = null
- @cmdType varchar(50)=null
- @Details as SalesTransDetails Readonly
## Tables Read
- [[Assets]]
- [[Customers]]
- [[Locations]]
- [[PaymentsTypes]]
- [[PriceListDetails]]
- [[SalesPersons]]
- [[SalesTransDetails]]
- [[SalesTransHeader]]
## Tables Written
- [[SalesTransHeader]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Assets]]
- [[Customers]]
- [[Locations]]
- [[PaymentsTypes]]
- [[PriceListDetails]]
- [[SalesPersons]]
- [[SalesTransDetails]]
- [[SalesTransHeader]]

**Tables Written**
- [[SalesTransHeader]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
