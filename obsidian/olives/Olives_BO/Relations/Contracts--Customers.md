---
type: relation
database: Olives_BO
name: Contracts--Customers
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[Contracts]]
referenced_table: [[Customers]]
columns: "Contracts.CustomerID → Customers.ID"
---

# Contracts → Customers

**FK**: Contracts.CustomerID → [[Customers]].ID

**Business meaning**: Each contract is assigned to a customer. Enables contract lifecycle tracking, renewal management, and customer-level contract profitability reporting.

**Source table**: [[Contracts]]
**Target table**: [[Customers]]
