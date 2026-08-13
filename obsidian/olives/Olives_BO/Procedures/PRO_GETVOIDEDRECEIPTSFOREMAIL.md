---
type: procedure
database: Olives_BO
name: PRO_GETVOIDEDRECEIPTSFOREMAIL
schema: dbo
tags: [#backoffice, #billing]
reads_from:
  - [[Companies]]
  - [[CompanyParameters]]
  - [[Customers]]
  - Fun_GetReceiptsChecksTotal
  - [[Receipts]]
  - [[SMTPEmailSettings]]
  - [[SalesPersons]]
  - [[Users]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# PRO_GETVOIDEDRECEIPTSFOREMAIL


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, CompanyParameters, Customers, Fun_GetReceiptsChecksTotal, Receipts, SMTPEmailSettings, SalesPersons, Users. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
_None_
## Tables Read
- [[Companies]]
- [[CompanyParameters]]
- [[Customers]]
- Fun_GetReceiptsChecksTotal
- [[Receipts]]
- [[SMTPEmailSettings]]
- [[SalesPersons]]
- [[Users]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Companies]]
- [[CompanyParameters]]
- [[Customers]]
- Fun_GetReceiptsChecksTotal
- [[Receipts]]
- [[SMTPEmailSettings]]
- [[SalesPersons]]
- [[Users]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
