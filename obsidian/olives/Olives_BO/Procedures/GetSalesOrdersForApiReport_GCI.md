---
type: procedure
database: Olives_BO
name: GetSalesOrdersForApiReport_GCI
schema: dbo
tags: [#backoffice, #integration, #order, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[SalesOrderHistoryHF]]
  - [[SalesOrderHistoryDF]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# GetSalesOrdersForApiReport_GCI


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, Items, ItemsUnits, SalesOrderHistoryHF, SalesOrderHistoryDF, SalesPersons, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int= 2
- @SalesmanNo int=2
- @CustID bigint=-1
- @FromDate smalldatetime='2020-01-01'
- @ToDate smalldatetime='2025-07-17'
- @Status int= -1
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Items]]
- [[ItemsUnits]]
- [[SalesOrderHistoryHF]]
- [[SalesOrderHistoryDF]]
- [[SalesPersons]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Items]]
- [[ItemsUnits]]
- [[SalesOrderHistoryHF]]
- [[SalesOrderHistorydF]]
- [[SalesPersons]]
- dbo

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
