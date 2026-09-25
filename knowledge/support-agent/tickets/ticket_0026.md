# Ticket 0026: Customer-Info Update Popup on Every Login — Op 438 + Op 732 (Ovalio)

* **Date & Time**: 2026-09-22 (documented)
* **Client**: Ovalio
* **System Component**: OSFA (Tablet) — customer login / edit-customer-info prompt; System Options (`OT_SystemOptions`, Op_ID 438, Op_ID 732)
* **Symptom Category**: Configuration
* **Reported Issue**:
  When a salesman **logs in to a customer**, the app **pops up asking to update the customer's info — every time**, not once. For some salespersons it **should not appear at all**.

* **Root Cause & Diagnosis**:
  - The prompt is governed by two options acting together:
    - **Op 438 = "Allow Salesman to Edit Customer Info"** (`0=Off | 1=On`) — master switch for whether the salesman may be asked to edit customer info at login.
    - **Op 732 = "Allow edit customer one time only"** (`0=Off | 1=On`) — when 1, the prompt appears at most once per customer (then stops); when 0 with 438 = 1, it re-appears on every login (the reported symptom).
  - For salespersons where it should never appear: **438 = 0** (732 irrelevant then).
  - For salespersons where it should appear once: **438 = 1 and 732 = 1**.

* **Resolution / Customer Action**:
  | Group | Op 438 | Op 732 |
  |---|---|---|
  | Never prompt | 0 | — (0 recommended) |
  | Prompt one time only | 1 | 1 |
  | Prompt every login (current broken behavior) | 1 | 0 — change this |
  - Apply per-`SalesmanNo` (or `SalesmanNo = 0` default), then **tablet data update**.

* **Vault Validation Notes**:
  - ✅ **Op 438 = "Allow Salesman to Edit Customer Info" — `0=Off | 1=On`** confirmed in `knowledge/reference/system option explained.md` (line 433) and `apps/support-agent/system_options_guide.md` (`438`, Invoicing & Sales Orders). Description matches behavior — correct, no KB change needed.
  - ✅ **Op 732 = "Allow edit customer one time only" — `0=Off | 1=On`** confirmed in `knowledge/reference/system option explained.md` (line 723) and `system_options_guide.md` (`732`, General & Sync). Description matches behavior — correct, no KB change needed.
  - ✅ Same verdict for the other options in this batch: **Op 12 (Price Tax)** terse but accurate (see ticket_0022). No system-option descriptions required correction.

* **Suggested Verification Queries**:
  ```sql
  -- 1) Current values for the affected salesmen (or SalesmanNo=0 default)
  SELECT CompNo, Op_ID, SalesmanNo, Op_Value
  FROM OSFA_DB.dbo.OT_SystemOptions
  WHERE Op_ID IN (438, 732) AND CompNo = <company>
    AND (SalesmanNo = 0 OR SalesmanNo IN (<sp1>, <sp2>))
  ORDER BY SalesmanNo, Op_ID;

  -- 2a) Never prompt (set 438 = 0)
  -- UPDATE OSFA_DB.dbo.OT_SystemOptions SET Op_Value = '0'
  -- WHERE CompNo = <company> AND Op_ID = 438 AND SalesmanNo = <sp_never>;
  -- 2b) Prompt once (set 438 = 1 AND 732 = 1)
  -- UPDATE OSFA_DB.dbo.OT_SystemOptions SET Op_Value = '1'
  -- WHERE CompNo = <company> AND Op_ID IN (438, 732) AND SalesmanNo = <sp_once>;
  -- (Prefer the BO-supported path — direct OT_SystemOptions edits are overwritten by BO sync.)
  ```

* **Verification Result**: Behavior explained by the 438/732 combination; both option definitions verified correct in the knowledge base (no update required). Pending: apply per-salesman values + tablet data update, confirm prompt appears once / never as configured.

(End of file)
