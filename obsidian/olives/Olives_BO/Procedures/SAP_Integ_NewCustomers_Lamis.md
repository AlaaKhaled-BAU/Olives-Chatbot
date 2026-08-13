---
type: procedure
database: Olives_BO
name: SAP_Integ_NewCustomers_Lamis
schema: dbo
tags: [#backoffice, #customer, #integration]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - [[PaymentsTypes]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[Customers]]
  - NewCustomers
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SAP_Integ_NewCustomers_Lamis


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, CustomersTypes, PaymentsTypes, SalesPersons, dbo. Writes Customers, NewCustomers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[PaymentsTypes]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[Customers]]
- NewCustomers
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[PaymentsTypes]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[Customers]]
- NewCustomers

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
