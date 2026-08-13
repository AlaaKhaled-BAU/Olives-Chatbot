---
type: procedure
database: Olives_BO
name: Rpt_DeliveryInvoiceTransaction
schema: dbo
tags: [#backoffice, #billing, #order, #reporting]
reads_from:
  - [[Customers]]
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
  - [[LogActionTransaction]]
  - [[NoTransactionsReasons]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_DeliveryInvoiceTransaction


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, InvoiceDeliveryDF, InvoiceDeliveryHF, LogActionTransaction, NoTransactionsReasons, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1
- @FromDate nvarchar(50)='2023-08-01'
- @ToDate nvarchar(50)='2023-09-14'
- @FromTransNo Bigint=0
- @ToTransNo Bigint=9999999999
## Tables Read
- [[Customers]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[LogActionTransaction]]
- [[NoTransactionsReasons]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[LogActionTransaction]]
- [[NoTransactionsReasons]]
- [[SalesPersons]]

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
