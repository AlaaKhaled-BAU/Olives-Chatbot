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
last_verified: 2026-10-03
---
# RequestSalesmanNoTransaction

## Business Purpose
Stores notification/alert events raised when a salesman reports that no transactions could be conducted (e.g. daily alert or route stop exception). Corresponds to workflow `FunctionID = 24` ("NoTransaction Notification"). Captures salesman number (`SalesPersonNo`), transaction date (`TrDate`), read status flag (`IsReadNotification`), and `CompanyID`. Queryable via `t.RequestSalesmanNoTransaction`.

## Chatbot semantics
(Query `t.RequestSalesmanNoTransaction` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| إشعارات عدم وجود حركات | `SalesPersonNo`, `TrDate` | Direct filter | Alerts sent from salesmen |
| حالة قراءة الإشعار | `IsReadNotification` | `1` = Read, `0` = Unread | Supervisor acknowledged alert |
| الربط مع سجل الموافقات العام | Join `t.WF_MasterLog` | `m.FunctionID = 24 AND TRY_CAST(m.Ref1 AS numeric) = req.AutoID AND m.CompanyID = req.CompanyID` | Links alert to workflow record |

## Grain & keys
- **PK**: `AutoID` (numeric identity, 1 row = 1 no-transaction notification)
- **Tenant key**: `CompanyID`
- **Conventions**: `SalesPersonNo` → [[SalesPersons]](ID)

## Pipeline (how rows get here)
Sent from mobile devices → imported via `OT_ImportRequestSalesmanNoTransaction` → calls `WF_AddWorkFlowLevelOne @CompNo, 24, @NewAutoID` → inserts `WF_MasterLog` (`Ref1 = AutoID`).

## Related
- [[WF_MasterLog]]
- [[WF_SubLog]]
- [[WF_Functions]]
- [[NoTransactionsLog]]
- [[NoTransactionsReasons]]
- [[_RequestTo-Join-Conventions]]


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
