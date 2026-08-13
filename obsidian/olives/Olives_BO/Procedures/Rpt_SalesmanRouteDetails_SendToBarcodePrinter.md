---
type: procedure
database: Olives_BO
name: Rpt_SalesmanRouteDetails_SendToBarcodePrinter
schema: dbo
tags: [#backoffice, #gps, #inventory, #reference, #reporting, #sales]
reads_from:
  - [[Companies]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - Fun_ConvArrayToTable
  - [[PriceLists]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[SalesPersonsRoutes]]
  - `dbo`
writes_to:
  - tmpSalesmanRouteDetails
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanRouteDetails_SendToBarcodePrinter


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, Customers, CustomersFinancialDetails, Fun_ConvArrayToTable, PriceLists, RoutesInformation, SalesPersons, SalesPersonsRoutes, dbo. Writes tmpSalesmanRouteDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @SalesmanArray VARCHAR(MAX)
- @WeekNoArray  VARCHAR(MAX)
- @WeekDayArray  VARCHAR(MAX)
## Tables Read
- [[Companies]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_ConvArrayToTable
- [[PriceLists]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- `dbo`
## Tables Written
- tmpSalesmanRouteDetails
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Companies]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_ConvArrayToTable
- [[PriceLists]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- dbo

**Tables Written**
- tmpSalesmanRouteDetails

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
