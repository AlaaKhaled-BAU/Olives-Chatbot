---
type: procedure
database: OSFA_DB
name: OT_Online_RptNotSoldCustomersByItemsAndSalesman_Orders
schema: dbo
tags: [#customer, #inventory, #mobile, #sales, #order]
reads_from:
  - Olives_BO
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-08-06
---
# OT_Online_RptNotSoldCustomersByItemsAndSalesman_Orders

## Purpose

Orders variant of `OT_Online_RptNotSoldCustomersByItemsAndSalesman`. Same "not sold customers"
report, but the sold/not-sold evidence is taken from **Orders** (`OrdersHeaders` / `OrdersDetails`)
instead of **Transactions** (`TransactionsHeaders` / `TransactionsDetails`).

The orders path is wired into the procedure under a new client branch: `if @clientID = 8`
(ClientsActive). Clients other than 8 keep the original transactions-based logic exactly.

## Parameters
- @CompanyID smallint = 2
- @SupervisorNo int = 4
- @SalesmanNo int = 4
- @FromCustomer bigint = 6
- @ToCustomer bigint = 6
- @FromItemNo nvarchar(100) = '0'
- @ToItemNo nvarchar(100)  = 'zzzzzzzzzzzzz'
- @FromDate smalldatetime = '2021-04-06'
- @ToDate smalldatetime = '2021-04-06'

## Changes vs Original (Transactions → Orders)

| Original | Orders version |
|----------|----------------|
| `TransactionsHeaders` / `TransactionsDetails` | `OrdersHeaders` / `OrdersDetails` |
| Header-detail join on `CompanyID, TransactionTypeID, TransactionYear, TransactionNo` | join on `CompanyID, OrderYear, OrderNo` (no TransactionTypeID — column does not exist) |
| `TransactionsHeaders.TransactionDate` | `OrdersHeaders.OrderDate` |
| `AND TransactionsHeaders.TransactionTypeID IN (1)` filters | removed (column does not exist in orders) |
| `abs(...)` qty handling (118 branch) | client-8 orders branch uses plain `ISNULL(n.Qty,0)` (orders qty always positive, no returns) |

Preserved exactly:
- `Fun_GetSalesmanTreeByID(@CompanyID, @SupervisorNo)` joins and `ID = @SalesmanNo` filter
- `@TmpSalesmanByCustomer` (CustomersFinancialDetails → SalesPersons) insert
- `@TmpSalesmanItems` (SalesPersonItemsAssignment → SalesPersons) insert
- Output column names: `SalesmanNo, SalesmanName, CustomerID, CustomerName, ItemCode, ItemName, Qty, TransactionDate` (kept identical to original so the web-service consumer is untouched)
- Clients `118` and all others: original transactions branches byte-for-byte
- `Row_Number` partition/`ItemSer = 1` "latest order outside period" logic

## Procedure

```sql
USE [OSFA_DB]
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER PROCEDURE [dbo].[OT_Online_RptNotSoldCustomersByItemsAndSalesman]

@CompanyID smallint = 2,
@SupervisorNo int = 4,
@SalesmanNo int = 4,
@FromCustomer bigint = 6,
@ToCustomer bigint = 6,
@FromItemNo nvarchar(100) = '0',
@ToItemNo nvarchar(100)  = 'zzzzzzzzzzzzz',
@FromDate smalldatetime = '2021-04-06',
@ToDate smalldatetime = '2021-04-06'

AS
BEGIN

 declare @clientID int
select @clientID=ClientID from Olives_BO..ClientsActive where CompanyID=@CompanyID

DECLARE @TmpSalesItems Table (SalesmanNo int,CustomerID bigint,ItemCode nvarchar(100),TransactionDate smalldatetime, Qty float, primary key(SalesmanNo,CustomerID,ItemCode))
DECLARE @TmpSalesItemByCustomer Table (SalesmanNo int, CustomerID bigint, ItemCode nvarchar(100), primary key(SalesmanNo,CustomerID,ItemCode))
DECLARE @TmpSalesmanByCustomer Table (SalesmanNo int, CustomerID bigint, primary key(SalesmanNo,CustomerID))
DECLARE @TmpSalesmanItems Table (SalesmanNo int, ItemCode nvarchar(100), primary key(SalesmanNo,ItemCode))

if @clientID = 8
Begin
INSERT INTO @TmpSalesItemByCustomer
SELECT        OrdersHeaders.SalesPersonID, OrdersHeaders.CustomerID, OrdersDetails.ItemCode
FROM            Olives_BO.dbo.OrdersDetails INNER JOIN
                         Olives_BO.dbo.OrdersHeaders ON OrdersDetails.CompanyID = OrdersHeaders.CompanyID AND 
                         OrdersDetails.OrderYear = OrdersHeaders.OrderYear AND OrdersDetails.OrderNo = OrdersHeaders.OrderNo INNER JOIN
                         Olives_BO.dbo.Items ON OrdersDetails.CompanyID = Items.CompanyID AND OrdersDetails.ItemCode = Items.ItemCode INNER JOIN
                         Olives_BO.dbo.Fun_GetSalesmanTreeByID(@CompanyID, @SupervisorNo) AS Fun_GetSalesmanTreeByID_1 ON OrdersHeaders.CompanyID = Fun_GetSalesmanTreeByID_1.CompanyID AND 
                         OrdersHeaders.SalesPersonID = Fun_GetSalesmanTreeByID_1.ID
WHERE        (OrdersDetails.CompanyID = @CompanyID) AND (OrdersDetails.ItemCode BETWEEN @FromItemNo AND @ToItemNo) AND (OrdersHeaders.OrderDate BETWEEN @FromDate AND @ToDate) AND 
                         (OrdersHeaders.CustomerID BETWEEN @FromCustomer AND @ToCustomer) AND (Fun_GetSalesmanTreeByID_1.ID = @SalesmanNo)
GROUP BY OrdersHeaders.SalesPersonID, OrdersHeaders.CustomerID, OrdersDetails.ItemCode
End
else
Begin
INSERT INTO @TmpSalesItemByCustomer
SELECT        TransactionsHeaders.SalesPersonID, TransactionsHeaders.CustomerID, TransactionsDetails.ItemCode
FROM            Olives_BO.dbo.TransactionsDetails INNER JOIN
                         Olives_BO.dbo.TransactionsHeaders ON TransactionsDetails.CompanyID = TransactionsHeaders.CompanyID AND TransactionsDetails.TransactionTypeID = TransactionsHeaders.TransactionTypeID AND 
                         TransactionsDetails.TransactionYear = TransactionsHeaders.TransactionYear AND TransactionsDetails.TransactionNo = TransactionsHeaders.TransactionNo INNER JOIN
                         Olives_BO.dbo.Items ON TransactionsDetails.CompanyID = Items.CompanyID AND TransactionsDetails.ItemCode = Items.ItemCode INNER JOIN
                         Olives_BO.dbo.Fun_GetSalesmanTreeByID(@CompanyID, @SupervisorNo) AS Fun_GetSalesmanTreeByID_1 ON TransactionsHeaders.CompanyID = Fun_GetSalesmanTreeByID_1.CompanyID AND 
                         TransactionsHeaders.SalesPersonID = Fun_GetSalesmanTreeByID_1.ID
WHERE        (TransactionsDetails.CompanyID = @CompanyID) AND (TransactionsDetails.ItemCode BETWEEN @FromItemNo AND @ToItemNo) AND (TransactionsHeaders.TransactionDate BETWEEN @FromDate AND @ToDate) AND 
                         (TransactionsHeaders.CustomerID BETWEEN @FromCustomer AND @ToCustomer) AND (Fun_GetSalesmanTreeByID_1.ID = @SalesmanNo)
								AND (TransactionsHeaders.TransactionTypeID IN(1))
GROUP BY TransactionsHeaders.SalesPersonID, TransactionsHeaders.CustomerID, TransactionsDetails.ItemCode
End

INSERT INTO @TmpSalesmanByCustomer
SELECT   distinct     SalesPersons.ID AS SalesmanNo, CustomersFinancialDetails.CustomerID
FROM            Olives_BO.dbo.CustomersFinancialDetails INNER JOIN
                         Olives_BO.dbo.SalesPersons ON CustomersFinancialDetails.CompanyID = SalesPersons.CompanyID AND CustomersFinancialDetails.PositionsID = SalesPersons.PositionID INNER JOIN
                         Olives_BO.dbo.Fun_GetSalesmanTreeByID(@CompanyID, @SupervisorNo) AS Fun_GetSalesmanTreeByID_1 ON SalesPersons.CompanyID = Fun_GetSalesmanTreeByID_1.CompanyID AND 
                         SalesPersons.ID = Fun_GetSalesmanTreeByID_1.ID
WHERE        (CustomersFinancialDetails.CompanyID = @CompanyID) AND (CustomersFinancialDetails.CustomerID BETWEEN @FromCustomer AND @ToCustomer) AND (Fun_GetSalesmanTreeByID_1.ID = @SalesmanNo)

INSERT INTO @TmpSalesmanItems
SELECT        Fun_GetSalesmanTreeByID_1.ID AS SalesmanNo, SalesPersonItemsAssignment.ItemCode
FROM            Olives_BO.dbo.SalesPersonItemsAssignment INNER JOIN
                         Olives_BO.dbo.SalesPersons ON SalesPersonItemsAssignment.CompanyID = SalesPersons.CompanyID AND SalesPersonItemsAssignment.PositionsID = SalesPersons.PositionID INNER JOIN
                         Olives_BO.dbo.Fun_GetSalesmanTreeByID(@CompanyID, @SupervisorNo) AS Fun_GetSalesmanTreeByID_1 ON SalesPersons.CompanyID = Fun_GetSalesmanTreeByID_1.CompanyID AND 
                         SalesPersons.ID = Fun_GetSalesmanTreeByID_1.ID
WHERE        (SalesPersonItemsAssignment.CompanyID = @CompanyID) AND (SalesPersonItemsAssignment.ItemCode BETWEEN @FromItemNo AND @ToItemNo) AND (Fun_GetSalesmanTreeByID_1.ID = @SalesmanNo)

if @clientID = 8
Begin
INSERT INTO @TmpSalesItems
SELECT SalesPersonID,CustomerID,ItemCode,OrderDate, Qty
FROM(
SELECT        OrdersHeaders.SalesPersonID, OrdersHeaders.CustomerID, OrdersDetails.ItemCode, OrdersDetails.Quantity AS Qty, OrdersHeaders.OrderDate,
				ROW_NUMBER() OVER (PARTITION BY OrdersHeaders.SalesPersonID, OrdersHeaders.CustomerID, OrdersDetails.ItemCode ORDER BY OrdersHeaders.SalesPersonID, OrdersHeaders.CustomerID, OrdersDetails.ItemCode, OrdersHeaders.OrderDate DESC) AS ItemSer
FROM            Olives_BO.dbo.OrdersDetails INNER JOIN
                         Olives_BO.dbo.OrdersHeaders ON OrdersDetails.CompanyID = OrdersHeaders.CompanyID AND 
                         OrdersDetails.OrderYear = OrdersHeaders.OrderYear AND OrdersDetails.OrderNo = OrdersHeaders.OrderNo INNER JOIN
                         Olives_BO.dbo.Items ON OrdersDetails.CompanyID = Items.CompanyID AND OrdersDetails.ItemCode = Items.ItemCode INNER JOIN
                         Olives_BO.dbo.Fun_GetSalesmanTreeByID(@CompanyID, @SupervisorNo) AS Fun_GetSalesmanTreeByID_1 ON OrdersHeaders.CompanyID = Fun_GetSalesmanTreeByID_1.CompanyID AND 
                         OrdersHeaders.SalesPersonID = Fun_GetSalesmanTreeByID_1.ID
WHERE        (OrdersDetails.CompanyID = @CompanyID) AND (OrdersDetails.ItemCode BETWEEN @FromItemNo AND @ToItemNo) AND (NOT (OrdersHeaders.OrderDate BETWEEN @FromDate AND @ToDate)) AND 
                         (OrdersHeaders.CustomerID BETWEEN @FromCustomer AND @ToCustomer) AND (Fun_GetSalesmanTreeByID_1.ID = @SalesmanNo)
) AS Xtbl
WHERE ItemSer = 1
End
else
Begin
INSERT INTO @TmpSalesItems
SELECT SalesPersonID,CustomerID,ItemCode,TransactionDate, Qty
FROM(
SELECT        TransactionsHeaders.SalesPersonID, TransactionsHeaders.CustomerID, TransactionsDetails.ItemCode, TransactionsDetails.Quantity AS Qty, TransactionsHeaders.TransactionDate,
				ROW_NUMBER() OVER (PARTITION BY TransactionsHeaders.SalesPersonID, TransactionsHeaders.CustomerID, TransactionsDetails.ItemCode ORDER BY TransactionsHeaders.SalesPersonID, TransactionsHeaders.CustomerID, TransactionsDetails.ItemCode, TransactionsHeaders.TransactionDate DESC) AS ItemSer
FROM            Olives_BO.dbo.TransactionsDetails INNER JOIN
                         Olives_BO.dbo.TransactionsHeaders ON TransactionsDetails.CompanyID = TransactionsHeaders.CompanyID AND TransactionsDetails.TransactionTypeID = TransactionsHeaders.TransactionTypeID AND 
                         TransactionsDetails.TransactionYear = TransactionsHeaders.TransactionYear AND TransactionsDetails.TransactionNo = TransactionsHeaders.TransactionNo INNER JOIN
                         Olives_BO.dbo.Items ON TransactionsDetails.CompanyID = Items.CompanyID AND TransactionsDetails.ItemCode = Items.ItemCode INNER JOIN
                         Olives_BO.dbo.Fun_GetSalesmanTreeByID(@CompanyID, @SupervisorNo) AS Fun_GetSalesmanTreeByID_1 ON TransactionsHeaders.CompanyID = Fun_GetSalesmanTreeByID_1.CompanyID AND 
                         TransactionsHeaders.SalesPersonID = Fun_GetSalesmanTreeByID_1.ID
WHERE        (TransactionsDetails.CompanyID = @CompanyID) AND (TransactionsDetails.ItemCode BETWEEN @FromItemNo AND @ToItemNo) AND (NOT (TransactionsHeaders.TransactionDate BETWEEN @FromDate AND @ToDate)) AND 
                         (TransactionsHeaders.CustomerID BETWEEN @FromCustomer AND @ToCustomer) AND (Fun_GetSalesmanTreeByID_1.ID = @SalesmanNo)
						 AND TransactionsHeaders.TransactionTypeID IN(1)
) AS Xtbl
WHERE ItemSer = 1
End


if @clientID = 8
Begin
select xtbl.SalesmanNo, SalesPersons.Name AS SalesmanName, xtbl.CustomerID, Customers.Name AS CustomerName,xtbl.ItemCode, Items.Name AS ItemName,
		ISNULL(n.Qty,0) AS Qty, n.TransactionDate AS TransactionDate
from(
select i.SalesmanNo,i.ItemCode, j.CustomerID
from @TmpSalesmanItems AS i INNER JOIN @TmpSalesmanByCustomer as j ON
i.SalesmanNo = j.SalesmanNo
) AS xtbl LEFT OUTER JOIN @TmpSalesItemByCustomer AS k ON
xtbl.SalesmanNo = k.SalesmanNo AND
xtbl.CustomerID = k.CustomerID AND
xtbl.ItemCode = k.ItemCode LEFT OUTER JOIN @TmpSalesItems AS n ON
xtbl.SalesmanNo = n.SalesmanNo AND
xtbl.CustomerID = n.CustomerID AND
xtbl.ItemCode = n.ItemCode INNER JOIN Olives_BO.dbo.Customers ON
xtbl.CustomerID = Customers.ID INNER JOIN Olives_BO.dbo.SalesPersons ON
xtbl.SalesmanNo = SalesPersons.ID INNER JOIN Olives_BO.dbo.Items ON
xtbl.ItemCode = Items.ItemCode
WHERE k.SalesmanNo IS NULL AND Customers.CompanyID = @CompanyID AND SalesPersons.CompanyID = @CompanyID AND Items.CompanyID = @CompanyID
End
else if @clientID = 118
Begin
select xtbl.SalesmanNo, SalesPersons.Name AS SalesmanName, xtbl.CustomerID, Customers.Name AS CustomerName,xtbl.ItemCode, Items.Name AS ItemName,
		abs(ISNULL(n.Qty,0)) AS Qty, n.TransactionDate AS TransactionDate
from(
select i.SalesmanNo,i.ItemCode, j.CustomerID
from @TmpSalesmanItems AS i INNER JOIN @TmpSalesmanByCustomer as j ON
i.SalesmanNo = j.SalesmanNo
) AS xtbl LEFT OUTER JOIN @TmpSalesItemByCustomer AS k ON
xtbl.SalesmanNo = k.SalesmanNo AND
xtbl.CustomerID = k.CustomerID AND
xtbl.ItemCode = k.ItemCode LEFT OUTER JOIN @TmpSalesItems AS n ON
xtbl.SalesmanNo = n.SalesmanNo AND
xtbl.CustomerID = n.CustomerID AND
xtbl.ItemCode = n.ItemCode INNER JOIN Olives_BO.dbo.Customers ON
xtbl.CustomerID = Customers.ID INNER JOIN Olives_BO.dbo.SalesPersons ON
xtbl.SalesmanNo = SalesPersons.ID INNER JOIN Olives_BO.dbo.Items ON
xtbl.ItemCode = Items.ItemCode
WHERE k.SalesmanNo IS NULL AND Customers.CompanyID = @CompanyID AND SalesPersons.CompanyID = @CompanyID AND Items.CompanyID = @CompanyID and 	abs(ISNULL(n.Qty,0))=0
End
else
Begin
select xtbl.SalesmanNo, SalesPersons.Name AS SalesmanName, xtbl.CustomerID, Customers.Name AS CustomerName,xtbl.ItemCode, Items.Name AS ItemName,
		ISNULL(n.Qty,0) AS Qty, n.TransactionDate AS TransactionDate
from(
select i.SalesmanNo,i.ItemCode, j.CustomerID
from @TmpSalesmanItems AS i INNER JOIN @TmpSalesmanByCustomer as j ON
i.SalesmanNo = j.SalesmanNo
) AS xtbl LEFT OUTER JOIN @TmpSalesItemByCustomer AS k ON
xtbl.SalesmanNo = k.SalesmanNo AND
xtbl.CustomerID = k.CustomerID AND
xtbl.ItemCode = k.ItemCode LEFT OUTER JOIN @TmpSalesItems AS n ON
xtbl.SalesmanNo = n.SalesmanNo AND
xtbl.CustomerID = n.CustomerID AND
xtbl.ItemCode = n.ItemCode INNER JOIN Olives_BO.dbo.Customers ON
xtbl.CustomerID = Customers.ID INNER JOIN Olives_BO.dbo.SalesPersons ON
xtbl.SalesmanNo = SalesPersons.ID INNER JOIN Olives_BO.dbo.Items ON
xtbl.ItemCode = Items.ItemCode
WHERE k.SalesmanNo IS NULL AND Customers.CompanyID = @CompanyID AND SalesPersons.CompanyID = @CompanyID AND Items.CompanyID = @CompanyID
End


END
```

## Notes

- Orders join key is `CompanyID + OrderYear + OrderNo` (3 columns) — `OrdersDetails` PK is
  `CompanyID, OrderYear, OrderNo, ItemCode, UnitID`, header PK is `CompanyID, OrderYear, OrderNo`.
  `TransactionTypeID` does not exist in the orders tables, so the `IN(1)` type filters were removed.
- `OrdersHeaders.OrderDate` replaces `TransactionsHeaders.TransactionDate`.
- The client-8 select intentionally keeps output column alias `TransactionDate` (temp table
  `@TmpSalesItems.TransactionDate` holds the order date) — consumer output shape unchanged.
- Client-8 branch uses the plain `ISNULL(n.Qty,0)` style (like the general `else` branch), not the
  `abs()` style of the 118 branch: order quantities are always positive, so `abs()` is unnecessary.
- Non-8 clients: behavior identical to the original procedure.
- Verify `ClientsActive.ClientID = 8` is the intended company before deploying.

## Related

- [[OT_Online_RptNotSoldCustomersByItemsAndSalesman]]
- [[OrdersHeaders]]
- [[OrdersDetails]]
- [[_MOC-OSFA_DB|OSFA_DB MOC]]
