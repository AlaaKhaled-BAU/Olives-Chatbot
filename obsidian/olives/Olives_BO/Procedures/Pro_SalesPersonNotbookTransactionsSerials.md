---
type: procedure
database: Olives_BO
name: Pro_SalesPersonNotbookTransactionsSerials
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[Customers]]
  - [[SalesPersonNotbookTransactionsSerials]]
  - [[SalesPersons]]
  - [[TransactionsTypes]]
  - if
writes_to:
  - [[SalesPersonNotbookTransactionsSerials]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesPersonNotbookTransactionsSerials


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, SalesPersonNotbookTransactionsSerials, SalesPersons, TransactionsTypes, if. Writes SalesPersonNotbookTransactionsSerials. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @cmdType varchar(50)=null
- @SerYear smallint = null
- @SalesPersonID int  = null
- @NotbookNo nvarchar(50) = null
- @SerType smallint = null
- @ToNo int  = null
- @FromNo int  = null
- @NextSerial int  = null
- @IsSuspended bit = null
- @CustomerID bigint = null
## Tables Read
- [[Customers]]
- [[SalesPersonNotbookTransactionsSerials]]
- [[SalesPersons]]
- [[TransactionsTypes]]
- if
## Tables Written
- [[SalesPersonNotbookTransactionsSerials]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[SalesPersonNotbookTransactionsSerials]]
- [[SalesPersons]]
- [[TransactionsTypes]]
- if

**Tables Written**
- [[SalesPersonNotbookTransactionsSerials]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
