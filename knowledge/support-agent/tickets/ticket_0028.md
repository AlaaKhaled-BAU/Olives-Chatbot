# Ticket 0028: Workflow App Does Not Sign In — op_code 60 Timeout, Fixed by SQL Server Restart (الأمن الغذائي)

* **Date & Time**: 2026-09-22 (documented)
* **Client**: الأمن الغذائي
* **System Component**: Workflow app sign-in (live SQL connection); error log (`OT_ErrorLog` / `Error-Log`); SQL Server
* **Symptom Category**: Infrastructure / Connectivity (timeout)
* **Reported Issue**:
  The **workflow app does not sign in**.

* **Root Cause & Diagnosis**:
  - Tried **Send Data** and **changing the connection** (and everything else client-side) — did not work, ruling out tablet data / connection-string causes.
  - Checked the **error log**: it logged **op_code 60 — a timeout**.
  - Restarted the **SQL Server** — **it worked**. Root cause was server-side (stuck connections / blocking / exhausted resources timing out the login), not app configuration.

* **Resolution / Customer Action**:
  - Restart SQL Server (as done) to clear the timeout state; confirm workflow sign-in works.
  - If it recurs: check SQL Server error log + active blocks/deadlocks around the sign-in time, review connection pool / max connections, and schedule log/error-table archiving before considering deeper fixes.

* **Vault Validation Notes**:
  - ✅ **Error-log path confirmed**: tablet `OT_ERRORLOG` (`ID, CompNo, SalesmanNo, ErrDesc, SysDate`) in `db/osfa_tables.md` (lines 688–694) + obsidian `OT_ErrorLog.md`; BO `Error-Log` / `Integration-Error-Log` tables in `knowledge/reference/Olives SQL_Documentation.md` (lines 222, 244, 1085–1096, 4222+) — matches the "checked the error log" step.
  - ⚠️ **op_code 60 = timeout** is case-reported; no op-code lookup table found in vault — recorded here as observed (workflow sign-in timeout code).
  - ✅ No duplicate: full-text search over `apps/support-agent/tickets/*.md` for op_code/workflow-sign-in/timeout/SQL-restart returns no prior record — first of its kind.

* **Suggested Verification Queries**:
  ```sql
  -- 1) Recent error-log rows around the sign-in failure (tablet side)
  SELECT TOP 50 ID, CompNo, SalesmanNo, ErrDesc, SysDate
  FROM OSFA_DB.dbo.OT_ErrorLog
  WHERE SysDate >= DATEADD(day, -2, GETDATE())
  ORDER BY SysDate DESC;
  -- expect: op_code 60 / timeout entries at login time

  -- 2) If it recurs: live blocks / long-runners on the server at sign-in time
  SELECT session_id, status, blocking_session_id, wait_type,
         wait_time, cpu_time, login_name, program_name
  FROM sys.dm_exec_requests
  WHERE status NOT IN (N'background', N'sleeping');
  ```

* **Verification Result**: Client-side causes excluded (send-data + connection change failed); error log showed op_code 60 timeout; SQL Server restart restored workflow sign-in. Infrastructure-level fix — monitor for recurrence and investigate blocking/connections if it returns.

(End of file)
