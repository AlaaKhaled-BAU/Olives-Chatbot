# Ticket 0020: Data Import Error for New Supervisor (Type 3) — "No Assigned Customers" / Op 176 (baha'a soft)

* **Date & Time**: 2026-08-13 (lodged)
* **Client**: baha'a soft
* **Reported Via**: Abdallah zmr
* **System Component**: OSFA (Mobile) — Data Update / Import flow, System Options (`OT_SystemOptions`, Op_ID 176), `OT_SendCustomersInfo`
* **Symptom Category**: Configuration / Data Sync
* **Reported Issue**:
  A **cash-van customer was converted to a supervisor (SalesPersonType 3)**. When he now **loads the OSFA app and imports (updates) data**, it **results in an error**.

* **Root Cause & Diagnosis**:
  - Ran the **configuration diagnoses procedure** — it reported **"there is no assigned customers"**.
  - This is **expected** for a supervisor: a supervisor (type 3) does **not** own customers directly — customers are assigned to the salespersons (children) under him. The supervisor really has **zero direct customers**, and the diagnosis correctly found none.
  - The fix is to enable the system option that lets the supervisor **view the salespersons' customers** on the tablet.
  - The relevant option is **Op_ID 176 = "Group Cust By Related Salespersons"** (0=Off | 1=On).

* **Resolution / Customer Action**:
  - Enable **Op_ID 176** ("Group Cust By Related Salespersons") in the system options — set to **1**.
  - Instruct the client to **update the system options on the app** and re-run the data update, so the supervisor receives the customers linked to his salespersons.

* **Vault Validation Notes**:
  - ✅ **Op_ID 176 = "Group Cust By Related Salespersons"** confirmed (`knowledge/reference/system option explained.md` — values `0=Off | 1=On`; also listed in `apps/support-agent/system_options_guide.md` as `176 | Group Cust By Related Salespersons | 0=Off`).
  - ✅ Mechanism confirmed in the send-customers flow (`OT_SendCustomersInfo`, referenced from the main send-data procedure): op 176 is read from `OT_SystemOptions` (per-salesman row, falling back to `SalesmanNo = 0`), then passed into `OT_SendCustomersInfo`.
    ```sql
    SELECT @GroupCustByRelatedSalespersons = Op_Value
    FROM OSFA_DB.dbo.OT_SystemOptions
    WHERE CompNo = @CompNo AND Op_ID = 176 AND SalesmanNo = @SalesmanNo;  -- falls back to SalesmanNo=0
    ```
  - ✅ With `@GroupCustByRelatedSalespersons = 1` and `@SalesPersonType in (0,1,2,3)` (includes supervisor type 3), `OT_SendCustomersInfo` links each customer to the **related salesperson** (`LinkedSalesmanNo`) — so the supervisor can see the customers belonging to his salespersons even though he has none of his own.
  - ✅ SalesmanNo = 0 is the "all salesmen" default row pattern; a single row for op 176 with SalesmanNo=0 covers every salesman.

* **Suggested Verification Queries**:
  ```sql
  -- 1) Check op 176 for the supervisor (or the SalesmanNo=0 default)
  SELECT CompNo, Op_ID, SalesmanNo, Op_Value
  FROM OSFA_DB.dbo.OT_SystemOptions
  WHERE Op_ID = 176 AND CompNo = <company>
    AND (SalesmanNo = 0 OR SalesmanNo = <supervisor_no>);

  -- 2) Confirm the person is a supervisor (type 3) and has no direct customers
  SELECT ID, Name, PositionID, Parent, SalesPersonType
  FROM Olives_BO.dbo.SalesPersons
  WHERE CompanyID = <company> AND ID = <supervisor_no>;

  -- 3) If op 176 is missing, insert it for all salesmen:
  INSERT INTO OSFA_DB.dbo.OT_SystemOptions (CompNo, Op_ID, SalesmanNo, Op_Desc, Op_Value, Notes)
  VALUES (<company>, 176, 0, N'Group Cust  By Related Salespersons', N'1', N'0=Off | 1=On');
  ```

* **Verification Result**: Root cause = supervisor (type 3) has no direct customer assignments by design; the config diagnosis "no assigned customers" was expected, not a fault. Resolved by enabling **Op_ID 176** (Group Cust By Related Salespersons = 1) so the supervisor views the salespersons' customers, then re-running the data update on the app.