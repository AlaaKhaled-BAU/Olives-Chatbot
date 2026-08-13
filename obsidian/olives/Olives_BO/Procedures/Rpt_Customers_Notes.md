---
type: procedure
database: Olives_BO
name: Rpt_Customers_Notes
schema: dbo
tags: [#backoffice, #customer, #reporting]
reads_from:
  - [[Customers]]
  - [[SurveyCustomers]]
  - [[SurveyCustomersAnswers]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_Customers_Notes


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, SurveyCustomers, SurveyCustomersAnswers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int
- @fromdate nvarchar(50)
- @Todate nvarchar(50)
- @Fromcust int
- @Tocust int
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
