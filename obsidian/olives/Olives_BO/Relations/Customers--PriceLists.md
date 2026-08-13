---
type: relation
database: Olives_BO
name: Customers--PriceLists
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[Customers]]
referenced_table: [[PriceLists]]
columns: "Customers.PriceListID → PriceLists.ID"
---

# Customers → PriceLists

**FK**: Customers.PriceListID → [[PriceLists]].ID

**Business meaning**: Sets the default pricing tier for a customer. Transactions use this price list unless overridden.

**Source table**: [[Customers]]
**Target table**: [[PriceLists]]
