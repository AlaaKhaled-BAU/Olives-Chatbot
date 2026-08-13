---
type: procedure
database: Olives_BO
name: Rpt_DeliveryCarSummaryReport
schema: dbo
tags: [#backoffice, #order, #reporting]
reads_from:
  - [[Companies]]
  - [[Customers]]
  - [[DeliveryCars]]
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
  - [[Items]]
  - [[ItemsUnits]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_DeliveryCarSummaryReport


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, Customers, DeliveryCars, InvoiceDeliveryDF, InvoiceDeliveryHF, Items, ItemsUnits. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @cmdType varchar(50)=null
- @TransTbl TransactionsHeaders_Type READONLY
- @FromSalesman int = 1
- @ToSalesman int = 99999
- @FromDate datetime ='2000-01-01'
- @ToDate datetime ='2024-04-01'
## Tables Read
- [[Companies]]
- [[Customers]]
- [[DeliveryCars]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Items]]
- [[ItemsUnits]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Companies]]
- [[Customers]]
- [[DeliveryCars]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Items]]
- [[ItemsUnits]]

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
