---
type: table
database: Olives_BO
name: PaymentsOrders
schema: dbo
tags: [#backoffice, #billing, #order]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
  - [[SalesPersons]]
referenced_by:
  - [[Alpha_Integ_SendIssuePaymentOrder]]
  - [[OT_CustIssueAmount_Update]]
  - [[Pro_GetCashCloseTotals]]
  - [[Pro_OrdersPayment]]
  - [[Rpt_CashSummary]]
  - [[Rpt_ExpensesTrans]]
  - [[Rpt_MonthlySalesProfit]]
  - [[Rpt_SalesmanSalesRecStatment]]
support_relevance: high
last_verified: 2026-07-05
---
# PaymentsOrders


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores paymentsorders records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| SalespersonID | int | YES |  | ✓ | [[SalesPersons]] |
| OrderDate | smalldatetime | YES |  |  |  |
| CustomerID | bigint | YES |  | ✓ | [[Customers]] |
| Amount | float | YES |  |  |  |
| IssuedAmount | float | YES |  |  |  |
| IsIssued | bit | YES |  |  |  |
| IssuedDate | smalldatetime | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
| RefNo | nvarchar | YES |  |  |  |
| PostedToERP | bit | YES |  |  |  |
| ForeignIssuedAmount | float | YES |  |  |  |
| CurrencyID | smallint | YES |  |  |  |
| ExchangeRate | float | YES |  |  |  |
| OrderType | int | YES |  |  |  |
| IsFromCash | bit | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
## Primary Key
CompanyID
OrderYear
OrderNo
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, SalespersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (8):**
- [[Alpha_Integ_SendIssuePaymentOrder]]
- [[OT_CustIssueAmount_Update]]
- [[Pro_GetCashCloseTotals]]
- [[Pro_OrdersPayment]]
- [[Rpt_CashSummary]]
- [[Rpt_ExpensesTrans]]
- [[Rpt_MonthlySalesProfit]]
- [[Rpt_SalesmanSalesRecStatment]]

**Writes (3):**
- [[Alpha_Integ_SendIssuePaymentOrder]]
- [[OT_CustIssueAmount_Update]]
- [[Pro_OrdersPayment]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
