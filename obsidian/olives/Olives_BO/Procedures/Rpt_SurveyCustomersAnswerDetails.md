---
type: procedure
database: Olives_BO
name: Rpt_SurveyCustomersAnswerDetails
schema: dbo
tags: [#backoffice, #customer, #reporting, #survey]
reads_from:
  - [[Customers]]
  - [[SalesPersons]]
  - [[SurveyCustomers]]
  - [[SurveyCustomersAnswers]]
  - [[Surveys]]
  - [[Surveys_Questions]]
  - [[Surveys_Questions_Options]]
  - tmp
writes_to:
  - tmp
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SurveyCustomersAnswerDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, SalesPersons, SurveyCustomers, SurveyCustomersAnswers, Surveys, Surveys_Questions, Surveys_Questions_Options, tmp. Writes tmp. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromDate smalldatetime='2018-05-27'
- @ToDate smalldatetime='2019-03-01'
- @FromSalesmanNo int = 0
- @ToSalesmanNo int = 999999
- @FromCust bigint = 0
- @ToCust bigint = 99999999
- @FromSurveyID int = 0
- @ToSurveyID int = 9999
- @UserID nvarchar(50) = null
## Tables Read
- [[Customers]]
- [[SalesPersons]]
- [[SurveyCustomers]]
- [[SurveyCustomersAnswers]]
- [[Surveys]]
- [[Surveys_Questions]]
- [[Surveys_Questions_Options]]
- tmp
## Tables Written
- tmp
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[SalesPersons]]
- [[SurveyCustomers]]
- [[SurveyCustomersAnswers]]
- [[Surveys]]
- [[Surveys_Questions]]
- [[Surveys_Questions_Options]]
- tmp

**Tables Written**
- tmp

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
