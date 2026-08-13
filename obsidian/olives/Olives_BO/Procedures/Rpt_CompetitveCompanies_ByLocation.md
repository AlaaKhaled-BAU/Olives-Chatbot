---
type: procedure
database: Olives_BO
name: Rpt_CompetitveCompanies_ByLocation
schema: dbo
tags: [#backoffice, #gps, #reporting]
reads_from:
  - [[Customers]]
  - [[SurveyCustomers]]
  - [[SurveyCustomersAnswers]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CompetitveCompanies_ByLocation


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, SurveyCustomers, SurveyCustomersAnswers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int
- @FromCustomerID bigint
- @ToCustomerID bigint
- @FromDate varchar(50), -- Keep the parameter type as varchar
- @ToDate varchar(50) -- Keep the parameter type as varchar
## Tables Read
- [[Customers]]
- [[SurveyCustomers]]
- [[SurveyCustomersAnswers]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[SurveyCustomers]]
- [[SurveyCustomersAnswers]]

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
