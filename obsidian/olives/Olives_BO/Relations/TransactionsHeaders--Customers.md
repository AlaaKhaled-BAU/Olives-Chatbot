---
type: relation
database: Olives_BO
name: TransactionsHeaders--Customers
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[TransactionsHeaders]]
referenced_table: [[Customers]]
columns: "TransactionsHeaders.CustomerID → Customers.ID"
---

# TransactionsHeaders → Customers

**FK**: TransactionsHeaders.CustomerID → [[Customers]].ID

**Business meaning**: Links every transaction (invoice/order/return) to its customer. Critical for customer balance tracking, aged receivables, and invoice history.

**Source table**: [[TransactionsHeaders]]
**Target table**: [[Customers]]
