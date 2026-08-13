---
type: relation
database: Olives_BO
name: BankDepositDF--BankDepositHF
tags: [#fk]
support_relevance: medium
parent_table: [[BankDepositDF]]
referenced_table: [[BankDepositHF]]
columns: "BankDepositDF.CompanyID, VouYear, VouNo → BankDepositHF.CompanyID, VouYear, VouNo"
---

# BankDepositDF → BankDepositHF

**FK**: BankDepositDF.CompanyID, VouYear, VouNo → [[BankDepositHF]].CompanyID, VouYear, VouNo

**Business meaning**: AUTO-GENERATED — verify before trusting.

**Source table**: [[BankDepositDF]]
**Target table**: [[BankDepositHF]]
