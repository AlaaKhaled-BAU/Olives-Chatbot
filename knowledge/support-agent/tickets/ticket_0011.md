# Ticket 0011: Printer Not Printing — Wrong PrinterType in System Options

* **Date & Time**: 2026-07-20 (lodged)
* **Customer**: Luxury Items
* **Salesman ID**: 28
* **System Component**: OSFA (Mobile) — `OT_SystemOptions` (PrinterType)
* **Symptom Category**: Hardware / Configuration
* **Reported Issue**:
  The salesman's printer does not print. The **`PrinterType`** column in the `OT_SystemOptions` table was set to **0**, but his printer should be **15**.

* **Root Cause & Diagnosis**:
  - On the tablet, printing behaviour is driven by the **`PrinterType`** column in **`OT_SystemOptions`** (OSFA_DB), keyed by `CompNo`, `Op_ID`, `SalesmanNo`.
  - The invoice-printing setting lives at **`Op_ID = 10`** (invoice printing). For this salesman (No. 28) the row had `PrinterType = 0`, which is an invalid/unsupported printer type, so nothing prints.
  - The correct value for his hardware is **`PrinterType = 15`**.
  - This is a configuration mismatch, not a hardware fault.

* **Proposed Solution**:
  - Update the salesman's invoice-printing system option to the correct printer type:
    ```sql
    UPDATE dbo.OT_SystemOptions
    SET PrinterType = 15
    WHERE SalesmanNo = 28
      AND Op_ID = 10;   -- invoice printing
    ```
  - (If set per company, also include `AND CompNo = <companyNo>` and verify the row exists.)
  - Alternatively, fix it from Back Office (System Options / Settings) and re-send data to the salesman so the tablet receives `PrinterType = 15` on next sync.
  - After the change, have the salesman retry printing an invoice.

* **Verification Result**: After setting `PrinterType = 15` for `SalesmanNo = 28` at `Op_ID = 10`, the printer prints invoices correctly.

* **Vault References (validated)**:
  - Table: `OT_SystemOptions` (OSFA_DB) — confirmed columns include `Op_ID`, `SalesmanNo`, `Op_Value`, `PrinterType` (int).
  - Keyed by `CompNo, Op_ID, SalesmanNo`.
  - Related procedures: `OT_CopySystemOption`, `Technical_CopySystemoptionsForSeveralSalespersons` (bulk copy to other salesmen if needed).

(End of file - total 36 lines)
