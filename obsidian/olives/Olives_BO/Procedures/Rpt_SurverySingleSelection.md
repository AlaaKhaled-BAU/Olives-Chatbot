---
type: procedure
database: Olives_BO
name: Rpt_SurverySingleSelection
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - Fun_Surveys
  - Fun_SurveysCustomersAnswers
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SurverySingleSelection


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, Fun_Surveys, Fun_SurveysCustomersAnswers, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
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
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_Surveys
- Fun_SurveysCustomersAnswers
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_Surveys
- Fun_SurveysCustomersAnswers
- [[SalesPersons]]

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
