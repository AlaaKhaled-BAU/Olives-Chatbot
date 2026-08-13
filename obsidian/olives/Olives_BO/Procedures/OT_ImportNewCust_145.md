---
type: procedure
database: Olives_BO
name: OT_ImportNewCust_145
schema: dbo
tags: [#backoffice, #mobile]
reads_from:
  - [[ClientsActive]]
  - Cur_NewCustomer
  - [[Customers]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersPromotionsGroupsLink]]
  - [[OT_CustomerMF]]
  - [[OT_ErrorLog]]
  - [[OT_GPSLog]]
  - [[OT_NewCustomers]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportNewCust_145


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Cur_NewCustomer, Customers, SalesPersons, dbo. Writes Customers, CustomersFinancialDetails, CustomersPromotionsGroupsLink, OT_CustomerMF, OT_ErrorLog, OT_GPSLog, OT_NewCustomers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=1
## Tables Read
- [[ClientsActive]]
- Cur_NewCustomer
- [[Customers]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPromotionsGroupsLink]]
- [[OT_CustomerMF]]
- [[OT_ErrorLog]]
- [[OT_GPSLog]]
- [[OT_NewCustomers]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- Cur_NewCustomer
- [[Customers]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPromotionsGroupsLink]]
- [[OT_CustomerMF]]
- [[OT_ErrorLog]]
- [[OT_GPSLog]]
- [[OT_NewCustomers]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
