---
type: procedure
database: Olives_BO
name: Pro_AddDiscountToCustomerOrders
schema: dbo
tags: [#backoffice, #billing, #customer, #order]
reads_from:
  - [[AddDiscountToCustomerOrders]]
writes_to:
  - [[AddDiscountToCustomerOrders]]
called_by:
  - [[WF_AddWorkFlowLevelOne]]
support_relevance: high
last_verified: 2026-07-05
---
# Pro_AddDiscountToCustomerOrders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads AddDiscountToCustomerOrders. Writes AddDiscountToCustomerOrders. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID INT=1
- @CustomerID INT=314
- @SalesPersonID INT=3003
- @CategCode NVARCHAR(50)=4
- @DiscountAmount DECIMAL(18, 2)=14
- @Notes NVARCHAR(MAX)='TEST'
- @TrDateTime DATETIME='2024-01-01'
## Tables Read
- [[AddDiscountToCustomerOrders]]
## Tables Written
- [[AddDiscountToCustomerOrders]]
## Callers
_None (no known callers)_
## Callees
- [[WF_AddWorkFlowLevelOne]]
## Impact / Dependencies

**Tables Read**
- [[AddDiscountToCustomerOrders]]

**Tables Written**
- [[AddDiscountToCustomerOrders]]

**Callers**
- [[WF_AddWorkFlowLevelOne]]

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
