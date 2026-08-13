---
type: procedure
database: Olives_BO
name: Pro_AssignOrderDeliveryToCar
schema: dbo
tags: [#backoffice, #order]
reads_from:
  - [[Customers]]
  - [[DeliveryCars]]
  - [[InvoiceDeliveryHF]]
  - [[SalesPersons]]
writes_to:
  - [[InvoiceDeliveryHF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_AssignOrderDeliveryToCar


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, DeliveryCars, InvoiceDeliveryHF, SalesPersons. Writes InvoiceDeliveryHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID                INT =NULL
- @CarID                    INT =NULL
- @VouNo                    INT =NULL
- @CMD                      NVARCHAR(MAX) =NULL
## Tables Read
- [[Customers]]
- [[DeliveryCars]]
- [[InvoiceDeliveryHF]]
- [[SalesPersons]]
## Tables Written
- [[InvoiceDeliveryHF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[DeliveryCars]]
- [[InvoiceDeliveryHF]]
- [[SalesPersons]]

**Tables Written**
- [[InvoiceDeliveryHF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
