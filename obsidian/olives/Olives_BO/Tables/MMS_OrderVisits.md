---
type: table
database: Olives_BO
name: MMS_OrderVisits
schema: dbo
tags: [#backoffice, #mms, #order, #sales]
foreign_keys:
referenced_by:
  - [[Pro_MMS_OrderDetailsForVisit]]
  - [[Pro_MMS_OrderVisits]]
  - [[Pro_MMS_ScheduleSupportVisits]]
  - [[Pro_MMS_SetDataForAndroid]]
  - [[Rpt_TechnicianSummary]]
  - [[Rpt_TechnicianVisitDetails]]
support_relevance: high
last_verified: 2026-07-05
---
# MMS_OrderVisits


## Business Purpose

Maintenance management data — technician, order, and visit records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| OrderAutoID | numeric | YES | ✓ |  |  |
| OrderSubID | int | NO | ✓ |  |  |
| ScheduleID | int | NO | ✓ |  |  |
| VisitID | int | NO | ✓ |  |  |
| StartDateTime | smalldatetime | YES |  |  |  |
| EndDateTime | smalldatetime | YES |  |  |  |
| StartDateTime_Sys | smalldatetime | YES |  |  |  |
| EndDateTime_Sys | smalldatetime | YES |  |  |  |
| ProcedureDescription | nvarchar | YES |  |  |  |
| IsDeviceBring | bit | YES |  |  |  |
| BringDate | smalldatetime | YES |  |  |  |
| DeviceAttachment | nvarchar | YES |  |  |  |
| DeviceStatus | nvarchar | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| VisitResult | int | YES |  |  |  |
| DeviceSerialNo | nvarchar | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| DeviceID | int | YES |  |  |  |
| WarrantyNo | nvarchar | YES |  |  |  |
| WarrantyExpireDate | smalldatetime | YES |  |  |  |
| PurchaseDate | smalldatetime | YES |  |  |  |
| PurchaseLocation | nvarchar | YES |  |  |  |
| Cust_FullAddress | nvarchar | YES |  |  |  |
| Cust_TelephoneNo | nvarchar | YES |  |  |  |
| Cust_TaxTypeID | int | YES |  |  |  |
| Cust_MobileNo | nvarchar | YES |  |  |  |
| ExpectedAmount | float | YES |  |  |  |
| DiagnosticDesc | nvarchar | YES |  |  |  |
| CloseReasonID | int | YES |  |  |  |
| DiagnosticID | int | YES |  |  |  |
| ServiceResolutionID | int | YES |  |  |  |
| ServiceConditionID | int | YES |  |  |  |
| PostedToERP | bit | YES |  |  |  |
| IsInWarranty | bit | YES |  |  |  |
| CustName | nvarchar | YES |  |  |  |
| ShowRoomID | int | YES |  |  |  |
| OtherShowRoom | nvarchar | YES |  |  |  |
| InvRef | nvarchar | YES |  |  |  |
| IsBlackList | bit | YES |  |  |  |
| IsValidSerialNo | bit | YES |  |  |  |
| POInvNo | nvarchar | YES |  |  |  |
| Cust_CityID | int | YES |  |  |  |
| Cust_AreaID | int | YES |  |  |  |
| OrderStatusReasonID | int | YES |  |  |  |
| IsReplace | bit | YES |  |  |  |
| ReplaceNote | nvarchar | YES |  |  |  |
| ReadingVoltage | nvarchar | YES |  |  |  |
| ReadingAmber | nvarchar | YES |  |  |  |
| ReadingHertz | nvarchar | YES |  |  |  |
| ReadingTemp | nvarchar | YES |  |  |  |
| ImagesCount | varchar | YES |  |  |  |
## Primary Key
CompanyID
OrderAutoID
OrderSubID
ScheduleID
VisitID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (6):**
- [[Pro_MMS_OrderDetailsForVisit]]
- [[Pro_MMS_OrderVisits]]
- [[Pro_MMS_ScheduleSupportVisits]]
- [[Pro_MMS_SetDataForAndroid]]
- [[Rpt_TechnicianSummary]]
- [[Rpt_TechnicianVisitDetails]]

**Writes (2):**
- [[Pro_MMS_OrderVisits]]
- [[Pro_MMS_SetDataForAndroid]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
