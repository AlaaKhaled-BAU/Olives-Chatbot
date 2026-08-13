---
type: table
database: Olives_BO
name: Users
schema: dbo
tags: [#auth, #backoffice]
foreign_keys:
referenced_by:
  - [[DR_DynamicReports_PRO]]
  - [[OMS]]
  - [[OSFA_MobileDeliveryAPI]]
  - [[OT_AppCarAndSalesperson]]
  - [[PRO_GETRECEIPTSFOREMAIL]]
  - [[PRO_GETVOIDEDRECEIPTSFOREMAIL]]
  - [[Pro_AssetTransfer]]
  - [[Pro_CustomersPromotionsGroups]]
  - [[Pro_CustomersPromotionsGroupsLink]]
  - [[Pro_InternalMemo]]
  - [[Pro_IssueAssets]]
  - [[Pro_OlivesUserPermissions]]
  - [[Pro_PromotionsApproval]]
  - [[Pro_UserActivity]]
  - [[Pro_UserCompanyBranchesLink]]
  - [[Pro_Users]]
  - [[Rpt_IntenalMemo]]
  - [[Rpt_SecurityLog]]
  - [[Sama_GPS_Integ]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Users-and-Permissions
---
# Users


## Business Purpose

System user accounts — login credentials, permissions, and role assignments.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| UserID | nvarchar | YES | ✓ |  |  |
| UserPWD | nvarchar | YES |  |  |  |
| UserName | nvarchar | YES |  |  |  |
| PhoneNo | nvarchar | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
| LastLoginDate | smalldatetime | YES |  |  |  |
| LastPassChangeDate | smalldatetime | YES |  |  |  |
| TrasnDateClose | smalldatetime | YES |  |  |  |
| AllPromotions | bit | YES |  |  |  |
| Email | nvarchar | YES |  |  |  |
| IsLoggedIn | bit | YES |  |  |  |
## Primary Key
UserID
## Foreign Keys
(none)
## Known Circular Dependencies
- Part of a circular FK chain: AssetsTransactions → SalesPersons → Users → AssetsTransactions.
## Impact / Procedures Using This Table

**Reads (19):**
- [[DR_DynamicReports_PRO]]
- [[OMS]]
- [[OSFA_MobileDeliveryAPI]]
- [[OT_AppCarAndSalesperson]]
- [[PRO_GETRECEIPTSFOREMAIL]]
- [[PRO_GETVOIDEDRECEIPTSFOREMAIL]]
- [[Pro_AssetTransfer]]
- [[Pro_CustomersPromotionsGroups]]
- [[Pro_CustomersPromotionsGroupsLink]]
- [[Pro_InternalMemo]]
- [[Pro_IssueAssets]]
- [[Pro_OlivesUserPermissions]]
- [[Pro_PromotionsApproval]]
- [[Pro_UserActivity]]
- [[Pro_UserCompanyBranchesLink]]
- [[Pro_Users]]
- [[Rpt_IntenalMemo]]
- [[Rpt_SecurityLog]]
- [[Sama_GPS_Integ]]

**Writes (1):**
- [[Pro_Users]]

## Estimated Size / Volatility
Typical business table
## Common Issues
> [!warning] AUTO-GENERATED — verify before trusting

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Olives_BO/Tables/UsersGroupsLink]]
- [[Shared/Runbooks/Login-Device-Issues]]
