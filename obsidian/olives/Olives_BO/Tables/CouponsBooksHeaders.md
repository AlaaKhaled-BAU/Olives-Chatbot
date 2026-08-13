---
type: table
database: Olives_BO
name: CouponsBooksHeaders
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
referenced_by:
  - [[Pro_CouponsBooksDetails]]
  - [[Pro_CouponsBooksHeaders]]
  - [[SMS_ZumotPromoCodes]]
support_relevance: high
last_verified: 2026-07-05
---
# CouponsBooksHeaders


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores couponsbooksheaders records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Customers]] |
| ID | int | NO | ✓ |  |  |
| BookNo | nvarchar | YES |  |  |  |
| CustomerID | bigint | YES |  | ✓ | [[Customers]] |
| IsSuspended | bit | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (3):**
- [[Pro_CouponsBooksDetails]]
- [[Pro_CouponsBooksHeaders]]
- [[SMS_ZumotPromoCodes]]

**Writes (2):**
- [[Pro_CouponsBooksDetails]]
- [[Pro_CouponsBooksHeaders]]

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
