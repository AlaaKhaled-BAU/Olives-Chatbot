---
type: procedure
database: Olives_BO
name: SAP_Tyconz_Integ_SendNewCustomers
schema: dbo
tags: [#backoffice, #customer, #integration]
reads_from:
  - [[CustomersTypes]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - New_Customers
  - [[OT_NewCustomers]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SAP_Tyconz_Integ_SendNewCustomers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersTypes, SalesPersons, dbo. Writes New_Customers, OT_NewCustomers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
## Tables Read
- [[CustomersTypes]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- New_Customers
- [[OT_NewCustomers]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomersTypes]]
- [[SalesPersons]]
- dbo

**Tables Written**
- New_Customers
- [[OT_NewCustomers]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
