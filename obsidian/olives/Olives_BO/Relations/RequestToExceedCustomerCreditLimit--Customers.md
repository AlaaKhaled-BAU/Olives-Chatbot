---
type: relation
database: Olives_BO
name: RequestToExceedCustomerCreditLimit--Customers
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[RequestToExceedCustomerCreditLimit]]
referenced_table: [[Customers]]
columns: "RequestToExceedCustomerCreditLimit.CustomerID → Customers.ID"
---

# RequestToExceedCustomerCreditLimit → Customers

**FK**: RequestToExceedCustomerCreditLimit.CustomerID → [[Customers]].ID

**Business meaning**: Workflow approval records for credit limit overrides reference the customer requesting the exception.

**Source table**: [[RequestToExceedCustomerCreditLimit]]
**Target table**: [[Customers]]
