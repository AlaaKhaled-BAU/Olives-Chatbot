---
type: procedure
database: Olives_BO
name: ABS_Integ_SendInvoices_Injaz
schema: dbo
tags: [#integration]
reads_from:
  - Customers
  - CustomersGPSLocations
  - Items
  - SalesPersons
  - TransactionsDetails
writes_to:
  - IntegrationErrorLog
  - IntegrationPostedTransactions
  - TransactionsHeaders
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# ABS_Integ_SendInvoices_Injaz

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 5 table(s); writes 3; calls 4 proc(s). See sections below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Customers]]
- [[CustomersGPSLocations]]
- [[Items]]
- [[SalesPersons]]
- [[TransactionsDetails]]
## Tables Written
- [[IntegrationErrorLog]]
- [[IntegrationPostedTransactions]]
- [[TransactionsHeaders]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- [[ABS_Integ_PostDataToAPI_Injaz]]
- `Fun_GetInvVouAndCustDiscPerc`
- `GetItemOrgUnitQty`
- `Trim`
## When to Run

Run during API sync cycles: pulls from or pushes to an external ERP/API when new data is ready or on-demand refresh.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
