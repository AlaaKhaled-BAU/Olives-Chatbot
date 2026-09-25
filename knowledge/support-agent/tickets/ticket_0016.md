# Ticket 0016: OSFA App Crash on "Add Customer" Button (Luxury Items)

* **Date & Time**: 2026-07-30 (lodged)
* **Client**: Luxury Items / المواد الفخمة
* **Reported Via**: Adnan
* **System Component**: OSFA (Mobile) — Add Customer flow (`OT_RequestToAddNewCustomer` / `OT_NewCustomers`)
* **Symptom Category**: App Crash / Device Environment
* **Reported Issue**:
  The OSFA app **stops working and closes automatically (crashes)** on the salesman's tablet whenever the **"Add Customer"** button is pressed.

* **Root Cause & Diagnosis**:
  1. **Technical check**: Performed a data update and reset of system settings on the client's device, then restarted the app — the problem **persisted**.
  2. **Simulation**: Pulled a copy of the data to a local device and reproduced the **"Add Customer"** flow using the same steps — the process **completed successfully with no errors**.
  3. **Final diagnosis**: The system and database are confirmed **working correctly**. The crash is caused by the **client's work environment / device**, not by the application or data layer.
  4. **Follow-up**: Contacted the client and reported the check result. The client said they would re-contact immediately if the problem repeats. No further reports were received.

* **Resolution / Customer Action**:
  - No code or database change was required (simulation passed cleanly on a fresh device with the same data).
  - Client advised to re-contact support if the crash recurs on the actual device — the fault is device/environment-specific.

* **Vault Validation Notes**:
  - ✅ `OT_RequestToAddNewCustomer` (OSFA_DB) confirmed as the tablet-side new-customer request table (workflow-tagged: `#customer, #mobile, #workflow`); written by `OT_RequestToAddNewCustomer_Insert`.
  - ✅ `OT_NewCustomers` (OSFA_DB) confirmed as the tablet-side new-customer master (created via the Add Customer flow, synced to BO).
  - ✅ Add Customer flow fits the known Salesman-Onboarding / Customer-Setup workflows (new customers are requested on-tablet, then posted/approved via BO).

* **Verification Result**: Reproduced cleanly on a local device copy — system + DB healthy. Root cause = client's device/work environment. Status: **temporarily closed / awaiting client confirmation** (no recurrence reported).
