---
type: procedure
database: Olives_BO
name: Pro_DocumentsTypes
schema: dbo
tags: [#backoffice, #reference]
reads_from:
  - [[DocumentsTypes]]
  - [[TransactionsTypes]]
writes_to:
  - [[DocumentsTypes]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_DocumentsTypes


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads DocumentsTypes, TransactionsTypes. Writes DocumentsTypes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID smallint = null
- @TransactionTypeID smallint = null
- @Name nvarchar (200)=null
- @ShortName nvarchar (100)=null
- @Notes nvarchar (max)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (40)=null
- @IsSuspended bit=null
- @cmdType varchar(50)=null
## Tables Read
- [[DocumentsTypes]]
- [[TransactionsTypes]]
## Tables Written
- [[DocumentsTypes]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[DocumentsTypes]]
- [[TransactionsTypes]]

**Tables Written**
- [[DocumentsTypes]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
