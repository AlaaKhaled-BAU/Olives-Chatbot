# Ticket 0029: SAP API Integration Job Fails with Wrong-JSON-Format Error — Implicit Timeout Cut the Connection; Fixed by Explicit Timeout Increase (Jibrini)

* **Date & Time**: 2026-09-22 (documented)
* **Client**: Jibrini
* **System Component**: Olives_BO — SAP API integration job (`SAP_Integ_*` family); JSON payload build; SQL Server connection/transaction timeout
* **Symptom Category**: DB / Integration (ERP handoff)
* **Reported Issue**:
  The **integration job with the SAP API fails**, with the error saying **wrong JSON format**.

* **Root Cause & Diagnosis**:
  - Checked **all possible format-side causes**: added `LTRIM`/`RTRIM`, removed the dots (decimal-separator cleanup) — **did not work**. The JSON builders were fine.
  - Final root cause: **SQL Server has an implicit limit ("implicit barrier" per case wording) that times out after a certain time** — for a long-running send, the **connection is cut mid-build, so the JSON arrives broken/truncated** and SAP rejects it as wrong format.
  - Fix: added an **explicit setting ("explicit barrier" per case wording) that increases the allowed time** — after that **it worked**.

* **Resolution / Customer Action**:
  - Explicit timeout increase applied on the SQL Server side for the SAP send job (exact statements were not provided with the case — see open item below), so the long JSON build/send completes before any implicit timeout cuts the connection.
  - Guideline: "wrong JSON format" from SAP on large payloads → check payload completeness (truncation) and job runtime vs timeouts before editing format code.

* **Vault Validation Notes**:
  - ✅ **SAP integration job family confirmed** in vault (`db/name_index.json`): `SAP_Integ_SendSalesInvoices`, `SAP_Integ_SendSalesInvoices_Malak`, `SAP_Integ_SendReturnSales_Malak`, `SAP_Integ_SendReturnSales_UniCharm`, `SAP_Integ_SendTransferOrders`, `SAP_Integ_NewCustomers_Lamis`, `SAP_Integ_SendPayments_Kaylani` — matches the "integration job with SAP API" component.
  - ✅ **Failure signature consistent**: truncated JSON from a cut connection parses as malformed — explains why string scrubbing (`LTRIM`/`RTRIM`, dot removal) had no effect.
  - ⚠️ **Implementation queries not on file**: the reporter noted the exact SQL Server statements were not available ("you can check how it was done on sql server, i dont have the queries") and this environment has no live SQL access — the precise explicit-timeout change (likely an explicit transaction / extended command/connection timeout on the send procedure or job step) still needs to be pasted into this ticket from the production job definition.
  - ✅ No duplicate: full-text search over `apps/support-agent/tickets/*.md` for SAP/JSON/Jibrini returns no prior record — first of its kind.

* **Suggested Verification Queries**:
  ```sql
  -- 1) Confirm the SAP send procedure text and its timeout/transaction handling
  SELECT OBJECT_DEFINITION(OBJECT_ID(N'dbo.<SAP_Integ_Jibrini_Proc>')) AS ProcText;
  -- expect: explicit timeout/transaction setting raising the allowed run time

  -- 2) Check the SQL Agent job step for the SAP send (command + retry/timeout config)
  SELECT j.name AS JobName, s.step_id, s.step_name, s.command
  FROM msdb.dbo.sysjobs j
  JOIN msdb.dbo.sysjobsteps s ON s.job_id = j.job_id
  WHERE j.name LIKE N'%SAP%' OR j.name LIKE N'%Jibrini%';

  -- 3) After a run: confirm SAP no longer reports wrong-JSON-format
  SELECT TOP 50 *
  FROM Olives_BO.dbo.IntegrationErrorLog
  ORDER BY 1 DESC;
  ```

* **Verification Result**: Format code exonerated (trim/dot fixes had no effect); broken JSON was a symptom of the connection being cut by SQL Server's implicit timeout. Explicit timeout increase resolved it — SAP accepts the payload. Open item: attach the exact production statements to this ticket when available.

(End of file)
