---
type: procedure
database: Olives_BO
name: RouteCoverageSummary_New_Excel
schema: dbo
tags: [#backoffice, #gps, #sales]
reads_from:
  - [[CustomersFinancialDetails]]
  - Fun_Get_Salesmen_AssignedRoutes
  - [[LogActionTransaction]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# RouteCoverageSummary_New_Excel


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersFinancialDetails, Fun_Get_Salesmen_AssignedRoutes, LogActionTransaction, OrdersDetails, OrdersHeaders, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=2
- @salespersonID int=30
- @Fromdate Date ='2023-08-01'
- @Todate Date ='2023-08-20'
## Tables Read
- [[CustomersFinancialDetails]]
- Fun_Get_Salesmen_AssignedRoutes
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomersFinancialDetails]]
- Fun_Get_Salesmen_AssignedRoutes
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
