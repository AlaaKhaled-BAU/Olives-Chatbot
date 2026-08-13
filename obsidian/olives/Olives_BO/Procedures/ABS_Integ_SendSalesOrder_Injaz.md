---
type: procedure
database: Olives_BO
name: ABS_Integ_SendSalesOrder_Injaz
schema: dbo
tags: [#integration]
reads_from:
  - CompanyBranches
  - Customers
  - CustomersGPSLocations
  - Items
  - OrdersDetails
  - SalesPersons
writes_to:
  - IntegrationErrorLog
  - IntegrationPostedTransactions
  - OrdersHeaders
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# ABS_Integ_SendSalesOrder_Injaz

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 6 table(s); writes 3; calls 4 proc(s). See sections below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersGPSLocations]]
- [[Items]]
- [[OrdersDetails]]
- [[SalesPersons]]
## Tables Written
- [[IntegrationErrorLog]]
- [[IntegrationPostedTransactions]]
- [[OrdersHeaders]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- [[ABS_Integ_PostDataToAPI_Injaz]]
- `Fun_GetSalesOrderVouAndCustDiscPerc`
- `GetItemOrgUnitQty`
- `Trim`
## When to Run

Run during API sync cycles: pulls from or pushes to an external ERP/API when new data is ready or on-demand refresh.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
