---
type: procedure
database: Olives_BO
name: Rpt_CustomerSalesByItems
schema: dbo
tags: [#backoffice, #customer, #inventory, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - Fun_GetCompanyBranchesByUser
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomerSalesByItems


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, Fun_GetCompanyBranchesByUser, InvoiceHistoryDF, InvoiceHistoryHF, Items, ItemsCategories, SalesPersons, SalesPersonsGroups, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromItem varchar(100)
- @ToItem varchar(100)
- @FromCustomer bigint
- @ToCustomer bigint
- @FromGroup int = 0
- @ToGroup int = 99999999
- @FromSalesman int
- @ToSalesman int
- @FromCateg nvarchar(20)='0'
- @ToCateg nvarchar(20)='zzzzzzzzzzzzzzzz'
- @UserID nvarchar(50)=null
- @TransType Smallint
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- Fun_GetCompanyBranchesByUser
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[ItemsCategories]]
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
- Fun_GetCompanyBranchesByUser
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[ItemsCategories]]
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
