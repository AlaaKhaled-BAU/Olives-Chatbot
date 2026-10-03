---
type: relation
database: Olives_BO
name: SalesPersons--SalesPersons
tags: [#fk, #hierarchy, #salesforce]
support_relevance: high
parent_table: [[SalesPersons]]
referenced_table: [[SalesPersons]]
columns: "SalesPersons.Parent → SalesPersons.ID"
last_verified: 2026-10-03
verified_source: live Olives_BO & schema_cache.json
---

# SalesPersons (Subordinate) → SalesPersons (Supervisor/Parent)

**Join Key**: `subordinate.Parent = supervisor.ID`

**Business meaning**: Self-referencing organizational hierarchy for sales representatives and supervisors. 
- A supervisor typically has `SalesPersonType = 3` (or NULL parent).
- Field salesmen typically have `SalesPersonType = 4` and `Parent` set to their supervisor's `ID`.

## Recursive / Subordinate Query Pattern
```sql
SELECT 
    sup.ID AS SupervisorID, 
    sup.Name AS SupervisorName, 
    sp.ID AS SalesmanID, 
    sp.Name AS SalesmanName
FROM t.SalesPersons sp
INNER JOIN t.SalesPersons sup ON sp.Parent = sup.ID
WHERE sp.IsDeleted = 0 AND sup.IsDeleted = 0;
```

## Tenancy
Chatbot queries `t.SalesPersons` which filters automatically by `SESSION_CONTEXT(N'CompanyID')`.

## See also
- [[SalesPersons]]
- [[SystemCodes]]
- [[Positions]]
