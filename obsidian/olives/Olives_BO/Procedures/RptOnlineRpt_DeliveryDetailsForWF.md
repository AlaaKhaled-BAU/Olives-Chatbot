---
type: procedure
database: Olives_BO
name: RptOnlineRpt_DeliveryDetailsForWF
schema: dbo
tags: [#reporting, #workflow]
reads_from:
  - ClientsActive
  - Customers
  - CustomersFinancialDetails
  - InvoiceDeliveryDF
  - InvoiceDeliveryHF
  - Items
  - ItemsUnits
  - SalesPersons
writes_to:
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# RptOnlineRpt_DeliveryDetailsForWF

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 8 table(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @FromDate smalldatetime
- @ToDate smalldatetime
- @SalesmanNo int
- @TransactionTypeID int
- @FromCustomerNo bigint
- @ToCustomerNo bigint
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Items]]
- [[ItemsUnits]]
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
