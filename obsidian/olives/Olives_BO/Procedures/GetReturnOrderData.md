---
type: procedure
database: Olives_BO
name: GetReturnOrderData
schema: dbo
tags: [#backoffice]
reads_from:
  - ClientsActive
  - Customers
  - CustomersFinancialDetails
  - Items
  - ItemsUnits
  - ReturnOrdersDetails
  - ReturnOrdersHeaders
  - SalesPersons
writes_to:
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# GetReturnOrderData

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 8 table(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @SalesmanNo int
- @CustID bigint
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Items]]
- [[ItemsUnits]]
- [[ReturnOrdersDetails]]
- [[ReturnOrdersHeaders]]
- [[SalesPersons]]
## Tables Written
_None_
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[OSFA_DB/Tables/OT_InvoiceHF|OT_InvoiceHF]]
## Callers
_None_
## Callees
- `GetItemOrgUnitQty`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
