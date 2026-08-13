---
type: table
database: Olives_BO
name: MMS_OrderVisitImages
schema: dbo
tags: [#backoffice, #mms, #order, #sales]
foreign_keys:
referenced_by:
  - [[Pro_MMS_OrderVisitImages]]
  - [[Pro_MMS_SetDataForAndroid]]
support_relevance: high
last_verified: 2026-07-05
---
# MMS_OrderVisitImages


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
| LineID | int | NO | ✓ |  |  |
| ImageData | image | YES |  |  |  |
| IsCustSigns | bit | YES |  |  |  |
| IsReplace | bit | YES |  |  |  |
| ImageDataBase64 | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
OrderAutoID
OrderSubID
ScheduleID
VisitID
LineID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_MMS_OrderVisitImages]]
- [[Pro_MMS_SetDataForAndroid]]

**Writes (1):**
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
