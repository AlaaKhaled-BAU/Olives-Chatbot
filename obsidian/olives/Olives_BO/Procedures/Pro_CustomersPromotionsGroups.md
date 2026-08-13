---
type: procedure
database: Olives_BO
name: Pro_CustomersPromotionsGroups
schema: dbo
tags: [#backoffice, #customer, #reference, #sales]
reads_from:
  - [[CompanyBranches]]
  - [[CustomersPromotionsGroups]]
  - [[PromotionsCustomersGroupsLink]]
  - [[UserCustomersPromotionsGroupLink]]
  - [[Users]]
  - int
writes_to:
  - [[CustomersPromotionsGroups]]
  - [[UserCustomersPromotionsGroupLink]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CustomersPromotionsGroups


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CompanyBranches, CustomersPromotionsGroups, PromotionsCustomersGroupsLink, UserCustomersPromotionsGroupLink, Users, int. Writes CustomersPromotionsGroups, UserCustomersPromotionsGroupLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID smallint = null
- @Name nvarchar (200)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (40)=null
- @cmdType varchar(50)=null
- @UserID nvarchar(50)=null
- @PromotionID int=null
- @CopyFrom int = null
- @AppUser varchar(200) = null
## Tables Read
- [[CompanyBranches]]
- [[CustomersPromotionsGroups]]
- [[PromotionsCustomersGroupsLink]]
- [[UserCustomersPromotionsGroupLink]]
- [[Users]]
- int
## Tables Written
- [[CustomersPromotionsGroups]]
- [[UserCustomersPromotionsGroupLink]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CompanyBranches]]
- [[CustomersPromotionsGroups]]
- [[PromotionsCustomersGroupsLink]]
- [[UserCustomersPromotionsGroupLink]]
- [[Users]]
- int

**Tables Written**
- [[CustomersPromotionsGroups]]
- [[UserCustomersPromotionsGroupLink]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
