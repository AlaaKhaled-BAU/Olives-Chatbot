---
type: table
database: Olives_BO
name: Receipts_Currency
schema: dbo
tags: [#backoffice, #billing]
foreign_keys:
  - [[Companies]]
  - [[Currencies]]
  - [[Receipts]]
referenced_by:
  - [[Rpt_CustomersVisitsCount]]
  - [[Rpt_SalesmanReceiptsCurrency]]
  - [[Rpt_SalesmanSummaryRoute]]
  - [[Rpt_SalesmanSummaryRoute_60]]
  - [[Rpt_SalesmanSummaryRoute_Atieh]]
  - [[Rpt_SalesmanSummaryRoute_zz]]
  - [[Rpt_SalesmanTimeSpentPerCustomer3]]
  - [[Rpt_SalesmanTimeSpentPerCustomer6_QimaH]]
  - [[Rpt_SalesmanTimeSpentPerCustomerQima7]]
  - [[Rpt_SalesmanTimeSpentPerCustomerQima8]]
support_relevance: high
last_verified: 2026-07-05
---
# Receipts_Currency


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores receipts currency records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Receipts]] |
| TransactionTypeID | smallint | NO | ✓ | ✓ | [[Receipts]] |
| TransactionYear | smallint | NO | ✓ | ✓ | [[Receipts]] |
| TransactionNo | int | NO | ✓ | ✓ | [[Receipts]] |
| CurrencyID | smallint | NO | ✓ | ✓ | [[Currencies]] |
| Amount | float | YES |  |  |  |
| ExchangeRate | float | YES |  |  |  |
## Primary Key
CompanyID
TransactionTypeID
TransactionYear
TransactionNo
CurrencyID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CurrencyID -> [[Currencies]](ID)
CompanyID, TransactionTypeID, TransactionYear, TransactionNo -> [[Receipts]](CompanyID, TransactionTypeID, TransactionYear, TransactionNo)
## Impact / Procedures Using This Table

**Reads (10):**
- [[Rpt_CustomersVisitsCount]]
- [[Rpt_SalesmanReceiptsCurrency]]
- [[Rpt_SalesmanSummaryRoute]]
- [[Rpt_SalesmanSummaryRoute_60]]
- [[Rpt_SalesmanSummaryRoute_Atieh]]
- [[Rpt_SalesmanSummaryRoute_zz]]
- [[Rpt_SalesmanTimeSpentPerCustomer3]]
- [[Rpt_SalesmanTimeSpentPerCustomer6_QimaH]]
- [[Rpt_SalesmanTimeSpentPerCustomerQima7]]
- [[Rpt_SalesmanTimeSpentPerCustomerQima8]]

**Writes (0):**
_None_

## Estimated Size / Volatility
Typical business table
## Common Issues

> [!warning] AUTO-GENERATED — verify before trusting

- **Purpose**: per-currency split of a Receipts session amount; sums need not equal header Amount when multi-currency
## Tenancy

Chatbot queries `t.Receipts_Currency` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`. Raw dbo access is blocked for `chatbot_ro`.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
