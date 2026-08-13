---
type: procedure
database: Olives_BO
name: Pro_CustomerImages
schema: dbo
tags: [#backoffice]
reads_from:
  - CompanyParameters
  - Customers
  - ImageTypes
  - SalesPersons
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Pro_CustomerImages

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 4 table(s); calls 2 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @CustomerID bigint
- @SalesPersonID int
- @SalesmanID int
- @cmdType nvarchar(50)
- @FromDate smalldatetime
- @ToDate smalldatetime
- @ImageID int
## Tables Read
- [[CompanyParameters]]
- [[Customers]]
- [[ImageTypes]]
- [[SalesPersons]]
## Tables Written
_None_
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[CompanyParameters]]
## Callers
_None_
## Callees
- `Fun_GetCustomersGalleryData`
- `Fun_GetSalesPersonTree`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
