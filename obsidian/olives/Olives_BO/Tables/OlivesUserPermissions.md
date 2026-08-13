---
type: table
database: Olives_BO
name: OlivesUserPermissions
schema: dbo
tags: [#auth, #backoffice, #integration]
foreign_keys:
  - [[Companies]]
  - [[OlivesPages]]
  - [[Users]]
referenced_by:
  - [[AppDashBoard]]
  - [[Pro_InternalMemo]]
  - [[Pro_OlivesMenu]]
  - [[Pro_OlivesUserPermissions]]
  - [[Pro_Users]]
support_relevance: high
last_verified: 2026-07-05
---
# OlivesUserPermissions


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores olivesuserpermissions records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| UserID | nvarchar | YES | ✓ | ✓ | [[Users]] |
| PrID | int | NO | ✓ | ✓ | [[OlivesPages]] |
| CanAccess | bit | YES |  |  |  |
| CanAdd | bit | YES |  |  |  |
| CanEdit | bit | YES |  |  |  |
| CanDelete | bit | YES |  |  |  |
## Primary Key
CompanyID
UserID
PrID
## Foreign Keys
CompanyID -> [[Companies]](ID)
PrID -> [[OlivesPages]](ID)
UserID -> [[Users]](UserID)
## Impact / Procedures Using This Table

**Reads (5):**
- [[AppDashBoard]]
- [[Pro_InternalMemo]]
- [[Pro_OlivesMenu]]
- [[Pro_OlivesUserPermissions]]
- [[Pro_Users]]

**Writes (2):**
- [[Pro_OlivesMenu]]
- [[Pro_OlivesUserPermissions]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Integration stuck**: IsPosted flag not clearing — check ERP connection and error log
- **Duplicate sent**: Same transaction sent multiple times — ERP shows duplicates
- **Mapping error**: Field mapping fails — check IntegrationPostedTransactions for error details
- **Timeout**: Large batch exceeds ERP timeout — split into smaller batches

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Olives_BO/Procedures/RunSQLWebAPI_Integ]]
- [[Olives_BO/Procedures/EncodeArabicToUTF8DataFromOSFA_API]]
- [[Olives_BO/Procedures/Awtar_Integ_GetDataFromAPI]]
