---
type: relation
database: OSFA_DB
name: OT_Payments--OT_Customers
tags: [#fk, #mobile]
support_relevance: high
parent_table: [[OT_Payments]]
referenced_table: `"`OT_Customers`"`
columns: "OT_Payments.CustomerID → `OT_Customers`.ID"
---

# OT_Payments → OT_Customers

**FK**: OT_Payments.CustomerID → `OT_Customers`.ID

**Business meaning**: Mobile payment records link to the customer who made the payment. Synced back to BO Receipts.

**Source table**: [[OT_Payments]]
**Target table**: `OT_Customers`
