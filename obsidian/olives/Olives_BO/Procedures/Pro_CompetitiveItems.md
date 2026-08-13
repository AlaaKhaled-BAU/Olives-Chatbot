---
type: procedure
database: Olives_BO
name: Pro_CompetitiveItems
schema: dbo
tags: [#backoffice, #inventory]
reads_from:
  - [[CompetitiveItems]]
  - [[Items]]
writes_to:
  - [[CompetitiveItems]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CompetitiveItems


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CompetitiveItems, Items. Writes CompetitiveItems. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @CompetitiveItemCode nvarchar(100) = null
- @Name nvarchar (200)=null
- @ItemCode nvarchar(100) = null
- @CategCode nvarchar (100) = null
- @CompetitiveCompany nvarchar (100) = null
- @ItemImage Image = null
- @cmdType varchar(50)=null
## Tables Read
- [[CompetitiveItems]]
- [[Items]]
## Tables Written
- [[CompetitiveItems]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CompetitiveItems]]
- [[Items]]

**Tables Written**
- [[CompetitiveItems]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
