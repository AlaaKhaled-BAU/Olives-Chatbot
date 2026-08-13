---
type: procedure
database: OSFA_DB
name: servics_app_OSFA_Mobile_Ver
schema: dbo
tags: [#mobile]
reads_from:
  - [[OT_Administrators]]
  - [[OT_Banks]]
  - [[OT_Branchs]]
  - [[OT_CustType]]
  - [[OT_CustomerMF]]
  - [[OT_CustomersGPSLocations]]
  - [[OT_DocTypes]]
  - [[OT_Drawers]]
  - [[OT_GPSLog]]
  - [[OT_ImageTypes]]
  - [[OT_InvoiceHistoryDF]]
  - [[OT_InvoiceHistoryHF]]
  - [[OT_ItemUnits]]
  - [[OT_ItemsCateg]]
  - [[OT_ItemsMF]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# servics_app_OSFA_Mobile_Ver


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_Administrators, OT_Banks, OT_Branchs, OT_CustType, OT_CustomerMF, OT_CustomersGPSLocations, OT_DocTypes, OT_Drawers, OT_GPSLog, OT_ImageTypes, OT_InvoiceHistoryDF, OT_InvoiceHistoryHF, OT_ItemUnits, OT_ItemsCateg, OT_ItemsMF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @SalesmanNo varchar(50)='3003' ,@password varchar(50)='123' ,@cmd varchar(50)='admin' ,@compNo varchar(50)='1' ,@ItemNo varchar(50)=''
- @UserID varchar(50)='admin'
## Tables Read
- [[OT_Administrators]]
- [[OT_Banks]]
- [[OT_Branchs]]
- [[OT_CustType]]
- [[OT_CustomerMF]]
- [[OT_CustomersGPSLocations]]
- [[OT_DocTypes]]
- [[OT_Drawers]]
- [[OT_GPSLog]]
- [[OT_ImageTypes]]
- [[OT_InvoiceHistoryDF]]
- [[OT_InvoiceHistoryHF]]
- [[OT_ItemUnits]]
- [[OT_ItemsCateg]]
- [[OT_ItemsMF]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_Administrators]]
- [[OT_Banks]]
- [[OT_Branchs]]
- [[OT_CustType]]
- [[OT_CustomerMF]]
- [[OT_CustomersGPSLocations]]
- [[OT_DocTypes]]
- [[OT_Drawers]]
- [[OT_GPSLog]]
- [[OT_ImageTypes]]
- [[OT_InvoiceHistoryDF]]
- [[OT_InvoiceHistoryHF]]
- [[OT_ItemUnits]]
- [[OT_ItemsCateg]]
- [[OT_ItemsMF]]

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
