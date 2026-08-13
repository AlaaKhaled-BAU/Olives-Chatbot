---
type: procedure
database: Olives_BO
name: Alpha_Integ_SendIssuePaymentOrder
schema: dbo
tags: [#backoffice, #billing, #integration, #order]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[PaymentsOrders]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - OT_IssuePaymentOrder
  - [[PaymentsOrders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Alpha_Integ_SendIssuePaymentOrder


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, PaymentsOrders, SalesPersons, dbo. Writes OT_IssuePaymentOrder, PaymentsOrders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 60
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[PaymentsOrders]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- OT_IssuePaymentOrder
- [[PaymentsOrders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- [[PaymentsOrders]]
- [[SalesPersons]]
- dbo

**Tables Written**
- OT_IssuePaymentOrder
- [[PaymentsOrders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
