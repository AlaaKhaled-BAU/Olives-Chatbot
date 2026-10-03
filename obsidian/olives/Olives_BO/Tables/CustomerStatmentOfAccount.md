---
type: table
database: Olives_BO
name: CustomerStatmentOfAccount
schema: dbo
tags: [#backoffice, #customer]
foreign_keys:
referenced_by:
  - [[Rpt_CustomerAccountStatement_Sukhtian]]
  - [[Rpt_CustomerStatmentOfAccount]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomerStatmentOfAccount


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customerstatmentofaccount records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| CustomerID | bigint | NO | ✓ |  |  |
| TrType | varchar | NO | ✓ |  |  |
| TrNo | varchar | NO | ✓ |  |  |
| TrSer | smallint | NO | ✓ |  |  |
| DeptNo | int | NO | ✓ |  |  |
| TrDate | smalldatetime | NO | ✓ |  |  |
| TrName | varchar | YES |  |  |  |
| Debit | money | YES |  |  |  |
| Credit | money | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
| Balance | money | YES |  |  |  |
## Primary Key
CompanyID
CustomerID
TrType
TrNo
TrSer
DeptNo
TrDate
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (28):**
- [[Rpt_CustomerAccountStatement_Sukhtian]]
- [[Rpt_CustomerStatmentOfAccount]]

**Writes (24):**

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Ledger role**: running Debit/Credit/Balance ledger — authoritative for "what does X owe" over CFD cached balances
- **TrType domain**: varchar codes seen live: '0','1','3','9999' — decode against source transaction family before filtering; do not guess
- **Join hint**: TrType+TrNo point back at source vouchers; pair with TransactionTypeID lookups (see TransactionsTypes catalog)
## Tenancy

Chatbot queries `t.CustomerStatmentOfAccount` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`. Raw dbo access is blocked for `chatbot_ro`.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
