---
type: procedure
database: Olives_BO
name: Rpt_SalesPerRoute
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersGPSLocations]]
  - Fun_ConvArrayToTable
  - [[Items]]
  - [[Locations]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesPerRoute


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, CustomersGPSLocations, Fun_ConvArrayToTable, Items, Locations, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1
- @FromDate datetime='2023-06-01'
- @ToDate datetime='2023-06-06'
- @Locations nvarchar(max) = null
- @CompanyBranch int=-1
- @FromPrice int = 1
- @ToPrice int = 99999999
- @FromLocation int = 1
- @ToLocation int = 10001
- @Categ nvarchar(max)= '104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,136,137,138,139,140,141,'
- @TaxPerc float= 0
- @OwnAssets bit= 1
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGPSLocations]]
- Fun_ConvArrayToTable
- [[Items]]
- [[Locations]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
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
- [[CustomersGPSLocations]]
- Fun_ConvArrayToTable
- [[Items]]
- [[Locations]]
- [[SalesPersons]]
- [[TransactionsDetails]]
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
