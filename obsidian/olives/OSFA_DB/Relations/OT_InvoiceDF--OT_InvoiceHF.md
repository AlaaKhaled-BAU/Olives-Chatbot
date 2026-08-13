---
type: relation
database: OSFA_DB
name: OT_InvoiceDF--OT_InvoiceHF
tags: [#fk, #mobile]
support_relevance: high
parent_table: [[OT_InvoiceDF]]
referenced_table: [[OT_InvoiceHF]]
columns: "OT_InvoiceDF.VouNo,VouType,VouYear,CompNo → OT_InvoiceHF.VouNo,VouType,VouYear,CompNo"
---

# OT_InvoiceDF → OT_InvoiceHF

**FK**: OT_InvoiceDF.VouNo,VouType,VouYear,CompNo → [[OT_InvoiceHF]].VouNo,VouType,VouYear,CompNo

**Business meaning**: Mobile invoice header-to-detail relationship. Compound FK matches the header on all four key columns.

**Source table**: [[OT_InvoiceDF]]
**Target table**: [[OT_InvoiceHF]]
