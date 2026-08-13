---
type: procedure
database: Olives_BO
name: SMS_Niroukh
schema: dbo
tags: [#backoffice]
reads_from:
writes_to:
called_by:
  - sp_OACreate
  - sp_OADestroy
  - sp_OAGetProperty
  - sp_OAMethod
  - sp_OASetProperty
support_relevance: high
last_verified: 2026-07-05
---
# SMS_Niroukh


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Invoked by 1 procedure(s). Calls 5 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @TelephoneNo nvarchar(2000)='0798731927'
- @MsgTxt nvarchar(max) ='EEE'
## Tables Read
_None_
## Tables Written
_None_
## Callers
- [[Pro_Users]]
## Callees
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod
- sp_OASetProperty
## Impact / Dependencies

**Tables Read**
_None_

**Tables Written**
_None_

**Callers**
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod
- sp_OASetProperty

**Callees**
- [[Pro_Users]]


## When to Run This

SMS notification procedure. Called when the system needs to send SMS alerts. Check SMS configuration if messages aren't being delivered.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]

- [[SMS_AnwarMakesTransfer]]
- [[SMS_SpartenNew]]
- [[SMS_DahlakeNewCustomers]]
- [[Glossary]]
