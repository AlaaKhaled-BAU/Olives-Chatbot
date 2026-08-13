---
type: procedure
database: Olives_BO
name: Pro_Companies
schema: dbo
tags: [#backoffice]
reads_from:
  - [[ClientsActive]]
  - [[Companies]]
  - Log
writes_to:
  - [[Companies]]
  - Log
called_by:
  - [[OT_SendCompData]]
support_relevance: high
last_verified: 2026-07-05
---
# Pro_Companies


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Companies, Log. Writes Companies, Log. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @ID smallint=1
- @Name nvarchar (200)=null
- @ShortName nvarchar (100)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (40)=null
- @Address nvarchar (400)=null
- @TelephoneNo nvarchar (100)=null
- @FaxNo nvarchar (100)=null
- @POBox nvarchar (100)=null
- @WebSite nvarchar (200)=null
- @Email nvarchar (200)=null
- @Logo image=null
- @Watermark image=null
- @Notes nvarchar (600)=null
- @SalesTaxNum nvarchar (200)=null
- @cmdType varchar(50)=null
- @CurrencyID int=null
- @DataSize int = null
- @LogSize int = null
- @NullData bit = null
- @CID int = null
## Tables Read
- [[ClientsActive]]
- [[Companies]]
- Log
## Tables Written
- [[Companies]]
- Log
## Callers
_None (no known callers)_
## Callees
- [[OT_SendCompData]]
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Companies]]
- Log

**Tables Written**
- [[Companies]]
- Log

**Callers**
- [[OT_SendCompData]]

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
