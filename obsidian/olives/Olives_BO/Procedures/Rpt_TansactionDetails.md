---
type: procedure
database: Olives_BO
name: Rpt_TansactionDetails
schema: dbo
tags: [#reporting]
reads_from:
  - Customers
  - TransactionsDetails
  - TransactionsHeaders
  - TransactionsTypes
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Rpt_TansactionDetails

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 4 table(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @ID bigint
- @SalesmanNo int
- @CustType int
- @PrNo int
- @Class_ID int
- @LocationID int
- @PayType int
- @CustName nvarchar(MAX)
- @Address nvarchar(MAX)
- @Tel nvarchar(MAX)
- @Mobile nvarchar(MAX)
- @Contact nvarchar(MAX)
- @Email nvarchar(MAX)
- @Notes nvarchar(MAX)
- @CommercialRegistrationNo nvarchar(MAX)
- @ProfessionlicenceNo nvarchar(MAX)
- @CompanyNationalID nvarchar(MAX)
- @RefNo nvarchar(MAX)
- @ShipAddress nvarchar(MAX)
- @MoreInfo1 nvarchar(MAX)
- @MoreInfo2 nvarchar(MAX)
- @CollectionDue nvarchar(MAX)
- @CommercialName nvarchar(MAX)
- @Approve bit
- @CreditLimit float
- @ExpectedAnnualSales float
- @ChecksLimit float
- @RegistrationDate smalldatetime
- @ChequeDueDays int
- @InvoiceDueDays int
- @cmdType nvarchar(50)
- @GroupID int
- @NewCustID bigint
- @ContactPersonID int
## Tables Read
- [[Customers]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsTypes]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
