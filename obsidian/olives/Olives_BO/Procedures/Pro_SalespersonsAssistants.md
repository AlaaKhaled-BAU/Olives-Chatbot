---
type: procedure
database: Olives_BO
name: Pro_SalespersonsAssistants
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[SalespersonsAssistants]]
  - [[SalespersonsAssistantsTransactions]]
  - `dbo`
writes_to:
  - AssistantsImages
  - [[SalespersonsAssistants]]
  - [[SalespersonsAssistantsTransactions]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalespersonsAssistants


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalespersonsAssistants, SalespersonsAssistantsTransactions, dbo. Writes AssistantsImages, SalespersonsAssistants, SalespersonsAssistantsTransactions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID int = null
- @SalesmanID int = null
- @Date SmallDateTime=null
- @ImageID int = null
- @Name nvarchar (100)=null
- @Tel nvarchar (50)=null
- @Ref1 nvarchar (50)=null
- @Ref2 nvarchar (50)=null
- @NationalID nvarchar (50)=null
- @Nationality nvarchar (50)=null
- @Image image=null
- @cmdType varchar(50)=null
- @IsSuspended bit = null
## Tables Read
- [[SalespersonsAssistants]]
- [[SalespersonsAssistantsTransactions]]
- `dbo`
## Tables Written
- AssistantsImages
- [[SalespersonsAssistants]]
- [[SalespersonsAssistantsTransactions]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalespersonsAssistants]]
- [[SalespersonsAssistantsTransactions]]
- dbo

**Tables Written**
- AssistantsImages
- [[SalespersonsAssistants]]
- [[SalespersonsAssistantsTransactions]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
