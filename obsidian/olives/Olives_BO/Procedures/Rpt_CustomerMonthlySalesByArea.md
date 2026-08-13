---
type: procedure
database: Olives_BO
name: Rpt_CustomerMonthlySalesByArea
schema: dbo
tags: [#backoffice, #customer, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersTypes]]
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[Locations]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[ClientsActive]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomerMonthlySalesByArea


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersTypes, InvoiceHistoryDF, InvoiceHistoryHF, Items, ItemsCategories, Locations, SalesPersons, SalesPersonsGroups, TransactionsDetails, TransactionsHeaders, ClientsActive. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @Year smallint
- @FromMonth smallint
- @ToMonth smallint
- @FromItem varchar(100)
- @ToItem varchar(100)
- @FromCustomer bigint
- @ToCustomer bigint
- @FromLocID int
- @ToLocID int
- @FromGroup int = 0
- @ToGroup int = 99999999
- @FromSalesman int=1
- @ToSalesman int=99999
- @UserID nvarchar(50)=null
## Tables Read
- [[Customers]]
- [[CustomersTypes]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[ItemsCategories]]
- [[Locations]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[ClientsActive]]
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
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[ItemsCategories]]
- [[Locations]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[clientsactive]]

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
