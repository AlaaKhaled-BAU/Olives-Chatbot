---
type: procedure
database: Olives_BO
name: Rpt_SurveyCustomers
schema: dbo
tags: [#reporting]
reads_from:
  - Customers
  - CustomersClasses
  - Locations
  - SalesPersons
  - SurveyCustomers
  - SurveyCustomersAnswers
  - Surveys_Questions
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Rpt_SurveyCustomers

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 7 table(s); calls 2 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @SalesmanNo int
- @CustomerNo int
- @ImageDate datetime
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromCustomer bigint
- @ToCustomer bigint
- @URL nvarchar(200)
- @cmdType nvarchar(50)
## Tables Read
- [[Customers]]
- [[CustomersClasses]]
- [[Locations]]
- [[SalesPersons]]
- [[SurveyCustomers]]
- [[SurveyCustomersAnswers]]
- [[Surveys_Questions]]
## Tables Written
_None_
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[OSFA_DB/Tables/OT_CustGalaryImages|OT_CustGalaryImages]]
## Callers
_None_
## Callees
- `Fun_GetCustomersGalleryData`
- `GetAnswerDescByID`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
