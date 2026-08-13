---
type: procedure
database: Olives_BO
name: RPT_ZheimanRouteSummaryForExcel
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - [[CustomersFinancialDetails]]
  - Fun_Get_Salesmen_AssignedRoutes
  - [[LogActionTransaction]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[SalesPersonsRoutes]]
  - Start
  - employee_cursor
  - the
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-07-05
---
# RPT_ZheimanRouteSummaryForExcel


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CustomersFinancialDetails, Fun_Get_Salesmen_AssignedRoutes, LogActionTransaction, RoutesInformation, SalesPersons, SalesPersonsRoutes, Start, employee_cursor, the, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID_ smallint=2
- @FomSalespersonGroup int=09
- @ToSalespersonGroup int=100
- @FromDate1 date= '2024-11-01'
- @ToDate2 date='2024-11-09'
## Tables Read
- [[ClientsActive]]
- [[CustomersFinancialDetails]]
- Fun_Get_Salesmen_AssignedRoutes
- [[LogActionTransaction]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- Start
- employee_cursor
- the
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[CustomersFinancialDetails]]
- Fun_Get_Salesmen_AssignedRoutes
- [[LogActionTransaction]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- Start
- employee_cursor
- the
- [[transactionsheaders]]

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
