# Ticket 0001: Send Data Blocked by isupdated stock = false

* **Date & Time**: 2026-06-15 14:59:03
* **System Component**: Back Office
* **Symptom Category**: DB
* **Reported Issue**:
  i want to send data to salesperson and the print diplays "isupdated stock = false"

* **Root Cause & Diagnosis**:
  - Mapped System Options: `CompanyParameters.UseMustUpdateDataInSendData`
  - Database Tables Audited: `dbo.SalesPersons` (Field: `IsUpdatedStock`), `dbo.CompanyParameters`
  - Analysis detail: 
    1. The Back Office user attempted to execute "Send Data" to a salesperson.
    2. A system parameter check (`UseMustUpdateDataInSendData` in `dbo.CompanyParameters`) validates if the salesperson's field stock matches the back-office records.
    3. The flag `IsUpdatedStock` on the `dbo.SalesPersons` table for this salesman is currently `0` (False). 
    4. This occurs because the salesman has not performed an "Update Data" sync from their OSFA tablet to report their latest stock movements. The system blocks "Send Data" to prevent new master data from overwriting and corrupting un-synced field stock balances.

* **Proposed Solution**:
  - **Operational Fix**: Instruct the salesperson to open their OSFA tablet and perform a full "Update Data" sync. This will transmit pending transactions and automatically set `IsUpdatedStock = 1`. Then, you can retry sending data.
  - **Technical Override (If Tablet is Broken/Lost)**: If you confirm there are no pending transactions in the field, you can manually reset the constraint on the Back Office database using the following queries:
  ```sql
  -- 1. Verification CHECK (Identify the Salesman and their current flag status)
  SELECT ID, Name, IsUpdatedStock, IsSendData
  FROM dbo.SalesPersons
  WHERE ID = [Insert_Salesman_ID];

  -- 2. Check if the Company Parameter is enforcing this block
  SELECT CompanyID, UseMustUpdateDataInSendData
  FROM dbo.CompanyParameters;

  -- 3. (Optional) Force Update ONLY IF data loss is confirmed not to occur
  UPDATE dbo.SalesPersons
  SET IsUpdatedStock = 1
  WHERE ID = [Insert_Salesman_ID];
  ```

* **Verification Result**: Pending user execution of the SELECT queries to verify the salesman's ID.
