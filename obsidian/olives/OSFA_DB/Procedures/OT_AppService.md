---
type: procedure
database: OSFA_DB
name: OT_AppService
schema: dbo
tags: [#mobile, #core, #api]
support_relevance: high
last_verified: 2026-07-21
---

# OT_AppService — Tablet API Gateway

## Purpose
The **single entry point** for the OSFA Android tablet app. Every screen, every action, every data load goes through this one procedure. The tablet never calls BO procedures directly.

## Architecture
```
Tablet App ──HTTP/JSON──▶ .NET Web Service ──▶ OT_AppService (@CmdType, @SalesmanNo, ...)
                                                      │
                                                      ├── Olives_BO.dbo (live ERP data)
                                                      └── OSFA_DB.dbo   (synced tablet tables)
```

The .NET layer is a thin pass-through — no business logic, no ORM. All logic lives in this single stored procedure (~3000+ lines).

## How It Works
1. Tablet sends `@CmdType` + parameters for the specific screen
2. Procedure resolves device context (`@ClientActive`, `@PositionsID`, permissions)
3. A giant `IF @CmdType = ...` chain matches the request
4. Each cmdType runs its own query — may read from `Olives_BO.dbo` (live), `OSFA_DB.dbo` (synced), or both

## Key Parameters
| Param | Type | Default | Purpose |
|---|---|---|---|
| `@CmdType` | nvarchar(200) | 'GetOT_OrderHistoryHFDataDB_Online' | Which screen/action |
| `@CompanyID` | smallint | 1 | Company |
| `@SalesmanNo` | int | 3003 | **Logged-in user** (used for data scoping) |
| `@UserID` | nvarchar(100) | 1 | Position / system user |
| `@ClientActive` | smallint | *(resolved internally)* | Client variant — same cmdType can return different data per client |
| `@PositionsID` | int | *(resolved internally)* | Salesperson position from SalesPersons |
| `@TabletSysID` | varchar(100) | null | Unique tablet transaction ID (for idempotency) |

## Important cmdTypes
### Salesmen / Selection
| cmdType | Returns | Hierarchy-aware? |
|---|---|---|
| `SalesmanBySupervisorData` | Subordinates via `Fun_GetSalesmanTreeByID` (downward) | ✅ Yes |
| `GetSalesmanList` | **Fixed** — now uses `Fun_GetSalesmanTreeByID` (previously flat `<4` filter, bug) | ✅ Yes (was ❌) |

### Master Data (synced from BO)
| cmdType | What |
|---|---|
| `GetOT_SalesmanMFDataDB` | Logged-in salesman's own master data + permissions |
| `GetOT_CustomerMFDataDB` | Customers assigned to this salesman |
| `GetOT_ItemsMFDataDB` | Product catalog |
| `GetOT_PriceListDataDB` | Price lists |
| `GetOT_RouteMFDataDB` | Route definitions |

### Transactions (written by tablet, synced to BO)
| cmdType | What |
|---|---|
| `SaveInvoice` | Save an invoice |
| `OT_InvoiceHF_Insert` / `OT_InvoiceDF_Insert` | Invoice header/detail |
| `OT_OrderHF_Insert` / `OT_OrderDF_Insert` | Orders |
| `OT_Payments_Insert` | Payments |

### Workflow / Approvals
| cmdType | What |
|---|---|
| `WFChekAccess` | Check if user has WF access |
| `WFGetVer` | Get WF version/positions config |
| `WFGetWFSalesmanRef` | Get WF reference string for the user |

### Reports (Online)
Various `OT_Online_Rpt*` cmdTypes for real-time reports requested from tablet.

## Why One Big Proc?
- **Centralized auth/permissions** — every cmdType has `@SalesmanNo`, `@PositionsID`, `@ClientActive`
- **Client-specific branches** — same cmdType can behave differently per @ClientActive (e.g. `GetOT_SalesmanMFDataDB` has 3+ variants)
- **No API versioning** — just add a new @CmdType

## Known Bug Fixed (malayo 2026-07-21)
`GetSalesmanList` originally used:
```sql
WHERE ISNULL([SalesPersonType],0) < 4
```
This was a flat type filter — returned all type 0-3 salesmen across the entire company, ignoring supervisor hierarchy. Fixed to use `Fun_GetSalesmanTreeByID(@CompanyID, @SalesmanNo)`.

See [[Supervisor-Sees-Parents-In-WF]] for full details.

## Related
- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[Supervisor-Sees-Parents-In-WF]]
- [[Fun_GetSalesmanTreeByID]]
- [[OT_SalesmanMF]]
