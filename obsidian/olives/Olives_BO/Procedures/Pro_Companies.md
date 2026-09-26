---
type: procedure
database: Olives_BO
name: Pro_Companies
schema: dbo
tags: [#backoffice]
reads_from:
  - [[ClientsActive]]
  - [[Companies]]
  - Log
writes_to:
  - [[Companies]]
  - Log
called_by:
  - [[OT_SendCompData]]
support_relevance: high
last_verified: 2026-09-26
---
# Pro_Companies


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Companies, Log. Writes Companies, Log. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @ID smallint=1
- @Name nvarchar (200)=null
- @ShortName nvarchar (100)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (40)=null
- @Address nvarchar (400)=null
- @TelephoneNo nvarchar (100)=null
- @FaxNo nvarchar (100)=null
- @POBox nvarchar (100)=null
- @WebSite nvarchar (200)=null
- @Email nvarchar (200)=null
- @Logo image=null
- @Watermark image=null
- @Notes nvarchar (600)=null
- @SalesTaxNum nvarchar (200)=null
- @cmdType varchar(50)=null
- @CurrencyID int=null
- @DataSize int = null
- @LogSize int = null
- @NullData bit = null
- @CID int = null
## Tables Read
- [[ClientsActive]]
- [[Companies]]
- Log
## Tables Written
- [[Companies]]
- Log
## Callers
_None (no known callers)_
## Callees
- [[OT_SendCompData]]
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Companies]]
- Log

**Tables Written**
- [[Companies]]
- Log

**Callers**
- [[OT_SendCompData]]

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Verified behavior (2026-09-26, live DB via sp_helptext)

- `@cmdType='Update Log File'` is the sole writer of the license-flag trio on `[[Companies]]`:
  ```sql
  UPDATE Companies
  SET DataSize=@DataSize, LogSize=@LogSize, NullData=@NullData, ServerDate=GETDATE()
  -- no WHERE clause: touches every row
  ```
  Called by the external admin/license tool that pushes DB-size counters + the enforcement flag. `INSERT`/`Update` branches do NOT touch these columns.
- `SELECT` branches (`Select All`, `Select All by ID`, `Select Comp login`, `Select All By User`) return `DataSize, LogSize, NullData` through to callers such as `[[OT_SendCompData]]`.
- Downstream (not called by this proc): `dbo.GetSalesman()` TVF reads `TOP 1 ISNULL(NullData,0) FROM Companies`. When `1`, it derives salesman quotas `(@DataSize+45)/700` / `(@LogSize+45)/700` and returns over-quota salesmen; `OT_Import*` procs (`[[OT_ImportSalesOrders]]`, `[[OT_ImportSalesInvoices]]`, `[[OT_ImportSalesIssueItems]]`, `[[OT_ImportSalesQuotations]]`, `[[OT_ImportReturnOrder]]`) exclude them via `SalesmanNo NOT IN (... GetSalesman() ... TType='FOC')`. See `[[Companies]]` note for full semantics.
- Type note: param `@NullData bit` vs column `NullData int` — implicit conversion on write.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
