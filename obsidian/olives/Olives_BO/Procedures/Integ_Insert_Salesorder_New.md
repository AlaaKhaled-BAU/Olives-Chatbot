---
type: procedure
database: Olives_BO
name: Integ_Insert_Salesorder_New
schema: dbo
tags: [#integration]
reads_from:
  - OrdersDetails
  - OrdersHeaders
  - SalesOrderDeliveryHF
writes_to:
  - SalesOrderDeliveryDF
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Integ_Insert_Salesorder_New

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 3 table(s); writes 1. See sections below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesOrderDeliveryHF]]
## Tables Written
- [[SalesOrderDeliveryDF]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Run during API sync cycles: pulls from or pushes to an external ERP/API when new data is ready or on-demand refresh.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
