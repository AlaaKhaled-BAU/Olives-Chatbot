---
type: procedure
database: Olives_BO
name: rpt_althurayaRefrshabel_Excel
schema: dbo
tags: [#reporting]
reads_from:
  - Customers
  - CustomersClasses
  - CustomersFinancialDetails
  - CustomersGroups
  - CustomersTypes
  - ERPStores
  - Items
  - ItemsCategories
  - Locations
  - LogActionTransaction
  - OrdersDetails
  - OrdersHeaders
  - SalesPersons
  - SalesPersonsItemsGroups
  - SurveyCustomers
  - Surveys
  - Surveys_Questions
writes_to:
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# rpt_althurayaRefrshabel_Excel

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 17 table(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @FromDate smalldatetime
- @ToDate smalldatetime
## Tables Read
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[CustomersGroups]]
- [[CustomersTypes]]
- [[ERPStores]]
- [[Items]]
- [[ItemsCategories]]
- [[Locations]]
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[SalesPersonsItemsGroups]]
- [[SurveyCustomers]]
- [[Surveys]]
- [[Surveys_Questions]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `GetAnswerDescByID`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
