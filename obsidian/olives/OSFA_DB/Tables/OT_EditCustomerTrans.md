---
type: table
database: OSFA_DB
name: OT_EditCustomerTrans
schema: dbo
tags: [#customer, #mobile]
foreign_keys:
referenced_by:
  - [[CheckCustomerHaveApprovedEditTrans]]
  - [[OT_EditCustomerTrans_Insert]]
  - [[OT_EditCustomerTrans_Verify]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_EditCustomerTrans



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
| CustomerNo | bigint | NO | ✓ |  |  |
| TabletSysID | nvarchar | YES | ✓ |  |  |
| ArName | nvarchar | YES |  |  |  |
| EnName | nvarchar | YES |  |  |  |
| CustType | int | YES |  |  |  |
| CustClass | int | YES |  |  |  |
| Tel | nvarchar | YES |  |  |  |
| Email | varchar | YES |  |  |  |
| FullAddress | nvarchar | YES |  |  |  |
| Group_ID | int | YES |  |  |  |
| ContactPerson | varchar | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| PaymentTypeID | int | YES |  |  |  |
| AssetsRef1 | nvarchar | YES |  |  |  |
| AssetsRef2 | nvarchar | YES |  |  |  |
| IsPosted | nvarchar | YES |  |  |  |
| VerificationCode | varchar | YES |  |  |  |
| IsVerified | bit | YES |  |  |  |
| ServerDatetime | datetime | YES |  |  |  |
## Primary Key
CompNo
SalesmanNo
CustomerNo
TabletSysID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[CheckCustomerHaveApprovedEditTrans]]
- [[OT_EditCustomerTrans_Insert]]
- [[OT_EditCustomerTrans_Verify]]

**Writes (2):**
- [[OT_EditCustomerTrans_Insert]]
- [[OT_EditCustomerTrans_Verify]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Duplicate customers**: Multiple records with same name/phone created during sync — support agent sees duplicate entries in dropdowns
- **Orphan references**: Customer records referenced by transactions that were soft-deleted — causes FK violation on cleanup
- **Balance mismatch**: CustomerBalance field diverges from actual calculated balance — run reconciliation proc
- **Suspend stuck**: IsSuspended flag not clearing after payment — check WF approval chain
- **GPS not collected**: IsCollectedGPS flag false — affects route optimization

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
