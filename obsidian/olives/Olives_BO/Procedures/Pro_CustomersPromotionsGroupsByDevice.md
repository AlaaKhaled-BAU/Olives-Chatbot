---
type: procedure
database: Olives_BO
name: Pro_CustomersPromotionsGroupsByDevice
schema: dbo
tags: [#backoffice, #customer, #reference, #sales]
reads_from:
  - CHKCursor
  - [[Customers]]
  - [[CustomersPromotionsExceptions]]
  - [[CustomersPromotionsGroups]]
  - [[CustomersPromotionsGroupsLink]]
  - Fun_ConvArrayToTable
  - [[PromotionsCustomersGroupsLink]]
  - [[PromotionsHeaders]]
  - [[PromotionsSalesmanGroupsLink]]
  - [[SalesPersons]]
writes_to:
  - [[CustomersPromotionsExceptions]]
  - [[CustomersPromotionsGroups]]
  - [[CustomersPromotionsGroupsLink]]
  - [[PromotionsCustomersGroupsLink]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CustomersPromotionsGroupsByDevice


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CHKCursor, Customers, CustomersPromotionsExceptions, CustomersPromotionsGroups, CustomersPromotionsGroupsLink, Fun_ConvArrayToTable, PromotionsCustomersGroupsLink, PromotionsHeaders, PromotionsSalesmanGroupsLink, SalesPersons. Writes CustomersPromotionsExceptions, CustomersPromotionsGroups, CustomersPromotionsGroupsLink, PromotionsCustomersGroupsLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @cmdType varchar(50)='Select All'
- @CustomerID bigint=314
- @SalesmanNo int=3003
- @CustomersPromotionsGroupsIDs varchar(MAX)='342,343,'
- @CustomersPromotionsIDsNotSelected varchar(MAX)='351,352,350,'
## Tables Read
- CHKCursor
- [[Customers]]
- [[CustomersPromotionsExceptions]]
- [[CustomersPromotionsGroups]]
- [[CustomersPromotionsGroupsLink]]
- Fun_ConvArrayToTable
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- [[PromotionsSalesmanGroupsLink]]
- [[SalesPersons]]
## Tables Written
- [[CustomersPromotionsExceptions]]
- [[CustomersPromotionsGroups]]
- [[CustomersPromotionsGroupsLink]]
- [[PromotionsCustomersGroupsLink]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- CHKCursor
- [[Customers]]
- [[CustomersPromotionsExceptions]]
- [[CustomersPromotionsGroups]]
- [[CustomersPromotionsGroupsLink]]
- Fun_ConvArrayToTable
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- [[PromotionsSalesmanGroupsLink]]
- [[SalesPersons]]

**Tables Written**
- [[CustomersPromotionsExceptions]]
- [[CustomersPromotionsGroups]]
- [[CustomersPromotionsGroupsLink]]
- [[PromotionsCustomersGroupsLink]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
