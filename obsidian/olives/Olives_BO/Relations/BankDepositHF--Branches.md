---
type: relation
database: Olives_BO
name: BankDepositHF--Branches
tags: [#fk]
support_relevance: medium
parent_table: [[BankDepositHF]]
referenced_table: [[Branches]]
columns: "BankDepositHF.CompanyID, BankNo, BranchNo → Branches.CompanyID, BankID, ID"
---

# BankDepositHF → Branches

**FK**: BankDepositHF.CompanyID, BankNo, BranchNo → [[Branches]].CompanyID, BankID, ID

**Business meaning**: AUTO-GENERATED — verify before trusting.

**Source table**: [[BankDepositHF]]
**Target table**: [[Branches]]
