---
type: table
database: OSFA_DB
name: OT_CustomersGPSLocations
schema: dbo
tags: [#customer, #gps, #mobile]
foreign_keys:
referenced_by:
  - [[servics_app_OSFA_Mobile_Ver]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_CustomersGPSLocations



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
| CustomerID | bigint | NO | ✓ |  |  |
| LineID | int | NO | ✓ |  |  |
| GPSX | nvarchar | YES |  |  |  |
| GPSY | nvarchar | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| Loc_Address | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
SalesmanNo
CustomerID
LineID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[servics_app_OSFA_Mobile_Ver]]

**Writes (0):**
_None_

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
- [[OSFA_DB/Tables/OT_CustomerImage]]
- [[OSFA_DB/Tables/OT_CustomersPromotionsExceptions]]
- [[OSFA_DB/Tables/OT_PromotionsGroupsCustomersLink]]
