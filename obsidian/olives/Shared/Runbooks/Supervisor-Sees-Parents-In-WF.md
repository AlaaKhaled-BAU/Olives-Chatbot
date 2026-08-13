---
type: shared
name: Supervisor-Sees-Parents-In-WF
tags: [#runbook, #support, #billing]
customer: malayo
support_relevance: high
last_verified: 2026-07-21
---

# Supervisor-Sees-Parents-In-WF

## Symptom
Supervisor opens WF/report screens ("تقرير ملخص المسارات لكل مندوب") on tablet. Dropdown shows his ancestors (parents) instead of his subordinates (children).

## Hierarchy
```
2000 → 1000 → [1003] → [1005, 1004, 990]
```
Supervisor 1003 sees 1000 and 2000 in dropdown, not 1005, 1004, 990.

## Root Cause
`OT_AppService` @CmdType=`GetSalesmanList` (OSFA_DB.sql:9519) had a flat filter:
```sql
WHERE ISNULL([SalesPersonType],0) < 4
```
No supervisor hierarchy. Returned all type 0-3 salesmen company-wide.

If supervisor children were type 4 → excluded. If ancestors were type 0-3 → included. Caused exact reverse of expected list.

## Fix Applied
Changed `GetSalesmanList` to use downward hierarchy function:
```sql
SELECT Fun_GetSalesmanTreeByID.ID, SalesPersons.Name, SalesPersons.SalesPersonType
FROM Olives_BO.dbo.Fun_GetSalesmanTreeByID(@CompanyID, @SalesmanNo) AS Fun_GetSalesmanTreeByID
INNER JOIN Olives_BO.dbo.SalesPersons ON Fun_GetSalesmanTreeByID.CompanyID = SalesPersons.CompanyID AND Fun_GetSalesmanTreeByID.ID = SalesPersons.ID
```

## Files Changed
- `db/OSFA_DB.sql` — `GetSalesmanList` cmdType in `OT_AppService` proc (line 9519)
- `db/OSFA_DB6-8-2026.sql` — same fix

## Key Functions/Tables
| Object | Location | Purpose |
|---|---|---|
| `OT_AppService` | OSFA_DB.sql:6774 | Main tablet API stored procedure |
| `Fun_GetSalesmanTreeByID` | BO.sql:6257 | Recursive downward CTE — returns ID + descendants |
| `Fun_GetSalesPersonTree` | BO.sql:6637 | Upward traversal (parent/ancestor chain) |
| `SalesmanBySupervisorData` | OSFA_DB.sql:8910 | **Correct** cmdType — already uses `Fun_GetSalesmanTreeByID` |
| `GetSalesmanList` | OSFA_DB.sql:9519 | **Buggy** cmdType — was using flat `<4` filter |

## Related cmdTypes
- `SalesmanBySupervisorData` (8910) — already correct, used elsewhere
- `GetSalesmanList` (9519) — **was** buggy, now fixed
- `WFGetWFSalesmanRef` (8959) — returns WF ref string, unaffected
- `GetOT_SalesmanMFDataDB` (6979) — returns logged-in salesman's own record

## Prevention
- Dropdown/selection cmdTypes must use hierarchy-aware functions (`Fun_GetSalesmanTreeByID` downward, or `Fun_GetSalesPersonTree` upward) — never flat SalesPersonType filters.
- When adding new cmdTypes that list salesmen, always pass @SalesmanNo and use tree functions.
