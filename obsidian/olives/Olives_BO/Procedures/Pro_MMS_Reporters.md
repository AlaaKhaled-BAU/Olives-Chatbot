---
type: procedure
database: Olives_BO
name: Pro_MMS_Reporters
schema: dbo
tags: [#backoffice, #mms, #reporting]
reads_from:
  - [[MMS_Reporters]]
writes_to:
  - [[MMS_Reporters]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_Reporters


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MMS_Reporters. Writes MMS_Reporters. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	= null
- @ReportersID	int	= null
- @Name	nvarchar(100)	= null
- @ForeignName	nvarchar(100)	= null
- @Reference1	nvarchar(100)	= null
- @Reference2	nvarchar(100)	= null
- @cmdType nvarchar(50) = null
## Tables Read
- [[MMS_Reporters]]
## Tables Written
- [[MMS_Reporters]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MMS_Reporters]]

**Tables Written**
- [[MMS_Reporters]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
