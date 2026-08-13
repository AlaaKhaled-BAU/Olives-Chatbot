---
type: procedure
database: Olives_BO
name: Rpt_NotSoldPerCateg
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[AssetsCustomerLink]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersGPSLocations]]
  - Fun_ConvArrayToTable
  - Fun_IsHaveAssets
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
# Rpt_NotSoldPerCateg


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads AssetsCustomerLink, Customers, CustomersFinancialDetails, CustomersGPSLocations, Fun_ConvArrayToTable, Fun_IsHaveAssets, Items, Locations, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint =1
- @LocationID nvarchar(max)=' 401,'
- @ItemCateg nvarchar (max)=' 104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,136,137,138,139,140,141,142,143,144,145,'
- @CompanyBarnch smallint =0
- @IsHaveAssets bit=-1
- @FromDate datetime='2025-02-01'
- @ToDate datetime='2025-02-24'
## Tables Read
- [[AssetsCustomerLink]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGPSLocations]]
- Fun_ConvArrayToTable
- Fun_IsHaveAssets
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
- [[AssetsCustomerLink]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGPSLocations]]
- Fun_ConvArrayToTable
- Fun_IsHaveAssets
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
