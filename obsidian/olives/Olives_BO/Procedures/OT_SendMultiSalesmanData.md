---
type: procedure
database: Olives_BO
name: OT_SendMultiSalesmanData
schema: dbo
tags: [#backoffice, #mobile, #sales]
reads_from:
  - [[Receipts]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
  - cur_Salesman
  - [[OrdersHeaders]]
writes_to:
called_by:
  - [[OT_SendSalesmanData]]
  - [[SP_IntegrationErrorLog]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_SendMultiSalesmanData


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Receipts, SalesPersons, TransactionsHeaders, cur_Salesman, OrdersHeaders. Calls 2 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @companyid int
## Tables Read
- [[Receipts]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- cur_Salesman
- [[OrdersHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[OT_SendSalesmanData]]
- [[SP_IntegrationErrorLog]]
## Impact / Dependencies

**Tables Read**
- [[Receipts]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- cur_Salesman
- [[ordersheaders]]

**Tables Written**
_None_

**Callers**
- [[ot_sendsalesmandata]]
- [[SP_IntegrationErrorLog]]

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
