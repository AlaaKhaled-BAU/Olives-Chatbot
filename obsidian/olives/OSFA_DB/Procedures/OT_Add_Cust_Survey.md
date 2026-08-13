---
type: procedure
database: OSFA_DB
name: OT_Add_Cust_Survey
schema: dbo
tags: [#mobile, #survey]
reads_from:
  - [[OT_Cust_Survey]]
writes_to:
  - [[OT_Cust_Survey]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Add_Cust_Survey


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_Cust_Survey. Writes OT_Cust_Survey. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @Cust_Survey_No bigint
- @CompNo smallint
- @Survey_ID int
- @Customer_No bigint
- @Survey_Date datetime
- @ErrNo SmallInt Output
- @Used_Cust_Survey_No bigint Output
- @GPSX varchar(50)
- @GPSY varchar(50)
- @SalesmanNo nvarchar(50)
- @IsProspectiveCustomer bit = 0
## Tables Read
- [[OT_Cust_Survey]]
## Tables Written
- [[OT_Cust_Survey]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_Cust_Survey]]

**Tables Written**
- [[OT_Cust_Survey]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
