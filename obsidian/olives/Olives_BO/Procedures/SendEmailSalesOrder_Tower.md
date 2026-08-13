---
type: procedure
database: Olives_BO
name: SendEmailSalesOrder_Tower
schema: dbo
tags: [#backoffice, #order, #sales]
reads_from:
  - Cur_SendEmail
  - [[Customers]]
  - GetSalesOrderTotalAmount
  - [[OrdersHeaders]]
  - [[SalesPersons]]
writes_to:
  - [[OrdersHeaders]]
called_by:
  - msdb
support_relevance: high
last_verified: 2026-07-05
---
# SendEmailSalesOrder_Tower


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Cur_SendEmail, Customers, GetSalesOrderTotalAmount, OrdersHeaders, SalesPersons. Writes OrdersHeaders. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
## Tables Read
- Cur_SendEmail
- [[Customers]]
- GetSalesOrderTotalAmount
- [[OrdersHeaders]]
- [[SalesPersons]]
## Tables Written
- [[OrdersHeaders]]
## Callers
_None (no known callers)_
## Callees
- msdb
## Impact / Dependencies

**Tables Read**
- Cur_SendEmail
- [[Customers]]
- GetSalesOrderTotalAmount
- [[OrdersHeaders]]
- [[SalesPersons]]

**Tables Written**
- [[OrdersHeaders]]

**Callers**
- msdb

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
