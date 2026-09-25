# Ticket 0006: GDI+ Generic Error When Editing Customer

* **Date & Time**: 2026-07-16 11:30:00
* **System Component**: Back Office (Customers Tab)
* **Symptom Category**: Permissions / Runtime
* **Reported Issue**:
  When the user opens the Customers tab to edit any record, the error "A generic error occurred in GDI+" is thrown.

* **Root Cause & Diagnosis**:
  - The web application runs under an IIS application pool identity that needs write access to the web root to process customer images (barcodes, photos, signatures, or thumbnail generation via GDI+).
  - GDI+ raises "A generic error occurred in GDI+" when it cannot write/save to the target path. In this deployment the customer-edit flow writes to a folder under the published `wwwroot` directory, and the app pool / users group lacks the required permissions on that folder.

* **Proposed Solution**:
  - **Operational Fix**: Grant full control (Read / Write / Modify) to the IIS web root folder for the site's users / application pool identity:
    1. Open the application's published folder: `C:\inetpub\wwwroot` (or the application's `wwwroot` directory).
    2. Right-click the folder -> Properties -> Security -> Edit -> Add the users / app pool identity (e.g. `IIS_IUSRS` or the application pool account).
    3. Grant **Full Control** and apply.
    4. Recycle the application pool (or restart the site) and retry editing the customer.
  - **Note**: Only grant the minimum required write scope; prefer the specific subfolder the app writes to over the entire `wwwroot` if known.

* **Verification Result**: After applying full permissions and recycling the app pool, the user can open the Customers tab and edit records without the GDI+ error.
