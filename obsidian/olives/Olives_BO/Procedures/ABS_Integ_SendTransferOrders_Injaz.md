---
type: procedure
database: Olives_BO
name: ABS_Integ_SendTransferOrders_Injaz
schema: dbo
tags: [#integration]
reads_from:
  - Items
  - ItemsUnits
  - SalesPersons
  - TransfersOrdersDetails
writes_to:
  - IntegrationErrorLog
  - IntegrationPostedTransactions
  - TransfersOrdersHeaders
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# ABS_Integ_SendTransferOrders_Injaz

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 4 table(s); writes 3; calls 2 proc(s). See sections below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Items]]
- [[ItemsUnits]]
- [[SalesPersons]]
- [[TransfersOrdersDetails]]
## Tables Written
- [[IntegrationErrorLog]]
- [[IntegrationPostedTransactions]]
- [[TransfersOrdersHeaders]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- [[ABS_Integ_PostDataToAPI_Injaz]]
- `GetItemOrgUnitQty`
## When to Run

Run during API sync cycles: pulls from or pushes to an external ERP/API when new data is ready or on-demand refresh.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
