---
type: procedure
database: Olives_BO
name: WF_AddRequestToIncreaseCustomerCreditlimit
schema: dbo
tags: [#auth, #backoffice, #billing, #customer, #workflow]
reads_from:
  - Alpha
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - OPENQUERY
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[RequestToIncreaseCustomerCreditlimit]]
  - [[SalesPersons]]
  - WF
  - [[WF_MasterLog]]
  - [[WF_SubLog]]
  - `dbo`
writes_to:
  - [[OrdersHeaders]]
  - [[RequestToIncreaseCustomerCreditlimit]]
  - [[WF_MasterLog]]
  - [[WF_SubLog]]
called_by:
  - [[WF_AddWorkFlowLevelOne]]
support_relevance: high
last_verified: 2026-07-05
---
# WF_AddRequestToIncreaseCustomerCreditlimit


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Alpha, ClientsActive, Customers, CustomersFinancialDetails, OPENQUERY, OrdersDetails, OrdersHeaders, RequestToIncreaseCustomerCreditlimit, SalesPersons, WF, WF_MasterLog, WF_SubLog, dbo. Writes OrdersHeaders, RequestToIncreaseCustomerCreditlimit, WF_MasterLog, WF_SubLog. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @SID numeric(30, 0)
- @PositionID int
- @SalesmanNo int
- @ActionDate smalldatetime
- @Note nvarchar(max) = ''
## Tables Read
- Alpha
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- OPENQUERY
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[RequestToIncreaseCustomerCreditlimit]]
- [[SalesPersons]]
- WF
- [[WF_MasterLog]]
- [[WF_SubLog]]
- `dbo`
## Tables Written
- [[OrdersHeaders]]
- [[RequestToIncreaseCustomerCreditlimit]]
- [[WF_MasterLog]]
- [[WF_SubLog]]
## Callers
_None (no known callers)_
## Callees
- [[WF_AddWorkFlowLevelOne]]
## Impact / Dependencies

**Tables Read**
- Alpha
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- OPENQUERY
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[RequestToIncreaseCustomerCreditlimit]]
- [[SalesPersons]]
- WF
- [[WF_MasterLog]]
- [[WF_SubLog]]
- dbo

**Tables Written**
- [[OrdersHeaders]]
- [[RequestToIncreaseCustomerCreditlimit]]
- [[WF_MasterLog]]
- [[WF_SubLog]]

**Callers**
- [[WF_AddWorkFlowLevelOne]]

**Callees**
_None_


## When to Run This

Workflow procedure — called automatically by the WF engine when processing approval chains. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
