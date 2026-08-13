---
type: procedure
database: Olives_BO
name: Pro_PriceListCustomerAssignment
schema: dbo
tags: [#backoffice]
reads_from:
  - Customers
  - PriceLists
writes_to:
  - CustomersFinancialDetails
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Pro_PriceListCustomerAssignment

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 2 table(s); writes 1; calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @CustomerIDs nvarchar(MAX)
- @cmdType varchar(50)
- @PriceListID int
## Tables Read
- [[Customers]]
- [[PriceLists]]
## Tables Written
- [[CustomersFinancialDetails]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_ConvArrayToTable`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
