---
type: table
database: Olives_BO
name: OWGM_Transactions
schema: dbo
tags: [#backoffice]
foreign_keys:
referenced_by:
  - [[OWGM_AUTOGATESASSIGMENT]]
  - [[OWGM_AppService]]
  - [[Pro_OWGM_Transactions]]
support_relevance: high
last_verified: 2026-07-05
---
# OWGM_Transactions


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores owgm transactions records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| TransID | numeric | YES | ✓ |  |  |
| TransType | int | NO |  |  |  |
| CompanyID | smallint | NO |  |  |  |
| TrDateTime | datetime | YES |  |  |  |
| Barcode | nvarchar | YES |  |  |  |
| ERP_TransYear | int | YES |  |  |  |
| ERP_TransType | int | YES |  |  |  |
| ERP_TransNo | bigint | YES |  |  |  |
| GateUserID | int | YES |  |  |  |
| SalesmanNo | int | YES |  |  |  |
| SalesmanName | varchar | YES |  |  |  |
| TransGateID | int | YES |  |  |  |
| GateDateTimeAssigment | datetime | YES |  |  |  |
| DeliveryUserID | int | YES |  |  |  |
| DeliveryUserDateTimeAssigment | datetime | YES |  |  |  |
| IsDone | bit | YES |  |  |  |
## Primary Key
TransID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OWGM_AUTOGATESASSIGMENT]]
- [[OWGM_AppService]]
- [[Pro_OWGM_Transactions]]

**Writes (1):**
- [[OWGM_AppService]]

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
