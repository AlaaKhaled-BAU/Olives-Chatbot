---
type: procedure
database: Olives_BO
name: Rpt_DeliveryDetailsForWF
schema: dbo
tags: [#reporting, #workflow]
reads_from:
  - Customers
  - InvoiceDeliveryDF
  - InvoiceDeliveryHF
  - Items
  - ItemsUnits
  - PaymentsTypes
  - SalesPersons
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Rpt_DeliveryDetailsForWF

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 7 table(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @VouNo int
- @VouType int
- @VouYear bigint
## Tables Read
- [[Customers]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Items]]
- [[ItemsUnits]]
- [[PaymentsTypes]]
- [[SalesPersons]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `GetItemOrgUnitQty`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
