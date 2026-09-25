# Ticket 0008: Return Shows Items Without Tax (Unit Code Mismatch Bug)

* **Date & Time**: 2026-07-20 (lodged)
* **Customer**: Venus
* **System Component**: OSFA (Mobile) / Back Office — Sales Return
* **Symptom Category**: Tax / Data Bug
* **Reported Issue**:
  The customer made a sale and later returned 3 items. In the return, 2 of the 3 items appeared without tax, even though the original invoice had tax applied to those items. The return-only tax omission made the return totals incorrect.

* **Root Cause & Diagnosis**:
  - Investigation path in Back Office (BO):
    1. Checked the **Items** table — the items were configured with tax applied. (OK)
    2. Checked `CustomerFinancialDetails` table — the customer had "tax included" enabled. (OK)
    3. Checked the tax setting on the items in `PriceListDetails` — tax was present. (OK)
    4. From `OT_InvoiceReturnLink` obtained the original invoice number, then checked `OT_InvoiceHistoryDF` for the tax and the unit code.
  - **Conclusion**: The item code was not matched between the invoice and the return. In the original invoice the unit was **piece**, but in the return it was **car**. Because the unit code differed, the tax mapping failed for those 2 items and they showed as non-taxable in the return only.
  - This is a **bug in the system** (unit-code mismatch on return linkage), not a configuration issue.

* **Proposed Solution**:
  - The affected device was running `OSFA.apk v1.104` (old build). Installed the **updated version v1.105** on the device, which resolves the unit-code mismatch on returns.
  - No data/configuration change was required; the fix is delivered via the updated APK.

* **Verification Result**: After installing the updated OSFA.apk v1.105, returns correctly preserve the original unit code (piece) and tax, matching the original invoice.

(End of file - total 26 lines)
