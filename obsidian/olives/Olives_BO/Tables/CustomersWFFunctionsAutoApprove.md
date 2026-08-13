---
type: table
database: Olives_BO
name: CustomersWFFunctionsAutoApprove
schema: dbo
tags: [#backoffice, #customer]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
  - [[WF_Functions]]
referenced_by:
  - [[Pro_WFFunctionsAutoApprove]]
  - [[WF_AddWorkFlowLevelOne_Promotions]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomersWFFunctionsAutoApprove


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customerswffunctionsautoapprove records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| CustomerID | bigint | NO | ✓ | ✓ | [[Customers]] |
| FunctionID | smallint | NO | ✓ | ✓ | [[WF_Functions]] |
## Primary Key
CompanyID
CustomerID
FunctionID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
FunctionID -> [[WF_Functions]](ID)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_WFFunctionsAutoApprove]]
- [[WF_AddWorkFlowLevelOne_Promotions]]

**Writes (1):**
- [[Pro_WFFunctionsAutoApprove]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Duplicate customers**: Multiple records with same name/phone created during sync — support agent sees duplicate entries in dropdowns
- **Orphan references**: Customer records referenced by transactions that were soft-deleted — causes FK violation on cleanup
- **Balance mismatch**: CustomerBalance field diverges from actual calculated balance — run reconciliation proc
- **Suspend stuck**: IsSuspended flag not clearing after payment — check WF approval chain
- **GPS not collected**: IsCollectedGPS flag false — affects route optimization

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
