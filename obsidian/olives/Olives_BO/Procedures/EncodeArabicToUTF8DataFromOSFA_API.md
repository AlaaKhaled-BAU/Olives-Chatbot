---
type: procedure
database: Olives_BO
name: EncodeArabicToUTF8DataFromOSFA_API
schema: dbo
tags: [#backoffice, #integration, #reference]
reads_from:
writes_to:
called_by:
  - sp_OACreate
  - sp_OADestroy
  - sp_OAGetProperty
  - sp_OAMethod
support_relevance: high
last_verified: 2026-07-05
---
# EncodeArabicToUTF8DataFromOSFA_API


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Calls 4 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @APILink nvarchar(1000)='http://10.0.10.105:8081/Srv/Services/General.aspx?op=366&contentVer=2&salesmanno=0&CompNo=1&IMEI_ID=139192006050120&Sys_ID=1'
- @text nvarchar(max)='اسامة الحلواني'
- @textResult nvarchar(MAX)='' OUTPUT
## Tables Read
_None_
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod
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

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Glossary]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[OlivesUserPermissions]]
- [[PromotionsApprovalLog]]
- [[CustomerPaidTrans_FormERP]]
- [[DR_DynamicReportsParameters]]
- [[MMS_TaxType]]
- [[MMS_OrderTypes]]
