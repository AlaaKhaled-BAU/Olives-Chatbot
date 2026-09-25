# Ticket 0013: Order Price Discrepancy — Alpha vs Olives (CustomerVoucher Discount)

* **Date & Time**: 2026-07-29 (lodged)
* **Client**: Ma'mon / الأمن الغذائي
* **System Component**: Alpha ERP Integration — `Alpha_Integ_SendSalesOrders` / `Alpha_SendData`
* **Symptom Category**: DB / Integration — Data Sync (Price Mismatch)
* **Reported Issue**:
  The client reported an order where the sell value reached Alpha at **17.64** but remained **18** on Olives. The customer (الأمن الغذائي) should **not** have any discount.

* **Root Cause & Diagnosis**:
  The support agent traced the sell value across all 4 databases in the data pipeline:
  1. **"DB" (final Alpha ERP database)** — sell value = **17.64** ✅ (discount subtracted)
  2. **alpha_integ DB (intermediate DB between Olives and Alpha)** — sell value = **18** ❌ (no discount)
  3. **Olives_BO (`dbo.OrdersHeaders`)** — sell value = **18** ❌
  4. **OSFA_DB (`dbo.OT_OrderHF`)** — sell value = **18** ❌

  The discrepancy of ~**0.36** (18.00 − 17.64) matched the `CustomerDiscountAmount` column value in `OrdersHeaders`. In Olives_BO and alpha_integ, the sell value reflects the **gross** price without discount. The discount is only **subtracted when data lands in the final Alpha ERP database ("DB")**.

  - **Tables inspected (per database)**:
    - **Final Alpha ERP ("DB")**: Alpha's `OrdersHeaders`-equivalent table — value = 17.64 (post-discount)
    - **alpha_integ DB**: Intermediate staging — value = 18 (pre-discount)
    - **Olives_BO**: `dbo.OrdersHeaders` → `CustomerDiscountAmount` column ≈ 0.36
    - **OSFA_DB**: `dbo.OT_OrderHF` → `VouDisc` / `CustomerDiscountAmount` columns
  - The same item price was verified consistent across all databases.
  - The client confirmed this customer should **not** have a discount applied.
  - Root cause: A discount (`CustomerDiscountAmount` / `VouDisc`) was configured at the Alpha ERP level for this customer, which only gets subtracted in the final "DB" stage. It does **not** appear in Olives_BO or alpha_integ staging values.

* **Resolution / Customer Action**:
  - The support agent advised the client to **check the discount setup from Alpha's side** (ERP-level customer discount/voucher configuration).
  - The discount is applied by Alpha's logic at the final stage — not by Olives. The fix must be on the Alpha ERP side to remove the customer's discount entitlement.

* **Vault Validation Notes**:
  - ✅ `OrdersHeaders` (Olives_BO) columns `CustomerDiscountAmount` and `CustomerDiscountPerc` confirmed — store per-order customer discount.
  - ✅ `OT_OrderHF` (OSFA_DB) columns `VouDisc` and `VouDiscPer` confirmed — tablet-side discount fields.
  - ✅ `Alpha_Integ_SendSalesOrders` confirmed as the integration procedure that reads from `OrdersHeaders` and writes to Alpha.

* **Suggested Verification Queries (run on Olives_BO)**:
  ```sql
  -- Check the order's sell value and discount
  SELECT CompanyID, OrderYear, OrderNo, CustomerDiscountPerc, CustomerDiscountAmount
  FROM dbo.OrdersHeaders
  WHERE OrderNo = <order_no> AND OrderYear = <year>;

  -- Verify item price consistency across DBs
  -- Run equivalent query on each DB and compare
  ```

* **Verification Result**: Root cause identified as Alpha-ERP-side customer discount that only subtracts at the final DB stage. Client directed to check Alpha's customer discount/voucher configuration. Pending client confirmation.
