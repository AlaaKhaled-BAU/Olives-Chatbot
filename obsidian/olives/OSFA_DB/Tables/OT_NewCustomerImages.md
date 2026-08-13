---
type: table
database: OSFA_DB
name: OT_NewCustomerImages
schema: dbo
tags: [#customer, #mobile]
foreign_keys:
referenced_by:
  - [[OT_Add_NewCustomerImages]]
  - [[OT_NewCustomerImages_CheckExist]]
  - [[Pro_NewCustImages]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_NewCustomerImages



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| NewCustSysID | varchar | YES | ✓ |  |  |
| ImageSerial | int | NO | ✓ |  |  |
| ImageType_ID | int | YES |  |  |  |
| SysID | varchar | YES |  |  |  |
| NewCustImage | image | YES |  |  |  |
## Primary Key
CompNo
NewCustSysID
ImageSerial
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OT_Add_NewCustomerImages]]
- [[OT_NewCustomerImages_CheckExist]]
- [[Pro_NewCustImages]]

**Writes (1):**
- [[OT_Add_NewCustomerImages]]

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
