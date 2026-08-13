---
type: procedure
database: Olives_BO
name: Rpt_InvoiceByDocTypes
schema: dbo
tags: [#backoffice, #billing, #reference, #reporting]
reads_from:
  - [[Customers]]
  - [[CustomersTypes]]
  - [[DocumentsTypes]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_InvoiceByDocTypes


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersTypes, DocumentsTypes, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
- @FromSalesMan int =null
- @ToSalesMan int=null
- @FromCust bigint=null
- @ToCust bigint =null
- @FromCustType int=null
- @ToCustType int=null
- @FromDoc int =null
- @ToDoc int =null
- @FromDate Smalldatetime=null
- @ToDate Smalldatetime=null
## Tables Read
- [[Customers]]
- [[CustomersTypes]]
- [[DocumentsTypes]]
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
- [[CustomersTypes]]
- [[DocumentsTypes]]
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
