-- Phase 2: the tenant wall. Run as SA against the target client DB.
-- __DB_NAME__ is substituted by setup/03_apply_db_sql.py before execution.
--
-- Builds schema `t`: one view per dbo table that has a CompanyID column,
-- each filtered to WHERE CompanyID = CONVERT(int, SESSION_CONTEXT(N'CompanyID')).
-- SESSION_CONTEXT returns NULL when core/sql.py hasn't set it yet, and
-- "CompanyID = NULL" is never true in SQL -- so a missing/unset tenant
-- fails closed to zero rows with no special-case code. chatbot_ro is
-- granted SELECT on this schema only; it has no base-table access
-- (see 01_readonly_login.sql), so the views are the only path to data.
USE __DB_NAME__;
GO

IF NOT EXISTS (SELECT 1 FROM sys.schemas WHERE name = 't')
    EXEC('CREATE SCHEMA t');
GO

DECLARE @table_name sysname;
DECLARE @sql NVARCHAR(MAX);

DECLARE tenant_tables CURSOR LOCAL FAST_FORWARD FOR
    SELECT t.TABLE_NAME
    FROM INFORMATION_SCHEMA.TABLES t
    JOIN INFORMATION_SCHEMA.COLUMNS c
      ON c.TABLE_SCHEMA = t.TABLE_SCHEMA AND c.TABLE_NAME = t.TABLE_NAME
    WHERE t.TABLE_TYPE = 'BASE TABLE' AND t.TABLE_SCHEMA = 'dbo' AND c.COLUMN_NAME = 'CompanyID';

OPEN tenant_tables;
FETCH NEXT FROM tenant_tables INTO @table_name;
WHILE @@FETCH_STATUS = 0
BEGIN
    SET @sql = N'DROP VIEW IF EXISTS t.' + QUOTENAME(@table_name);
    EXEC sp_executesql @sql;

    SET @sql = N'CREATE VIEW t.' + QUOTENAME(@table_name) + N' AS SELECT * FROM dbo.' +
               QUOTENAME(@table_name) + N' WHERE CompanyID = CONVERT(int, SESSION_CONTEXT(N''CompanyID''))';
    EXEC sp_executesql @sql;

    FETCH NEXT FROM tenant_tables INTO @table_name;
END
CLOSE tenant_tables;
DEALLOCATE tenant_tables;
GO

