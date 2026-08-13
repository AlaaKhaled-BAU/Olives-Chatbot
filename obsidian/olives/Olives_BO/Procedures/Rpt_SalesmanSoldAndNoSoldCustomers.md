---
type: procedure
database: Olives_BO
name: Rpt_SalesmanSoldAndNoSoldCustomers
schema: dbo
tags: [#backoffice, #customer, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[Items]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanSoldAndNoSoldCustomers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, InvoiceHistoryDF, InvoiceHistoryHF, Items, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1
- @SalesmanNo int=24, -- Current In Tablet
- @FromDate smalldatetime='2023-09-01'
- @ToDate smalldatetime='2023-09-30'
- @ItemCode varchar(100)='-1'
- @CategCode varchar(100)='196-12'
- @RepType varchar(100)='Sold'
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
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
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
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
