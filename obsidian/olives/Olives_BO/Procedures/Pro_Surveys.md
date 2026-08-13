---
type: procedure
database: Olives_BO
name: Pro_Surveys
schema: dbo
tags: [#backoffice, #survey]
reads_from:
  - [[SurveySalesPersonsAssignment]]
  - [[Surveys]]
  - [[Surveys_Questions]]
  - [[Surveys_Questions_Options]]
  - `dbo`
writes_to:
  - [[Surveys]]
  - [[SurveySalesPersonsAssignment]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_Surveys


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SurveySalesPersonsAssignment, Surveys, Surveys_Questions, Surveys_Questions_Options, dbo. Writes Surveys, SurveySalesPersonsAssignment. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @Survey_ID smallint = null
- @Active bit = null
- @IsRequired bit = null
- @IsSalesmanSurvey bit = null
- @Survey_Name nvarchar (200)=null
- @cmdType varchar(50)=null
- @SalesPersonsID int = null
## Tables Read
- [[SurveySalesPersonsAssignment]]
- [[Surveys]]
- [[Surveys_Questions]]
- [[Surveys_Questions_Options]]
- `dbo`
## Tables Written
- [[Surveys]]
- [[SurveySalesPersonsAssignment]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SurveySalesPersonsAssignment]]
- [[Surveys]]
- [[Surveys_Questions]]
- [[Surveys_Questions_Options]]
- dbo

**Tables Written**
- [[Surveys]]
- [[SurveySalesPersonsAssignment]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
