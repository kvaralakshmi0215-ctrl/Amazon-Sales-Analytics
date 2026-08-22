# ==========================================================
# AMAZON SALES ANALYTICS PROJECT
# FILE NAME : 03_Data_Visualization.py
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt

print("="*60)
print(" AMAZON SALES ANALYTICS - DATA VISUALIZATION ")
print("="*60)

# ----------------------------------------------------------
# LOAD DATASET
# ----------------------------------------------------------

file_path = r"C:\Users\kanav\OneDrive\ドキュメント\Amazon-Sales-Analytics-Dashboard\Dataset\Amazon_Sales_Cleaned.csv"

df = pd.read_csv(file_path)

# ----------------------------------------------------------
# SALES BY CATEGORY
# ----------------------------------------------------------

category = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
category.plot(kind="bar", color="royalblue")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# ----------------------------------------------------------
# PROFIT BY CATEGORY
# ----------------------------------------------------------

profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))
profit.plot(kind="bar", color="green")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

# ----------------------------------------------------------
# SALES BY REGION
# ----------------------------------------------------------

region = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8,5))
region.plot(kind="bar", color="orange")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# ----------------------------------------------------------
# SALES BY SEGMENT
# ----------------------------------------------------------

segment = df.groupby("Segment")["Sales"].sum()

plt.figure(figsize=(6,6))
segment.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Sales by Segment")
plt.tight_layout()
plt.show()

# ----------------------------------------------------------
# SALES BY SHIP MODE
# ----------------------------------------------------------

ship = df.groupby("Ship Mode")["Sales"].sum()

plt.figure(figsize=(8,5))
ship.plot(kind="bar", color="purple")
plt.title("Sales by Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# ----------------------------------------------------------
# TOP 10 STATES
# ----------------------------------------------------------

states = df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
states.plot(kind="bar")
plt.title("Top 10 States by Sales")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# ----------------------------------------------------------
# TOP 10 CITIES
# ----------------------------------------------------------

cities = df.groupby("City")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
cities.plot(kind="bar", color="red")
plt.title("Top 10 Cities by Sales")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# ----------------------------------------------------------
# TOP 10 PRODUCTS
# ----------------------------------------------------------

products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
products.plot(kind="barh", color="teal")
plt.title("Top 10 Products")
plt.xlabel("Sales")
plt.tight_layout()
plt.show()

# ----------------------------------------------------------
# MONTHLY SALES
# ----------------------------------------------------------

month_order = ["January","February","March","April","May","June",
               "July","August","September","October","November","December"]

monthly = df.groupby("Month")["Sales"].sum().reindex(month_order)

plt.figure(figsize=(12,5))
monthly.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

# ----------------------------------------------------------
# YEARLY SALES
# ----------------------------------------------------------

yearly = df.groupby("Year")["Sales"].sum()

plt.figure(figsize=(8,5))
yearly.plot(kind="line", marker="o")
plt.title("Yearly Sales")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

# ----------------------------------------------------------
# DISCOUNT VS PROFIT
# ----------------------------------------------------------

plt.figure(figsize=(8,5))
plt.scatter(df["Discount"], df["Profit"], alpha=0.5)
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.grid(True)
plt.tight_layout()
plt.show()

# ----------------------------------------------------------
# SALES DISTRIBUTION
# ----------------------------------------------------------

plt.figure(figsize=(8,5))
plt.hist(df["Sales"], bins=30)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

print("\nALL VISUALIZATIONS GENERATED SUCCESSFULLY!")