-- Companies itself has no CompanyID column (its PK IS the company identity,
-- see core/catalog.py's note) -- excluded from the loop above by construction,
-- but a client legitimately asking "how many companies do I have" or "what's
-- my company name" needs it. Scope it the same way, just on its own PK.
IF OBJECT_ID('t.Companies') IS NOT NULL DROP VIEW t.Companies;
GO
CREATE VIEW t.Companies AS
    SELECT * FROM dbo.Companies WHERE ID = CONVERT(int, SESSION_CONTEXT(N'CompanyID'));
GO

-- C0 (2026-07-26, see db/table_classification.md for the full per-table
-- reasoning): the loop above only catches a literal `CompanyID` column, but
-- 60/404 real tables in this schema have none -- some genuinely have no
-- tenant-varying data at all (safe to expose unscoped), some scope by an
-- older `CompNo`/`Compno`/`compno` column instead (same concept, different
-- name -- already-documented interchangeability, see params.py). Neither
-- was reachable before this, yet schema_cache.json listed all 404 tables
-- regardless -- introspect_schema was advertising tables the agent could
-- never actually query, a guaranteed dead end.
--
-- Tables NOT in either list below (Users, Clients, cross-client/internal-
-- diagnostic tables, unscoped real business data, scratch tables -- full
-- list + reasoning in table_classification.md) get NO view here, same as
-- today: no view = unreachable, the existing default-deny behavior, no new
-- code needed to keep them blocked.

-- @sql from the first batch above is OUT OF SCOPE here -- GO starts a new
-- batch and T-SQL variables don't persist across GO. Re-declare.
DECLARE @sql NVARCHAR(MAX);
DECLARE @company_col_table sysname;
DECLARE @actual_col_name sysname;

-- Tenant data under a different company-scoping column name.
DECLARE company_col_tables CURSOR LOCAL FAST_FORWARD FOR
    SELECT t.TABLE_NAME, c.COLUMN_NAME
    FROM INFORMATION_SCHEMA.TABLES t
    JOIN INFORMATION_SCHEMA.COLUMNS c
      ON c.TABLE_SCHEMA = t.TABLE_SCHEMA AND c.TABLE_NAME = t.TABLE_NAME
    WHERE t.TABLE_TYPE = 'BASE TABLE' AND t.TABLE_SCHEMA = 'dbo'
      AND UPPER(c.COLUMN_NAME) = 'COMPNO'
      AND t.TABLE_NAME IN (
        'CustomerChqList', 'CustomerReceivablesInfo', 'CustomerSalesByCategory',
        'DebitCreditNoteTrans', 'DeliveryRoute', 'InvoiceDeliveryDF', 'InvoiceDeliveryHF',
        'InvoiceHistoryDF', 'InvoiceHistoryHF', 'LogActionTransaction', 'LogActionTransaction_',
        'Pos_InvoiceOrderHF', 'SalesOrderDeliveryDF', 'SalesOrderDeliveryHF',
        'SalesOrderHistoryDF', 'SalesOrderHistoryHF', 'Themar', 'TransactionsSuggestedItems'
      );

OPEN company_col_tables;
FETCH NEXT FROM company_col_tables INTO @company_col_table, @actual_col_name;
WHILE @@FETCH_STATUS = 0
BEGIN
    SET @sql = N'DROP VIEW IF EXISTS t.' + QUOTENAME(@company_col_table);
    EXEC sp_executesql @sql;

    SET @sql = N'CREATE VIEW t.' + QUOTENAME(@company_col_table) + N' AS SELECT * FROM dbo.' +
               QUOTENAME(@company_col_table) + N' WHERE ' + QUOTENAME(@actual_col_name) +
               N' = CONVERT(int, SESSION_CONTEXT(N''CompanyID''))';
    EXEC sp_executesql @sql;

    FETCH NEXT FROM company_col_tables INTO @company_col_table, @actual_col_name;
END
CLOSE company_col_tables;
DEALLOCATE company_col_tables;
GO

-- Global reference/lookup data verified to carry no per-company rows at all
-- (checked full column lists by hand, not pattern-matched by name) --
-- unscoped, no WHERE clause. Explicit named list, not a heuristic: this is
-- a judgment call about table CONTENT that no catalog query can make.
-- Same GO-scoping reason as above -- fresh batch, re-declare @sql.
DECLARE @sql NVARCHAR(MAX);
DECLARE @ref_table sysname;
DECLARE reference_tables CURSOR LOCAL FAST_FORWARD FOR
    SELECT v.name FROM (VALUES
        ('ActivityList'), ('CustomerLoginActions'), ('Currencies'), ('DeviceReportsList'),
        ('ExcelReports'), ('Language'), ('LanguageDictionary'), ('LogActions'), ('Menu'),
        ('MIMETypes'), ('MMS_MaintenanceTechnicianPermissions_Def'), ('MMS_OrderStatus'),
        ('OlivesMenu'), ('OlivesPages'), ('PromotionTypes'), ('SystemCodes'),
        ('TargetsTypes'), ('TransactionsTypes'), ('WF_Functions')
    ) AS v(name)
    -- only build a view for tables that actually exist in THIS database --
    -- not every client image necessarily has every one of these.
    WHERE EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES t
                  WHERE t.TABLE_SCHEMA = 'dbo' AND t.TABLE_NAME = v.name AND t.TABLE_TYPE = 'BASE TABLE');

OPEN reference_tables;
FETCH NEXT FROM reference_tables INTO @ref_table;
WHILE @@FETCH_STATUS = 0
BEGIN
    SET @sql = N'DROP VIEW IF EXISTS t.' + QUOTENAME(@ref_table);
    EXEC sp_executesql @sql;

    SET @sql = N'CREATE VIEW t.' + QUOTENAME(@ref_table) + N' AS SELECT * FROM dbo.' + QUOTENAME(@ref_table);
    EXEC sp_executesql @sql;

    FETCH NEXT FROM reference_tables INTO @ref_table;
END
CLOSE reference_tables;
DEALLOCATE reference_tables;
GO

GRANT SELECT ON SCHEMA :: t TO chatbot_ro;
GO
