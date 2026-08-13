---
type: relation
database: OSFA_DB
name: OT_OrderDF--OT_OrderHF
tags: [#fk, #mobile]
support_relevance: high
parent_table: [[OT_OrderDF]]
referenced_table: [[OT_OrderHF]]
columns: "OT_OrderDF.OrderNo,OrderYear,CompNo,VouType → OT_OrderHF.OrderNo,OrderYear,CompNo,VouType"
---

# OT_OrderDF → OT_OrderHF

**FK**: OT_OrderDF.OrderNo,OrderYear,CompNo,VouType → [[OT_OrderHF]].OrderNo,OrderYear,CompNo,VouType

**Business meaning**: Mobile order details under their parent order header. Compound FK matching all key columns.

**Source table**: [[OT_OrderDF]]
**Target table**: [[OT_OrderHF]]
