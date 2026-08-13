---
type: procedure
database: Olives_BO
name: Rpt_CustomersOrdersSummary
schema: dbo
tags: [#backoffice, #customer, #order, #reporting]
reads_from:
  - [[Customers]]
  - [[CustomersTypes]]
  - Fun_GetCompanyBranchesByUser
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomersOrdersSummary


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersTypes, Fun_GetCompanyBranchesByUser, OrdersDetails, OrdersHeaders, SalesPersons, SalesPersonsGroups. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromDate smalldatetime='2020-06-22'
- @ToDate smalldatetime='2023-01-01'
- @FromCust bigint=1
- @Tocust bigint=99999999
- @FromCustType int=1
- @ToCustType int=999999
- @FromGroup int = 1
- @ToGroup int = 9999999
- @UserID nvarchar(50)='admin'
## Tables Read
- [[Customers]]
- [[CustomersTypes]]
- Fun_GetCompanyBranchesByUser
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersTypes]]
- Fun_GetCompanyBranchesByUser
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]

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
