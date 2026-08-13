---
type: relation
database: Olives_BO
name: Customers--SalesPersons
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[Customers]]
referenced_table: [[SalesPersons]]
columns: "Customers.SalesPersonID → SalesPersons.ID"
---

# Customers → SalesPersons

**FK**: Customers.SalesPersonID → [[SalesPersons]].ID

**Business meaning**: Assigns each customer to a primary salesperson. Controls route assignments, commission calculations, and sales territory management.

**Source table**: [[Customers]]
**Target table**: [[SalesPersons]]
