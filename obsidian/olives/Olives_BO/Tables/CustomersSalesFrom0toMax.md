---
type: table
database: Olives_BO
name: CustomersSalesFrom0toMax
schema: dbo
tags: [#backoffice, #customer, #sales]
foreign_keys:
referenced_by:
  - [[ZeidanCustomersSales0ToMax]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomersSalesFrom0toMax


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customerssalesfrom0tomax records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| TypeID | int | YES |  |  |  |
| TypeName | nvarchar | YES |  |  |  |
| CustomerID | bigint | YES |  |  |  |
| CustomerName | nvarchar | YES |  |  |  |
| SalesValue | float | YES |  |  |  |
| ReturnValue | float | YES |  |  |  |
| NetSalesValue | nvarchar | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[ZeidanCustomersSales0ToMax]]

**Writes (1):**
- [[ZeidanCustomersSales0ToMax]]

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
