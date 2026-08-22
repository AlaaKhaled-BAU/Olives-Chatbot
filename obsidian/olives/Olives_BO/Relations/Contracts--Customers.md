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
tenant_scoping: "chatbot queries t.-views only; SESSION_CONTEXT('CompanyID')"
last_verified: 2026-08-22
---

# Contracts → Customers

**FK**: Contracts.CustomerID → [[Customers]].ID

**Business meaning**: Each contract is assigned to a customer. Enables contract lifecycle tracking, renewal management, and customer-level contract profitability reporting.

**Source table**: [[Contracts]]
**Target table**: [[Customers]]
