---
type: relation
database: Olives_BO
name: RequestToExceedCustomerCreditLimit--Customers
tags: [#convention, #workflow]
support_relevance: high
parent_table: [[RequestToExceedCustomerCreditLimit]]
referenced_table: [[Customers]]
columns: "RequestToExceedCustomerCreditLimit.CompanyID,CustomerNo → Customers.CompanyID,ID"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# RequestToExceedCustomerCreditLimit → Customers

**Convention join** (no DB-level FK): RequestToExceedCustomerCreditLimit.CompanyID+CustomerNo → [[Customers]].CompanyID+ID

**Business meaning**: Device-raised approval request fired when an invoice would push a customer past their credit limit. CustomerNo identifies the customer (the old CustomerID claim was wrong — that column does not exist); IsAproved gates whether the tablet may post the invoice.

## Tenancy

Chatbot queries `t.RequestToExceedCustomerCreditLimit` and `t.Customers` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[RequestToExceedCustomerCreditLimit]]
- [[Customers]]
- [[_RequestTo-Join-Conventions]]
- [[_MOC-Olives_BO]]
