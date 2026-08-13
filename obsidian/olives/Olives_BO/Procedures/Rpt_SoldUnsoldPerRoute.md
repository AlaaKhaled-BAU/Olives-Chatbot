---
type: procedure
database: Olives_BO
name: Rpt_SoldUnsoldPerRoute
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[AssetsCustomerLink]]
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersGPSLocations]]
  - [[Locations]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SoldUnsoldPerRoute


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads AssetsCustomerLink, ClientsActive, Customers, CustomersFinancialDetails, CustomersGPSLocations, Locations, SalesPersons, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1
- @FromDate datetime='2015-04-18'
- @ToDate datetime='2024-04-18'
- @CompanyBranch int=-1
- @FromLocation int = 1
- @ToLocation int = 1
- @OwnAssets int= -1
- @IsSuspended int=-1
## Tables Read
- [[AssetsCustomerLink]]
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGPSLocations]]
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
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGPSLocations]]
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
