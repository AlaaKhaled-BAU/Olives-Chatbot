---
type: relation
database: Olives_BO
name: CustomersFinancialDetails--Customers
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[CustomersFinancialDetails]]
referenced_table: [[Customers]]
columns: "CustomersFinancialDetails.CompanyID,CustomerID → Customers.CompanyID,ID"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# CustomersFinancialDetails → Customers

**FK**: CustomersFinancialDetails.CompanyID,CustomerID → [[Customers]].CompanyID,ID

**Business meaning**: Per-position commercial terms row: credit limit, due days, balances (CustomerBalance/ChqBalance), price list override. One customer can hold several rows across positions/business units.

## Tenancy

Chatbot queries `t.CustomersFinancialDetails` and `t.Customers` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[CustomersFinancialDetails]]
- [[Customers]]
- [[CustomersFinancialDetails--RoutesInformation]]
- [[RequestToExceedCustomerCreditLimit--Customers]]
