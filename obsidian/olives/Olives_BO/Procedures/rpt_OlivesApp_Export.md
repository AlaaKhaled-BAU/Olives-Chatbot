---
type: procedure
database: Olives_BO
name: rpt_OlivesApp_Export
schema: dbo
tags: [#integration, #reporting]
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
writes_to:
called_by:
  - rpt_OlivesApp_Export_ByUser
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# rpt_OlivesApp_Export

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 15 table(s); called by 1 proc(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @FromDate date
- @ToDate date
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
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
- [[rpt_OlivesApp_Export_ByUser]]
## Callees
- `GetAnswerDescByID`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
