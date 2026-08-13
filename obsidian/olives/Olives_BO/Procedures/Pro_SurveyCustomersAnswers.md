---
type: procedure
database: Olives_BO
name: Pro_SurveyCustomersAnswers
schema: dbo
tags: [#backoffice, #customer, #survey]
reads_from:
  - [[SurveyCustomersAnswers]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SurveyCustomersAnswers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SurveyCustomersAnswers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @cmdType nvarchar(50) = null
- @CompanyID smallint = null
- @Cust_Survey_No bigint = null
- @Question_No int = null
- @Answer nvarchar(1000) = null
## Tables Read
- [[SurveyCustomersAnswers]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SurveyCustomersAnswers]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
