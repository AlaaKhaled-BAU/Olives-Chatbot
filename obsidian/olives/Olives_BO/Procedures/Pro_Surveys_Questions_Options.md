---
type: procedure
database: Olives_BO
name: Pro_Surveys_Questions_Options
schema: dbo
tags: [#backoffice, #survey]
reads_from:
  - [[Surveys_Questions_Options]]
  - `dbo`
writes_to:
  - [[Surveys_Questions_Options]]
  - Surveys_Questions_Options_Images
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_Surveys_Questions_Options


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Surveys_Questions_Options, dbo. Writes Surveys_Questions_Options, Surveys_Questions_Options_Images. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @Survey_ID smallint = null
- @Question_No smallint =null
- @Option_No smallint =null
- @SortID int =null
- @Option_Desc nvarchar (300)=null
- @cmdType varchar(50)=null
- @OptionImage image =null
## Tables Read
- [[Surveys_Questions_Options]]
- `dbo`
## Tables Written
- [[Surveys_Questions_Options]]
- Surveys_Questions_Options_Images
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Surveys_Questions_Options]]
- dbo

**Tables Written**
- [[Surveys_Questions_Options]]
- Surveys_Questions_Options_Images

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
