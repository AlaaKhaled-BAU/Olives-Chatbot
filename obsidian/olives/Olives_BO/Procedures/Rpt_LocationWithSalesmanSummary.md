---
type: procedure
database: Olives_BO
name: Rpt_LocationWithSalesmanSummary
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersTypes]]
  - Fun_GetCustomerTotalSales
  - Fun_GetMultiLocationTree
  - [[Locations]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_LocationWithSalesmanSummary


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersTypes, Fun_GetCustomerTotalSales, Fun_GetMultiLocationTree, Locations, SalesPersons, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int = 1
- @LocationID nvarchar(max) = '1,38,44,'
- @FromSalesman int = 1
- @ToSalesman int = 99999
- @FromDate smalldatetime = '2024-07-01'
- @ToDate smalldatetime = '2024-10-01'
- @UserID nvarchar(50) = 'admin'
## Tables Read
- [[Customers]]
- [[CustomersTypes]]
- Fun_GetCustomerTotalSales
- Fun_GetMultiLocationTree
- [[Locations]]
- [[SalesPersons]]
- `dbo`
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
- Fun_GetCustomerTotalSales
- Fun_GetMultiLocationTree
- [[Locations]]
- [[SalesPersons]]
- dbo

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
