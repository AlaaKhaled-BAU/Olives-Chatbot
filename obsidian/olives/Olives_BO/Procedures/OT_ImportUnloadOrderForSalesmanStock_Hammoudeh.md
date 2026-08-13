---
type: procedure
database: Olives_BO
name: OT_ImportUnloadOrderForSalesmanStock_Hammoudeh
schema: dbo
tags: [#maintenance]
reads_from:
  - PriceListDetails
  - SalesPersonItemsBalance
  - SalesPersonStockTackingDetails
  - SalesPersons
writes_to:
  - SalesPersonStockTacking
  - TransactionsDetails
  - TransactionsHeaders
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# OT_ImportUnloadOrderForSalesmanStock_Hammoudeh

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 4 table(s); writes 3; calls 2 proc(s). See sections below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[PriceListDetails]]
- [[SalesPersonItemsBalance]]
- [[SalesPersonStockTackingDetails]]
- [[SalesPersons]]
## Tables Written
- [[SalesPersonStockTacking]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[OSFA_DB/Tables/OT_ConsOrderDF|OT_ConsOrderDF]]
- [[OSFA_DB/Tables/OT_ConsOrderHF|OT_ConsOrderHF]]
## Callers
_None_
## Callees
- `GetItemSmallUnitQty`
- `GetItemUnitBySerial`
## When to Run

Run when importing data from tablets/external files into the back-office (batch or scheduled import).

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
