---
type: procedure
database: Olives_BO
name: Pro_SalespersonsProcedures
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[Customers]]
  - [[DailyProcedures]]
  - [[SalespersonsProcedures]]
writes_to:
  - [[SalespersonsProcedures]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalespersonsProcedures


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, DailyProcedures, SalespersonsProcedures. Writes SalespersonsProcedures. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ProcedureID int = null
- @PositionID int =null
- @CustomerID bigint=null
- @ProcedureDate smalldatetime=null
- @Status bit=null
- @TrDateTime datetime=null
- @cmdType varchar(50)=null
## Tables Read
- [[Customers]]
- [[DailyProcedures]]
- [[SalespersonsProcedures]]
## Tables Written
- [[SalespersonsProcedures]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[DailyProcedures]]
- [[SalespersonsProcedures]]

**Tables Written**
- [[SalespersonsProcedures]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
