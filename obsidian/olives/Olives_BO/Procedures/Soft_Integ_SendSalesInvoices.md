---
type: procedure
database: Olives_BO
name: Soft_Integ_SendSalesInvoices
schema: dbo
tags: [#integration]
reads_from:
  - Customers
  - CustomersFinancialDetails
  - InvoiceReturnLink
  - Items
  - ItemsUnits
  - PaymentsTypes
  - SalesPersons
  - TransactionsDetails
writes_to:
  - TransactionsHeaders
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Soft_Integ_SendSalesInvoices

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 8 table(s); writes 1; calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[InvoiceReturnLink]]
- [[Items]]
- [[ItemsUnits]]
- [[PaymentsTypes]]
- [[SalesPersons]]
- [[TransactionsDetails]]
## Tables Written
- [[TransactionsHeaders]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `GetItemOrgUnitQty`
## When to Run

Run during API sync cycles: pulls from or pushes to an external ERP/API when new data is ready or on-demand refresh.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
