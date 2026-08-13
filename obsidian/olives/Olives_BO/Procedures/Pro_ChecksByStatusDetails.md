---
type: procedure
database: Olives_BO
name: Pro_ChecksByStatusDetails
schema: dbo
tags: [#backoffice]
reads_from:
  - [[Checks]]
  - [[Customers]]
  - [[Receipts]]
  - [[Receipts_PaidTransChecks]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ChecksByStatusDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, Customers, Receipts, Receipts_PaidTransChecks, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int
- @FromSalesman bigint =null
- @ToSalesman bigint=null
- @FromCust bigint=null
- @ToCust bigint =null
- @FromLocation int =null
- @ToLocation int =null
- @FromDate Smalldatetime=null
- @ToDate Smalldatetime=null
## Tables Read
- [[Checks]]
- [[Customers]]
- [[Receipts]]
- [[Receipts_PaidTransChecks]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Checks]]
- [[Customers]]
- [[Receipts]]
- [[Receipts_PaidTransChecks]]
- [[SalesPersons]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
