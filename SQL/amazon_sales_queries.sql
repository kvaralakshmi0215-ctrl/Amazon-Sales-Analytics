-- ==========================================================
-- AMAZON SALES ANALYTICS PROJECT
-- FILE NAME : amazon_sales_queries.sql
-- ==========================================================

-- 1. View Complete Dataset
SELECT * FROM amazon_sales;

-- 2. Total Records
SELECT COUNT(*) AS Total_Records
FROM amazon_sales;

-- 3. Total Sales
SELECT ROUND(SUM(Sales),2) AS Total_Sales
FROM amazon_sales;

-- 4. Total Profit
SELECT ROUND(SUM(Profit),2) AS Total_Profit
FROM amazon_sales;

-- 5. Total Quantity Sold
SELECT SUM(Quantity) AS Total_Quantity
FROM amazon_sales;

-- 6. Total Orders
SELECT COUNT(DISTINCT `Order ID`) AS Total_Orders
FROM amazon_sales;

-- 7. Total Customers
SELECT COUNT(DISTINCT `Customer ID`) AS Total_Customers
FROM amazon_sales;

-- 8. Total Products
SELECT COUNT(DISTINCT `Product ID`) AS Total_Products
FROM amazon_sales;

-- 9. Average Sales
SELECT ROUND(AVG(Sales),2) AS Average_Sales
FROM amazon_sales;

-- 10. Average Profit
SELECT ROUND(AVG(Profit),2) AS Average_Profit
FROM amazon_sales;

-- 11. Average Discount
SELECT ROUND(AVG(Discount),2) AS Average_Discount
FROM amazon_sales;

-- 12. Highest Sale
SELECT MAX(Sales) AS Highest_Sale
FROM amazon_sales;

-- 13. Lowest Sale
SELECT MIN(Sales) AS Lowest_Sale
FROM amazon_sales;

-- 14. Highest Profit
SELECT MAX(Profit) AS Highest_Profit
FROM amazon_sales;

-- 15. Lowest Profit
SELECT MIN(Profit) AS Lowest_Profit
FROM amazon_sales;

-- 16. Sales by Category
SELECT Category,
ROUND(SUM(Sales),2) AS Total_Sales
FROM amazon_sales
GROUP BY Category
ORDER BY Total_Sales DESC;

-- 17. Profit by Category
SELECT Category,
ROUND(SUM(Profit),2) AS Total_Profit
FROM amazon_sales
GROUP BY Category
ORDER BY Total_Profit DESC;

-- 18. Quantity by Category
SELECT Category,
SUM(Quantity) AS Total_Quantity
FROM amazon_sales
GROUP BY Category
ORDER BY Total_Quantity DESC;

-- 19. Sales by Sub-Category
SELECT `Sub-Category`,
ROUND(SUM(Sales),2) AS Sales
FROM amazon_sales
GROUP BY `Sub-Category`
ORDER BY Sales DESC;

-- 20. Profit by Sub-Category
SELECT `Sub-Category`,
ROUND(SUM(Profit),2) AS Profit
FROM amazon_sales
GROUP BY `Sub-Category`
ORDER BY Profit DESC;

-- 21. Sales by Region
SELECT Region,
ROUND(SUM(Sales),2) AS Sales
FROM amazon_sales
GROUP BY Region
ORDER BY Sales DESC;

-- 22. Profit by Region
SELECT Region,
ROUND(SUM(Profit),2) AS Profit
FROM amazon_sales
GROUP BY Region
ORDER BY Profit DESC;

-- 23. Sales by State
SELECT State,
ROUND(SUM(Sales),2) AS Sales
FROM amazon_sales
GROUP BY State
ORDER BY Sales DESC;

-- 24. Profit by State
SELECT State,
ROUND(SUM(Profit),2) AS Profit
FROM amazon_sales
GROUP BY State
ORDER BY Profit DESC;

-- 25. Top 10 Cities by Sales
SELECT City,
ROUND(SUM(Sales),2) AS Sales
FROM amazon_sales
GROUP BY City
ORDER BY Sales DESC
LIMIT 10;

-- 26. Top 10 States by Profit
SELECT State,
ROUND(SUM(Profit),2) AS Profit
FROM amazon_sales
GROUP BY State
ORDER BY Profit DESC
LIMIT 10;

-- 27. Sales by Segment
SELECT Segment,
ROUND(SUM(Sales),2) AS Sales
FROM amazon_sales
GROUP BY Segment
ORDER BY Sales DESC;

