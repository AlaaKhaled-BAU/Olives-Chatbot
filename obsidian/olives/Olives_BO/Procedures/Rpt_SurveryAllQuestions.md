---
type: procedure
database: Olives_BO
name: Rpt_SurveryAllQuestions
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[SalesPersons]]
  - [[SurveyCustomers]]
  - [[SurveyCustomersAnswers]]
  - [[Surveys_Questions]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SurveryAllQuestions


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, SalesPersons, SurveyCustomers, SurveyCustomersAnswers, Surveys_Questions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @SurveryID int
- @UserID nvarchar(50)
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromSalesman int
- @ToSalesman int
- @FromCustomer Bigint
- @ToCustomer Bigint
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[SalesPersons]]
- [[SurveyCustomers]]
- [[SurveyCustomersAnswers]]
- [[Surveys_Questions]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- [[SalesPersons]]
- [[SurveyCustomers]]
- [[SurveyCustomersAnswers]]
- [[Surveys_Questions]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
