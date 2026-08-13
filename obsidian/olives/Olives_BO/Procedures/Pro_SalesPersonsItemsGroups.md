---
type: procedure
database: Olives_BO
name: Pro_SalesPersonsItemsGroups
schema: dbo
tags: [#backoffice, #inventory, #reference, #sales]
reads_from:
  - [[SalesPersonsItemsGroups]]
  - [[ClientsActive]]
writes_to:
  - [[SalesPersonsItemsGroups]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesPersonsItemsGroups


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersonsItemsGroups, ClientsActive. Writes SalesPersonsItemsGroups. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID int = null
- @Name nvarchar (200)=null
- @ShortName nvarchar (100)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (40)=null
- @cmdType varchar(50)=null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @UserID nvarchar(100)=null
## Tables Read
- [[SalesPersonsItemsGroups]]
- [[ClientsActive]]
## Tables Written
- [[SalesPersonsItemsGroups]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalesPersonsItemsGroups]]
- [[clientsactive]]

**Tables Written**
- [[SalesPersonsItemsGroups]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
