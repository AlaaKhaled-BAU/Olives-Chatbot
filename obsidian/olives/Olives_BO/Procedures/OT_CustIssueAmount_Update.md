---
type: procedure
database: Olives_BO
name: OT_CustIssueAmount_Update
schema: dbo
tags: [#backoffice, #mobile]
reads_from:
  - [[ClientsActive]]
  - [[CurrenciesRate]]
  - [[PaymentsOrders]]
  - `dbo`
writes_to:
  - [[PaymentsOrders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_CustIssueAmount_Update


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CurrenciesRate, PaymentsOrders, dbo. Writes PaymentsOrders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @OrderYear smallint
- @OrderNo int
- @SalesmanNo int
- @CustID bigint=0
- @IssuedDate smalldatetime
- @IssuedAmount float
- @OrderType	int=0
- @Notes varchar(max)=''
## Tables Read
- [[ClientsActive]]
- [[CurrenciesRate]]
- [[PaymentsOrders]]
- `dbo`
## Tables Written
- [[PaymentsOrders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[CurrenciesRate]]
- [[PaymentsOrders]]
- dbo

**Tables Written**
- [[PaymentsOrders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
