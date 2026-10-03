---
type: table
database: Olives_BO
name: PendingOrdersHeaders
schema: dbo
tags: [#backoffice, #order]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# PendingOrdersHeaders


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores pendingordersheaders records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | int | NO |  |  |  |
| OrderNo | int | NO |  |  |  |
| SalespersonID | int | NO |  |  |  |
| CustomerNo | bigint | NO |  |  |  |
| CustomerName | nvarchar | NO |  |  |  |
| OrderDate | smalldatetime | NO |  |  |  |
| TotalBeforeTax | float | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**

**Writes (0):**
_None_

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Carrier naming**: this family uses SalespersonID(int) + CustomerNo(bigint) — join Customers via CompanyID+CustomerNo, NOT CustomerID
## Tenancy

Chatbot queries `t.PendingOrdersHeaders` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`. Raw dbo access is blocked for `chatbot_ro`.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
