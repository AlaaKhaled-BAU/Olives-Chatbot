---
type: procedure
database: Olives_BO
name: Rpt_TargetSpartan
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[CustomersFinancialDetails]]
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[Items]]
  - [[LogActionTransaction]]
  - ON
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[Receipts]]
  - [[SalesPersonTargets]]
  - [[SalesPersonTargetsDetails]]
  - [[SalesPersonTargetsOffDays]]
  - [[SalesPersons]]
  - [[TargetsReferences]]
  - [[TransactionsDetails]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_TargetSpartan


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersFinancialDetails, InvoiceHistoryDF, InvoiceHistoryHF, Items, LogActionTransaction, ON, OrdersDetails, OrdersHeaders, Receipts, SalesPersonTargets, SalesPersonTargetsDetails, SalesPersonTargetsOffDays, SalesPersons, TargetsReferences, TransactionsDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @TYear smallint=2024
- @TMonth smallint=4
- @SalesmanNo int=2
## Tables Read
- [[CustomersFinancialDetails]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[LogActionTransaction]]
- ON
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersonTargetsOffDays]]
- [[SalesPersons]]
- [[TargetsReferences]]
- [[TransactionsDetails]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomersFinancialDetails]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[LogActionTransaction]]
- ON
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersonTargetsOffDays]]
- [[SalesPersons]]
- [[TargetsReferences]]
- [[TransactionsDetails]]

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
