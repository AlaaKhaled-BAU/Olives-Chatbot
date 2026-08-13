---
type: procedure
database: Olives_BO
name: Pro_CustomersPromotionsGroupsLink
schema: dbo
tags: [#backoffice, #customer, #reference, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersClasses]]
  - [[CustomersFinancialDetails]]
  - [[CustomersPromotionsGroupsLink]]
  - [[CustomersTypes]]
  - Group
  - [[PriceLists]]
  - [[UserCompanyBranchesLink]]
  - [[Users]]
writes_to:
  - [[CustomersPromotionsGroupsLink]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CustomersPromotionsGroupsLink


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, CustomersClasses, CustomersFinancialDetails, CustomersPromotionsGroupsLink, CustomersTypes, Group, PriceLists, UserCompanyBranchesLink, Users. Writes CustomersPromotionsGroupsLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @CustomerID  bigint = null
- @CustomersPromotionsGroupsID int = null
- @Name nvarchar (200)=null
- @Reference1 nvarchar (40)=null
- @cmdType varchar(50)=null
- @CustomersPromotionsGroupsLink_DATATABLE CustomersPromotionsGroupsLink_Type  readonly
- @ToGroupID int = null
- @AssignCustomersPromotionsGroups AssignCustomersPromotionsGroups readonly
- @UserID nvarchar(100)=null
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[CustomersPromotionsGroupsLink]]
- [[CustomersTypes]]
- Group
- [[PriceLists]]
- [[UserCompanyBranchesLink]]
- [[Users]]
## Tables Written
- [[CustomersPromotionsGroupsLink]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[CustomersPromotionsGroupsLink]]
- [[CustomersTypes]]
- Group
- [[PriceLists]]
- [[UserCompanyBranchesLink]]
- [[Users]]

**Tables Written**
- [[CustomersPromotionsGroupsLink]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
