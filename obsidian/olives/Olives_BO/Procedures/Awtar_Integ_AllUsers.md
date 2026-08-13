---
type: procedure
database: Olives_BO
name: Awtar_Integ_AllUsers
schema: dbo
tags: [#auth, #backoffice, #integration]
reads_from:
  - Cur_Users
  - [[Customers]]
  - [[CustomersPromotionsGroupsLink]]
  - [[Items]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesOrderHistoryDF]]
  - [[SalesOrderHistoryHF]]
  - [[SalesPersons]]
writes_to:
  - [[CustomersPromotionsGroupsLink]]
  - [[SalesOrderHistoryDF]]
  - [[SalesOrderHistoryHF]]
called_by:
  - [[Awtar_Integration_WithLog]]
  - [[SP_IntegrationErrorLog]]
support_relevance: high
last_verified: 2026-07-05
---
# Awtar_Integ_AllUsers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Cur_Users, Customers, CustomersPromotionsGroupsLink, Items, OrdersDetails, OrdersHeaders, SalesOrderHistoryDF, SalesOrderHistoryHF, SalesPersons. Writes CustomersPromotionsGroupsLink, SalesOrderHistoryDF, SalesOrderHistoryHF. Calls 2 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int=2
## Tables Read
- Cur_Users
- [[Customers]]
- [[CustomersPromotionsGroupsLink]]
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesOrderHistoryDF]]
- [[SalesOrderHistoryHF]]
- [[SalesPersons]]
## Tables Written
- [[CustomersPromotionsGroupsLink]]
- [[SalesOrderHistoryDF]]
- [[SalesOrderHistoryHF]]
## Callers
_None (no known callers)_
## Callees
- [[Awtar_Integration_WithLog]]
- [[SP_IntegrationErrorLog]]
## Impact / Dependencies

**Tables Read**
- Cur_Users
- [[Customers]]
- [[CustomersPromotionsGroupsLink]]
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesOrderHistoryDF]]
- [[SalesOrderHistoryHF]]
- [[SalesPersons]]

**Tables Written**
- [[CustomersPromotionsGroupsLink]]
- [[SalesOrderHistoryDF]]
- [[SalesOrderHistoryHF]]

**Callers**
- [[Awtar_Integration_WithLog]]
- [[SP_IntegrationErrorLog]]

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
