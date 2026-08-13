---
type: relation
database: OSFA_DB
name: OT_OrderHF--OT_Customers
tags: [#fk, #mobile]
support_relevance: high
parent_table: [[OT_OrderHF]]
referenced_table: `"`OT_Customers`"`
columns: "OT_OrderHF.CustomerID → `OT_Customers`.ID"
---

# OT_OrderHF → OT_Customers

**FK**: OT_OrderHF.CustomerID → `OT_Customers`.ID

**Business meaning**: Mobile order headers belong to a customer. Synced to BO OrdersHeaders during posting.

**Source table**: [[OT_OrderHF]]
**Target table**: `OT_Customers`
