---
type: shared
name: Naming-Conventions
tags: [#reference, #shared]
---

# Naming Conventions

> Auto-audited: 2026-07-05

## Issues Found

| Issue | Count | Details |
|-------|-------|---------|
| Unregistered tags in use | 1 | `synth` — only tag still used but not previously listed in conventions (now documented below) |
| Stale counts | 18 | All tag counts outdated since Phase 1 |
| Invalid YAML format | 2 | 2 MOC files have tags without `#` prefix |
| Missing tag clusters | Yes | #salesperson, #onboarding, #routes, #promotion, #returns, #payments, #targets, #pricing, #admin, #setup should be documented |

## Tag Distribution

| Tag | Olives_BO | OSFA_DB | Workflows | Relations | Shared |
|-----|-----------|---------|-----------|-----------|--------|
| #backoffice | 1,860 | 0 | 0 | 0 | 0 |
| #sales | 740 | 35 | 1 | 0 | 0 |
| #reporting | 563 | 0 | 0 | 0 | 0 |
| #mobile | 0 | 506 | 0 | 0 | 0 |
| #integration | 406 | 1 | 0 | 0 | 0 |
| #order | 360 | 25 | 0 | 0 | 0 |
| #billing | 314 | 40 | 0 | 0 | 0 |
| #inventory | 310 | 42 | 1 | 0 | 0 |
| #customer | 317 | 30 | 1 | 0 | 0 |
| #workflow | 153 | 31 | 9 | 0 | 0 |
| #reference | 155 | 16 | 0 | 0 | 6 |
| #gps | 146 | 5 | 1 | 0 | 0 |
| #log | 72 | 12 | 0 | 0 | 0 |
| #auth | 79 | 2 | 1 | 0 | 0 |
| #mms | 72 | 0 | 0 | 0 | 0 |
| #survey | 32 | 7 | 0 | 0 | 0 |
| #legal | 25 | 1 | 0 | 0 | 0 |
| #fk | 20 | 0 | 0 | 0 | 0 |
| #assets | 17 | 0 | 0 | 0 | 0 |
| #shared | 0 | 0 | 1 | 0 | 10 |
| #setup | 0 | 0 | 4 | 0 | 0 |
| #moc | 1 | 1 | 1 | 0 | 0 |
| #admin | 0 | 0 | 3 | 0 | 0 |
| #pricing | 0 | 0 | 2 | 0 | 0 |
| #transactions | 0 | 0 | 1 | 0 | 0 |
| #targets | 0 | 0 | 1 | 0 | 0 |
| #sync | 0 | 0 | 1 | 0 | 0 |
| #stock | 0 | 0 | 1 | 0 | 0 |
| #security | 0 | 0 | 1 | 0 | 0 |
| #salespersons | 0 | 0 | 1 | 0 | 0 |
| #routes | 0 | 0 | 1 | 0 | 0 |
| #returns | 0 | 0 | 1 | 0 | 0 |
| #promotions | 0 | 0 | 1 | 0 | 0 |
| #payments | 0 | 0 | 1 | 0 | 0 |
| #onboarding | 0 | 0 | 1 | 0 | 0 |
| #master-data | 0 | 0 | 1 | 0 | 0 |
| #kpi | 0 | 0 | 1 | 0 | 0 |
| #items | 0 | 0 | 1 | 0 | 0 |
| #dashboards | 0 | 0 | 1 | 0 | 0 |
| #dashboard | 0 | 0 | 0 | 0 | 1 |
| #daily-operations | 0 | 0 | 1 | 0 | 0 |
| #collections | 0 | 0 | 1 | 0 | 0 |
| #approvals | 0 | 0 | 1 | 0 | 0 |

**Total unique tags**: 43 (plus 2 without `#` prefix — YAML format errors to fix)

## Conventions

| Tag | Domain | Description |
|-----|--------|-------------|
| #admin | Shared | Administrator utilities, system configuration |
| #approvals | Workflow | Workflow approval processes |
| #assets | BO | Asset management, fixed assets |
| #auth | Both | Authentication, login, user permissions |
| #backoffice | BO | Back-office system tables |
| #billing | Both | Invoicing, billing, financial transactions |
| #collections | Workflow | Payment collection processes |
| #customer | Both | Customer data, CRM |
| #daily-operations | Workflow | Day-to-day operational processes |
| #dashboard | Shared | Dashboard, KPI views |
| #dashboards | Workflow | KPI targets and dashboards |
| #fk | Both | Foreign key relationships |
| #gps | Both | GPS tracking, location data |
| #integration | Both | Third-party API integration, data sync |
| #inventory | Both | Inventory, stock, warehouse |
| #items | Workflow | Item master data |
| #kpi | Shared | Key performance indicator |
| #legal | Both | Legal documents, contracts |
| #log | Both | Audit logs, action logs, error logs |
| #master-data | Workflow | Master data setup |
| #mms | BO | Maintenance management system |
| #mobile | OSFA | Mobile/Front-Office tables |
| #moc | Shared | Map of Content index notes |
| #onboarding | Workflow | Salesman or customer onboarding |
| #order | Both | Sales orders, order management |
| #payments | Workflow | Payment processing |
| #pricing | Workflow | Pricing, price lists |
| #promotions | Workflow | Promotions, offers |
| #reference | Both | Reference, documentation, indexes |
| #reporting | BO | Reporting, analytics |
| #returns | Workflow | Returns, reversals |
| #routes | Workflow | Route planning |
| #sales | Both | Sales, salespersons |
| #salespersons | Workflow | Salesperson management |
| #security | Workflow | System security |
| #setup | Workflow | Initial setup, configuration |
| #shared | Shared | Shared cross-database documents |
| #stock | Workflow | Stock management |
| #survey | Both | Surveys, questionnaires |
| #synth | Shared | Synthetic / generated documentation tag |
| #sync | Workflow | Data synchronization |
| #targets | Workflow | Targets and performance |
| #transactions | Workflow | Transaction processing |
| #workflow | Both | Workflow, business process |