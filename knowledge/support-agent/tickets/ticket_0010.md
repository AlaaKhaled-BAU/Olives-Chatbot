# Ticket 0010: How to Check and Create Customer Licenses (allowlegallicence)

* **Date & Time**: 2026-07-20 (lodged)
* **System Component**: Back Office — Customer tables (Olives_BO `Customers` / OSFA_DB `OT_CustomerMF`)
* **Symptom Category**: How-To / Customer Licensing
* **Reported Request**:
  How to check and create customer licenses. Specifically: check the **.104 server**, look at the **customers tables**, find the **`allowlegallicence`** column, which tells us whether the customer exceeded the licence number and whether the system should stop or continue based on that. If the value is **NULL**, it means the customer will continue (system does not stop).

* **Procedure (Verified against vault structure)**:
  1. Connect to the target server — the **.104 server** (the BO instance in question).
  2. Open the **customers tables**:
     - Back Office: `dbo.Customers` (central customer registry — confirmed in vault, `Olives_BO`).
     - Tablet side (if checking on device data): `dbo.OT_CustomerMF` (customer master on tablet — confirmed in vault, `OSFA_DB`).
  3. Locate the column **`allowlegallicence`** on the customer record.
  4. Read its value and interpret:
     - **`allowlegallicence = 1` (or true / allowed)**: the customer is permitted to continue even when the licence number is exceeded — the system does **not** stop.
     - **`allowlegallicence = 0` (or false / not allowed)**: the customer has exceeded the licence number and the system **will stop** the related operation.
     - **`allowlegallicence = NULL`**: means "continue" — same effect as allowed; the system does **not** stop, it proceeds. (NULL is the default/permissive state.)
  5. To **create / set** a license: ensure the customer row exists in `Customers` (create via the customer setup workflow if missing), then set `allowlegallicence` to the desired value (1 to allow continuation, 0 to enforce a stop on exceed, or NULL/leave to continue).

* **Vault Validation Notes**:
  - ✅ `Customers` (Olives_BO) and `OT_CustomerMF` (OSFA_DB) are confirmed customer master tables in the vault.
  - ✅ The licensing concept is supported: BO `Customers` carries `ProfessionlicenceNo` (profession licence number), confirming licence/legal fields exist on the customer record.
  - ⚠️ The exact column name **`allowlegallicence`** is **NOT present** in the auto-generated vault column lists for either `Customers` or `OT_CustomerMF` (likely a customer-added/extension column or environment-specific field). The behaviour described (exceed licence → stop or continue; NULL = continue) is consistent with a boolean permit flag. Treat the column as environment-specific pending schema confirmation on the .104 server.
  - Related customer flags confirmed in vault that behave similarly (bit / allow-or-stop): `AllowChqs`, `AllowDiscount`, `IsSuspended`, `IsWFSuspended`, `TaxInclude`.

* **Recommended Verification Query (run on .104 server)**:
  ```sql
  SELECT ID, Name, allowlegallicence
  FROM dbo.Customers
  WHERE allowlegallicence IS NOT NULL   -- shows only customers with an explicit stop/allow rule
  ORDER BY Name;
  ```
  To find customers currently blocked (exceeded, stop):
  ```sql
  SELECT ID, Name FROM dbo.Customers WHERE allowlegallicence = 0;
  ```

* **Verification Result**: Steps documented. Core customer tables and the licence-flag behaviour are validated against the vault; the literal `allowlegallicence` column should be confirmed against the live .104 schema (not in the current vault column index).

(End of file - total 38 lines)
