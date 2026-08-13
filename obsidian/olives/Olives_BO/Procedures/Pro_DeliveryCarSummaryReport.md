---
type: procedure
database: Olives_BO
name: Pro_DeliveryCarSummaryReport
schema: dbo
tags: [#backoffice, #order, #reporting]
reads_from:
  - [[ClientsActive]]
  - [[Companies]]
  - [[Customers]]
  - [[DeliveryCars]]
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[SalesOrderDeliveryDF]]
  - [[SalesOrderDeliveryHF]]
writes_to:
  - [[InvoiceDeliveryHF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_DeliveryCarSummaryReport


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Companies, Customers, DeliveryCars, InvoiceDeliveryDF, InvoiceDeliveryHF, Items, ItemsUnits, SalesOrderDeliveryDF, SalesOrderDeliveryHF. Writes InvoiceDeliveryHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @cmdType varchar(50)=null
- @DeliveryBatchID  INT =0 output
- @TransTbl TransactionsHeaders_Type READONLY
- @FromDate datetime ='2000-01-01'
- @ToDate datetime ='2024-04-01'
- @FromBatch int =1
- @ToBatch int =999999
- @VouNo int =Null
- @VouYear INT =NULL
## Tables Read
- [[ClientsActive]]
- [[Companies]]
- [[Customers]]
- [[DeliveryCars]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Items]]
- [[ItemsUnits]]
- [[SalesOrderDeliveryDF]]
- [[SalesOrderDeliveryHF]]
## Tables Written
- [[InvoiceDeliveryHF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Companies]]
- [[Customers]]
- [[DeliveryCars]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Items]]
- [[ItemsUnits]]
- [[SalesOrderDeliveryDF]]
- [[SalesOrderDeliveryHF]]

**Tables Written**
- [[InvoiceDeliveryHF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
