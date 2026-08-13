---
type: procedure
database: Olives_BO
name: Phenix_Sukhtian_Integ_OpenSession
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[CompanyParameters]]
  - OPENJSON
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Phenix_Sukhtian_Integ_OpenSession


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CompanyParameters, OPENJSON. Invoked by 6 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @APILink nvarchar(1000)='http://176.28.201.214:8282/'
- @ReqDataName nvarchar(1000)=''
- @JSONResult nvarchar(MAX)=''
## Tables Read
- [[CompanyParameters]]
- OPENJSON
## Tables Written
_None_
## Callers
- [[Phenix_Sukhtian_Integ_GetItemsBalance]]
- [[Phenix_Sukhtian_Integ_LoadAndUnLoad]]
- [[Phenix_Sukhtian_Integ_SendInvoiceAndReturn]]
- [[Phenix_Sukhtian_Integ_SendReceipts]]
- [[Phenix_Sukhtian_Integ_SendSalesOrder]]
- [[Phenix_Sukhtian_Integ_WithLog]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CompanyParameters]]
- OPENJSON

**Tables Written**
_None_

**Callers**
_None_

**Callees**
- [[Phenix_Sukhtian_Integ_GetItemsBalance]]
- [[Phenix_Sukhtian_Integ_LoadAndUnLoad]]
- [[Phenix_Sukhtian_Integ_SendInvoiceAndReturn]]
- [[Phenix_Sukhtian_Integ_SendReceipts]]
- [[Phenix_Sukhtian_Integ_SendSalesOrder]]
- [[Phenix_Sukhtian_Integ_WithLog]]


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
