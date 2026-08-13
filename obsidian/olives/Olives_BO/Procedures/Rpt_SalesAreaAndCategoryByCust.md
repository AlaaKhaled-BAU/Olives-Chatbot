---
type: procedure
database: Olives_BO
name: Rpt_SalesAreaAndCategoryByCust
schema: dbo
tags: [#backoffice, #reference, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersGPSLocations]]
  - Fun_ConvArrayToTable
  - Fun_GetCompanyBranchesByUser
  - [[Items]]
  - [[ItemsCategories]]
  - [[Locations]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesAreaAndCategoryByCust


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, CustomersFinancialDetails, CustomersGPSLocations, Fun_ConvArrayToTable, Fun_GetCompanyBranchesByUser, Items, ItemsCategories, Locations, SalesPersons, SalesPersonsGroups, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromDate smalldatetime='04-04-2022'
- @ToDate smalldatetime='04-04-2024'
- @FromItem VARCHAR(100)='0'
- @ToItem VARCHAR(100)='zzzzzzzzzzzzzzzzzzz'
- @Categs VARCHAR(100)='104,105,106,'
- @Location int=-1
- @UserID NVARCHAR(50)='admin'
- @FromCustomer bigint
- @ToCustomer bigint
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGPSLocations]]
- Fun_ConvArrayToTable
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[ItemsCategories]]
- [[Locations]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
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
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGPSLocations]]
- Fun_ConvArrayToTable
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[ItemsCategories]]
- [[Locations]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
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
