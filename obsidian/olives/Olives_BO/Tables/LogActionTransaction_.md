---
type: table
database: Olives_BO
name: LogActionTransaction_
schema: dbo
tags: [#backoffice, #log]
foreign_keys:
referenced_by:
support_relevance: low
last_verified: 2026-07-05
---
# LogActionTransaction_


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores logactiontransaction  records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES |  |  |  |
| CompNo | smallint | NO |  |  |  |
| ActionID | nvarchar | YES |  |  |  |
| TimeStamp | datetime | NO |  |  |  |
| SalesmanID | nvarchar | YES |  |  |  |
| Data1 | nvarchar | YES |  |  |  |
| Data2 | nvarchar | YES |  |  |  |
| Data3 | nvarchar | YES |  |  |  |
| Data4 | nvarchar | YES |  |  |  |
| Data5 | nvarchar | YES |  |  |  |
| GpsX | nchar | YES |  |  |  |
| GpsY | nchar | YES |  |  |  |
| RouteID | int | YES |  |  |  |
| OSFA_AutoID | numeric | YES |  |  |  |
| PostedByEmail | bit | YES |  |  |  |
| VehicleId | varchar | YES |  |  |  |
| CarCounter | bigint | YES |  |  |  |
| IsSMSSend | bit | YES |  |  |  |
| GPSOn | bit | YES |  |  |  |
| NetworkOn | bit | YES |  |  |  |
| InternetOn | bit | YES |  |  |  |
| AppVersion | varchar | YES |  |  |  |
| IsProcced | bit | YES |  |  |  |
| CustLocLineID | varchar | YES |  |  |  |
| AssistantsIDs | varchar | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

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
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[PromotionsApprovalLog]]
- [[OWGM_LockLog]]
- [[TransfersOrdersDetails_ErrorQty]]
