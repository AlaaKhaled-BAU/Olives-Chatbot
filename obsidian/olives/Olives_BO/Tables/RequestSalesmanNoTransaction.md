---
type: table
database: Olives_BO
name: RequestSalesmanNoTransaction
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
referenced_by:
  - [[OT_ImportRequestSalesmanNoTransaction]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AlertsRemoveAll]]
  - [[WF_AlertsUpdate]]
support_relevance: high
last_verified: 2026-07-05
---
# RequestSalesmanNoTransaction


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores requestsalesmannotransaction records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
| SalesPersonNo | int | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| IsReadNotification | bit | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OT_ImportRequestSalesmanNoTransaction]]
- [[WF_AlertsRemoveAll]]
- [[WF_AlertsUpdate]]

**Writes (4):**
- [[OT_ImportRequestSalesmanNoTransaction]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AlertsRemoveAll]]
- [[WF_AlertsUpdate]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Orphan lines**: Detail rows without matching header — causes sync failures
- **Posting failure**: IsPosted flag stuck false — check ERP integration log
- **Duplicate vouchers**: Same VouNo generated for different transactions — run dedup check
- **Currency mismatch**: ExRate different from CurrenciesRate table — financial reconciliation off
- **Void inconsistency**: IsVoid flag but original transaction still active — check WF approval

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
