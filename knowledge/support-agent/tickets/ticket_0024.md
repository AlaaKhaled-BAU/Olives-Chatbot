# Ticket 0024: Receipts PostedToERP = 1 While Collected = 0 — Guard Query in Jazeera ERP Integration Job (Jarwan)

* **Date & Time**: 2026-09-22 (documented)
* **Client**: Jarwan
* **System Component**: Olives_BO — `Receipts` (`PostedToERP`, `Collected`); back-office approve/collect flow; Jazeera ERP intermediate-DB integration job
* **Symptom Category**: DB / Data Integrity (ERP posting vs BO approval)
* **Reported Issue**:
  **Receipts show `PostedToERP = 1` while `Collected = 0`** (`Collected` = approved in back office). Unapproved receipts must never be marked posted to ERP.

* **Root Cause & Diagnosis**:
  - Checked **all jobs and procedures that update `PostedToERP`** — nothing updates it without `Collected = 1` in the normal path, so the stray `1`s have no legitimate writer found (race / legacy path / external write suspected, not proven).
  - Also checked **`CompanyParameters` auto-send flags** (`AutoSendReceiptsToERP`, plus `AutoSendInvoiceToERP` / `AutoSendReturnInvoiceToERP` / `AutoSendOrderToERP` / `AutoSendReturnOrderToERP`) to see whether the company is configured to auto-send receipts to ERP — i.e. whether an automatic post path could be stamping `PostedToERP = 1` outside the collect flow.
  - Workaround (explicitly **not a root fix**): added a guard query that **resets `PostedToERP` to 0 wherever `Collected` is still 0**, executed **at the start of the integration job that sends data to the Jazeera ERP intermediate database**, before any send step runs. This stops uncollected receipts from flowing to ERP.

* **Resolution / Customer Action**:
  - Guard query now runs first inside the Jazeera-send job:
  ```sql
  UPDATE Olives_BO.dbo.Receipts
  SET PostedToERP = 0
  WHERE Collected = 0 AND PostedToERP <> 0;
  ```
  (scope further by CompanyID / date window as the job already does).
  - Monitor: if rows are hit by this guard repeatedly, the true writer is still active — capture `PostedToERPDateTime` / job history to hunt it down for a real root fix.

* **Vault Validation Notes**:
  - ✅ **`Receipts.PostedToERP [bit]` + `Receipts.Collected [bit]`** confirmed side-by-side in `db/bo_tables.md` (lines 3334–3335), with `PostedToERPDateTime`, `SecondCollected`, `VoidPostedToERP` nearby — matches the case columns exactly.
  - ✅ Semantics match: `Collected` = BO approval/collection flag; `PostedToERP` = ERP handoff flag. Invariant `PostedToERP = 1 ⇒ Collected = 1` is the documented expectation; the guard enforces it at the Jazeera job boundary.
  - ✅ **`CompanyParameters` auto-send flags** confirmed in `db/bo_tables.md` (lines 273–277): `AutoSendInvoiceToERP`, `AutoSendReturnInvoiceToERP`, `AutoSendReceiptsToERP`, `AutoSendOrderToERP`, `AutoSendReturnOrderToERP` — the exact parameters checked for an auto-post path.
  - ⚠️ Workaround acknowledged as non-root: the job now self-heals each run, but the original stray writer is still unknown.

* **Suggested Verification Queries**:
  ```sql
  -- 1) Find violations (should return 0 rows after the guard runs)
  SELECT CompanyID, TransactionTypeID, TransactionYear, TransactionNo,
         CustomerID, SalesPersonID, Amount, Collected, PostedToERP, PostedToERPDateTime
  FROM Olives_BO.dbo.Receipts
  WHERE Collected = 0 AND PostedToERP = 1;

  -- 2) Guard (as embedded at the start of the Jazeera-send job)
  UPDATE Olives_BO.dbo.Receipts
  SET PostedToERP = 0
  WHERE Collected = 0 AND PostedToERP <> 0;

  -- 3) Confirm the job text contains the guard before the intermediate-DB send step
  SELECT OBJECT_DEFINITION(OBJECT_ID(N'dbo.<JazeeraSendJobProc>')) AS JobText;

  -- 4) Company auto-send configuration (was auto-post to ERP enabled?)
  SELECT CompanyID, AutoSendReceiptsToERP, AutoSendInvoiceToERP,
         AutoSendReturnInvoiceToERP, AutoSendOrderToERP, AutoSendReturnOrderToERP
  FROM Olives_BO.dbo.CompanyParameters
  WHERE CompanyID = <company>;
  ```

* **Verification Result**: No legitimate updater sets Posted without Collected; guard query in the Jazeera ERP job now forces uncollected rows back to Posted = 0 before each send. Symptom contained, root cause still open — track repeat hits.

(End of file)
