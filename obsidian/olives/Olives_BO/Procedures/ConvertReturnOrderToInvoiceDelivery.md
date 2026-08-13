---
type: procedure
database: Olives_BO
name: ConvertReturnOrderToInvoiceDelivery
schema: dbo
tags: [#backoffice, #billing, #order]
reads_from:
  - [[InvoiceDeliveryHF]]
  - [[ReturnOrdersDetails]]
  - [[ReturnOrdersHeaders]]
  - [[SalesPersons]]
writes_to:
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# ConvertReturnOrderToInvoiceDelivery


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads InvoiceDeliveryHF, ReturnOrdersDetails, ReturnOrdersHeaders, SalesPersons. Writes InvoiceDeliveryDF, InvoiceDeliveryHF. Invoked by 2 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
- @TraYear int
- @TraNo int
## Tables Read
- [[InvoiceDeliveryHF]]
- [[ReturnOrdersDetails]]
- [[ReturnOrdersHeaders]]
- [[SalesPersons]]
## Tables Written
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
## Callers
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[InvoiceDeliveryHF]]
- [[ReturnOrdersDetails]]
- [[ReturnOrdersHeaders]]
- [[SalesPersons]]

**Tables Written**
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]

**Callers**
_None_

**Callees**
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
