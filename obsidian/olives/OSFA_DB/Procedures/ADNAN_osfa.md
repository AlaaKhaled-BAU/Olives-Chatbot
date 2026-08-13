---
type: procedure
database: OSFA_DB
name: ADNAN_osfa
schema: dbo
tags: [#mobile]
reads_from:
  - [[OT_ConsOrderHF]]
  - [[OT_InvoiceHF]]
  - [[OT_OrderHF]]
  - [[OT_Payments]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# ADNAN_osfa


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_ConsOrderHF, OT_InvoiceHF, OT_OrderHF, OT_Payments. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @companyID smallint
- @transactionYear smallint
- @SalesmanNo int
- @OrderYear smallint=@transactionYear
- @CompNO smallint=@companyID
- @VouYear smallint= @transactionYear
## Tables Read
- [[OT_ConsOrderHF]]
- [[OT_InvoiceHF]]
- [[OT_OrderHF]]
- [[OT_Payments]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_ConsOrderHF]]
- [[OT_InvoiceHF]]
- [[OT_OrderHF]]
- [[OT_Payments]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
