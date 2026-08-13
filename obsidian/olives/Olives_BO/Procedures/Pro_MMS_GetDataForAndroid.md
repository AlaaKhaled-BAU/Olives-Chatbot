---
type: procedure
database: Olives_BO
name: Pro_MMS_GetDataForAndroid
schema: dbo
tags: [#backoffice, #mms, #mobile]
reads_from:
  - AxServiceWarranty
  - [[Banks]]
  - [[Branches]]
  - [[Companies]]
  - [[Customers]]
  - [[MMS_CloseOrderReasons]]
  - [[MMS_DevicesInfo]]
  - [[MMS_Diagnostic]]
  - [[MMS_InvoicesHeaders]]
  - [[MMS_Items]]
  - [[MMS_ItemsCategories]]
  - [[MMS_Link_Device_Diagnostic]]
  - [[MMS_Link_Device_Items]]
  - [[MMS_MaintenanceTechnician]]
  - [[MMS_MaintenanceTechnicianPermissions]]
writes_to:
  - [[MMS_MaintenanceTechnician]]
  - [[MMS_MaintenanceTechnicianTransSerials]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_GetDataForAndroid


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads AxServiceWarranty, Banks, Branches, Companies, Customers, MMS_CloseOrderReasons, MMS_DevicesInfo, MMS_Diagnostic, MMS_InvoicesHeaders, MMS_Items, MMS_ItemsCategories, MMS_Link_Device_Diagnostic, MMS_Link_Device_Items, MMS_MaintenanceTechnician, MMS_MaintenanceTechnicianPermissions. Writes MMS_MaintenanceTechnician, MMS_MaintenanceTechnicianTransSerials. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @cmdType varchar(50)=null
- @TechnicianID int=null
- @TabletSysID  varchar(50)=null
- @DeviceSerialNo  varchar(50)=null
- @Exist SmallInt=0 Output
- @SerialNo nvarchar(1000)=''
- @Phone nvarchar(1000)= ''
## Tables Read
- AxServiceWarranty
- [[Banks]]
- [[Branches]]
- [[Companies]]
- [[Customers]]
- [[MMS_CloseOrderReasons]]
- [[MMS_DevicesInfo]]
- [[MMS_Diagnostic]]
- [[MMS_InvoicesHeaders]]
- [[MMS_Items]]
- [[MMS_ItemsCategories]]
- [[MMS_Link_Device_Diagnostic]]
- [[MMS_Link_Device_Items]]
- [[MMS_MaintenanceTechnician]]
- [[MMS_MaintenanceTechnicianPermissions]]
## Tables Written
- [[MMS_MaintenanceTechnician]]
- [[MMS_MaintenanceTechnicianTransSerials]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- AxServiceWarranty
- [[Banks]]
- [[Branches]]
- [[Companies]]
- [[Customers]]
- [[MMS_CloseOrderReasons]]
- [[MMS_DevicesInfo]]
- [[MMS_Diagnostic]]
- [[MMS_InvoicesHeaders]]
- [[MMS_Items]]
- [[MMS_ItemsCategories]]
- [[MMS_Link_Device_Diagnostic]]
- [[MMS_Link_Device_Items]]
- [[MMS_MaintenanceTechnician]]
- [[MMS_MaintenanceTechnicianPermissions]]

**Tables Written**
- [[MMS_MaintenanceTechnician]]
- [[MMS_MaintenanceTechnicianTransSerials]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
