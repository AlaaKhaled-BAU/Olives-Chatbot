---
type: moc
name: MOC-Runbooks
tags: [#moc, #runbook, #support]
support_relevance: high
last_verified: 2026-07-14
---
# MOC — Runbooks

Troubleshooting runbooks for the Olives ERP (Olives_BO + OSFA_DB). Each links OUT to the tables/procedures they reference.

## Runbooks
- [[Sync-Conflict]] — tablet vs BO simultaneous edit, last-write-wins loss, duplicate TabletSysID, orphan rows, IsPosted stuck false
- [[Orphan-Records]] — missing parent refs / FK violations, query failures
- [[Duplicate-Keys]] — duplicate PK / unique-key violations on import/sync
- [[Duplicate-Visit]] — same customer visit logged twice (tablet MMS_OrderVisits / BO CustomersVisitActivity)
- [[Credit-Limit-Block]] — customer/salesman credit-limit exceed, approval WF
- [[Invoice-Posting-Failure]] — invoice not posted to integration/ERP, stuck in IntegrationPostedTransactions
- [[ZATCA-Validation]] — KSA e-invoice validation failures
- [[Login-Device-Issues]] — salesman device/login, passkey, permissions
- [[Van-Stock-Mismatch]] — van load/unload vs SalesPersonsItemsBalance divergence, shrinkage

## Cross-references
- System overview: [[Welcome]], [[Glossary]]
- Integration flow: [[Cross-DB-Links]], [[IntegrationPostedTransactions]], [[IntegrationErrorLog]]
- Impact analysis: use the `get_impact` MCP tool / `referenced_by` frontmatter on table/proc notes.
