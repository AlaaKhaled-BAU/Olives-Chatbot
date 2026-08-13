---
type: procedure
database: Olives_BO
name: Pro_SalespersonsMessagesDefinition
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[SalespersonsMessagesDefinition]]
writes_to:
  - [[SalespersonsMessagesDefinition]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalespersonsMessagesDefinition


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalespersonsMessagesDefinition. Writes SalespersonsMessagesDefinition. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID int = null
- @MessageTitle nvarchar (500)=null
- @MessageText nvarchar (max)=null
- @cmdType varchar(50)=null
## Tables Read
- [[SalespersonsMessagesDefinition]]
## Tables Written
- [[SalespersonsMessagesDefinition]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalespersonsMessagesDefinition]]

**Tables Written**
- [[SalespersonsMessagesDefinition]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
