# Ticket 0012: Receipt Stuck / Duplicate PK on Bonanza Integration (Reference Column)

* **Date & Time**: 2026-07-20 (lodged)
* **Client**: Morec (Yasmeen)
* **System Component**: Olives_BO → Bonanza Integration — `Bonanza_Integ_SendReceipts_Yasmeen`
* **Symptom Category**: Integration / Data Sync
* **Reported Issue**:
  A receipt is **hung** — it does not move from Olives to the Bonanza integration. The integration procedure throws a **"duplicate PK"** error on Bonanza, while in Olives the receipt still shows as present (not posted).

* **Root Cause & Diagnosis**:
  - Bonanza stores **headers and details separately**. For this receipt, one side was already stored in Bonanza while the other was not — so the partial insert causes a duplicate-PK collision on the next retry (the already-inserted side clashes, the missing side never completes).
  - The receipt's **header** carries a column called **`Reference`** — this is the **buyer's account number**.
  - The Olives → Bonanza mapping procedure derives this reference using a **`SUBSTRING` that splits on the `-` character**, expecting the pattern `XXXX-XXXX` (4 chars, dash, 4 chars). The problematic receipt's reference was **only 4 characters** (no dash), so the substring logic produced an empty/incorrect value, which collided / failed the insert.
  - Because the header never posted cleanly (and one side was already in Bonanza), the receipt stays hung in Olives and re-triggers the duplicate-PK error.

* **Resolution / Customer Action**:
  - The customer agreed to **delete the hung receipt** and **re-enter it for another customer using the same value** — but she must **edit the `Reference` (account-no) column for that specific buyer** so it matches the expected `XXXX-XXXX` format (or whatever the substring logic requires) before resending.
  - This avoids the substring failure and the duplicate-PK on the partial Bonanza insert.

* **Vault Validation Notes**:
  - ✅ Integration procedure **`Bonanza_Integ_SendReceipts_Yasmeen`** (Olives_BO) confirmed: reads `Receipts`, `Customers`, `Checks`; writes staging tables **`TrnHeader_InCube`** (header) and **`Transactions_InCube`** (detail) — matching the "headers and details stored separately" behaviour. (Other Bonanza variants exist: `Bonanza_Integ_SendReceipts_SmokingCenter`, `Bonanza_Integ_Esmint`, `Bonanza_Integ_Yasmeen`.)
  - ✅ `Receipts` table (Olives_BO) confirmed: carries `Reference1` / `Reference2` (nvarchar) — the account/reference columns referenced as the buyer account no.
  - ✅ `Receipts` common issues in vault include **"Duplicate vouchers: same VouNo generated … run dedup check"** and **"Orphan lines: detail rows without matching header — causes sync failures"** — consistent with the partial header/detail insert described.
  - ⚠️ The exact **`SUBSTRING(..., '-')`** splitting logic and the literal `Reference` column name are **not** in the auto-generated vault notes (the procedure body is not indexed). Treat the substring behaviour as environment-specific; confirm against the live `Bonanza_Integ_SendReceipts_Yasmeen` definition on the Morec server. The fix (correct the reference format / re-enter) is sound regardless.

* **Suggested Verification Queries (run on Olives_BO)**:
  ```sql
  -- Find the hung receipt (still not posted to ERP)
  SELECT CompanyID, TransactionTypeID, TransactionYear, TransactionNo,
         Reference1, Reference2, PostedToERP
  FROM dbo.Receipts
  WHERE PostedToERP = 0
    AND TransactionNo = <receipt_no>;

  -- Inspect Bonanza staging for the partial insert (duplicate PK source)
  SELECT * FROM dbo.TrnHeader_InCube WHERE <receipt_key> = <value>;
  SELECT * FROM dbo.Transactions_InCube WHERE <receipt_key> = <value>;
  ```

* **Verification Result**: Root cause = partial Bonanza insert + malformed `Reference` (4-char, no dash) breaking the substring mapping → duplicate PK. Resolution agreed: delete + re-enter with corrected buyer `Reference`. Pending customer re-entry to confirm.

(End of file - total 44 lines)
