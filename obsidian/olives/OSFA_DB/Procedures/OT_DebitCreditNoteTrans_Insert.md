---
type: procedure
database: OSFA_DB
name: OT_DebitCreditNoteTrans_Insert
schema: dbo
tags: [#billing, #mobile]
reads_from:
  - [[OT_DebitCreditNoteTrans]]
writes_to:
  - [[OT_DebitCreditNoteTrans]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_DebitCreditNoteTrans_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_DebitCreditNoteTrans. Writes OT_DebitCreditNoteTrans. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=1
- @VouYear smallint=1
- @VouNo  int=1
- @VouDate smalldatetime='2020-01-01'
- @CustomerNo varchar(50)='11'
- @SalesmanNo smallint=3003
- @InvNo varchar(500)='fahed'
- @InvAmount float=0
- @TotDisccount float =0
- @Tax float=0
- @NetDisccount float =0
- @TrDateTime smalldatetime='2020-01-01'
- @Notes varchar(500)='fahed'
- @TabletSysID varchar(50)='2020-01-01'
- @Posted bit =0
- @VouType	smallint=1
## Tables Read
- [[OT_DebitCreditNoteTrans]]
## Tables Written
- [[OT_DebitCreditNoteTrans]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_DebitCreditNoteTrans]]

**Tables Written**
- [[OT_DebitCreditNoteTrans]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
