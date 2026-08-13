---
type: procedure
database: Olives_BO
name: Diag_Check_Linked_Sales_Cust_Promotions
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersPromotionsGroups]]
  - [[CustomersPromotionsGroupsLink]]
  - [[PromotionsCustomersGroupsLink]]
  - [[PromotionsHeaders]]
  - [[PromotionsSalesmanGroupsLink]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Diag_Check_Linked_Sales_Cust_Promotions


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersPromotionsGroups, CustomersPromotionsGroupsLink, PromotionsCustomersGroupsLink, PromotionsHeaders, PromotionsSalesmanGroupsLink, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @compID smallint
- @salespersonsid int
- @CustomerID bigint
- @PromotionID int
## Tables Read
- [[Customers]]
- [[CustomersPromotionsGroups]]
- [[CustomersPromotionsGroupsLink]]
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- [[PromotionsSalesmanGroupsLink]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersPromotionsGroups]]
- [[CustomersPromotionsGroupsLink]]
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- [[PromotionsSalesmanGroupsLink]]
- [[SalesPersons]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
