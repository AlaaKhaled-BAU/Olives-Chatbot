---
type: table
database: OSFA_DB
name: OT_RequestToLoginToCustomerWithoutVerficiation
schema: dbo
tags: [#auth, #customer, #log, #mobile, #workflow]
foreign_keys:
referenced_by:
  - [[OT_RequestToLoginToCustomerWithoutVerficiation_Insert]]
support_relevance: low
last_verified: 2026-07-05
---
# OT_RequestToLoginToCustomerWithoutVerficiation



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
| SalesPersonNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| IsPosted | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| LoggedIn | bit | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_RequestToLoginToCustomerWithoutVerficiation_Insert]]

**Writes (1):**
- [[OT_RequestToLoginToCustomerWithoutVerficiation_Insert]]

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
