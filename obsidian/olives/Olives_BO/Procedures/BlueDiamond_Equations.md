---
type: procedure
database: Olives_BO
name: BlueDiamond_Equations
schema: dbo
tags: [#backoffice]
reads_from:
  - Class_Curs
  - [[CustomersFinancialDetails]]
  - [[SalesPersons]]
  - Salesman_Curs
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - `dbo`
writes_to:
  - AutoChangeCustomerClassLog
  - [[CustomersFinancialDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# BlueDiamond_Equations


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Class_Curs, CustomersFinancialDetails, SalesPersons, Salesman_Curs, TransactionsDetails, TransactionsHeaders, dbo. Writes AutoChangeCustomerClassLog, CustomersFinancialDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
- @CmdType Varchar(50) = ''
## Tables Read
- Class_Curs
- [[CustomersFinancialDetails]]
- [[SalesPersons]]
- Salesman_Curs
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- `dbo`
## Tables Written
- AutoChangeCustomerClassLog
- [[CustomersFinancialDetails]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Class_Curs
- [[CustomersFinancialDetails]]
- [[SalesPersons]]
- Salesman_Curs
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- dbo

**Tables Written**
- AutoChangeCustomerClassLog
- [[CustomersFinancialDetails]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
