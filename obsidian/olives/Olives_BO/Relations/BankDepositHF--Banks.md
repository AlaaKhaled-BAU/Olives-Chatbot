---
type: relation
database: Olives_BO
name: BankDepositHF--Banks
tags: [#fk]
support_relevance: medium
parent_table: [[BankDepositHF]]
referenced_table: [[Banks]]
columns: "BankDepositHF.CompanyID, BankNo → Banks.CompanyID, ID"
---

# BankDepositHF → Banks

**FK**: BankDepositHF.CompanyID, BankNo → [[Banks]].CompanyID, ID

**Business meaning**: AUTO-GENERATED — verify before trusting.

**Source table**: [[BankDepositHF]]
**Target table**: [[Banks]]
