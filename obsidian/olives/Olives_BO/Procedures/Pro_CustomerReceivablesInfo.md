---
type: procedure
database: Olives_BO
name: Pro_CustomerReceivablesInfo
schema: dbo
tags: [#backoffice, #customer]
reads_from:
  - [[CustomerReceivablesInfo]]
  - [[Customers]]
  - [[CustomersClasses]]
  - [[CustomersFinancialDetails]]
  - Payment
  - [[PaymentsTypes]]
  - [[SalesPersons]]
writes_to:
  - [[CustomerReceivablesInfo]]
  - [[CustomersFinancialDetails]]
  - Payment
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CustomerReceivablesInfo


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerReceivablesInfo, Customers, CustomersClasses, CustomersFinancialDetails, Payment, PaymentsTypes, SalesPersons. Writes CustomerReceivablesInfo, CustomersFinancialDetails, Payment. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @cmdType nvarchar(50)= null
- @CompNo smallint=null
- @CustomerID bigint =null
- @ReceivablesMonth smallint =null
- @ReceivablesYear smallint =null
- @Receivables float = null
- @ExcludeCashPayments float = null
- @ExcludeReturns float = null
- @ExcludePendingOrders float = null
- @ExceptionCollectionManager float = null
- @PaymentTypeID int = null
- @SalesPersons int = null
## Tables Read
- [[CustomerReceivablesInfo]]
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- Payment
- [[PaymentsTypes]]
- [[SalesPersons]]
## Tables Written
- [[CustomerReceivablesInfo]]
- [[CustomersFinancialDetails]]
- Payment
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomerReceivablesInfo]]
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- Payment
- [[PaymentsTypes]]
- [[SalesPersons]]

**Tables Written**
- [[CustomerReceivablesInfo]]
- [[CustomersFinancialDetails]]
- Payment

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
