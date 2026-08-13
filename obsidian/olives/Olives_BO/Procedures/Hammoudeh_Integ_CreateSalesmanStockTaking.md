---
type: procedure
database: Olives_BO
name: Hammoudeh_Integ_CreateSalesmanStockTaking
schema: dbo
tags: [#integration]
reads_from:
  - CustomersFinancialDetails
  - Items
  - PriceListDetails
  - SalesPersonStockTacking
  - SalesPersonStockTackingDetails
  - SalesPersons
  - TransactionsHeaders
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Hammoudeh_Integ_CreateSalesmanStockTaking

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 7 table(s); calls 2 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
## Tables Read
- [[CustomersFinancialDetails]]
- [[Items]]
- [[PriceListDetails]]
- [[SalesPersonStockTacking]]
- [[SalesPersonStockTackingDetails]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[OSFA_DB/Tables/OT_InvoiceDF|OT_InvoiceDF]]
- [[OSFA_DB/Tables/OT_InvoiceHF|OT_InvoiceHF]]
## Callers
_None_
## Callees
- `Fun_ConvArrayToTable`
- `GetItemSmallUnitQty`
## When to Run

Run during API sync cycles: pulls from or pushes to an external ERP/API when new data is ready or on-demand refresh.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
