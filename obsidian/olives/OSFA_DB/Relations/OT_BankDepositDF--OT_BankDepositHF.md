---
type: relation
database: OSFA_DB
name: OT_BankDepositDF--OT_BankDepositHF
tags: [#fk]
support_relevance: medium
parent_table: [[OT_BankDepositDF]]
referenced_table: [[OT_BankDepositHF]]
columns: "OT_BankDepositDF.CompNo, VouYear, VouNo → OT_BankDepositHF.CompNo, VouYear, VouNo"
---

# OT_BankDepositDF → OT_BankDepositHF

**FK**: OT_BankDepositDF.CompNo, VouYear, VouNo → [[OT_BankDepositHF]].CompNo, VouYear, VouNo

**Business meaning**: AUTO-GENERATED — verify before trusting.

**Source table**: [[OT_BankDepositDF]]
**Target table**: [[OT_BankDepositHF]]
