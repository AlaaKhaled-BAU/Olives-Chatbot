# Ticket 0015: Only 3 of 5 Cheques Visible on OSFA App (Customer Chq List Rendering)

* **Date & Time**: 2026-08-02 (lodged)
* **Client**: Ma'mon / foodsecurity
* **Reported Via**: Called directly
* **System Component**: OSFA (Mobile) — `OT_AppService` cmd `GetOT_CustomerChqListDataDB` / `OT_CustomerChqList`
* **Symptom Category**: UI / Rendering (App version defect)
* **Reported Issue**:
  Only **3 of 5** cheques for the customer are visible on the OSFA app. The customer has **5** cheques. All cheques are confirmed to exist on both OSFA and Back Office.

* **Root Cause & Diagnosis**:
  - Cheques verified **present** on both sides:
    - **OSFA_DB**: `OT_CustomerChqList` — all 5 rows ✅
    - **Olives_BO**: `CustomerChqList` — all 5 rows ✅
  - Checked the appService procedure **`OT_AppService`** (OSFA_DB), cmd **`GetOT_CustomerChqListDataDB`**:
    ```sql
    SELECT * FROM OT_CustomerChqList WHERE (CompNo = @CompanyID) AND (SalesmanNo = @SalesmanNo)
    ```
    The select **returned all 5 cheques** — data layer is correct.
  - Problem is on the **development / app side**: the tablet's **screen resolution did not render the full list** (only 3 of 5 cheques displayed), even though the data was complete.
  - Fix delivered via a **new app version** that handles the rendering bug: **version 1.102.55**.

* **Resolution / Customer Action**:
  - Update the OSFA app on the tablet to the new version **1.102.55**, which fixes the cheque-list rendering.
  - After update, verify all 5 cheques display on the customer's cheque list.

* **Vault Validation Notes**:
  - ✅ `OT_CustomerChqList` (OSFA_DB) confirmed as the tablet-side cheque list table — columns include `CompNo`, `SalesmanNo`, `CustomerID`, `ChqNo`, `BankNo`, `DueDate`, `VouNo`, `ChqStatus`, `Amount`, `PaidAmount`, `RemAmount`.
  - ✅ `CustomerChqList` (Olives_BO) confirmed as the Back Office source table — PK (`CompNo`, `CustomerID`, `ChqNo`, `BankNo`); synced to the tablet.
  - ✅ `OT_AppService` (OSFA_DB) confirmed as the appService procedure; cmd `GetOT_CustomerChqListDataDB` reads `OT_CustomerChqList` filtered by `CompNo` + `SalesmanNo` (verified in DB script).

* **Suggested Verification Queries**:
  ```sql
  -- Back Office: confirm all 5 cheques exist
  SELECT CompNo, CustomerID, ChqNo, BankNo, DueDate, ChqStatus, Amount
  FROM Olives_BO.dbo.CustomerChqList
  WHERE CustomerID = <customer_id>;

  -- OSFA tablet side: confirm all 5 reached the salesman
  SELECT CompNo, SalesmanNo, CustomerID, ChqNo, BankNo, DueDate, ChqStatus, Amount
  FROM OSFA_DB.dbo.OT_CustomerChqList
  WHERE CustomerID = <customer_id> AND SalesmanNo = <salesman_no>;

  -- Reproduce the appService cmd result (should return all 5)
  EXEC dbo.OT_AppService @CompanyID = <company>, @CmdType = 'GetOT_CustomerChqListDataDB', @SalesmanNo = <salesman_no>;
  ```

* **Verification Result**: Data confirmed complete on both OSFA and BO; the appService cmd returns all cheques. Root cause = app-side rendering (resolution) defect. Resolved by updating the OSFA app to **version 1.102.55**.
