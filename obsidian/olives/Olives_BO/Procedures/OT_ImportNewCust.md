---
type: procedure
database: Olives_BO
name: OT_ImportNewCust
schema: dbo
tags: [#backoffice, #mobile]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersPromotionsGroupsLink]]
  - OSFA_DB
  - Olives_BO
  - [[SalesPersons]]
  - [[SalesPersonsDevicePermissions]]
  - [[TransactionsHeaders]]
  - `dbo`
writes_to:
  - [[Customers]]
  - [[CustomersContactPersonsLink]]
  - [[CustomersFinancialDetails]]
  - [[CustomersPromotionsGroupsLink]]
  - [[Drawers]]
  - [[OT_CustomerMF]]
  - [[OT_GPSLog]]
  - [[OT_NewCustomers]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportNewCust


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, CustomersFinancialDetails, CustomersPromotionsGroupsLink, OSFA_DB, Olives_BO, SalesPersons, SalesPersonsDevicePermissions, TransactionsHeaders, dbo. Writes Customers, CustomersContactPersonsLink, CustomersFinancialDetails, CustomersPromotionsGroupsLink, Drawers, OT_CustomerMF, OT_GPSLog, OT_NewCustomers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=1
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPromotionsGroupsLink]]
- OSFA_DB
- Olives_BO
- [[SalesPersons]]
- [[SalesPersonsDevicePermissions]]
- [[TransactionsHeaders]]
- `dbo`
## Tables Written
- [[Customers]]
- [[CustomersContactPersonsLink]]
- [[CustomersFinancialDetails]]
- [[CustomersPromotionsGroupsLink]]
- [[Drawers]]
- [[OT_CustomerMF]]
- [[OT_GPSLog]]
- [[OT_NewCustomers]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPromotionsGroupsLink]]
- OSFA_DB
- Olives_BO
- [[SalesPersons]]
- [[SalesPersonsDevicePermissions]]
- [[TransactionsHeaders]]
- dbo

**Tables Written**
- [[Customers]]
- [[CustomersContactPersonsLink]]
- [[CustomersFinancialDetails]]
- [[CustomersPromotionsGroupsLink]]
- [[Drawers]]
- [[OT_CustomerMF]]
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
