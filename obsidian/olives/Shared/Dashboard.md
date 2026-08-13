---
type: shared
name: Dashboard
tags: [#dashboards, #shared]
---
See also: [[_MOC-Olives_BO|Olives_BO Index]] | [[_MOC-OSFA_DB|OSFA_DB Index]] | [[_MOC-Workflows|Workflows Index]]

# Knowledge Base Dashboard

## Overview
```dataview
TABLE
  rows.file.link AS Type,
  length(rows.file.outlinks) AS Outlinks,
  length(rows.file.inlinks) AS Inlinks
FROM ""
GROUP BY type
```

## Tables by Database
```dataview
TABLE
  rows.file.link AS Table,
  rows.support_relevance AS Relevance,
  rows.foreign_keys AS FK_Links
FROM ""
WHERE type = "table"
GROUP BY database
```

## Procedures by Database
```dataview
TABLE rows.file.link AS Procedure, rows.reads_from AS Reads, rows.writes_to AS Writes
FROM ""
WHERE type = "procedure"
GROUP BY database
```

## Objects by support_relevance
```dataview
TABLE
  rows.file.link AS Note,
  rows.database AS DB,
  rows.type AS Type
FROM ""
WHERE support_relevance = "high" OR support_relevance = "medium" OR support_relevance = "low"
GROUP BY support_relevance
```

## Orphan Detection
```dataview
TABLE
  file.link AS Note,
  type,
  database
FROM ""
WHERE length(file.inlinks) + length(file.outlinks) <= 1
```

## High Relevance Objects
```dataview
TABLE
  file.link AS Note,
  database
FROM ""
WHERE support_relevance = "high"
```

---
See also: [[_MOC-Olives_BO|Olives_BO Index]] | [[_MOC-OSFA_DB|OSFA_DB Index]] | [[_MOC-Workflows|Workflows Index]]
type: shared
name: Usability-Report
---
See also: [[_MOC-Olives_BO|Olives_BO Index]] | [[_MOC-OSFA_DB|OSFA_DB Index]] | [[_MOC-Workflows|Workflows Index]]

# Support Agent Usability Check

> Generated: 2026-07-05

## Navigation Test Results
| Scenario | Keywords Searched | Coverage | Verdict |
|----------|-------------------|----------|---------|
| Customer reports duplicate orders | Orders, Order, Customer | 1 keyword hits | ⚠️ |
| Invoice posting failed | Invoice, Transaction, Posting | 1 keyword hits | ⚠️ |
| Sync job failing between OSFA and BO | Integration, Sync, OSFA | 2 keyword hits | ✅ |
| Salesperson cannot log into tablet | Salesperson, User, Device | 1 keyword hits | ⚠️ |
| Payment not reflecting in customer balance | Payment, Receipt, Balance | 1 keyword hits | ⚠️ |
| Inventory discrepancy in van stock | Stock, Inventory, Balance | 1 keyword hits | ⚠️ |
| Workflow approval stuck | Workflow, WF, Approval | 1 keyword hits | ⚠️ |
| Duplicate customer created during sync | Customer, Duplicate, Sync | 1 keyword hits | ⚠️ |
| Report not showing expected data | Report, RPT, Data | 3 keyword hits | ✅ |
| ZATCA e-invoice validation failed | ZATCA, Tax, E-invoice | 1 keyword hits | ⚠️ |

## Verdict
- **Pass**: Support agent can start from symptom description, find relevant tables/procedures via MOC/Glossary/Dashboard, and navigate to the fix in ≤3 clicks.
- **All scenarios pass**: False
- **Recommended enhancement**: Add a "Troubleshooting" section to the Dashboard with direct links to Common Issues by domain.
