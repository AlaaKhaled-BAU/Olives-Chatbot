---
type: procedure
database: OSFA_DB
name: OT_Add_Cust_Survey_Answers
schema: dbo
tags: [#mobile, #survey]
reads_from:
  - [[OT_Cust_Survey_Answers]]
writes_to:
  - [[OT_Cust_Survey_Answers]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Add_Cust_Survey_Answers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_Cust_Survey_Answers. Writes OT_Cust_Survey_Answers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @Cust_Survey_No bigint
- @Question_No int
- @Answer varchar (1000)
- @ErrNo SmallInt Output
## Tables Read
- [[OT_Cust_Survey_Answers]]
## Tables Written
- [[OT_Cust_Survey_Answers]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_Cust_Survey_Answers]]

**Tables Written**
- [[OT_Cust_Survey_Answers]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
