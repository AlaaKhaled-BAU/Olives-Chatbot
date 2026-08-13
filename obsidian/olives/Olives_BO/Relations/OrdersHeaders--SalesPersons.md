---
type: relation
database: Olives_BO
name: OrdersHeaders--SalesPersons
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[OrdersHeaders]]
referenced_table: [[SalesPersons]]
columns: "OrdersHeaders.SalesPersonID → SalesPersons.ID"
---

# OrdersHeaders → SalesPersons

**FK**: OrdersHeaders.SalesPersonID → [[SalesPersons]].ID

**Business meaning**: Identifies the salesperson responsible for the order. Drives commission payout, sales performance tracking, and territory analysis.

**Source table**: [[OrdersHeaders]]
**Target table**: [[SalesPersons]]
