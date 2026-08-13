-- Phase 2: the app login. Run as SA against the target client DB.
-- __CHATBOT_RO_PASSWORD__ is substituted by setup/03_apply_db_sql.py before execution.
--
-- Deliberately NOT db_datareader: that role grants SELECT on every base table,
-- which would let a query bypass the tenant views in 02_tenant_views.sql
-- entirely. This login gets NO base-table grants at all -- the only grant
-- (schema `t`, SELECT) is applied at the end of 02_tenant_views.sql. That is
-- the server-side wall (PLAN.md golden rule 3): the engine enforces
-- CompanyID, not a string check in Python.
USE master;
IF NOT EXISTS (SELECT 1 FROM sys.server_principals WHERE name = 'chatbot_ro')
    CREATE LOGIN chatbot_ro WITH PASSWORD = '__CHATBOT_RO_PASSWORD__', CHECK_POLICY = ON;
ELSE
    ALTER LOGIN chatbot_ro WITH PASSWORD = '__CHATBOT_RO_PASSWORD__';
GO

USE __DB_NAME__;
IF NOT EXISTS (SELECT 1 FROM sys.database_principals WHERE name = 'chatbot_ro')
    CREATE USER chatbot_ro FOR LOGIN chatbot_ro;
GO
