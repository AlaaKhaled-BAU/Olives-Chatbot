---
type: procedure
database: Olives_BO
name: Pro_DeliveryInvoiceAssigning
schema: dbo
tags: [#backoffice, #billing, #order]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[DeliveryCars]]
  - [[DeliveryProvaH]]
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
  - [[Locations]]
  - OSFA_DB
  - [[SystemCodes]]
writes_to:
  - [[InvoiceDeliveryHF]]
  - [[OT_InvoicesDelivery]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_DeliveryInvoiceAssigning


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, DeliveryCars, DeliveryProvaH, InvoiceDeliveryDF, InvoiceDeliveryHF, Locations, OSFA_DB, SystemCodes. Writes InvoiceDeliveryHF, OT_InvoicesDelivery. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
- @OrderYear smallint = 1
- @ProvaNo Bigint = 0
- @OrderNo int = 1
- @SalesmanNo int =6008
- @CarID int = 2
- @Weight float= null
- @DeliveryDate date = '2023-07-23'
- @UserID Nvarchar(max) = NULL
- @cmdType Nvarchar(max) = 'SelectAssignedOrders'
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[DeliveryCars]]
- [[DeliveryProvaH]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Locations]]
- OSFA_DB
- [[SystemCodes]]
## Tables Written
- [[InvoiceDeliveryHF]]
- [[OT_InvoicesDelivery]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- [[DeliveryCars]]
- [[DeliveryProvaH]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Locations]]
- OSFA_DB
- [[SystemCodes]]

**Tables Written**
- [[InvoiceDeliveryHF]]
- [[OT_InvoicesDelivery]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
