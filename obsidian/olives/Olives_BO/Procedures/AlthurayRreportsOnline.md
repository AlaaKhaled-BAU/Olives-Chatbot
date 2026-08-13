---
type: procedure
database: Olives_BO
name: AlthurayRreportsOnline
schema: dbo
tags: [#reporting]
reads_from:
  - Customers
  - CustomersTypes
  - ERPStores
  - Items
  - ItemsCategories
  - ItemsUnits
  - Locations
  - LogActionTransaction
  - OrdersDetails
  - OrdersHeaders
  - SalesPersons
  - SurveyCustomers
  - Surveys
  - Surveys_Questions
  - SystemCodes
  - TransactionsDetails
  - TransactionsHeaders
  - Vacations
writes_to:
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# AlthurayRreportsOnline

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 18 table(s); calls 3 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @FromDate datetime
- @ToDate datetime
- @SalesmanNo int
- @CMD nvarchar(100)
## Tables Read
- [[Customers]]
- [[CustomersTypes]]
- [[ERPStores]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Locations]]
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[SurveyCustomers]]
- [[Surveys]]
- [[Surveys_Questions]]
- [[SystemCodes]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[Vacations]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_GetSalesmanTreeByID`
- `Fun_GetTotalAmount`
- `GetAnswerDescByID`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
