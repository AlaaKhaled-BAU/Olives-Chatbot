---
type: procedure
database: Olives_BO
name: Rpt_UnloadCustomersPerRoute
schema: dbo
tags: [#backoffice, #customer, #gps, #order, #reporting, #sales]
reads_from:
  - [[AssetsCustomerLink]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersGPSLocations]]
  - Fun_ConvArrayToTable
  - [[Locations]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_UnloadCustomersPerRoute


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads AssetsCustomerLink, Customers, CustomersFinancialDetails, CustomersGPSLocations, Fun_ConvArrayToTable, Locations, SalesPersons, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int
- @FromDate datetime
- @ToDate datetime
- @Locations nvarchar(max)
- @CompanyBranch int
- @FromPrice int = null
- @ToPrice int = null
- @OwnAssets bit= null
## Tables Read
- [[AssetsCustomerLink]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGPSLocations]]
- Fun_ConvArrayToTable
- [[Locations]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[AssetsCustomerLink]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGPSLocations]]
- Fun_ConvArrayToTable
- [[Locations]]
- [[SalesPersons]]
- [[TransactionsHeaders]]

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
