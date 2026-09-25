# Ticket 0018: Null Exception Printing History Invoice — Op 558 Class Name Not Activated (Ecolan)

* **Date & Time**: 2026-08-02 (lodged)
* **Client**: Ecolan
* **Reported Via**: Abdallah Alzmr
* **System Component**: OSFA (Mobile) — Invoice History printing / System Options (`OT_SystemOptions`, Op_ID 558)
* **Symptom Category**: Configuration / Printing (Null Exception)
* **Reported Issue**:
  When a salesman tries to **print a history invoice**, the app throws a **null exception** and the print fails.

* **Root Cause & Diagnosis**:
  For this kind of printing problem there are **2 suspects**:
  1. **Salesman not linked to one of the items in the invoice** — if the salesman has no linkage to an item on the invoice, the print can fail.
  2. **Printer class** — the corresponding **`Op_ID`** must be activated. For **history invoice** printing the relevant system option is **`Op_ID = 558`** ("Invoice History Class Name").
  - Checked the system options: **Op 558 was NOT activated** for the salespersons (no active row for them in `OT_SystemOptions`). Without the printer class name configured, the app cannot resolve the report class for history invoices → **null exception**.

* **Resolution / Customer Action**:
  - **Created the record** in the system options table (`OT_SystemOptions`) for **Op_ID 558** = **"Invoice History Class Name"**, with value = `Rpt_PrintInvoiceHistory`, and included it for **SalesmanNo = 0 (all salesmen)**.
  - Asked the client to **update system options on the app** (data update) so the new option takes effect on the tablets.

* **Vault Validation Notes**:
  - ✅ `OT_SystemOptions` (OSFA_DB) confirmed — columns `CompNo`, `Op_ID`, `SalesmanNo`, `Op_Desc`, `Op_Value`, `Notes`, `PrinterType`; PK (`CompNo`, `Op_ID`, `SalesmanNo`).
  - ✅ **Op_ID 558 = "Invoice History Class Name"** confirmed (default row: value `Rpt_PrintInvoiceHistory`, `PrinterType` 1). It carries the **report/printer class name** used to instantiate the history-invoice print class — if missing/empty, the app gets a null class → null exception.
  - ✅ SalesmanNo = 0 is the "all salesmen" default row pattern (default system-options inserts use SalesmanNo=0).
  - ✅ System options are delivered to the tablet via the data update (`@cmd = 'OT_SystemOptions'` → `SELECT * FROM OT_SystemOptions WHERE CompNo = @CompNo AND SalesmanNo = @SalesmanNo`), so a **system-options update on the app** pushes the new row to the device.

* **Suggested Verification Queries**:
  ```sql
  -- Check the history-invoice class name option exists for the salesman (or SalesmanNo=0 all)
  SELECT CompNo, Op_ID, SalesmanNo, Op_Desc, Op_Value, PrinterType
  FROM OSFA_DB.dbo.OT_SystemOptions
  WHERE Op_ID = 558 AND CompNo = <company>
    AND (SalesmanNo = 0 OR SalesmanNo = <salesman_no>);

  -- If missing, add it for all salesmen:
  INSERT INTO OT_SystemOptions (CompNo, Op_ID, SalesmanNo, Op_Desc, Op_Value, Notes, PrinterType)
  VALUES (<company>, 558, 0, N'Invoice History  Class Name', N'Rpt_PrintInvoiceHistory', N'0', 1);
  ```

* **Verification Result**: Root cause = `Op_ID 558` (Invoice History Class Name) not activated for the salespersons → null print class → null exception on history-invoice print. Fixed by creating the system-option record for SalesmanNo=0 (all) with the correct class name (`Rpt_PrintInvoiceHistory`) and instructing the client to update system options on the app.
