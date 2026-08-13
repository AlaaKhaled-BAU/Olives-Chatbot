---
type: procedure
database: Olives_BO
name: Pro_PriceList_PromGroup_SalesLink
schema: dbo
tags: [#backoffice, #billing, #reference, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersPromotionsGroupsLink]]
  - insert
writes_to:
  - [[CustomersFinancialDetails]]
  - [[CustomersPromotionsGroupsLink]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_PriceList_PromGroup_SalesLink


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, CustomersFinancialDetails, CustomersPromotionsGroupsLink, insert. Writes CustomersFinancialDetails, CustomersPromotionsGroupsLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @PriceListsID int = 2
- @FromCustID bigint = 1
- @ToCustID bigint = 99999999999999
- @CustomersPromotionsGroupsID int=7
- @PositionsID int = 678
- @cmdType varchar(50)='Update'
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPromotionsGroupsLink]]
- insert
## Tables Written
- [[CustomersFinancialDetails]]
- [[CustomersPromotionsGroupsLink]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPromotionsGroupsLink]]
- insert

**Tables Written**
- [[CustomersFinancialDetails]]
- [[CustomersPromotionsGroupsLink]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
