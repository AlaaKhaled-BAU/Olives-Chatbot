# Ticket 0014: Missing Row in Statement of Account on Tablet (OSFA)

* **Date & Time**: 2026-07-29 (lodged)
* **Client**: Ma'mon / الأمن الغذائي
* **System Component**: Back Office → Tablet Sync — `OT_SendSalesmanData` → `OT_StateAccBalance`
* **Symptom Category**: DB / Sync — Missing Data on Tablet
* **Reported Issue**:
  The statement of account showed a **missing row** on the salesman's tablet (OSFA). The row existed in the Back Office but was not reaching the salesman.

* **Root Cause & Diagnosis**:
  - **Olives_BO**: `dbo.CustomerStatmentOfAccount` — row ✅ **present**
  - **OSFA_DB**: `dbo.OT_StateAccBalance` — row ❌ **missing**
  - The data sync from BO to the tablet (salesman) had not been refreshed. The `OT_SendSalesmanData` procedure is responsible for writing statement-of-account data from `CustomerStatmentOfAccount` (BO) to `OT_StateAccBalance` (OSFA) per salesman.
  - The salesman was seeing stale/cached data because the sync procedure had not been re-executed after the relevant transaction was posted.

* **Resolution / Customer Action**:
  - Ran `OT_SendSalesmanData` for the affected salesman to resend the statement of account data to OSFA.
  - The missing row appeared on the tablet after the sync completed.

* **Vault Validation Notes**:
  - ✅ `CustomerStatmentOfAccount` (Olives_BO) confirmed as the source table — stores per-customer debit/credit/balance rows.
  - ✅ `OT_StateAccBalance` (OSFA_DB) confirmed as the target tablet-side table — same structure with added `SalesmanNo` PK.
  - ✅ `OT_SendSalesmanData` (Olives_BO) confirmed to write to `OT_StateAccBalance` among its many tablet-side tables.

* **Suggested Verification Queries**:
  ```sql
  -- Check BO has the row
  SELECT * FROM Olives_BO.dbo.CustomerStatmentOfAccount
  WHERE CustomerID = <customer_id> AND TrNo = <tr_no>;

  -- Check if it reached tablet
  SELECT * FROM OSFA_DB.dbo.OT_StateAccBalance
  WHERE CustomerNo = <customer_id> AND TrNo = <tr_no>;
  ```

* **Verification Result**: Resolved by re-running `OT_SendSalesmanData` for the affected salesman. Data now present on OSFA tablet.
