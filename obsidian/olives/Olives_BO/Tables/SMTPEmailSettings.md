---
type: table
database: Olives_BO
name: SMTPEmailSettings
schema: dbo
tags: [#backoffice]
foreign_keys:
referenced_by:
  - [[PRO_GETCUSTVISITEXITNOTES]]
  - [[PRO_GETRECEIPTSFOREMAIL]]
  - [[PRO_GETVOIDEDRECEIPTSFOREMAIL]]
  - [[Pro_SMTPEmailSettings]]
support_relevance: high
last_verified: 2026-07-05
---
# SMTPEmailSettings


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores smtpemailsettings records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| FromEmail | varchar | YES |  |  |  |
| FromEmail_PW | varchar | YES |  |  |  |
| SMTP_HOST | varchar | YES |  |  |  |
| SMTP_Port | int | YES |  |  |  |
| ServiceTImerInterval | int | YES |  |  |  |
| EnableSsl | smallint | YES |  |  |  |
## Primary Key
CompanyID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (4):**
- [[PRO_GETCUSTVISITEXITNOTES]]
- [[PRO_GETRECEIPTSFOREMAIL]]
- [[PRO_GETVOIDEDRECEIPTSFOREMAIL]]
- [[Pro_SMTPEmailSettings]]

**Writes (1):**
- [[Pro_SMTPEmailSettings]]

## Estimated Size / Volatility
Typical business table
## Common Issues
> [!warning] AUTO-GENERATED — verify before trusting

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
