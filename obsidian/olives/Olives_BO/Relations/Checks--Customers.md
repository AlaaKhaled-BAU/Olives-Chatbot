---
type: relation
database: Olives_BO
name: Checks--Customers
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[Checks]]
referenced_table: [[Customers]]
columns: "Checks.CustomerID → Customers.ID"
---

# Checks → Customers

**FK**: Checks.CustomerID → [[Customers]].ID

**Business meaning**: Links a check to the customer who issued it. Tracks which customer payments are covered by check instruments.

**Source table**: [[Checks]]
**Target table**: [[Customers]]
