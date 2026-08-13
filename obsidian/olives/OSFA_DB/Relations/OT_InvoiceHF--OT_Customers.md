---
type: relation
database: OSFA_DB
name: OT_InvoiceHF--OT_Customers
tags: [#fk, #mobile]
support_relevance: high
parent_table: [[OT_InvoiceHF]]
referenced_table: `"`OT_Customers`"`
columns: "OT_InvoiceHF.CustomerID → `OT_Customers`.ID"
---

# OT_InvoiceHF → OT_Customers

**FK**: OT_InvoiceHF.CustomerID → `OT_Customers`.ID

**Business meaning**: Mobile counterpart of the BO invoice-to-customer relationship. Links tablet invoices to the customer master synced from BO.

**Source table**: [[OT_InvoiceHF]]
**Target table**: `OT_Customers`
