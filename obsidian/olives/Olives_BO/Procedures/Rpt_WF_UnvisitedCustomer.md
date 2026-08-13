---
type: procedure
database: Olives_BO
name: Rpt_WF_UnvisitedCustomer
schema: dbo
tags: [#auth, #backoffice, #customer, #reporting, #sales, #workflow]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - Fun_GetSalesmanTreeByID
  - [[LogActionTransaction]]
  - [[SalesPersons]]
  - [[SalesPersonsRoutes]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_WF_UnvisitedCustomer


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, Fun_GetSalesmanTreeByID, LogActionTransaction, SalesPersons, SalesPersonsRoutes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=1
- @FromDate  smalldatetime
- @ToDate smalldatetime
- @SuperVisorID int=1
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetSalesmanTreeByID
- [[LogActionTransaction]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
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
- Fun_GetSalesmanTreeByID
- [[LogActionTransaction]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]

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
