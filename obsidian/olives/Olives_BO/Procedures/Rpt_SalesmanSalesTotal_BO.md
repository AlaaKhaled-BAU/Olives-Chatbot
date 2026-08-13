---
type: procedure
database: Olives_BO
name: Rpt_SalesmanSalesTotal_BO
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[Items]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanSalesTotal_BO


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, InvoiceHistoryDF, InvoiceHistoryHF, Items, SalesPersons, SalesPersonsGroups, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1
- @FromSalesman int=23
- @ToSalesman int=23
- @FromGroup int = 0
- @ToGroup int = 99999999
- @CustNo Bigint=-1, -- No Tablet
- @FromDate smalldatetime='2023-05-01'
- @ToDate smalldatetime='2023-05-31'
- @ItemCode varchar(100)='-1'
- @CategCode varchar(100)='169'
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
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
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
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
