# Ticket 0009: How to Create a Linked Server in SQL Server (Cross-Server Access via IP)

* **Date & Time**: 2026-07-20 (lodged)
* **System Component**: SQL Server (SSMS) — Linked Servers
* **Symptom Category**: How-To / Reference
* **Reported Request**:
  Document how to set up a Linked Server in SQL Server so we can access another server (reachable by IP) from our instance.

* **Procedure (Verified against Microsoft Learn + community docs)**:
  1. Open **SQL Server Management Studio (SSMS)** and connect to the local instance where the linked server will live.
  2. In **Object Explorer**, expand **Server Objects** → right-click **Linked Servers** → choose **New Linked Server**.
     - Note: the node is **Linked Servers** (not "server links").
  3. On the **General** page:
     - **Linked server**: give it an alias name.
     - **Server type**: select **SQL Server**.
     - **Data source**: enter the remote server's **IP address** (optionally `IP,Port` for a named instance).
  4. On the **Security** page, configure the credentials:
     - Select **"Be made using this security context"** and enter the **remote login** and **password** (the credentials that exist on the remote server).
     - (Alternatively map specific local logins to remote logins via `sp_addlinkedsrvlogin`.)
  5. Click **OK** to create it.
  6. Test with a four-part query:
     ```sql
     SELECT TOP 10 * FROM [LinkedServerAlias].[DatabaseName].[dbo].[TableName];
     ```
     Or run `EXEC sp_testlinkedserver N'LinkedServerAlias';`

  **T-SQL equivalent**:
  ```sql
  EXEC sp_addlinkedserver
      @server    = 'LinkedServerAlias',
      @srvproduct = 'SQL Server',
      @datasrc   = '192.168.1.100';   -- remote IP (or IP,Port)

  EXEC sp_addlinkedsrvlogin
      @rmtsrvname = 'LinkedServerAlias',
      @useself    = 'false',
      @locallogin = NULL,
      @rmtuser    = 'RemoteUser',
      @rmtpassword = 'RemotePassword';
  ```

* **Correction of Original Notes (Misconceptions)**:
  - The node is **Linked Servers**, not "server links"; the action is **New Linked Server**, and the IP goes in **Data source** (General page), not a separate "add IP" field.
  - Credentials are configured on the **Security** page, not a generic "add credentials" step.
  - **"By default you have only write permission" is inaccurate.** By default, creating a linked server creates a default login mapping to the `public` role, meaning *all* local logins can see/use the linked server object. What a user can actually do on the remote side is determined entirely by the **permissions of the remote login** used in the security context — there is no built-in "write-only" default. Apply least privilege on the remote login as needed.

* **References**:
  - Microsoft Learn — Create Linked Servers (SQL Server): https://learn.microsoft.com/en-us/sql/relational-databases/linked-servers/create-linked-servers-sql-server-database-engine
  - SQL Solutions Group — Linked Server Security: https://sqlsolutionsgroup.com/linked-server-security/

(End of file - total 40 lines)
