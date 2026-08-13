---
type: procedure
database: OSFA_DB
name: OT_AutoStoreItemsQty
schema: dbo
tags: [#inventory, #mobile]
reads_from:
  - 168
  - DataBaseAccSqlExport
  - Db
  - Fun_ConvArrayToTable
  - GCI
  - LUXintegratopn
  - MultiValueStore
  - OPENJSON
  - OPENQUERY
  - [[OT_InvoiceDF]]
  - [[OT_InvoiceHF]]
  - [[OT_OrderDF]]
  - [[OT_OrderHF]]
  - [[OT_SalesmanMF]]
  - [[OT_StoreItemsQty]]
writes_to:
  - [[OT_StoreItemsQty]]
  - [[OT_StoreItemsQty_Main]]
called_by:
  - olives_bo
  - SkyTech_Integ_GetDataFromAPI
  - sp_OACreate
  - sp_OADestroy
  - sp_OAMethod
  - sp_OASetProperty
support_relevance: high
last_verified: 2026-07-05
---
# OT_AutoStoreItemsQty


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads 168, DataBaseAccSqlExport, Db, Fun_ConvArrayToTable, GCI, LUXintegratopn, MultiValueStore, OPENJSON, OPENQUERY, OT_InvoiceDF, OT_InvoiceHF, OT_OrderDF, OT_OrderHF, OT_SalesmanMF, OT_StoreItemsQty. Writes OT_StoreItemsQty, OT_StoreItemsQty_Main. Calls 6 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
- @SalesmanNo int = 57
- @ItemNo nvarchar(100) = 'FG000429'
- @MainStoreNo int=0
- @VouType int=0
- @CustID bigint=0
## Tables Read
- 168
- DataBaseAccSqlExport
- Db
- Fun_ConvArrayToTable
- GCI
- LUXintegratopn
- MultiValueStore
- OPENJSON
- OPENQUERY
- [[OT_InvoiceDF]]
- [[OT_InvoiceHF]]
- [[OT_OrderDF]]
- [[OT_OrderHF]]
- [[OT_SalesmanMF]]
- [[OT_StoreItemsQty]]
## Tables Written
- [[OT_StoreItemsQty]]
- [[OT_StoreItemsQty_Main]]
## Callers
_None (no known callers)_
## Callees
- olives_bo
- SkyTech_Integ_GetDataFromAPI
- sp_OACreate
- sp_OADestroy
- sp_OAMethod
- sp_OASetProperty
## Impact / Dependencies

**Tables Read**
- 168
- DataBaseAccSqlExport
- Db
- Fun_ConvArrayToTable
- GCI
- LUXintegratopn
- MultiValueStore
- OPENJSON
- OPENQUERY
- [[OT_InvoiceDF]]
- [[OT_InvoiceHF]]
- [[OT_OrderDF]]
- [[OT_OrderHF]]
- [[OT_SalesmanMF]]
- [[OT_StoreItemsQty]]

**Tables Written**
- [[OT_StoreItemsQty]]
- [[OT_StoreItemsQty_main]]

**Callers**
- olives_bo
- SkyTech_Integ_GetDataFromAPI
- sp_OACreate
- sp_OADestroy
- sp_OAMethod
- sp_OASetProperty

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
