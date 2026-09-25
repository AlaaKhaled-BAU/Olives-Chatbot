# Ticket 0027: Company 3 Salespersons Print Company 1 Logo — Oversized Logo Binary, Fixed by JPG Shrink + Re-upload (Blue Diamond)

* **Date & Time**: 2026-09-22 (documented)
* **Client**: Blue Diamond
* **System Component**: Back Office — `Companies` (`Logo`); OSFA tablet — `OT_COMPANY` (`comp_logo`); printed invoice/report layout (logo)
* **Symptom Category**: Data / Media Sync (image binary)
* **Reported Issue**:
  Salespersons of **company 3 print the logo of company 1**. The logo for company 3 was correctly placed in back office, yet printouts kept showing the wrong company's logo.

* **Root Cause & Diagnosis**:
  - Checked the **binary stored in the `Companies` table** for company 3 — present and looked correct.
  - Checked the **tablet-side companies table** (`OT_COMPANY`, reported as "OT_companies") and **what the salespersons actually read** — they had the correct binary on paper.
  - Suggested re-send: **Send Data again + tablet Update Data with images** (the with-images checkbox option on the app) — **did not work**; company 3 tablets still printed the company 1 logo.
  - Escalated to the **development team**: they suggested **shrinking the image and storing it as JPG, then re-uploading it** — **it worked**. Root cause was the logo binary itself (oversized / non-JPG format the tablet/printer path could not handle, so it fell back to the cached company 1 logo).

* **Resolution / Customer Action**:
  - Shrink the company 3 logo, save as **JPG**, re-upload in back office (Settings → Companies → logo), Send Data, then tablet Update Data **with images**.
  - Guideline going forward: keep company logos small-size JPGs (per back-office settings doc, logo must be JPG — e.g. saved via Paint; oversized/other formats risk the same fallback).

* **Vault Validation Notes**:
  - ✅ **BO `Companies.Logo [image]`** (+ `Logo2 [image]`, `WaterMarkImage [image]`) confirmed in `db/bo_tables.md` (lines 246, 254–255) — the binary checked in back office.
  - ✅ **Tablet `OT_COMPANY.comp_logo [image]`** confirmed in `db/osfa_tables.md` (line 198), PK `(comp_num, SalesmanNo)` — the "OT_companies" table from the case (vault name is singular `OT_COMPANY`).
  - ✅ JPG requirement consistent with `knowledge/back-office/settings.md` §1.1 (company logo "has to be in JPG format").
  - ✅ No duplicate: only prior logo mention is `ticket_0003` (Bluetooth print layout logo dimensions) — different issue.
  - ⚠️ Tablet logo fallback behavior (wrong-company logo when binary unusable) is empirical from this case, not documented in vault — recorded here.

* **Suggested Verification Queries**:
  ```sql
  -- 1) BO logo binaries present per company (non-null + size sanity)
  SELECT ID, Name,
         DATALENGTH(Logo) AS LogoBytes,
         DATALENGTH(Logo2) AS Logo2Bytes
  FROM Olives_BO.dbo.Companies
  WHERE ID IN (1, 3);

  -- 2) What the tablet side holds (per salesman)
  SELECT comp_num, SalesmanNo, comp_name,
         DATALENGTH(comp_logo) AS CompLogoBytes
  FROM OSFA_DB.dbo.OT_COMPANY
  WHERE comp_num IN (1, 3)
    AND (SalesmanNo = 0 OR SalesmanNo = <salesman_no>);
  -- expect: company 3 row non-null with small JPG-sized bytes after the fix
  ```

* **Verification Result**: Binary looked correct in both `Companies` and `OT_COMPANY` and re-sync with images failed — true fix was dev-advised JPG shrink + re-upload, after which company 3 prints its own logo. Keep logos small JPGs to prevent recurrence.

(End of file)
