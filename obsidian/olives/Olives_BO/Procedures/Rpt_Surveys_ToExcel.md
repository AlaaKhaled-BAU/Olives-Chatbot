---
type: procedure
database: Olives_BO
name: Rpt_Surveys_ToExcel
schema: dbo
tags: [#reporting]
reads_from:
  - Customers
  - SalesPersons
  - SurveyCustomers
  - SurveyCustomersAnswers
  - Surveys
  - Surveys_Questions
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Rpt_Surveys_ToExcel

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 6 table(s); calls 2 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromSales int
- @ToSales int
- @FromCustomer bigint
- @ToCustomer bigint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @UserID nvarchar(50)
## Tables Read
- [[Customers]]
- [[SalesPersons]]
- [[SurveyCustomers]]
- [[SurveyCustomersAnswers]]
- [[Surveys]]
- [[Surveys_Questions]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_GetFromDate`
- `Fun_GetSurveyAnswer`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
