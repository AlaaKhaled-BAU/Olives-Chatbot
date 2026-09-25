# Ticket 0000: Universal First-Response Checklist — 4 Things to Check for Almost Any Problem

* **Date & Time**: 2026-07-20 (lodged)
* **System Component**: OSFA (Mobile) + Back Office (Olives_BO) — Cross-DB
* **Symptom Category**: Diagnostic Checklist / Triage
* **Reported Request**:
  For almost any problem reported by the field, we must first check these 4 things before going deeper. Documented and enriched against the Olives vault (100% validated).

* **The 4 Universal Checks**:

  ### 1. OSFA / `OT_ErrorLog` (tablet-side error log)
  - The tablet (OSFA app) writes runtime errors into **`OT_ErrorLog`** (OSFA_DB, `dbo`): columns `ID`, `CompNo`, `SalesmanNo`, `ErrDesc`, `SysDate`.
  - It is also written/read by delivery flows: `OT_InvoicesDelivery_Insert`, `OT_InvoicesDelivery_Images_Insert`.
  - **What to do**: Pull the salesman's recent `OT_ErrorLog` rows (`WHERE SalesmanNo = @SalesmanNo ORDER BY SysDate DESC`) and read `ErrDesc`. This is the fastest signal of what actually failed on the device.
  - Related: `OT_ErrorLogInteg` (OSFA_DB) holds sync/integration errors between tablet and BO; `IntegrationErrorLog` (Olives_BO) holds BO-side import/ERP errors. Check both when a sync/integration is involved.
  - Common issues for `OT_ErrorLog`: rapid growth / orphan entries / no cleanup job — archive old rows periodically.

  ### 2. Any update triggers an app service (Update Data → OSFA service)
  - On the tablet, the salesman triggers sync via **Data Updates → Update Data** (options: *Update Images*, *Upload Only*, *Upload Action Log*). This kicks off the OSFA background service that pushes/pulls data.
  - The BO-side counterpart is **`OT_UpdateData`** (and `OT_UploadTransactions`), which imports the uploaded transactions into Olives_BO (via `Pro_ImportData` / `Pro_MapTransactionLog`).
  - **What to do**: Confirm the update actually completed. In the Data-Sync-Cycle workflow, a stuck sync shows as **0%** (server IP wrong / firewall) or **partial ✓/✗** (network interruption). Re-run Data Updates and check `OT_SyncLog` / `OT_SendDataLog`. Any config change in BO also requires re-sending data (see check 3).

  ### 3. `OT_SendSalesmanData` fills OSFA (BO → Tablet push)
  - **`OT_SendSalesmanData`** (Olives_BO) is THE procedure that populates the tablet's OSFA_DB. Menu: *Salespersons → Send Data to Salesman* → select salesman(s) → Send.
  - It reads master data (`SalesPersons`, `CustomersFinancialDetails`, `Items`, `StoresBalances`, `SalesPersonItemsAssignment`, `SalesPersonItemsBalance`, `SalesPersonsDevicePermissions`, `OT_SystemOptions`, etc.) and **writes ~90 OSFA_DB tables** — including `OT_ItemsMF`, `OT_CustomerMF`, `OT_RouteMF`, `OT_PriceListsMF`, `OT_SalesmanMF`, `OT_StoreItemsQty`, `OT_SystemOptions`, and even `OT_ErrorLog`.
  - **What to do**: If the tablet is missing data (items, customers, prices, routes, permissions), verify the last `OT_SendSalesmanData` run for that salesman succeeded. ⚠️ Always re-send after ANY configuration change. Progress popup shows "Send data to #N salesman(s)".

  ### 4. Salesman set up correctly (permissions, items, etc.)
  - Validate the salesman's configuration in Back Office. The dedicated diagnostic **`DiagnosticTools_CheckSalespersonConfiguration`** (Olives_BO) reads exactly the four pillars:
    1. **`SalesPersons`** — record exists, `IsSuspended` unchecked (a suspended salesman cannot work), Business Unit / Group / Position set.
    2. **`SalesPersonsDevicePermissions`** — tablet behavioral controls (cash-only vs credit, GPS-enforced login, document-type restrictions). A new/unauthorized device has no row → login blocked.
    3. **`SalesPersonItemsAssignment`** — which items the salesman can sell (copyable to a whole group). Missing → no items on tablet.
    4. **`SalesPersonTransactionsSerials`** — unique serial ranges per transaction type; missing → transaction serial error.
  - Also confirm (from Salesman-Onboarding workflow): customers assigned via `Pro_AssignCustomersForSalesman`, price list linked via `CustomersFinancialDetails.PriceListID`, and routes created/assigned.
  - **Common issues**: can't log in → `IsSuspended` / device permissions / tablet MAC in `DeviceInformation`; no customers → missing assignment step; wrong prices → wrong `PriceListID`; GPS login failure → permission requires GPS (generate override via `Pro_PasswordGenerator`).

* **Vault References (validated)**:
  - Procedure: `OT_SendSalesmanData` (Olives_BO) — writes ~90 OSFA_DB tables.
  - Table: `OT_ErrorLog` (OSFA_DB) — tablet error log.
  - Procedure: `DiagnosticTools_CheckSalespersonConfiguration` (Olives_BO) — 4-pillar salesman check.
  - Tables: `SalesPersons`, `SalesPersonsDevicePermissions`, `SalesPersonItemsAssignment`, `SalesPersonTransactionsSerials`.
  - Workflows: `Data-Sync-Cycle`, `Salesman-Onboarding`.
  - Related runbooks: `Sync-Conflict`, `Login-Device-Issues`, `Van-Stock-Mismatch`.

* **Verification Result**: All 4 points confirmed against the Obsidian vault (OSFA_DB + Olives_BO). Checklist is safe to use as the standard first-response triage for field issues.

(End of file - total 56 lines)
