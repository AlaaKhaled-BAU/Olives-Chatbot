---
type: procedure
database: Olives_BO
name: Integ_Normal_DeliveryOrder
schema: dbo
tags: [#backoffice, #integration, #order]
reads_from:
  - [[Items]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesOrderDeliveryDF]]
  - [[SalesOrderDeliveryHF]]
writes_to:
  - [[SalesOrderDeliveryDF]]
  - [[SalesOrderDeliveryHF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Integ_Normal_DeliveryOrder


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, OrdersDetails, OrdersHeaders, SalesOrderDeliveryDF, SalesOrderDeliveryHF. Writes SalesOrderDeliveryDF, SalesOrderDeliveryHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=290
## Tables Read
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesOrderDeliveryDF]]
- [[SalesOrderDeliveryHF]]
## Tables Written
- [[SalesOrderDeliveryDF]]
- [[SalesOrderDeliveryHF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesOrderDeliveryDF]]
- [[SalesOrderDeliveryHF]]

**Tables Written**
- [[SalesOrderDeliveryDF]]
- [[SalesOrderDeliveryHF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
