---
type: procedure
database: Olives_BO
name: Falcons_GetItemBalance
schema: dbo
tags: [#backoffice, #inventory]
reads_from:
  - [[Checks]]
  - [[ClientsActive]]
  - [[Companies]]
  - [[CompanyBranches]]
  - [[Currencies]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersGPSLocations]]
  - DBO
  - Fun_ConvArrayToTable
  - Fun_GetCompanyBranchesByUser
  - Fun_GetCustomersByLocations
  - Fun_GetSalesPersonFullTree
  - Fun_GetSalesmanTreeByID
  - [[InvoiceHistoryDF]]
writes_to:
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Falcons_GetItemBalance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, ClientsActive, Companies, CompanyBranches, Currencies, Customers, CustomersFinancialDetails, CustomersGPSLocations, DBO, Fun_ConvArrayToTable, Fun_GetCompanyBranchesByUser, Fun_GetCustomersByLocations, Fun_GetSalesPersonFullTree, Fun_GetSalesmanTreeByID, InvoiceHistoryDF. Writes SalesPersonItemsBalance, SalesPersons. Invoked by 2 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
- @SalesmanNo int
- @SendDate smalldatetime = null
## Tables Read
- [[Checks]]
- [[ClientsActive]]
- [[Companies]]
- [[CompanyBranches]]
- [[Currencies]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGPSLocations]]
- DBO
- Fun_ConvArrayToTable
- Fun_GetCompanyBranchesByUser
- Fun_GetCustomersByLocations
- Fun_GetSalesPersonFullTree
- Fun_GetSalesmanTreeByID
- [[InvoiceHistoryDF]]
## Tables Written
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
## Callers
- [[Falcons_UpdateItemBalance]]
- [[OT_SendSalesmanData]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Checks]]
- [[ClientsActive]]
- [[Companies]]
- [[CompanyBranches]]
- [[Currencies]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGPSLocations]]
- DBO
- Fun_ConvArrayToTable
- Fun_GetCompanyBranchesByUser
- Fun_GetCustomersByLocations
- Fun_GetSalesPersonFullTree
- Fun_GetSalesmanTreeByID
- [[InvoiceHistoryDF]]

**Tables Written**
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]

**Callers**
_None_

**Callees**
- [[Falcons_UpdateItemBalance]]
- [[OT_SendSalesmanData]]


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
