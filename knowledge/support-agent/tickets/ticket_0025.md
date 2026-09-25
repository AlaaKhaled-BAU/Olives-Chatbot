# Ticket 0025: Some Items Missing from Upload Orders — Check Items.UsedInUploadOrder (Jarwan)

* **Date & Time**: 2026-09-22 (documented)
* **Client**: Jarwan
* **System Component**: Olives_BO — `Items.UsedInUploadOrder`; OSFA Upload Order (van load, front-office §1.7)
* **Symptom Category**: Configuration / Master Data
* **Reported Issue**:
  Some items do **not appear in the upload orders** on the tablet.

* **Root Cause & Diagnosis**:
  - Cause is the per-item flag **`UsedInUploadOrder` on the `Items` table**: items with the flag off are excluded from the upload-order (van-load) item set.
  - Fix: set `UsedInUploadOrder = 1` for the missing items, then Send Data / tablet data update.
  - Duplicate check: searched existing tickets (`ticket_0000`–`ticket_0024`) for `IsUsedInUploadOrder` / `UsedInUploadOrder` / upload-order-missing-items — **no earlier ticket documents this**; this is the first record. (Note: user wrote `isusedinuploadorder`; vault column name is `UsedInUploadOrder`.)

* **Resolution / Customer Action**:
  - Flip the flag for the affected items and re-sync:
  ```sql
  UPDATE Olives_BO.dbo.Items
  SET UsedInUploadOrder = 1
  WHERE CompanyID = <company> AND ItemCode IN (N'<item1>', N'<item2>');
  ```
  - Then Send Data to the salesman and confirm the items appear in Upload Order.

* **Vault Validation Notes**:
  - ✅ **`Items.UsedInUploadOrder [bit]`** confirmed in `db/bo_tables.md` (line 1592, inside `## ITEMS`), alongside `IsTaxExempt`, `TaxType`, `Tax` — exact column the case refers to.
  - ✅ Upload Order flow confirmed in `knowledge/front-office/upload_order.md` (§1.7, van item count) — the tablet screen where the missing items should appear.
  - ✅ No duplicate: full-text search over `apps/support-agent/tickets/*.md` for upload-order/UsedInUploadOrder variants returns no prior record.

* **Suggested Verification Queries**:
  ```sql
  -- 1) Which of the missing items have the flag off?
  SELECT CompanyID, ItemCode, Name, UsedInUploadOrder, IsSuspended
  FROM Olives_BO.dbo.Items
  WHERE CompanyID = <company> AND ItemCode IN (N'<item1>', N'<item2>');

  -- 2) Fix
  UPDATE Olives_BO.dbo.Items
  SET UsedInUploadOrder = 1
  WHERE CompanyID = <company> AND ItemCode IN (N'<item1>', N'<item2>')
    AND ISNULL(UsedInUploadOrder, 0) = 0;
  ```

* **Verification Result**: First documentation of this cause. Flag name verified against vault (`UsedInUploadOrder`, not `IsUsedInUploadOrder`). Pending client confirmation that the flipped items now show in Upload Order after re-sync.

(End of file)
