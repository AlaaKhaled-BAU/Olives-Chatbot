---
type: procedure
database: Olives_BO
name: Pro_SalesPersonsMessages
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[SalespersonsMessages]]
writes_to:
  - [[SalespersonsMessages]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesPersonsMessages


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersons, SalesPersonsGroups, SalespersonsMessages. Writes SalespersonsMessages. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID int = null
- @GroupID int  = null
- @Message nvarchar(max) = null
- @UserID nvarchar(50) = null
- @MsgID bigint = null
- @cmdType nvarchar(50) = null
## Tables Read
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[SalespersonsMessages]]
## Tables Written
- [[SalespersonsMessages]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[SalespersonsMessages]]

**Tables Written**
- [[SalespersonsMessages]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
