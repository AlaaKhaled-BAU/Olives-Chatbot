---
type: procedure
database: Olives_BO
name: Soft_Integ_CreateSalesmanStockTaking
schema: dbo
tags: [#integration]
reads_from:
  - Customers
  - CustomersFinancialDetails
  - Items
  - PriceListDetails
  - PriceLists
  - Receipts
  - SalesPersonStockTackingDetails
  - SalesPersons
  - TransactionsHeaders
writes_to:
  - SalesPersonStockTacking
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Soft_Integ_CreateSalesmanStockTaking

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 9 table(s); writes 1; calls 3 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Items]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[Receipts]]
- [[SalesPersonStockTackingDetails]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
## Tables Written
- [[SalesPersonStockTacking]]
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[OSFA_DB/Tables/OT_InvoiceDF|OT_InvoiceDF]]
- [[OSFA_DB/Tables/OT_InvoiceHF|OT_InvoiceHF]]
- [[OSFA_DB/Tables/OT_Payment_Invoices|OT_Payment_Invoices]]
- [[OSFA_DB/Tables/OT_Payments|OT_Payments]]
## Callers
_None_
## Callees
- `Fun_ConvArrayToTable`
- `Fun_GetInvTotalAmountfromosfa`
- `GetItemSmallUnitQty`
## When to Run

Run during API sync cycles: pulls from or pushes to an external ERP/API when new data is ready or on-demand refresh.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
