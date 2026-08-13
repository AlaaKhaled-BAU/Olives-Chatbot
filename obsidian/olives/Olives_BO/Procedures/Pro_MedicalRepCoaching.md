---
type: procedure
database: Olives_BO
name: Pro_MedicalRepCoaching
schema: dbo
tags: [#backoffice]
reads_from:
  - Companies
  - SalesPersons
writes_to:
  - MedicalRepCoaching
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Pro_MedicalRepCoaching

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 2 table(s); writes 1. See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @ID bigint
- @TransDate datetime
- @CreatedBy int
- @RepNo int
- @Objective nvarchar(MAX)
- @CustomerCount int
- @DoctorsCount int
- @PharmaciesCount int
- @AccountsCount int
- @Appearance smallint
- @TerritoryManagement smallint
- @TimeManagement smallint
- @Discipline smallint
- @PreCallObjective smallint
- @CustomerData smallint
- @PharmacyVisit smallint
- @VisualAidsOrganization smallint
- @CompetitorIntelligence smallint
- @StrategyAdherence smallint
- @ProductKnowledge smallint
- @QuestioningSkills smallint
- @ActiveLestining smallint
- @QuickCallDirecting smallint
- @IdentifyDoctorNeeds smallint
- @LogicalDataFlow smallint
- @UsingFAB smallint
- @HandlingObjections smallint
- @UsingPromotionalMaterial smallint
- @ClosingAndCommitment smallint
- @PhysicianCardFollowIp smallint
- @ConstructiveFeedback smallint
- @AbilityToAssessTheCall smallint
- @TerritoryTarget smallint
- @PhysicianRelationship smallint
- @Stops nvarchar(MAX)
- @Start nvarchar(MAX)
- @Maintain nvarchar(MAX)
- @FromDate smalldatetime
- @ToDate smalldatetime
- @cmdType nvarchar(50)
## Tables Read
- [[Companies]]
- [[SalesPersons]]
## Tables Written
- [[MedicalRepCoaching]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
