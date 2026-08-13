---
type: procedure
database: Olives_BO
name: Pro_UnCloseOrder
schema: dbo
tags: [#backoffice, #order]
reads_from:
  - [[Customers]]
  - [[DeliveryManifest]]
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
  - [[NoTransactionsReasons]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[InvoiceDeliveryHF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_UnCloseOrder


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, DeliveryManifest, InvoiceDeliveryDF, InvoiceDeliveryHF, NoTransactionsReasons, SalesPersons, dbo. Writes InvoiceDeliveryHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate smalldatetime = null
- @ToDate smalldatetime = null
- @fromManifestID int= null
- @ToManifestID int = null
- @cmdType nvarchar(50) = null
- @VouNo int = null
- @VouYear int =null
- @VouType int =null
## Tables Read
- [[Customers]]
- [[DeliveryManifest]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[NoTransactionsReasons]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[InvoiceDeliveryHF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[DeliveryManifest]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[NoTransactionsReasons]]
- [[SalesPersons]]
- dbo

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
