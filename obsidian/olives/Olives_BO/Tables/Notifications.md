---
type: table
database: Olives_BO
name: Notifications
schema: dbo
tags: [#backoffice]
foreign_keys:
referenced_by:
  - [[GETNOTIFICATIONS]]
  - [[OT_ImportCustStockTacking]]
  - [[OT_ImportGapTrans]]
  - [[Pro_ConvertUnloadOrderToTransaction]]
  - [[Pro_NewCustomers]]
  - [[Pro_SalesPersons]]
  - [[Pro_TransLock]]
support_relevance: high
last_verified: 2026-07-05
---
# Notifications


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores notifications records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
| TrDateTime | datetime | YES |  |  |  |
| SalesmanNo | int | YES |  |  |  |
| Noti_Subject | nvarchar | YES |  |  |  |
| Noti_Description | nvarchar | YES |  |  |  |
| Ref1 | varchar | YES |  |  |  |
| Ref2 | varchar | YES |  |  |  |
| IsPosted | bit | YES |  |  |  |
| StopOSFA | bit | YES |  |  |  |
| MustUpdateData | bit | YES |  |  |  |
| ReleaseTransLock | bit | YES |  |  |  |
| SpecialOperation | nvarchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[GETNOTIFICATIONS]]
- [[Pro_NewCustomers]]
- [[Pro_TransLock]]

**Writes (6):**
- [[OT_ImportCustStockTacking]]
- [[OT_ImportGapTrans]]
- [[Pro_ConvertUnloadOrderToTransaction]]
- [[Pro_NewCustomers]]
- [[Pro_SalesPersons]]
- [[Pro_TransLock]]

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
