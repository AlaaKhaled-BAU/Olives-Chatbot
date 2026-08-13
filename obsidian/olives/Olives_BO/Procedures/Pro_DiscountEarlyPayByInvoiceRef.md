---
type: procedure
database: Olives_BO
name: Pro_DiscountEarlyPayByInvoiceRef
schema: dbo
tags: [#backoffice]
reads_from:
  - Customers
  - SalesPersons
  - SystemCodes
writes_to:
  - DiscountEarlyPayByInvoiceRef
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Pro_DiscountEarlyPayByInvoiceRef

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 3 table(s); writes 1. See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @InvoiceRefID nvarchar(200)
- @CustomerID bigint
- @SalespersonID int
- @DiscountPerc float
- @cmdType nvarchar(200)
## Tables Read
- [[Customers]]
- [[SalesPersons]]
- [[SystemCodes]]
## Tables Written
- [[DiscountEarlyPayByInvoiceRef]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
