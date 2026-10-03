---
type: table
database: Olives_BO
name: CustomerReceivablesInfo
schema: dbo
tags: [#backoffice, #customer]
foreign_keys:
referenced_by:
  - [[Pro_CustomerReceivablesInfo]]
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

**Writes (1):**
- [[Pro_CustomerReceivablesInfo]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Tenant key**: this table scopes by CompNo (not CompanyID) — inside t.-views it is pre-filtered; raw joins map CompNo -> Companies.ID
- **Semantics**: ReceivablesMonth aggregates monthly receivables; Exclude* flags mark rows kept out of the aggregate — verify intent before summing
## Tenancy

Chatbot queries `t.CustomerReceivablesInfo` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`. Raw dbo access is blocked for `chatbot_ro`.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
