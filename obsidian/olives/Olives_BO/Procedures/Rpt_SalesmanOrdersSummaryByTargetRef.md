---
type: procedure
database: Olives_BO
name: Rpt_SalesmanOrdersSummaryByTargetRef
schema: dbo
tags: [#backoffice, #order, #reporting, #sales]
reads_from:
  - Fun_GetCompanyBranchesByUser
  - [[Items]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
  - [[TargetsReferences]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanOrdersSummaryByTargetRef


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetCompanyBranchesByUser, Items, OrdersDetails, OrdersHeaders, SalesPersons, TargetsReferences. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromDate smalldatetime = '2018-01-01'
- @ToDate smalldatetime = '2018-03-19'
- @FromSalesman int = 0
- @ToSalesman int = 99999999
- @FromTargetRef nvarchar(50) = '0'
- @ToTargetRef nvarchar(50) = 'zzzzzzzzzz'
- @UserID  nvarchar(50) = 'admin'
- @IsMainTarget smallint = 1
## Tables Read
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[TargetsReferences]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[TargetsReferences]]

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