-- 28. Profit by Segment
SELECT Segment,
ROUND(SUM(Profit),2) AS Profit
FROM amazon_sales
GROUP BY Segment
ORDER BY Profit DESC;

-- 29. Sales by Ship Mode
SELECT `Ship Mode`,
ROUND(SUM(Sales),2) AS Sales
FROM amazon_sales
GROUP BY `Ship Mode`
ORDER BY Sales DESC;

-- 30. Profit by Ship Mode
SELECT `Ship Mode`,
ROUND(SUM(Profit),2) AS Profit
FROM amazon_sales
GROUP BY `Ship Mode`
ORDER BY Profit DESC;

-- 31. Top 10 Customers by Sales
SELECT `Customer Name`,
ROUND(SUM(Sales),2) AS Sales
FROM amazon_sales
GROUP BY `Customer Name`
ORDER BY Sales DESC
LIMIT 10;

-- 32. Top 10 Products by Sales
SELECT `Product Name`,
ROUND(SUM(Sales),2) AS Sales
FROM amazon_sales
GROUP BY `Product Name`
ORDER BY Sales DESC
LIMIT 10;

-- 33. Top 10 Profitable Products
SELECT `Product Name`,
ROUND(SUM(Profit),2) AS Profit
FROM amazon_sales
GROUP BY `Product Name`
ORDER BY Profit DESC
LIMIT 10;

-- 34. Top 10 Loss Making Products
SELECT `Product Name`,
ROUND(SUM(Profit),2) AS Loss
FROM amazon_sales
GROUP BY `Product Name`
ORDER BY Loss ASC
LIMIT 10;

-- 35. Orders by Region
SELECT Region,
COUNT(*) AS Orders
FROM amazon_sales
GROUP BY Region
ORDER BY Orders DESC;

-- 36. Orders by Segment
SELECT Segment,
COUNT(*) AS Orders
FROM amazon_sales
GROUP BY Segment
ORDER BY Orders DESC;

-- 37. Orders by Ship Mode
SELECT `Ship Mode`,
COUNT(*) AS Orders
FROM amazon_sales
GROUP BY `Ship Mode`
ORDER BY Orders DESC;

-- 38. Customers by Region
SELECT Region,
COUNT(DISTINCT `Customer ID`) AS Customers
FROM amazon_sales
GROUP BY Region
ORDER BY Customers DESC;

-- 39. Products by Category
SELECT Category,
COUNT(DISTINCT `Product ID`) AS Products
FROM amazon_sales
GROUP BY Category
ORDER BY Products DESC;

-- 40. Monthly Sales
SELECT Month,
ROUND(SUM(Sales),2) AS Sales
FROM amazon_sales
GROUP BY Month
ORDER BY MIN(`Month Number`);

-- 41. Yearly Sales
SELECT Year,
ROUND(SUM(Sales),2) AS Sales
FROM amazon_sales
GROUP BY Year
ORDER BY Year;

-- 42. Monthly Profit
SELECT Month,
ROUND(SUM(Profit),2) AS Profit
FROM amazon_sales
GROUP BY Month
ORDER BY MIN(`Month Number`);

-- 43. Yearly Profit
SELECT Year,
ROUND(SUM(Profit),2) AS Profit
FROM amazon_sales
GROUP BY Year
ORDER BY Year;

-- 44. Orders with Discount Greater Than 20%
SELECT *
FROM amazon_sales
WHERE Discount > 0.20;

-- 45. Products with Profit Greater Than 1000
SELECT *
FROM amazon_sales
WHERE Profit > 1000;

-- 46. Furniture Sales
SELECT *
FROM amazon_sales
WHERE Category = 'Furniture';

-- 47. Technology Sales
SELECT *
FROM amazon_sales
WHERE Category = 'Technology';

-- 48. Office Supplies Sales
SELECT *
FROM amazon_sales
WHERE Category = 'Office Supplies';

-- 49. Orders with Loss
SELECT *
FROM amazon_sales
WHERE Profit < 0;

-- 50. Business Summary
SELECT
ROUND(SUM(Sales),2) AS Total_Sales,
ROUND(SUM(Profit),2) AS Total_Profit,
SUM(Quantity) AS Total_Quantity,
COUNT(DISTINCT `Order ID`) AS Total_Orders,
COUNT(DISTINCT `Customer ID`) AS Total_Customers
FROM amazon_sales;