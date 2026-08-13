---
type: shared
name: Use-Cases
tags: [#usecase, #reference]
support_relevance: high
last_verified: 2026-07-14
---
# Use-Cases — Mapping Business Problems to Notes

Quick routing table for support engineers: pick the business situation, then open the linked runbook or reference note.

| # | Business situation | Go to |
|---|--------------------|-------|
| 1 | A customer says an invoice never reached SAP — trace it | [[Invoice-Posting-Failure]] + [[IntegrationPostedTransactions]] |
| 2 | Salesman can't log in on a new device | [[Login-Device-Issues]] |
| 3 | Van stock doesn't match system after unload | [[Van-Stock-Mismatch]] |
| 4 | Tablet shows stale / overwritten customer data | [[Sync-Conflict]] |
| 5 | Duplicate receipt / transaction posted | [[Duplicate-Keys]] |
| 6 | Credit limit keeps blocking a big order | [[Credit-Limit-Block]] |
| 7 | ZATCA rejected an e-invoice | [[ZATCA-Validation]] |
| 8 | Which procedures read table X (impact analysis) | Use the `get_impact` MCP tool / `referenced_by` frontmatter on the table note |
| 9 | Onboarding: what is this system? | [[Welcome]] + [[Glossary]] |
| 10 | Per-customer receivables aging | [[CustomersFinancialDetails]] + [[Rpt_CheckAging]] / [[Rpt_WF_FinancialAging]] |
| 11 | Route coverage / unvisited customers | [[SalespersonsGPSTracking]] + [[Locations]] + [[Rpt_UnvisitedCustomersByDate]] |
| 12 | Promotion not applied at van | [[PromotionsHeaders]] + [[PromotionsApprovalSetup]] |
| 13 | Supervisor sees wrong salesmen in WF dropdown (malayo) | [[Supervisor-Sees-Parents-In-WF]] |

## Notes
- Runbooks live in `Shared/Runbooks/` and link OUT to the tables/procedures they reference.
- For cross-DB data flow, see [[Cross-DB-Links]].
- For orphan/exception triage, see [[Exceptions]].
