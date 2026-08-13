---
type: table
database: Olives_BO
name: CustomerReceivablesInfo
schema: dbo
tags: [#backoffice, #customer]
foreign_keys:
referenced_by:
  - [[Pro_CustomerReceivablesInfo]]
  - [[Rpt_CustomerReceivablesInfo_Tablet]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomerReceivablesInfo


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customerreceivablesinfo records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| CustomerID | bigint | NO | ✓ |  |  |
| ExcludeCashPayments | float | YES |  |  |  |
| ExcludeReturns | float | YES |  |  |  |
| ExcludePendingOrders | float | YES |  |  |  |
| ExceptionCollectionManager | float | YES |  |  |  |
| ReceivablesMonth | smallint | YES |  |  |  |
| ReceivablesYear | smallint | YES |  |  |  |
| Receivables | float | YES |  |  |  |
## Primary Key
CompNo
CustomerID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_CustomerReceivablesInfo]]
- [[Rpt_CustomerReceivablesInfo_Tablet]]

**Writes (1):**
- [[Pro_CustomerReceivablesInfo]]

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
