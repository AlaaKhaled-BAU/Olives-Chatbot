---
type: procedure
database: Olives_BO
name: SP_IntegrationErrorLog
schema: dbo
tags: [#backoffice, #integration, #log]
reads_from:
  - [[IntegrationErrorLog]]
writes_to:
  - [[IntegrationErrorLog]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SP_IntegrationErrorLog


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads IntegrationErrorLog. Writes IntegrationErrorLog. Invoked by 21 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyCode nvarchar(max)
- @TableName nvarchar(max)
- @ErrorMsg nvarchar(max)
- @Ref1 varchar(100)=null
- @Ref2 varchar(100)=null
- @Ref3 varchar(100)=null
## Tables Read
- [[IntegrationErrorLog]]
## Tables Written
- [[IntegrationErrorLog]]
## Callers
- [[Awael_Integration_WithLog]]
- [[Awtar_Integration_WithLog]]
- [[Awtar_Integ_AllUsers]]
- [[Awtar_Integ_AllUsers_SOA]]
- [[CL_Integration]]
- [[Darwaza_Integration_WithLog]]
- [[GTS_Integration_WithLog]]
- [[Isco_Integration_WithLog]]
- [[Mira_Integration_WithLog]]
- [[Mira_Wales_Integration_WithLog]]
- [[Motakaml_Integration_WithLog]]
- [[Niroukh_Integration_WithLog]]
- [[Niroukh_Integ_AllUsers]]
- [[Niroukh_Integ_AllUsers_SOA]]
- [[NPF_Integration]]
- [[OT_SendMultiSalesmanData]]
- [[Phenix_Sukhtian_Integ_WithLog]]
- [[SAP_Tyconz_Integ]]
- [[Shamel_Integration]]
- [[SN_Integration]]
- [[SN_Integration_Items_Customers]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[IntegrationErrorLog]]

**Tables Written**
- [[IntegrationErrorLog]]

**Callers**
_None_

**Callees**
- [[Awael_Integration_WithLog]]
- [[Awtar_Integration_WithLog]]
- [[Awtar_Integ_AllUsers]]
- [[Awtar_Integ_AllUsers_SOA]]
- [[CL_Integration]]
- [[Darwaza_Integration_WithLog]]
- [[GTS_Integration_WithLog]]
- [[Isco_Integration_WithLog]]
- [[Mira_Integration_WithLog]]
- [[Mira_Wales_Integration_WithLog]]
- [[Motakaml_Integration_WithLog]]
- [[Niroukh_Integration_WithLog]]
- [[Niroukh_Integ_AllUsers]]
- [[Niroukh_Integ_AllUsers_SOA]]
- [[NPF_Integration]]
- [[OT_SendMultiSalesmanData]]
- [[Phenix_Sukhtian_Integ_WithLog]]
- [[SAP_Tyconz_Integ]]
- [[Shamel_Integration]]
- [[SN_Integration]]
- [[SN_Integration_Items_Customers]]


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
