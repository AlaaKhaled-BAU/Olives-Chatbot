---
type: table
database: Olives_BO
name: MMS_OrderDetails
schema: dbo
tags: [#backoffice, #mms, #order]
foreign_keys:
referenced_by:
  - [[Pro_MMS_OrderDetails]]
  - [[Pro_MMS_OrderDetailsForVisit]]
  - [[Pro_MMS_OrderVisits]]
  - [[Pro_MMS_ScheduleSupportVisits]]
support_relevance: high
last_verified: 2026-07-05
---
# MMS_OrderDetails


## Business Purpose

Maintenance management data — technician, order, and visit records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| OrderAutoID | numeric | YES | ✓ |  |  |
| OrderSubID | int | NO | ✓ |  |  |
| DeviceID | int | NO |  |  |  |
| DiagnosticID | int | NO |  |  |  |
| SerialNo | nvarchar | YES |  |  |  |
| IsInWarranty | bit | YES |  |  |  |
| WarrantyNo | nvarchar | YES |  |  |  |
| WarrantyExpireDate | smalldatetime | YES |  |  |  |
| PurchaseDate | smalldatetime | YES |  |  |  |
| PurchaseLocation | nvarchar | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| SubOrderStatus | int | YES |  |  |  |
| AssigmentDateTime | smalldatetime | YES |  |  |  |
| DiagnosticDesc | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
OrderAutoID
OrderSubID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (4):**
- [[Pro_MMS_OrderDetails]]
- [[Pro_MMS_OrderDetailsForVisit]]
- [[Pro_MMS_OrderVisits]]
- [[Pro_MMS_ScheduleSupportVisits]]

**Writes (1):**
- [[Pro_MMS_OrderDetails]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
