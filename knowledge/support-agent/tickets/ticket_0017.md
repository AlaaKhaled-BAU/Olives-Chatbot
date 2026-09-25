# Ticket 0017: SQL Server Jobs Setup — Payments FK Error & Missing Product Images (Almashreq)

* **Date & Time**: 2026-07-30 (lodged)
* **Client**: Almashreq / المشرق
* **Reported Via**: Abdulqader
* **System Component**: SQL Server Jobs / Back Office Integration — Payments & Sales Orders sync, OSFA app (images)
* **Symptom Category**: Integration / SQL Jobs / Data Sync
* **Reported Issue / Task**:
  Set up **SQL Server Jobs** to pull **Payments & Sales Orders** data and track the related problems.

* **Root Cause & Diagnosis**:

  **1. SQL Server Jobs setup + FK conflict error (`FK_routsinformation`)**:
  - When running the **Payments stored procedure** (part of the SQL Job), a **foreign-key conflict** error appeared: **`FK_routsinformation`**.
  - **Cause**: The required **Routes** data was **missing** in the relevant table referenced by the FK — the payments data could not be inserted because the route rows it depends on did not exist.
  - **Fix**: Identified the missing route data and **inserted the required routes** into the table, resolving the FK violation so the Payments procedure (and the Job) runs.

  **2. Product images not displaying**:
  - **Problem**: Product images were not showing on the system/app.
  - **Action**: Escalated to the **programming department**; they fixed the issue and **updated OSFA to version .110**.

* **Resolution / Customer Action**:
  - Route data inserted → Payments/Sales Orders SQL Jobs now run without the `FK_routsinformation` conflict.
  - Product images issue fixed by the programming team; OSFA updated to **version .110**.
  - **Pending**: deploy the changes to the **Almashreq production server**.

* **Vault Validation Notes**:
  - ✅ `RoutesInformation` (Olives_BO) confirmed as the route master table (PK `CompanyID` + `ID`) — the reference target for route-dependent records (e.g. `CustomersFinancialDetails.RouteID` joins to it). Missing route rows there cause FK failures on downstream inserts.
  - ✅ Payments/Sales Orders sync fits the known integration flow: Olives_BO tables (`Receipts`, `Payments`, `OrdersHeaders`) pushed via integration procedures to the ERP/intermediate database.
  - ⚠️ The literal FK name **`FK_routsinformation`** is **not** present in the current BO/OSFA DB scripts — it is likely named on the **customer's intermediate/integration database** (Almashreq ERP side). Treat as environment-specific; confirm against the live integration schema.

* **Verification Result**: Jobs configured; `FK_routsinformation` resolved by inserting the missing route data; product images fixed by programming team with OSFA updated to v.110. **Completed — remaining action: deploy to the Almashreq server**.
