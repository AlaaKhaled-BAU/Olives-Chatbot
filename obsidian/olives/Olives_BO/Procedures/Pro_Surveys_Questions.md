---
type: procedure
database: Olives_BO
name: Pro_Surveys_Questions
schema: dbo
tags: [#backoffice, #survey]
reads_from:
  - [[Surveys]]
  - [[Surveys_Questions]]
  - [[Surveys_Questions_Options]]
  - `dbo`
writes_to:
  - [[Surveys_Questions]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_Surveys_Questions


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Surveys, Surveys_Questions, Surveys_Questions_Options, dbo. Writes Surveys_Questions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @Survey_ID smallint = null
- @Question_No smallint =null
- @Template_No smallint =null
- @Question_String nvarchar (300)=null
- @cmdType varchar(50)=null
- @SortID int = null
- @IsRequired int = null
## Tables Read
- [[Surveys]]
- [[Surveys_Questions]]
- [[Surveys_Questions_Options]]
- `dbo`
## Tables Written
- [[Surveys_Questions]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Surveys]]
- [[Surveys_Questions]]
- [[Surveys_Questions_Options]]
- dbo

**Tables Written**
- [[Surveys_Questions]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
