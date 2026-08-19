# ==========================================================
# AMAZON SALES ANALYTICS PROJECT
# FILE NAME : 04_Business_Insights.py
# ==========================================================

import pandas as pd

print("="*60)
print(" AMAZON SALES ANALYTICS - BUSINESS INSIGHTS ")
print("="*60)

# ----------------------------------------------------------
# LOAD DATASET
# ----------------------------------------------------------

file_path = r"C:\Users\kanav\OneDrive\ドキュメント\Amazon-Sales-Analytics-Dashboard\Dataset\Amazon_Sales_Cleaned.csv"

df = pd.read_csv(file_path)

# ----------------------------------------------------------
# KPI VALUES
# ----------------------------------------------------------

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

print("\n================ KPI SUMMARY ================\n")

print(f"Total Sales        : ${total_sales:,.2f}")
print(f"Total Profit       : ${total_profit:,.2f}")
print(f"Total Orders       : {total_orders}")
print(f"Total Customers    : {total_customers}")

# ----------------------------------------------------------
# HIGHEST SALES CATEGORY
# ----------------------------------------------------------

best_category = df.groupby("Category")["Sales"].sum().idxmax()

best_category_sales = df.groupby("Category")["Sales"].sum().max()

print("\nHighest Sales Category")
print(best_category)
print("Sales :", round(best_category_sales,2))

# ----------------------------------------------------------
# HIGHEST PROFIT CATEGORY
# ----------------------------------------------------------

profit_category = df.groupby("Category")["Profit"].sum().idxmax()

print("\nMost Profitable Category")
print(profit_category)

# ----------------------------------------------------------
# BEST REGION
# ----------------------------------------------------------

best_region = df.groupby("Region")["Sales"].sum().idxmax()

print("\nBest Performing Region")
print(best_region)

# ----------------------------------------------------------
# BEST STATE
# ----------------------------------------------------------

best_state = df.groupby("State")["Sales"].sum().idxmax()

print("\nBest State")
print(best_state)

# ----------------------------------------------------------
# BEST CITY
# ----------------------------------------------------------

best_city = df.groupby("City")["Sales"].sum().idxmax()

print("\nBest City")
print(best_city)

# ----------------------------------------------------------
# BEST CUSTOMER
# ----------------------------------------------------------

best_customer = df.groupby("Customer Name")["Sales"].sum().idxmax()

print("\nTop Customer")
print(best_customer)

# ----------------------------------------------------------
# TOP PRODUCT
# ----------------------------------------------------------

best_product = df.groupby("Product Name")["Sales"].sum().idxmax()

print("\nTop Selling Product")
print(best_product)

# ----------------------------------------------------------
# MOST PROFITABLE PRODUCT
# ----------------------------------------------------------

profit_product = df.groupby("Product Name")["Profit"].sum().idxmax()

print("\nMost Profitable Product")
print(profit_product)

# ----------------------------------------------------------
# LOSS MAKING PRODUCT
# ----------------------------------------------------------

loss_product = df.groupby("Product Name")["Profit"].sum().idxmin()

print("\nHighest Loss Product")
print(loss_product)

# ----------------------------------------------------------
# SHIP MODE
# ----------------------------------------------------------

ship_mode = df["Ship Mode"].mode()[0]

print("\nMost Used Ship Mode")
print(ship_mode)

# ----------------------------------------------------------
# SEGMENT
# ----------------------------------------------------------

segment = df.groupby("Segment")["Sales"].sum().idxmax()

print("\nBest Customer Segment")
print(segment)

# ----------------------------------------------------------
# DISCOUNT
# ----------------------------------------------------------

avg_discount = df["Discount"].mean()

print("\nAverage Discount")
print(round(avg_discount,2))

# ----------------------------------------------------------
# RECOMMENDATIONS
# ----------------------------------------------------------

print("\n================ BUSINESS RECOMMENDATIONS ================\n")

print("1. Focus marketing on the highest selling category.")

print("2. Increase inventory for top-selling products.")

print("3. Improve performance in low-sales regions.")

print("4. Reward loyal customers with discounts.")

print("5. Reduce discounts on loss-making products.")

print("6. Promote profitable product categories.")

print("7. Optimize shipping methods to reduce delivery costs.")

print("8. Analyze low-profit products before discontinuing them.")

print("9. Increase promotions during high-sales months.")

print("10. Continue investing in the best-performing customer segment.")

# ----------------------------------------------------------
# FINAL SUMMARY
# ----------------------------------------------------------

print("\n================ PROJECT CONCLUSION ================\n")

print("Amazon Sales Analytics project successfully analyzed the sales dataset.")

print("The project identified top-performing categories, regions, products, customers, and business opportunities.")

print("These insights can help management make better business decisions and improve overall profitability.")

print("\nPROJECT COMPLETED SUCCESSFULLY!")