---
type: procedure
database: Olives_BO
name: GP_Integration_Wadi_Collect
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[Positions]]
  - `dbo`
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# GP_Integration_Wadi_Collect


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, Positions, dbo, SalesPersons. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @PositionID int
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Positions]]
- `dbo`
- [[SalesPersons]]
## Tables Written
_None_
## Callers
- [[OT_SendSalesmanData]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Positions]]
- dbo
- [[salespersons]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
- [[OT_SendSalesmanData]]


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
