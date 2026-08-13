---
type: procedure
database: Olives_BO
name: Niroukh_Integ_GetDataFromAPI
schema: dbo
tags: [#backoffice, #integration]
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
# Niroukh_Integ_GetDataFromAPI


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Invoked by 7 procedure(s). Calls 4 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @APILink nvarchar(1000)='http://192.168.1.9:8081/OlivesAPI/api/Banks/GetBanks?UserName=admin&Password=12'
- @ReqDataName nvarchar(1000)=''
- @JSONResult nvarchar(MAX)='' OUTPUT
## Tables Read
_None_
## Tables Written
_None_
## Callers
- [[Awtar_Integration_GetPromotion]]
- [[Awtar_Integration_SOA]]
- [[Awtar_Integration_WithLog]]
- [[Niroukh_Integration_GetPromotion]]
- [[Niroukh_Integration_SOA]]
- [[Niroukh_Integration_WithLog]]
- [[Tablet_GetInvoiceHistoryFromERP]]
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
- [[Awtar_Integration_GetPromotion]]
- [[Awtar_Integration_SOA]]
- [[Awtar_Integration_WithLog]]
- [[Niroukh_Integration_GetPromotion]]
- [[Niroukh_Integration_SOA]]
- [[Niroukh_Integration_WithLog]]
- [[Tablet_GetInvoiceHistoryFromERP]]


## When to Run This

Run when pulling data from an external API/system. Called during sync cycles or on-demand data refresh.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Glossary]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[OlivesUserPermissions]]
- [[PromotionsApprovalLog]]
- [[CustomerPaidTrans_FormERP]]
