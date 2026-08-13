---
type: table
database: Olives_BO
name: MedicalRepCoaching
schema: dbo
tags: [#backoffice]
foreign_keys: 0
procedures_reading: 1
support_relevance: low
last_verified: 2026-08-05
---
# MedicalRepCoaching

## Business Purpose

Back-office table in Olives_BO.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| ID | bigint | NO | ✓ |  |  |
| TransDate | smalldatetime | YES |  |  |  |
| CreatedBy | int | YES |  |  |  |
| RepNo | int | YES |  |  |  |
| Objective | nvarchar(4000) | YES |  |  |  |
| CustomerCount | int | YES |  |  |  |
| DoctorsCount | int | YES |  |  |  |
| PharmaciesCount | int | YES |  |  |  |
| AccountsCount | int | YES |  |  |  |
| Appearance | smallint | YES |  |  |  |
| TerritoryManagement | smallint | YES |  |  |  |
| TimeManagement | smallint | YES |  |  |  |
| Discipline | smallint | YES |  |  |  |
| PreCallObjective | smallint | YES |  |  |  |
| CustomerData | smallint | YES |  |  |  |
| PharmacyVisit | smallint | YES |  |  |  |
| VisualAidsOrganization | smallint | YES |  |  |  |
| CompetitorIntelligence | smallint | YES |  |  |  |
| StrategyAdherence | smallint | YES |  |  |  |
| ProductKnowledge | smallint | YES |  |  |  |
| QuestioningSkills | smallint | YES |  |  |  |
| ActiveLestining | smallint | YES |  |  |  |
| QuickCallDirecting | smallint | YES |  |  |  |
| IdentifyDoctorNeeds | smallint | YES |  |  |  |
| LogicalDataFlow | smallint | YES |  |  |  |
| UsingFAB | smallint | YES |  |  |  |
| HandlingObjections | smallint | YES |  |  |  |
| UsingPromotionalMaterial | smallint | YES |  |  |  |
| ClosingAndCommitment | smallint | YES |  |  |  |
| PhysicianCardFollowIp | smallint | YES |  |  |  |
| ConstructiveFeedback | smallint | YES |  |  |  |
| AbilityToAssessTheCall | smallint | YES |  |  |  |
| Stop | nvarchar(MAX) | YES |  |  |  |
| Start | nvarchar(MAX) | YES |  |  |  |
| Maintain | nvarchar(MAX) | YES |  |  |  |
| TerritoryTarget | smallint | YES |  |  |  |
| PhysicianRelationship | smallint | YES |  |  |  |
## Primary Key
CompanyID ID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 1 procedure(s): 1 writing, 0 reading.
**Writers (1):**
- [[Pro_MedicalRepCoaching]]

## Estimated Size / Volatility
~31 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
