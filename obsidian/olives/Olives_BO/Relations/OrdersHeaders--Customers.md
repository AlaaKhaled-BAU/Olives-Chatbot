---
type: relation
database: Olives_BO
name: OrdersHeaders--Customers
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[OrdersHeaders]]
referenced_table: [[Customers]]
columns: "OrdersHeaders.CustomerID → Customers.ID"
---
tenant_scoping: "chatbot queries t.-views only; SESSION_CONTEXT('CompanyID')"
last_verified: 2026-08-22
---

# OrdersHeaders → Customers

**FK**: OrdersHeaders.CustomerID → [[Customers]].ID

**Business meaning**: Links each sales order to the customer who placed it. Core for order processing, customer history, and accounts receivable.

**Source table**: [[OrdersHeaders]]
**Target table**: [[Customers]]
